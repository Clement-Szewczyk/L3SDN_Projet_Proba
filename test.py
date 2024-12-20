import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV avec l'encodage spécifié
file_path = "data/data2022.csv"  
df = pd.read_csv(file_path, encoding='latin-1', sep=';')  

somme = 0
df["Incendies"] = (
    df["Incendies"]
    .replace(r"[^\d]", "", regex=True)  # Supprime tout sauf les chiffres
    .astype(int)  # Convertit en int pour les calculs
)

somme += df["Incendies"].sum()

print(somme)