import sys
from collections import Counter

def histo_optimized(input_file):
    """ Lit un fichier en streaming et construit un histogramme des longueurs de runs. """
    """ Garde en mémoire la première lettre, la longueur du premier run, la dernière lettre, la longueur de la dernière run et l'histogramme """
    histo = []
    with open(input_file, 'r') as f:
        prev_char = None
        run_length = 0
        first_char = ''
        last_char = ''
        first_length = 1
        last_length = 0
        is_first = True

        for char in f.read():
            if char == '\n':
                histo.append(run_length)
                continue
            if char == prev_char:
                run_length += 1
            else:
                if is_first and (run_length > 0):
                    first_char = prev_char
                    first_length = run_length
                    is_first = False
                if run_length > 0:
                    histo.append(run_length)
                prev_char = char
                run_length = 1
            last_char = char
            last_length = run_length
            print(f'char {char} first_char {first_char} first_length {first_length} last_char {last_char} last_length {last_length}')
    return histo, first_char, first_length, last_char, last_length

def write_histo_optimized(histo, first_char, first_length, last_char, last_length, out):
    """ Affiche l'histogramme des longueurs de runs sous forme de texte. """
    histo_count = Counter(histo)
    with open(out, 'w') as f:
        f.write(f'first_char {first_char}\n')
        f.write(f'first_length {first_length}\n')
        f.write(f'last_char {last_char}\n')
        f.write(f'last_length {last_length}\n')
        for length, count in sorted(histo_count.items()):
            f.write(f'{length} {count}\n')

if __name__ == "__main__":
    # run_length_stat.py [input_file]
    input_file = sys.argv[1]
    out_file = sys.argv[2]
    histo, first_char, first_length, last_char, last_length = histo_optimized(input_file)
    write_histo_optimized(histo, first_char, first_length, last_char, last_length, out_file)