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



## 💾 Model Weights | Pesos del Modelo
[ES] Debido a restricciones de tamaño, los pesos de los modelos están alojados en Google Drive:

- [📥 Bi-LSTM Weights (model.pth)](https://drive.google.com/file/d/1v3vZIhzwcnSR_Zf6e2yvvg6zxvFT7NNo/view?usp=drive_link)
- [📥 Transformer Weights (model_transformer1.pth)](https://drive.google.com/file/d/1E285T6fi5twBebOPIIwkaBHF6dfssKgL/view?usp=drive_link)


Building the future, line by line. 🤖
