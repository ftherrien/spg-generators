import json
from scipy.spatial.transform import Rotation as R
import numpy as np
import matplotlib.pyplot as plt

gens = json.load(open('generator_database.json'))

generators = []
spg_embeddings = {}

for spg, syms in gens.items():
    spg_embeddings[spg] = {"indices": []}
    for s in syms:
        if s not in generators:
            generators.append(s)
            spg_embeddings[spg]["indices"].append(len(generators)-1)
        else:
            spg_embeddings[spg]["indices"].append(generators.index(s))

quaternions = [R.from_matrix(np.array(g)[:,:3]).as_quat().tolist() + np.array(g)[:,3].tolist() for g in generators]

spacegroups = []
z = np.zeros(len(generators))
for spg, syms in gens.items():
    zz = z.copy()
    zz[spg_embeddings[spg]["indices"]] = 1
    spacegroups.append(zz.tolist())


json.dump({"generators": quaternions, "spacegroups": spacegroups}, open('spg_embeddings.json', 'w'))

plt.imshow(np.array(spacegroups).T)

plt.axvline(x=2  -1/2, color='r', linestyle='--')
plt.axvline(x=15 -1/2, color='r', linestyle='--')
plt.axvline(x=74 -1/2, color='r', linestyle='--')
plt.axvline(x=142-1/2, color='r', linestyle='--')
plt.axvline(x=168-1/2, color='r', linestyle='--')
plt.axvline(x=194-1/2, color='r', linestyle='--')

plt.savefig('spg_embeddings.png', dpi=300)

