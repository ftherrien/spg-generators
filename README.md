# Space Group Generators Database

This repository contains crystallographic generators extracted from the [Bilbao Crystallographic Server](https://cryst.ehu.es/index.html) for all 230 space groups.

## Contents

- **generator_database.json** - File containing generators for each space group
  - Keys: space group numbers (1-230)
  - Values: sets of generator matrices (4x3 format)

- **spg_embeddings** - File containing a disctionary withs keys "spacegroups" and "generators".
  		     - "spacegroups" contains generator embedding (83) for each space groups (230) as a 230x83 matrix
		     - "spacegroups" contains a 83x7 matrix of all generators where a generator is represented as a quaternion of length 4 (rotation/inversion) and a translation of length 3

## Data Source

Generators were extracted from the Bilbao Crystallographic Server.
