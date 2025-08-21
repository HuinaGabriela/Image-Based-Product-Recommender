# Image-Based-Product-Recommender

sistema de recomendação baseado em similaridade de imagens, aplicação real de visão computacional
com aprendizado profundo (Deep Learning).

Objetivo do Projeto

Construir um sistema que, dado um produto (imagem), recomende outros produtos visualmente similares, sem usar dados textuais — apenas a aparência física (cor, formato, textura, etc.).

🧰 Ferramentas e Tecnologias

tensorflow
numpy
pandas
scikit-learn
tqdm
matplotlib
Pillow


🧠 Deep Learning:

TensorFlow ou PyTorch – para redes neurais (usaremos modelos pré-treinados).

Keras (se for com TensorFlow) – API de alto nível para facilitar.

---
Remover:
criar conta no https://www.kaggle.com
criar um novo tokem API - Um arquivo chamado kaggle.json será automaticamente baixado, é sua chave de acesso pessoal para usar a API do Kaggle.

📌 Importante:


⚠️ Para utilizar este notebook, você precisa gerar sua própria chave da API do Kaggle (kaggle.json) em: https://www.kaggle.com/account

---

📷 Visão Computacional:

OpenCV – manipulação de imagens.

Matplotlib – visualização de imagens.

📦 Modelos Pré-treinados:

ResNet50– para extração de embeddings.

📚 Indexação / Similaridade:

Scikit-learn – para k-NN simples.

FAISS (Facebook AI Similarity Search) – para grandes volumes, rápido e eficiente.
