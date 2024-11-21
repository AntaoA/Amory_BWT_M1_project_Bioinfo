
k = 1000000


from create_seq import generate_sequence
seq = generate_sequence("r", k)


with open("k_rand_seq.txt", 'w') as f:
    for i in range(1,k):
        if (i % (k//100)) == 0:
            print(f"{i/(k//100)}%")
            f.write(seq[:i])
            f.write("\n")