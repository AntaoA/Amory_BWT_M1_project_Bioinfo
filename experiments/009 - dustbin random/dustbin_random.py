import random
import os
import sys
import re

def capture_all_texts(text):
    matches = re.findall(r'd[^:]*', text)  # Trouve tous les motifs qui commencent par 'd' et se terminent par ':'
    return matches


# select 1k random genomes from dustbin batches

batches_path = [f"data/dustbin__{i:02d}" for i in range(1, 23)]

def select_random_genomes(nb):
    genomes_list = []
    for batch in batches_path:
        genomes = os.listdir(batch)
        genomes = [f"{batch}/{genome}" for genome in genomes]
        genomes_list.extend(genomes)
    random.shuffle(genomes_list)
    return genomes_list[:nb]

path_attotree = "data/selected_genomes/"

def del_genomes():
    for genome in os.listdir(path_attotree):
        if genome.endswith(".fa"):
            gen = genome.split("+")[0] +"/"+ genome.split("+")[1]
            os.system(f"mv {path_attotree}{genome} data/{gen}")
        else:
            os.system(f"rm {path_attotree}{genome}")
            
def move_genomes(genomes):
    for genome in genomes:
        gen = genome.split("/")[1] +"+"+ genome.split("/")[2]
        os.system(f"mv {genome} {path_attotree}{gen}")


# run attotree data/select_genomes/*.fa > data/attotree_output.txt
def run_attotree():
    os.system(f"attotree data/selected_genomes/*.fa > {path_attotree}attotree_output.txt")

def order_genomes(genomes, order):
    if order == "r":
        random.shuffle(genomes)
    elif order == "l":
        genomes.sort()
    elif order == "p":  
        if not os.path.exists(f"{path_attotree}attotree_output.txt"):
            run_attotree()
        with open(f"{path_attotree}attotree_output.txt", 'r') as f:
            genomes = capture_all_texts(f.read())
            gens = []
            for genome in genomes:
                gen = "data/selected_genomes/" + genome + ".fa"
                gens.append(gen)
            genomes = gens
            
    else:
        print("Invalid order type. Using random order.")
        random.shuffle(genomes)
    return genomes

def run_command(command):
    os.system(command)


if __name__ == "__main__":
    # dustbin_random.py [type_of_order] [new_select] [nb]
    # type_of_order: r, l, p for random, lexicographic, phylogenetic
    # r by default
    # new_select: y, n for yes, no
    # n by default
    
    if len(sys.argv) > 1:
        order = sys.argv[1]
        if len(sys.argv) > 2:
            new_select = sys.argv[2]
            nb = int(sys.argv[3])
            if new_select == "y":
                genomes = select_random_genomes(nb)
                del_genomes()
                move_genomes(genomes)
            genomes = os.listdir(path_attotree)
            genomes = [f"{path_attotree}{genome}" for genome in genomes]
    else:
        order = "r"
    print(genomes[0])
    genomes = order_genomes(genomes, order)
            
    # Commande Linux à exécuter
    command = "ropebwt3 build -bo random_dustbin_" + order + ".bwt"

    for genome in genomes:
        command += " " + genome
    
    with open("command_" + order + ".txt", 'w') as f:
        f.write(command)
    