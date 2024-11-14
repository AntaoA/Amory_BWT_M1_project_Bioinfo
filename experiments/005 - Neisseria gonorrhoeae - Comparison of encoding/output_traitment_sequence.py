with open("experiments/005 - Neisseria gonorrhoeae - Comparison of encoding/neisseria_gonorrhoeae__01/output_sequence.txt", "r") as f:
    output = f.read()

list_output = output.split("\n\n")

total_seq = 0
total_sym = 0
total_run = 0

for output in list_output:
    list_info = output.split("\n")
    total_seq += int(list_info[0].split(" ")[0])
    total_sym += int(list_info[1].split(" ")[0])
    total_run += int(list_info[2].split(" ")[0])
print("Total sequences:", total_seq)
print("Total symbols:", total_sym)
print("Total runs:", total_run)