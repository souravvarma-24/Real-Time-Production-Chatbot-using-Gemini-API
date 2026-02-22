class DialogueManager:
    def __init__(self, limit=8):
        self.limit = limit
        self.buffer = []

    def record(self, speaker: str, text: str):
        self.buffer.append((speaker, text))
        if len(self.buffer) > self.limit:
            self.buffer = self.buffer[-self.limit:]

    def get_buffer(self):
        return self.buffer