import os
from src.extract_features import extrair_embeddings
from src.recommender import RecomendadorVisual

# Caminhos
base_dir = "data/filtrado_200"
output_path = "embeddings/features_resnet50.pkl"

# Extrair features se ainda não foram salvas
if not os.path.exists(output_path):
    extrair_embeddings(base_dir, output_path)
else:
    print("Embeddings já extraídos. Pulando etapa.")

# Criar recomendador visual
recomendador = RecomendadorVisual(output_path)

# Mostrar recomendações visuais
recomendador.recomendar(index_consulta=10, k=4)
