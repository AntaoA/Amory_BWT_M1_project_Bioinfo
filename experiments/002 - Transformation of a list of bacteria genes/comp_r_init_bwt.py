import matplotlib.pyplot as plt
import sys


def nb_change(seq):
    letter = seq[0]
    nb_change = 0
    for j in range(1, len(seq)):
        if seq[j] != letter:
            nb_change += 1
            letter = seq[j]
    return nb_change


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wrong number of arguments (need 2) : comp_r_init_bwt.py <init_name> <bwt_name>")
        sys.exit(1)
        
    init_name = sys.argv[1]
    bwt_name = sys.argv[2]
    
    with open(init_name, 'r') as f:
        list_seq_init = f.readlines()

    with open(bwt_name, 'r') as f:
        list_seq_bwt = f.readlines()

    
    nb_change_init = []
    nb_change_bwt = []
    linear = []
    
    for i in range(len(list_seq_init)):
        nb_change_init.append(nb_change(list_seq_init[i]))
        nb_change_bwt.append(nb_change(list_seq_bwt[i]))
        linear.append(i)



    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(list_seq_init)+1), nb_change_init, label="Random sequence")
    plt.plot(range(1, len(list_seq_bwt+1)), nb_change_bwt, label="Fibonacci sequence")
    plt.plot(range(1, len(list_seq_bwt)+1), linear, label="Linear function")
    plt.xlabel("k")
    plt.ylabel("Number of changes")
    plt.legend()
    plt.title("Number of changes in the sequence")
    plt.show()