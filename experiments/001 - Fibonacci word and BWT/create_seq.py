import random



def random_sequence(n):
    DNA = ['A', 'C', 'G', 'T']
    return "".join(random.choices(DNA, k=n))

def fibonacci_word(n):
    if n == 0:
        return ""
    if n == 1:
        return "A"
    sequence_start = "A"
    for _ in range(n-1):
        sequence = ""
        for i in range(len(sequence_start)):
            if sequence_start[i] == 'A':
                sequence = sequence + "AC"
            else:
                sequence = sequence + "A" 
        sequence_start = sequence 
    return sequence


def fibonacci_length(k):
    n = 0
    while len(fibonacci_word(n)) < k:
        n += 1
    return fibonacci_word(n)[:k]

def generate_sequence(sequence_type, n):
    if sequence_type == "r":
        return random_sequence(n)
    elif sequence_type == "fib":
        return fibonacci_length(n)
    else:
        raise ValueError("Invalid sequence type. Choose 'r' or 'fib'.")
