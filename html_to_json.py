import json
import re
import numpy as np

generator_database = {}
for i in range(1, 231):
    filename = "htmls/spg_%d.html"%i
    with open(filename) as f:
        html = f.read()
        generators = re.findall("<pre>(.*\n.*\n.*)<\/pre>", html)
        generators = [[[float(eval(e)) for e in row.split()] for row in generator.split("\n")] for generator in generators]
        generator_database[i] = generators

with open("generator_database.json", "w") as f:
    json.dump(generator_database, f, indent=4)

