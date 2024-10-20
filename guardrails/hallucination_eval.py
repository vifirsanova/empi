import numpy as np
from transformers import AutoModel, AutoTokenizer
from sklearn.metrics.pairwise import cosine_similarity
from rouge_score import rouge_scorer
import nltk
nltk.download('punkt')

# Загрузка модели и токенизатора для векторизации текста
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# Функция для преобразования текста в вектор
def text_to_vector(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    return np.mean(outputs.last_hidden_state.detach().numpy(), axis=1)

# Функция для вычисления векторного сходства (косинусное сходство)
def compute_vector_similarity(vector1, vector2):
    return cosine_similarity(vector1, vector2)

# Функция для вычисления порогового сходства
def check_similarity_threshold(similarity_score, threshold=0.8):
    return similarity_score >= threshold

# Функция для вычисления метрики ROUGE
def compute_rouge(reference, generated):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    return scorer.score(reference, generated)

# Входные данные: образец использования скрипта
input_text = "The cat is on the mat."
generated_texts = [
    "The cat sits on the mat.",
    "A dog is in the house.",
    "The mat is under the cat."
]

# Преобразование текста в векторное представление
input_vector = text_to_vector(input_text)

# Преобразование каждого сгенерированного текста в векторы и вычисление сходства
similarities = []
for generated_text in generated_texts:
    gen_vector = text_to_vector(generated_text)
    similarity_score = compute_vector_similarity(input_vector, gen_vector)
    similarities.append(similarity_score)

# Проверка порога сходства и вычисление ROUGE
filtered_results = []
for i, sim_score in enumerate(similarities):
    if check_similarity_threshold(sim_score, threshold=0.8):
        rouge_result = compute_rouge(input_text, generated_texts[i])
        filtered_results.append((generated_texts[i], rouge_result, sim_score))

# Вывод результатов
for result in filtered_results:
    print(f"Generated Text: {result[0]}")
    print(f"ROUGE Score: {result[1]}")
    print(f"Similarity Score: {result[2]}")
