import os
import glob
from collections import Counter

# Chemin des fichiers triés (p_aa_h.txt → p_bm_h.txt)
files = sorted(glob.glob("p_*_h.txt"))

# Stockage de l'histogramme fusionné
global_histo = Counter()
prev_last_char = None
prev_last_run_length = 0

with open("merged_histo.txt", "w") as output:
    for file in files:
        with open(file, "r") as f:
            # Lecture de la première ligne (first/last letters et run lengths)
            bla, first_char = f.readline().strip().split()
            bla, first_run_length = f.readline().strip().split()
            bla, last_char = f.readline().strip().split()
            bla, last_run_length = f.readline().strip().split()
            first_run_length, last_run_length = int(first_run_length), int(last_run_length)

            # Lecture et fusion de l'histogramme du fichier actuel
            for line in f:
                run_length, count = map(int, line.strip().split())
                global_histo[run_length] += count

            # Fusion des runs si le dernier char du fichier précédent == premier char du fichier actuel
            if prev_last_char == first_char:
                combined_run = prev_last_run_length + first_run_length
                global_histo[combined_run] += 1  # Ajout du run fusionné
                global_histo[prev_last_run_length] -= 1  # Retrait des runs fusionnés
                global_histo[first_run_length] -= 1
                

            # Mise à jour des valeurs pour le prochain fichier
            prev_last_char = last_char
            prev_last_run_length = last_run_length

    # Écriture du fichier final trié
    for length, count in sorted(global_histo.items()):
        output.write(f"{length} {count}\n")

print("Fusion terminée. Résultats enregistrés dans 'merged_histo.txt'.")
