import matplotlib
matplotlib.use('module://pyplotsixel') # Pour afficher directement dans le terminal
import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(18, 5), dpi=400) # Optionel

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([10, 30, 31, 25])

plt.plot(x, y1, color="red", marker=".", markersize=20, mfc="black", linestyle="dashed")
plt.plot(x, y2, color="blue", marker="*", markersize=20, mfc="black")

# Ajouter un titre
plt.title("Ceci est le titre")

# ajouter un label pour l'abscisse
plt.xlabel("Années")

# ajouter un label pour l'ordonée
plt.ylabel("Nombre")

# formatter l'abscisse
# plt.xticks(x, ["année 1", "année 2", "année 3", "année 4"])
# plt.xticks(x)
plt.xticks(np.arange(2023, 2026.25, 0.25))

# quadrillage
plt.grid()

# afficher le graphique
plt.show()
