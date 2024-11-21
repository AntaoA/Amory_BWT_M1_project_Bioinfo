import re

def capture_all_texts(text):
    matches = re.findall(r'S[^:]*', text)  # Trouve tous les motifs qui commencent par 'S' et se terminent par ':'
    return matches

with open("experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + NG2/NG_NG_phylogenetic.txt", 'r') as f:
    list_files = capture_all_texts(f.read())


# Commande Linux à exécuter
command = "ropebwt3 build -LR -bo NG_NG_phylogenetic.fmr"

for file in list_files:
    command += " " + file + ".fa"


with open("experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + NG2/command_phylogenetic_NG_NG.txt", 'w') as f:
    f.write(command)
    
with open("experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + SP1/NG_SP_phylogenetic.txt", 'r') as f:
    list_files = capture_all_texts(f.read())


# Commande Linux à exécuter
command = "ropebwt3 build -LR -bo NG_SP_phylogenetic.fmr"

for file in list_files:
    command += " " + file + ".fa"


with open("experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + SP1/command_phylogenetic_NG_SP.txt", 'w') as f:
    f.write(command)
    
