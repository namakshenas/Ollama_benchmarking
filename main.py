import os

# List of Ollama models to test
models = ["llama2", "mistral", "gpt4all"]

# Tasks to evaluate
tasks = ["lambada", "piqa", "arc_easy"]

# Device configuration
device = "cpu"

for model_name in models:
    print(f"Running evaluation for model: {model_name}")
    # Construct the evaluation command
    command = f"""
    python main.py \
        --model ollama \
        --model_args model_name={model_name} \
        --tasks {" ".join(tasks)} \
        --device {device}
    """
    # Run the command
    os.system(command)


