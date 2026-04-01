# Space Group Generators Database

This repository contains crystallographic generators extracted from the [Bilbao Crystallographic Server](https://cryst.ehu.es/index.html) for all 230 space groups.

## Contents

- **generator_database.json** - Main data file containing generators for each space group
  - Keys: space group numbers (1-230)
  - Values: sets of generator matrices (4x3 format)

## Format

Each space group entry contains a list of 4×3 matrices representing the generators for that crystallographic space group.

## Data Source

Generators were extracted from the Bilbao Crystallographic Server.
