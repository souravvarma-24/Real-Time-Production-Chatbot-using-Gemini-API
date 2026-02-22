import google.generativeai as genai
import time
from core.logger import logger
from configuration.environment import API_TOKEN, ACTIVE_MODEL
from core.prompt_manager import PromptManager


class CareerAIEngine:

    def __init__(self):
        genai.configure(api_key=API_TOKEN)
        self.model = genai.GenerativeModel(ACTIVE_MODEL)
        logger.info("CareerAIEngine initialized successfully")

    def process(self, conversation_buffer, user_input):

        prompt = PromptManager.build_prompt(conversation_buffer, user_input)

        logger.info("Processing new request")
        logger.info(f"Prompt length: {len(prompt)} characters")

        max_retries = 2

        for attempt in range(max_retries):
            try:
                logger.info(f"Gemini API call attempt {attempt+1}")

                response = self.model.generate_content(prompt)

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