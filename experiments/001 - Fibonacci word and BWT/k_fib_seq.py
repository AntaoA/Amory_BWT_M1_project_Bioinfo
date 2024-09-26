
k = 1000


from create_seq import generate_sequence
seq = generate_sequence("fib", k)


with open("k_fib_seq.txt", 'w') as f:
    for i in range(1,k):
        f.write(seq[:i])
        f.write("\n")