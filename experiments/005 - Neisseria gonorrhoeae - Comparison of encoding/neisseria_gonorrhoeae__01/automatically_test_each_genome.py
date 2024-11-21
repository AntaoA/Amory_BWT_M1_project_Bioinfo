#it's important to be in the right environment, especially because vscode is not the same environment as the terminal
#so I run this program in the terminal, in the folder where the file is located

import subprocess
import os

list_files = os.listdir()

list_output = []
for file in list_files:
    if file[0] != 'S':
        continue
    command1 = "ropebwt3 build -LR -bo " + file + ".fmr " + file
    subprocess.run(command1, shell=True)
    command2 = "ropebwt3 stat " + file + ".fmr"
    output = subprocess.run(command2, shell=True, capture_output=True)
    list_output.append(output.stdout.decode())
    command3 = "rm " + file + ".fmr"
    subprocess.run(command3, shell=True)

with open("output_genome.txt", 'w') as f:
    f.write("\n".join(list_output))
