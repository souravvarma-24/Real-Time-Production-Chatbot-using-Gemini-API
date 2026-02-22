from google import genai
import time
from core.logger import logger
from configuration.environment import API_TOKEN, ACTIVE_MODEL
from core.prompt_manager import PromptManager


class CareerAIEngine:

    def __init__(self):
        # Initialize Gemini Client (NEW SDK FORMAT)
        self.client = genai.Client(api_key=API_TOKEN)
        logger.info("CareerAIEngine initialized successfully with google-genai")

    def process(self, conversation_buffer, user_input):

        # Build structured prompt
        prompt = PromptManager.build_prompt(conversation_buffer, user_input)

        logger.info("Processing new request")
        logger.info(f"Prompt length: {len(prompt)} characters")

        max_retries = 2

        for attempt in range(max_retries):
            try:
                logger.info(f"Gemini API call attempt {attempt+1}")

                # NEW google-genai format
                response = self.client.models.generate_content(
                    model=ACTIVE_MODEL,
                    contents=prompt
                )

                if not response or not response.text:
                    logger.warning("Empty response from Gemini")
                    return {
                        "status": "error",
                        "response": "⚠️ AI returned empty response. Please try again."
                    }

                logger.info("Successful Gemini response")

                return {
                    "status": "success",
                    "response": response.text
                }

            except Exception as e:
                logger.warning(f"Attempt {attempt+1} failed: {str(e)}")
                time.sleep(2)

        logger.error("All retry attempts failed")

        return {
            "status": "error",
            "response": "🚨 AI service temporarily unavailable."
        }