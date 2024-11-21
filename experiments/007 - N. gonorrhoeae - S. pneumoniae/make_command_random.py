import os
import random


file_paths1 = "experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + NG2"
file_paths2 =  "experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + SP1"


file_paths1 = os.listdir(file_paths1)
file_paths2 = os.listdir(file_paths2)

random.shuffle(file_paths1)
random.shuffle(file_paths2)

# Commande Linux à exécuter
command = "ropebwt3 build -LR -bo random.fmr"

for file in file_paths1:
    command += " " + file

with open("experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + NG2/NG_NG_random.txt", 'w') as f:
    f.write(command)
    
command = "ropebwt3 build -LR -bo random.fmr"
for file in file_paths2:
    command += " " + file

with open("experiments/007 - N. gonorrhoeae - S. pneumoniae/data/NG1 + SP1/NG_SP_random.txt", 'a') as f:
    f.write(command)