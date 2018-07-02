from chemistry import Atom, Molecule


def load_struct(file_name):
    atoms = []
    with open(file_name, "r") as f:
        for line in f:
            seper = line.split()
            if seper[0] != "Energy" and len(seper) == 4:
                atoms.append(Atom(seper[0], *map(float, seper[1:])))
    return Molecule(atoms)


if __name__ == '__main__':
    struct = load_struct("/scratch/becker/o2/simple_h2o/final.xyz")
