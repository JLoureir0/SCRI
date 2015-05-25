#!/bin/bash
echo ''
echo '*********************************************************'
echo '*                                                       *'
echo '*                        C++                            *'
echo '*                                                       *'
echo '*********************************************************'
echo ''
./cppversion/cppVersion input/readings output/v1
echo ''
echo '*********************************************************'
echo '*                                                       *'
echo '*                        JAVA                           *'
echo '*                                                       *'
echo '*********************************************************'
echo ''
java -jar javaversion/scri.jar input/readings output/v2
echo ''
echo '*********************************************************'
echo '*                                                       *'
echo '*                       PYTHON                          *'
echo '*                                                       *'
echo '*********************************************************'
echo ''
python pyversion/main.py input/readings output/v3
python voter/voter.py output/v1 output/v2 output/v3 output/dosage

echo ''
echo '*********************************************************'
echo '*                                                       *'
echo '*                        DOSAGES                        *'
echo '*                         voter                         *'
echo '*                                                       *'
echo '*********************************************************'
echo ''

cat output/dosage
