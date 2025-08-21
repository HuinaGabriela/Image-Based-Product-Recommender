import os
import pickle
import numpy as np
from tqdm import tqdm
from tensorflow.keras.applications import ResNet50
from src.utils import carregar_e_processar_imagem

def extrair_embeddings(base_dir, output_path):
    modelo = ResNet50(weights='imagenet', include_top=False, pooling='avg')

    categorias = [cat for cat in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, cat))]
    
    features = []
    imagem_paths = []
    categorias_imagem = []

    for categoria in categorias:
        pasta_categoria = os.path.join(base_dir, categoria)
        for nome_arquivo in tqdm(os.listdir(pasta_categoria), desc=f"Processando {categoria}"):
            caminho_imagem = os.path.join(pasta_categoria, nome_arquivo)
            try:
                img_tensor = carregar_e_processar_imagem(caminho_imagem)
                embedding = modelo.predict(img_tensor, verbose=0)
                features.append(embedding.flatten())
                imagem_paths.append(caminho_imagem)
                categorias_imagem.append(categoria)
            except Exception as e:
                print(f"Erro ao processar {caminho_imagem}: {e}")
    
    with open(output_path, "wb") as f:
        pickle.dump({
            "features": features,
            "paths": imagem_paths,
            "labels": categorias_imagem
        }, f)
    
    print(f"Embeddings salvos em {output_path}")
