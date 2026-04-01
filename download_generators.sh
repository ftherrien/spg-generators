#!/bin/bash

mkdir htmls

for i in {1..230}
do
    curl -o "htmls/spg_$i.html" "https://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-getgen?gnum=$i"
done
