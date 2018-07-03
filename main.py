from loader import load_struct
from chemistry import Atom, Cluster, Molecule
from copy import copy
import os, time
from shutil import copyfile
import subprocess


if __name__ == '__main__':
    with open('./def.def', 'r') as content_file:
        def_content = content_file.read()
        init_h2o = load_struct("/scratch/becker/o2/simple_h2o/final.xyz")
        o2 = load_struct("/scratch/becker/o2/simple_o2/final.xyz")
        init_h = Molecule([Atom('H', 0, 0, 0)])
        h2os = [copy(init_h2o) for _ in range(4)]
        h = copy(init_h)
    while True:
        h.translate_random(dist=7)
        for h2o in h2os:
            h2o.translate_random(dist=7)
        initial_cluster = Cluster(o2, h, *h2os)
        with open("./calc/tst.def", 'w') as out_def:
            out_def.write(def_content.format(name="initial cluster",
                                             coord_def=initial_cluster.to_def(),
                                             basis="all def2-TZVP"))
        open("./calc/CALC", 'a').close()
        while not os.path.exists("./calc/DONE"):
            time.sleep(1)
        min_en = 0
        try:
            with open("./calc/energy", "r") as energy_f:
                for line in energy_f:
                    seper = line.split()
                    if len(seper) == 4:
                        try:
                            min_en = float(seper[1])
                        except:
                            pass
            copyfile("./calc/final.xyz", "./structs/" + str(min_en) + ".xyz")
        except:
            pass
        for f in os.listdir("./calc"):
            if f != "do_calc.sh":
                os.remove(os.path.join("./calc", f))

