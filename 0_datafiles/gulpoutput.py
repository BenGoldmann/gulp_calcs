import re
import glob

def getEnergy(path):
    with open(path) as file:
        content = file.readlines()
    for line in content:
        if "Final defect energy" in line:
            return float(re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", line)[0])

def getLatticeEnergy(path):
    with open(path) as file:
        content = file.readlines()
    for line in content:
        if "Final energy" in line:
            return float(re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", line)[0])

def energyList(data):
    files = glob.glob(data)
    energies = dict()
    for f in files:
        energies[f] = getEnergy(f)
    return energies
        
def latticeEnergy(data):
    lattice_energy = getLatticeEnergy(data)
    return lattice_energy

energies = energyList('*.out')
lattice_energy = latticeEnergy('nacl_na_imig.out')

magic = open('output.txt', 'w+')

magic.write("Cl vacancy defect energy: " + str(energies['nacl_cl_vac.out']) + " eV" + "\n")
magic.write("Cl vacancy migration barrier: " + str(energies['nacl_cl_vmig.out'] - energies['nacl_cl_vac.out']) + " eV" + "\n")
magic.write("Cl interstitial defect energy: " + str(energies['nacl_cl_int.out']) + " eV" + "\n")
magic.write("Cl interstitial migration barrier: " + str(energies['nacl_cl_imig.out'] - energies['nacl_cl_int.out']) + " eV" + "\n")
magic.write("\n")
magic.write("Na vacancy defect energy: " + str(energies['nacl_na_vac.out']) + " eV" + "\n")
magic.write("Na vacancy migration barrier: " + str(energies['nacl_na_vmig.out'] - energies['nacl_na_vac.out']) + " eV" + "\n")
magic.write("Na interstitial defect energy: " + str(energies['nacl_na_int.out']) + " eV" + "\n")
magic.write("Na interstitial migration barrier: " + str(energies['nacl_na_imig.out'] - energies['nacl_na_int.out']) + " eV" + "\n")
magic.write("\n")
magic.write("NaCl Schottky defect energy: " + str(energies['nacl_na_vac.out'] + energies['nacl_cl_vac.out'] + lattice_energy) + " eV" + "\n")
magic.write("Cl Frenkel defect energy: " + str(energies['nacl_cl_vac.out'] + energies['nacl_cl_int.out']) + " eV" + "\n")
magic.write("Na Frenkel defect energy: " + str(energies['nacl_na_vac.out'] + energies['nacl_na_int.out']) + " eV" + "\n")
magic.write("Lattice energy: " + str(lattice_energy) + " eV" + "\n")

magic.close()