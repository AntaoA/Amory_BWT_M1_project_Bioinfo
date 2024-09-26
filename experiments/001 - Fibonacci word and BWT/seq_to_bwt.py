import os
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wrong number of arguments (need 2) : seq_to_bwt.py <input_name> <output_name>")
        sys.exit(1)
        
    input_name = sys.argv[1]
    output_name = sys.argv[2]
    
    with open(input_name, 'r') as f:
        list_seq = f.readlines()

    list_seq_bwt = []
    
    for seq in list_seq:
        seq = seq.strip()
        pipe = os.popen(f"echo {seq} | ropebwt3 build -LR -")
        seq_bwt = pipe.read()
        seq_bwt = seq_bwt.split("[")
        seq_bwt = seq_bwt[0]
        list_seq_bwt.append(seq_bwt)
        pipe.close()
    
    with open(output_name, 'w') as f:
        for l in list_seq_bwt:
            f.write(l)
