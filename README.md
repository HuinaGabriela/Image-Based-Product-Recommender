# Image-Based-Product-Recommender

sistema de recomendação baseado em similaridade de imagens, aplicação real de visão computacional
com aprendizado profundo (Deep Learning).

Objetivo do Projeto

Construir um sistema que, dado um produto (imagem), recomende outros produtos visualmente similares, sem usar dados textuais — apenas a aparência física (cor, formato, textura, etc.).

🧰 Ferramentas e Tecnologias
🧠 Deep Learning:

TensorFlow ou PyTorch – para redes neurais (usaremos modelos pré-treinados).

Keras (se for com TensorFlow) – API de alto nível para facilitar.

📷 Visão Computacional:

OpenCV – manipulação de imagens.

Matplotlib / PIL – visualização de imagens.

📦 Modelos Pré-treinados:

ResNet50, EfficientNet, VGG16, MobileNet (via Keras ou TorchVision) – para extração de embeddings.

📚 Indexação / Similaridade:

Scikit-learn – para k-NN simples.

FAISS (Facebook AI Similarity Search) – para grandes volumes, rápido e eficiente.
