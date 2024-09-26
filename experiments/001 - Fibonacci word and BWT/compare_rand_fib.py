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
        print("Usage: python wrong number of arguments (need 2) : compare_fib_rand.py <rand_name> <fib_name>")
        sys.exit(1)
        
    rand_name = sys.argv[1]
    fib_name = sys.argv[2]
    
    with open(rand_name, 'r') as f:
        list_seq_rand = f.readlines()

    with open(fib_name, 'r') as f:
        list_seq_fib = f.readlines()

    
    nb_change_rand = []
    nb_change_fib = []
    linear = []
    
    for i in range(len(list_seq_rand)):
        nb_change_rand.append(nb_change(list_seq_rand[i]))
        nb_change_fib.append(nb_change(list_seq_fib[i]))
        linear.append(i)



    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(list_seq_rand)+1), nb_change_rand, label="Random sequence")
    plt.plot(range(1, len(list_seq_fib)+1), nb_change_fib, label="Fibonacci sequence")
    plt.plot(range(1, len(list_seq_fib)+1), linear, label="Linear function")
    plt.xlabel("k")
    plt.ylabel("Number of changes")
    plt.legend()
    plt.title("Number of changes in the sequence")
    plt.show()