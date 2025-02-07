import random
import os
import sys
import re


def capture_all_texts(text):
    matches = re.findall(r'(D|S|N)[^:]*', text)  # Trouve tous les motifs qui commencent par 'd' et se terminent par ':'
    return matches



def repartition():
    nb_of_tests = 1000
    file_per_species = [0, 0, 0]
    for i in range(nb_of_tests):
        species = random.randint(0, 2)
        file_per_species[species] += 1
    print(file_per_species)
    
    
def mv_genomne(rep):
    nb_dustbin = rep[0]
    nb_ng = rep[1]
    nb_sp = rep[2]
    
    list_dustbin = os.listdir("data/dustbin")
    random.shuffle(list_dustbin)
    list_dustbin = list_dustbin[:nb_dustbin]
    
    list_ng = os.listdir("data/NG")
    random.shuffle(list_ng)
    list_ng = list_ng[:nb_ng]
    
    list_sp = os.listdir("data/SP")
    random.shuffle(list_sp)
    list_sp = list_sp[:nb_sp]
    
    for genome in list_dustbin:
        os.system(f"mv data/dustbin/{genome} data/selected_genomes/DB_{genome}")
    for genome in list_ng:
        os.system(f"mv data/NG/{genome} data/selected_genomes/NG_{genome}")
    for genome in list_sp:
        os.system(f"mv data/SP/{genome} data/selected_genomes/SP_{genome}")
    
def del_genomes():
    for genome in os.listdir("data/selected_genomes"):
        [species, gen] = genome.split("_")
        if species == "DB":
            os.system(f"mv data/selected_genomes/{genome} data/dustbin/{gen}")
        elif species == "NG":
            os.system(f"mv data/selected_genomes/{genome} data/NG/{gen}")
        elif species == "SP":
            os.system(f"mv data/selected_genomes/{genome} data/SP/{gen}")
        else:
            print("Error: unknown species")
            sys.exit(1)


# run attotree data/select_genomes/*.fa > data/attotree_output.txt
def run_attotree():
    os.system(f"attotree data/selected_genomes/*.fa > attotree_output.txt")
    
def order_genomes(order):
    genomes = os.listdir("data/selected_genomes")
    if order == "r":
        random.shuffle(genomes)
    elif order == "l":
        genomes.sort()
    elif order == "p":  
        if not os.path.exists(f"attotree_output.txt"):
            run_attotree()
        with open(f"attotree_output.txt", 'r') as f:
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
    # dustbin_NG_SP.py [type_of_order] [new_select]
    # type_of_order: r, l, p for random, lexicographic, phylogenetic
    # r by default
    # new_select: y, n for yes, no
    # n by default
    
    if len(sys.argv) > 1:
        order = sys.argv[1]
        if len(sys.argv) > 2:
            new_select = sys.argv[2]
            if new_select == "y":
                rep = repartition()
                del_genomes()
                mv_genomne(rep)
    else:
        order = "r"
    
    genomes = order_genomes(order)
            
    # Commande Linux à exécuter
    command = "ropebwt3 build -LR -bo random_dustbin_" + order + ".fmr"

    for genome in genomes:
        command += " " + genome
    
    with open("command_" + order + ".txt", 'w') as f:
        f.write(command)
    