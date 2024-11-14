import os
import random


file_paths = "experiments/004 - Neisseria gonorrhoeae - Comparison of orders/neisseria_gonorrhoeae__01/"


file_paths = os.listdir(file_paths)

random.shuffle(file_paths)

# Commande Linux à exécuter
command = "ropebwt3 build -LR -bo random.fmr"

for file in file_paths:
    command += " " + file


with open("experiments/004 - Neisseria gonorrhoeae - Comparison of orders/neisseria_gonorrhoeae__01/command_random.txt", 'w') as f:
    f.write(command)