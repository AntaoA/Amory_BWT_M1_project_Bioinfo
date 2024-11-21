import sys
from create_seq import generate_sequence

def write_to_file(sequence, filename="sequence_test.txt"):
    with open(filename, 'w') as f:
        f.write(sequence)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wrong number of arguments (need 2) : bwt.py <sequence_type> <n>")
        print("sequence_type: 'r' or 'fib'")
        print("n: Length of the sequence")
        sys.exit(1)
    
    sequence_type = sys.argv[1]  # Le premier argument est le type de séquence
    n = int(sys.argv[2])  # Le second argument est la longueur de la séquence
    
    # Génération de la séquence
    sequence = generate_sequence(sequence_type, n)
    
    # Écriture de la séquence dans le fichier
    name_type = "random" if sequence_type == "r" else "fibonacci"
    write_to_file(sequence)
    print(f"La séquence de type'{name_type}' : '{sequence}' a été écrite dans le fichier 'sequence_test.txt'.")
