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

quaternions = [(np.linalg.det(np.array(g)[:,:3])*R.from_matrix(np.linalg.det(np.array(g)[:,:3])*np.array(g)[:,:3]).as_quat()).tolist() + np.array(g)[:,3].tolist() for g in generators]

rotations, rot_inv = np.unique(np.array(quaternions)[:,:4], axis=0, return_inverse=True)
translations, trans_inv = np.unique(np.array(quaternions)[:,4:], axis=0, return_inverse=True)

# Create spacegroups matrix from generators
spacegroups = []
z = np.zeros(len(generators))
for spg, syms in gens.items():
    zz = z.copy()
    zz[spg_embeddings[spg]["indices"]] = 1
    spacegroups.append(zz.tolist())

spacegroups = np.array(spacegroups)

# Create new embedding using rotations and translations
spg_embeddings_rot_trans = []
for spg_idx in range(spacegroups.shape[0]):
    spg_vector = spacegroups[spg_idx]
    # Find which generators are used in this spacegroup
    gen_indices = np.where(spg_vector > 0)[0]
    
    # Create embedding: one-hot for rotations, one-hot for translations
    rot_embedding = np.zeros(len(rotations))
    trans_embedding = np.zeros(len(translations))
    
    for gen_idx in gen_indices:
        rot_idx = rot_inv[gen_idx]
        trans_idx = trans_inv[gen_idx]
        rot_embedding[rot_idx] = 1
        trans_embedding[trans_idx] = 1
    
    spg_embeddings_rot_trans.append(np.concatenate([rot_embedding, trans_embedding]).tolist())

spg_embeddings_rot_trans = np.array(spg_embeddings_rot_trans)

print("WARNING: spg_embeddings_rot_trans is not unique, do not use! np.unique(spg_embeddings_rot_trans, axis=0) = ",  np.shape(np.unique(spg_embeddings_rot_trans, axis=0)))

json.dump({"generators": quaternions, "spacegroups": spacegroups.tolist()}, open('spg_embeddings.json', 'w'))
#json.dump({"rotations": rotations.tolist(), "translations": translations.tolist(), "spacegroups": spg_embeddings_rot_trans.tolist()}, open('spg_embeddings_rot_trans.json', 'w'))

plt.figure(figsize=(14, 8))

plt.subplot(1, 2, 1)
plt.imshow(spacegroups.T)
plt.title("Generators-based embedding")
plt.ylabel("Generators")

plt.subplot(1, 2, 2)
plt.imshow(spg_embeddings_rot_trans.T)
plt.title("Rotations + Translations embedding")
plt.ylabel("Rotations + Translations")

plt.axvline(x=2  -1/2, color='r', linestyle='--')
plt.axvline(x=15 -1/2, color='r', linestyle='--')
plt.axvline(x=74 -1/2, color='r', linestyle='--')
plt.axvline(x=142-1/2, color='r', linestyle='--')
plt.axvline(x=168-1/2, color='r', linestyle='--')
plt.axvline(x=194-1/2, color='r', linestyle='--')

plt.tight_layout()
plt.savefig('spg_embeddings.png', dpi=300)
