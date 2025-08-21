import pickle
import numpy as np
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from PIL import Image

class RecomendadorVisual:
    def __init__(self, embeddings_path, n_vizinhos=5):
        with open(embeddings_path, "rb") as f:
            self.data = pickle.load(f)

        self.features = np.array(self.data["features"])
        self.modelo_nn = NearestNeighbors(n_neighbors=n_vizinhos + 1, metric='euclidean')
        self.modelo_nn.fit(self.features)

    def recomendar(self, index_consulta, k=5):
        distancias, indices = self.modelo_nn.kneighbors([self.features[index_consulta]], n_neighbors=k+1)

        print(f"Consulta: {self.data['paths'][index_consulta]}")
        plt.figure(figsize=(15, 4))

        # Mostrar imagem de consulta
        img = Image.open(self.data["paths"][index_consulta])
        plt.subplot(1, k+1, 1)
        plt.imshow(img)
        plt.title("Consulta")
        plt.axis('off')

        # Mostrar imagens similares
        for i, idx in enumerate(indices[0][1:]):
            img_similar = Image.open(self.data["paths"][idx])
            plt.subplot(1, k+1, i+2)
            plt.imshow(img_similar)
            plt.title(f"Similar {i+1}")
            plt.axis('off')

        plt.show()
