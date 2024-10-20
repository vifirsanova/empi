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

from collections import Counter
import numpy as np

def preprocess(text):
    return text.lower().split()

def rouge_n(reference, candidate, n):
    ref_ngrams = Counter(zip(*[reference[i:] for i in range(n)]))
    cand_ngrams = Counter(zip(*[candidate[i:] for i in range(n)]))
    overlap = sum((ref_ngrams & cand_ngrams).values())
    return overlap / sum(ref_ngrams.values())

def rouge_l(reference, candidate):
    m, n = len(reference), len(candidate)
    lcs = np.zeros((m+1, n+1))
    for i in range(1, m+1):
        for j in range(1, n+1):
            if reference[i-1] == candidate[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    return lcs[m][n] / m

input_tokens = preprocess(input_text)
generated_tokens = [preprocess(text) for text in generated_texts]

rouge_scores = []
for gen_tokens in generated_tokens:
    rouge_1 = rouge_n(input_tokens, gen_tokens, 1)
    rouge_2 = rouge_n(input_tokens, gen_tokens, 2)
    #rouge_l = rouge_l(input_tokens, gen_tokens)
    rouge_scores.append((rouge_1, rouge_2))

for i, scores in enumerate(rouge_scores):
    print(f"Generated Text {i+1}:")
    print(f"ROUGE-1: {scores[0]:.4f}")
    print(f"ROUGE-2: {scores[1]:.4f}")
    #print(f"ROUGE-L: {scores[2]:.4f}")
    print()
