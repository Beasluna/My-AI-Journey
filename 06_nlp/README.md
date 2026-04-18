# 🧠 Natural Language Processing (NLP) Lab

[ES] En este módulo comparo dos arquitecturas fundamentales para el análisis de sentimiento utilizando el dataset IMDB. El objetivo es documentar la transición desde los métodos secuenciales clásicos hacia los modelos modernos basados en mecanismos de atención.

[EN] In this module, I compare two fundamental architectures for sentiment analysis using the IMDB dataset. The goal is to document the transition from classical sequential methods to modern attention-based models.

---

## 📂 Estructura del Módulo | Module Structure

### 1. [Bi-LSTM Sentiment Analysis](lstm_sentiment/)
* **[ES] Arquitectura:** Red Neuronal Recurrente Bidireccional (Bi-LSTM). Ideal para aprender secuencias leyendo el texto en ambas direcciones.
* **[EN] Architecture:** Bidirectional LSTM (Bi-LSTM). Ideal for learning sequences by reading text in both directions.

### 2. [Transformer Sentiment Analysis](transformer_sentiment/)
* **[ES] Arquitectura:** Transformer Encoder (Self-Attention). Utiliza el mecanismo de atención para procesar toda la secuencia de forma paralela.
* **[EN] Architecture:** Transformer Encoder (Self-Attention). Uses the attention mechanism to process the entire sequence in parallel.

---

## 🔬 Comparativa Técnica | Technical Comparison

| Característica / Feature | Bi-LSTM | Transformer (Encoder) |
| :--- | :--- | :--- |
| **Procesamiento** | Secuencial | Paralelo |
| **Memoria** | Hidden State | Self-Attention (Contexto global) |
| **Uso Principal** | Gramática local | Semántica compleja |




---

## 🛠 Instrucciones de uso | Usage Instructions

[ES] Para ejecutar estos modelos, asegúrate de tener instaladas las dependencias básicas:
[EN] To run these models, ensure you have the basic dependencies installed:

```bash
pip install torch transformers pandas scikit-learn

Nota: Los archivos .pth (pesos del modelo) no están subidos al repositorio por su tamaño. Puedes entrenarlos tú misma usando los notebooks proporcionados.
Note: The .pth (model weights) files are not uploaded due to their size. You can train the models yourself using the provided notebooks.

Building the future, line by line. 🤖
