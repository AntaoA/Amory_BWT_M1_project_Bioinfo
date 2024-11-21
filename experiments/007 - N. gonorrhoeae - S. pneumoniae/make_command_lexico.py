import os


file_paths1 = "experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + NG2"
file_paths2 = "experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + SP1"


file_paths1 = os.listdir(file_paths1)
file_paths2 = os.listdir(file_paths2)

file_paths1.sort()
file_paths2.sort()

# Commande Linux à exécuter
command = "ropebwt3 build -LR -bo NG_NG_lexico.fmr"

for file in file_paths1:
    command += " " + file


with open("experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + NG2/command_lexico_NG_NG.txt", 'w') as f:
    f.write(command)
    
command = "ropebwt3 build -LR -bo NG_SP_lexico.fmr"

for file in file_paths2:
    command += " " + file


with open("experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + SP1/command_lexico_NG_SP.txt", 'w') as f:
    f.write(command)