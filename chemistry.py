import numpy as np

class Atom:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.coords = np.array([x, y, z, 1])

    def transformed(self, mat):
        return Atom(self.name, *mat.dot(self.coords))

    def __str__(self):
        return "%s at %f, %f, %f" % (self.name, self.x, self.y, self.z)

    def __repr__(self):
        return self.__str__()


class Molecule:
    def __init__(self, atoms):
        """
        Creates a molecule consisting of atoms in atoms.
        :param atoms: list of atoms .
        """
        self.atoms = atoms

    def transformed(self, mat):
        return Molecule([atom.transformed(mat) for atom in self.atoms])

    def __str__(self):
        return "\n".join(map(str, self.atoms))

    def __repr__(self):
        return self.__str__()
