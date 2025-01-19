import requests
from lm_eval.api.model import LM

class OllamaModel(LM):
    def __init__(self, model_name, device="cpu"):
        super().__init__()
        self.model_name = model_name
        self.device = device
        self.base_url = "http://localhost:11434"  # Default Ollama API endpoint

    def generate(self, prompt):
        """Generate a response from the Ollama model."""
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(f"{self.base_url}/api/generate", json=payload)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            raise Exception(f"Error generating response: {response.text}")

    def generate_until(self, prompts, until=None, max_length=None):
        """Generate text until a stopping condition is met."""
        responses = []
        for prompt in prompts:
            response = self.generate(prompt)
            if until:
                # Stop generation if any of the `until` strings are encountered
                for stop_str in until:
                    if stop_str in response:
                        response = response.split(stop_str)[0]
                        break
            responses.append(response)
        return responses

    def loglikelihood(self, prompts):
        """Skip tasks that require loglikelihood."""
        raise NotImplementedError("loglikelihood is not supported for Ollama models.")

    def loglikelihood_rolling(self, prompts):
        """Skip tasks that require loglikelihood_rolling."""
        raise NotImplementedError("loglikelihood_rolling is not supported for Ollama models.")