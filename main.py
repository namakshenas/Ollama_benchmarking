from lm_eval import tasks, evaluator
from tabulate import tabulate

# Import your custom OllamaModel class
from ollama_model import OllamaModel

# Define models and tasks
models = [
    "deepseek-v2:16b",
    "phi4:14b",
    "gemma2:27b",
    "llama3.1:8b-instruct-q8_0",
    "mistral-nemo:latest"
]
tasks_to_evaluate = [
    # "lambada",
    "piqa",
    "arc_easy",
    "hellaswag",
    # "winogrande",
    # "logiqa"
]

device = "cpu"

# Retrieve a dict of tasks: {task_name: task_obj}
all_tasks = tasks.get_task_dict(tasks_to_evaluate)  # Pass the list of task names directly
results_dict = {}

for model_name in models:
    print(f"Evaluating model: {model_name}")
    model = OllamaModel(model_name=model_name, device=device)

    # We'll accumulate task names in `supported_tasks`.
    supported_tasks = []

    for task_name in tasks_to_evaluate:
        # Make sure the task object exists
        task = all_tasks.get(task_name)
        if task is not None:
            # ---------------------------------------------------------
            # Check if the task requires loglikelihood
            # This is a heuristic and may need adjustment
            # based on how your tasks are actually implemented
            # ---------------------------------------------------------
            if not hasattr(task, "requires_loglikelihood") or not task.requires_loglikelihood:
                supported_tasks.append(task_name)
            else:
                print(f"Skipping '{task_name}' because it likely requires log-likelihood.")
        else:
            print(f"Task '{task_name}' not found in the task registry. Skipping.")

    if not supported_tasks:
        print(f"No supported tasks for model: {model_name}")
        continue

    # Evaluate on the supported tasks
    results = evaluator.simple_evaluate(
        model=model,
        tasks=supported_tasks,  # Pass the list of task names directly
        device=device
    )

    # Store results for this model
    results_dict[model_name] = results["results"]

# Prepare data for tabular output
table_data = []
for model_name, task_results in results_dict.items():
    row = [model_name]
    for t_name in tasks_to_evaluate:
        if t_name in task_results:
            row.append(task_results[t_name].get("acc,none", "N/A"))
        else:
            row.append("N/A")
    table_data.append(row)

headers = ["Model"] + tasks_to_evaluate
print(tabulate(table_data, headers=headers, tablefmt="pretty"))