import os


file_paths = "experiments/004 - Neisseria gonorrhoeae - Comparison of orders/neisseria_gonorrhoeae__01/"



file_paths = os.listdir(file_paths)

file_paths.sort()

# Commande Linux à exécuter
command = "ropebwt3 build -LR -bo lexico.fmr"

for file in file_paths:
    command += " " + file


with open("experiments/004 - Neisseria gonorrhoeae - Comparison of orders/neisseria_gonorrhoeae__01/command_lexico.txt", 'w') as f:
    f.write(command)