"""Llm Response Controller"""
from llama_cpp import Llama

class LlmResponseController:
    def __init__(self, model_path):
        self.model_path = model_path
        self.llama = Llama(model_path)

    def generate_text(self, prompt, max_tokens=5000):
        return self.llama(prompt, max_tokens=max_tokens)

    def set_context(self, n_ctx):
        self.llama = Llama(self.model_path, n_ctx=n_ctx)

    def use_chat_api(self, chat_format):
        self.llama = Llama(self.model_path, chat_format=chat_format)