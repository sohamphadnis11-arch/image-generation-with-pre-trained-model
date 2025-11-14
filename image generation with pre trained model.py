# -*- coding: utf-8 -*-
"""
Alternate Structured Version – Markov Chain Text Generator
ProDigy Infotech Internship – Task 3
"""

# =====================================================
# 📦 Import
# =====================================================
import random

# =====================================================
# 🧩 Step A — Text Source
# =====================================================
def get_corpus():
    corpus = """
    ProDigy Infotech is a leading IT company. It provides software development, training, and consultancy services.
    We focus on quality solutions and innovative technologies. Our team works with dedication and excellence.
    """
    return corpus

# =====================================================
# 🧹 Step B — Tokenization
# =====================================================
def tokenize(corpus_text):
    tokens = corpus_text.split()
    return tokens

# =====================================================
# 🏗️ Step C — Build Markov Model
# =====================================================
def create_markov_model(tokens):
    model = {}

    for index in range(len(tokens) - 1):
        word = tokens[index]
        next_word = tokens[index + 1]

        if word not in model:
            model[word] = []

        model[word].append(next_word)

    return model

# =====================================================
# ✨ Step D — Text Generation
# =====================================================
def generate_sequence(model, total_words=30):
    start = random.choice(list(model.keys()))
    sequence = [start]

    for _ in range(total_words - 1):
        if start in model:
            start = random.choice(model[start])
        else:
            start = random.choice(list(model.keys()))

        sequence.append(start)

    return " ".join(sequence)

# =====================================================
# ▶️ Step E — Program Execution
# =====================================================
def main():
    corpus = get_corpus()
    tokens = tokenize(corpus)
    markov_model = create_markov_model(tokens)

    generated_text = generate_sequence(markov_model, 50)

    print("✅ Generated Text:\n")
    print(generated_text)

# Run main()
if __name__ == "__main__":
    main()
