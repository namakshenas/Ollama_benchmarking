# Ollama_benchmarking
This script tests several benchmarking tasks via `LM-Eval-Harness` across various categories like reasoning, language understanding, knowledge retrieval, and more. Below is a list of other common benchmarks you can use, organized by type of task:

	•	lambada: Tests the ability of a model to predict the last word of a sentence in a context, requiring broad context understanding.
	•	piqa: Physical commonsense reasoning benchmark where the model must choose the most plausible solution to a problem.
	•	arc_easy: Easy multiple-choice science questions from the AI2 Reasoning Challenge dataset.
	•	arc_hard: Harder subset of multiple-choice science questions from the AI2 Reasoning Challenge.
	•	triviaqa: Open-domain QA benchmark with trivia questions and answers drawn from Wikipedia and web sources.
	•	natural_questions: Question-answering task using natural search queries and corresponding answers from Wikipedia.
	•	openbookqa: QA benchmark requiring a model to use knowledge beyond the given context, similar to an “open-book exam.”
	•	hellaswag: Commonsense reasoning task where the model predicts the most plausible continuation of a sentence or situation.
	•	winogrande: Winograd-style commonsense reasoning tasks designed to test coreference understanding and ambiguity resolution.
	•	siqa (Social IQa): A benchmark focused on reasoning about social and emotional commonsense.
	•	commonsenseqa: Multiple-choice QA task requiring a broad commonsense knowledge base to answer.
	•	squad: QA task where the model extracts answers to questions from a given passage of text.
	•	race: Reading comprehension dataset with multiple-choice questions aimed at middle and high school students.
	•	boolq: Binary question-answering dataset where the answers are either “yes” or “no,” based on short passages.
	•	mathqa: Mathematical reasoning dataset that tests the ability to solve math word problems.
	•	gsm8k: A collection of grade-school math problems that require multi-step reasoning to solve.
	•	arithmetic: Focuses on basic arithmetic operations like addition, subtraction, multiplication, and division.
	•	wmt14: Benchmark for evaluating translation quality, particularly English to French translations.
	•	flores101: Low-resource language translation benchmark covering over 100 languages.
	•	cnn_dailymail: Summarization benchmark where the model generates summaries of news articles.
	•	xsum: Abstractive summarization dataset focusing on generating one-sentence summaries.
	•	bbq: Bias Benchmark for Question Answering; evaluates models on bias-related scenarios.
	•	crowspairs: Measures model bias across gender, race, religion, and other demographic dimensions.
	•	humaneval: Tests a model’s ability to write code solutions to programming problems.
	•	apps: Programming problems for code generation models, ranging from easy to advanced difficulty.
	•	logiqa: Logical reasoning benchmark for scenarios involving deductive, inductive, and abductive reasoning.
	•	cosmosqa: Causal reasoning benchmark requiring understanding of implicit relationships in a given context.
	•	mmlu (Massive Multitask Language Understanding): Covers 57 diverse subjects across STEM, humanities, and more, evaluating multitask language understanding.
	•	super_glue: A suite of tasks testing textual entailment, coreference resolution, question answering, and more.
	•	storycloze: Evaluates a model’s ability to logically continue a given story.
	•	wikitext: Language modeling benchmark that tests a model’s ability to predict text in Wikipedia articles.
