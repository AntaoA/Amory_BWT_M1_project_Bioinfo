import re

def capture_all_texts(text):
    matches = re.findall(r'S[^:]*', text)  # Trouve tous les motifs qui commencent par 'S' et se terminent par ':'
    return matches

with open("experiments/004 - Neisseria gonorrhoeae - Comparison of orders/phylogenetic.txt", 'r') as f:
    list_files = capture_all_texts(f.read())


# Commande Linux à exécuter
command = "ropebwt3 build -LR -bo phylogenetic.fmr"

for file in list_files:
    command += " " + file + ".fa"


with open("experiments/004 - Neisseria gonorrhoeae - Comparison of orders/neisseria_gonorrhoeae__01/command_phylogenetic.txt", 'w') as f:
    f.write(command)