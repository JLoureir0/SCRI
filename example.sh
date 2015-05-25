#!/bin/bash
./cppversion/cppVersion input/readings output/v1
java -jar javaversion/scri.jar input/readings output/v2
python pyversion/main.py input/readings output/v3
python voter/voter.py output/v1 output/v2 output/v3 output/dosage
