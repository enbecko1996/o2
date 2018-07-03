import numpy as np
from linalg_helper import translate_mat, get_normalized_random_direction


class Atom:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.coords = np.array([x, y, z, 1])

    def transform(self, mat):
        self.coords = np.array(mat.dot(self.coords))
        return self

    def __str__(self):
        return "%s at %f, %f, %f" % (self.name, self.x, self.y, self.z)

    def __repr__(self):
        return self.__str__()

    def __copy__(self):
        return Atom(self.name, *self.coords[:-1])


class Molecule:
    def __init__(self, atoms):
        """
        Creates a molecule consisting of atoms in atoms.
        :param atoms: list of atoms .
        """
        self.atoms = list(atoms)

    def transform(self, mat):
        for atom in self.atoms:
            atom.transform(mat)
        return self

    def translate_random(self, dist=1):
        self.transform(translate_mat(*(dist * get_normalized_random_direction())))

    def __str__(self):
        return "[" + "\n".join(map(str, self.atoms)) + "]"

    def __repr__(self):
        return self.__str__()

    def to_def(self):
        out = ""
        for atom in self.atoms:
            out += atom.name + '\n'
            out += ' '.join(map(str, atom.coords[:-1])) + '\n'
            out += "*\n"
        return out

    def __copy__(self):
        return Molecule(map(Atom.__copy__, self.atoms))


class Cluster:
    def __init__(self, *molecules):
        self.molecules = list(molecules)

    def to_def(self):
        return ''.join(map(Molecule.to_def, self.molecules))



