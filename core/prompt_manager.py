from configuration.environment import SYSTEM_PROMPT
from core.logger import logger


class PromptManager:

    MAX_TOKENS = 3000   # Safe working limit for Gemini Flash
    CONTEXT_LIMIT = 8   # Maximum turns to consider

    @staticmethod
    def estimate_tokens(text: str) -> int:
        """
        Rough token estimation:
        1 token ≈ 4 characters (approximation used in production heuristics)
        """
        return len(text) // 4

    @classmethod
    def build_prompt(cls, conversation_buffer, user_input):

        # Take last N turns initially
        context = conversation_buffer[-cls.CONTEXT_LIMIT:]

        while True:
            compiled_context = "\n".join(
                [f"{role}: {message}" for role, message in context]
            )

            prompt = f"""
{SYSTEM_PROMPT}

Conversation:
{compiled_context}

User: {user_input}
""".strip()

            estimated_tokens = cls.estimate_tokens(prompt)

            logger.info(f"Estimated token usage: {estimated_tokens}")

            # If within safe range → return
            if estimated_tokens <= cls.MAX_TOKENS:
                return prompt

            # Otherwise trim oldest message
            if len(context) > 1:
                context = context[1:]
                logger.warning("Trimming conversation to optimize token usage")
            else:
                # If only one message left, break to avoid infinite loop
                return prompt