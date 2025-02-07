import sys
import matplotlib.pyplot as plt


def histo(input_file):
    # Read a bwt file and return an histogram of the run lengths
    with open(input_file, 'r') as f:
        bwt = f.read()
        letter = bwt[0]
        count = 1
        histo = []
        for i in range(1, len(bwt)):
            if bwt[i] == letter:
                count += 1
            else:
                histo.append(count)
                letter = bwt[i]
                count = 1
        histo.append(count)
    return histo

def show_histo(histo):
    plt.hist(histo, bins=range(1, max(histo)+1), align='left', rwidth=0.8)
    plt.xlabel('Run length')
    plt.ylabel('Frequency')
    plt.title('Run length histogram')
    plt.show()
    
def print_histo(histo):
    for i in range(1, max(histo)+1):
        print(f"{i}: {histo.count(i)}")
    
if __name__ == "__main__":
    # run_length_stat.py [input_file]
    input_file = sys.argv[1]
    histo = histo(input_file)
    print_histo(histo)
