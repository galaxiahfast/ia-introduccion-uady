# 🤖 Introducción a la Inteligencia Artificial

<p align="center">
  <strong>Maestría en Inteligencia Artificial · Facultad de Matemáticas</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=flat-square&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/scikit--learn-Machine%20Learning-F7931E?style=flat-square&logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=flat-square&logo=pytorch&logoColor=white">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=flat-square&logo=opencv&logoColor=white">
  <img src="https://img.shields.io/badge/LLM-RAG-8A2BE2?style=flat-square">
</p>

<p align="center">
  Repositorio de prácticas, experimentos y proyecto final de la asignatura
  <strong>Introducción a la Inteligencia Artificial</strong>.
</p>

---

## Overview

Este repositorio implementa los principales paradigmas de **Inteligencia Artificial**, desde algoritmos clásicos de búsqueda y razonamiento hasta **Machine Learning, Reinforcement Learning, Computer Vision, LLMs y RAG**.

El objetivo es transformar los conceptos teóricos de la asignatura en implementaciones reproducibles, experimentos y soluciones computacionales.

```text
                    Artificial Intelligence
                             │
          ┌──────────────────┼──────────────────┐
          ▼                  ▼                  ▼
       Classical             ML                GenAI
          AI                 │                  │
          │          ┌───────┼───────┐          │
          ▼          ▼       ▼       ▼          ▼
       Search     Supervised  Unsupervised   LLM / RAG
       Agents     Neural Nets   RL           NLP
       Logic      Clustering   Q-Learning     Embeddings
       Bayesian
```

La asignatura contempla cuatro unidades: fundamentos de IA; razonamiento y cómputo evolutivo; aprendizaje automático y visión computacional; y modelos de lenguaje y generación aumentada.

---

## 🧠 Topics

| Área                       | Implementaciones                                  |
| -------------------------- | ------------------------------------------------- |
| **Agents**                 | Reactive Agents, PEAS, Grid World                 |
| **Search**                 | BFS, DFS, UCS, Greedy, A*                         |
| **Logic**                  | Propositional Logic, First-Order Logic, Inference |
| **Probabilistic AI**       | Bayes, Bayesian Networks                          |
| **Evolutionary Computing** | Genetic Algorithms, Local Search                  |
| **Machine Learning**       | Decision Trees, MLP, K-Means                      |
| **Reinforcement Learning** | Q-Learning, Grid World                            |
| **Computer Vision**        | Image Processing, Classification                  |
| **LLMs**                   | Tokenization, Embeddings, Prompt Engineering      |
| **RAG**                    | Retrieval Pipeline, Document Indexing             |

Estos temas corresponden al contenido técnico establecido para las cuatro unidades de la asignatura.

---

## ⚙️ Tech Stack

**Core**

`Python 3.10+` · `NumPy` · `Matplotlib` · `NetworkX`

**Machine Learning**

`scikit-learn` · `pgmpy`

**Deep Learning**

`PyTorch` · `TensorFlow` · `Keras`

**Computer Vision**

`OpenCV`

**Reinforcement Learning**

`Gymnasium`

**LLM / NLP**

`Hugging Face Transformers` · `LangChain` · `LLM APIs`

**Environment**

`JupyterLab` · `Jupyter Notebook` · `VS Code`

El stack se basa en las herramientas indicadas como recursos de apoyo de la asignatura.

---

## 📁 Project Structure

```text
.
├── 01-fundamentos/
│   ├── agents/
│   ├── search/
│   │   ├── bfs/
│   │   ├── dfs/
│   │   ├── ucs/
│   │   └── astar/
│   └── notebooks/
│
├── 02-razonamiento/
│   ├── logic/
│   ├── bayesian/
│   ├── decision-trees/
│   └── genetic-algorithms/
│
├── 03-machine-learning/
│   ├── mlp/
│   ├── kmeans/
│   ├── q-learning/
│   └── computer-vision/
│
├── 04-llm-rag/
│   ├── prompting/
│   ├── embeddings/
│   ├── llm/
│   └── rag/
│
├── proyecto-final/
│   ├── src/
│   ├── data/
│   ├── notebooks/
│   └── README.md
│
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone

```bash
git clone https://github.com/<username>/<repository>.git
cd <repository>
```

### 2. Virtual Environment

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch

```bash
jupyter lab
```

---

## 🔬 Implementations

### Search Algorithms

Comparación de algoritmos mediante:

* Completeness
* Optimality
* Time complexity
* Space complexity
* Heuristic performance

Incluye implementaciones de **BFS, DFS, UCS y A*** sobre problemas de búsqueda.

### Machine Learning

Modelos introductorios para:

```text
Dataset
   │
   ▼
Preprocessing
   │
   ▼
Training
   │
   ▼
Evaluation
   │
   ├── Accuracy
   ├── Precision
   ├── Recall
   └── F1
```

Incluye árboles de decisión, MLP y clustering mediante K-Means.

### Reinforcement Learning

Implementación de **Q-Learning** sobre entornos simples:

```text
Agent ── action ──► Environment
  ▲                    │
  │                    ▼
  └──── reward ◄──── State
```

Se estudia particularmente el equilibrio entre **exploration** y **exploitation**.

### LLM & RAG

Pipeline conceptual:

```text
Documents
    │
    ▼
Chunking
    │
    ▼
Embeddings
    │
    ▼
Vector Index
    │
    ▼
Retriever
    │
    ▼
Relevant Context
    │
    ▼
LLM
    │
    ▼
Generated Response
```

La asignatura contempla tokenización, embeddings, Transformers, prompting, evaluación de LLMs y construcción de pipelines RAG.

---

## 📊 Experiments

Cada práctica busca mantener una estructura reproducible:

```text
Input
  ↓
Preprocessing
  ↓
Algorithm / Model
  ↓
Inference
  ↓
Evaluation
  ↓
Visualization
```

Los notebooks documentan el proceso experimental, resultados y conclusiones de cada implementación.

---

## 🎯 Final Project

Proyecto integrador orientado a resolver un problema utilizando uno o varios paradigmas estudiados durante la asignatura.

Posibles líneas:

* Search & Optimization
* Intelligent Agents
* Probabilistic Reasoning
* Machine Learning
* Reinforcement Learning
* Computer Vision
* LLM Applications
* Retrieval-Augmented Generation

El proyecto contempla implementación, resultados, documentación y presentación como parte del portafolio digital.

---

## 📚 References

* Russell & Norvig — *Artificial Intelligence: A Modern Approach*
* Sutton & Barto — *Reinforcement Learning: An Introduction*
* Tunstall, Von Werra & Wolf — *Natural Language Processing with Transformers*
* Aggarwal — *Neural Networks and Deep Learning*
* Eiben & Smith — *Introduction to Evolutionary Computing*

Bibliografía basada en las referencias oficiales de la asignatura.

---

## 👨‍💻 Author

**Julián Emiliano Ortiz Rivero**

Maestría en Inteligencia Artificial

---

<p align="center">
  <sub>Academic AI Portfolio · 2026</sub>
</p>
