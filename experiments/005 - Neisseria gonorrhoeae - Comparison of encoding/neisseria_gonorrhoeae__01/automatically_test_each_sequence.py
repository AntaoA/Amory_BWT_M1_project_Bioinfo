#it's important to be in the right environment, especially because vscode is not the same environment as the terminal
#so I run this program in the terminal, in the folder where the file is located

import subprocess
import os

list_files = os.listdir()

list_output = []

for file in list_files:
    if file[0] != 'S':
        continue
    with open(file) as f:
        lines = f.read().split("\n")
        for line in lines:
            if line == '':
                continue
            if line[0] == '>':
                continue
            with open("file.txt", 'w') as g:
                g.write(line)
            command1 = "ropebwt3 build -LR -bo file.fmr file.txt"
            subprocess.run(command1, shell=True)
            
            command2 = "ropebwt3 stat file.fmr"
            output = subprocess.run(command2, shell=True, capture_output=True)
            
            list_output.append(output.stdout.decode())
            
            command3 = "rm file.fmr"
            subprocess.run(command3, shell=True)
            
            command4 = "rm file.txt"
            subprocess.run(command4, shell=True)

with open("output_sequence.txt", 'w') as f:
    f.write("\n".join(list_output))
