#!/bin/bash

csv=$1
python NewApproach.py --printSeq 0 --csvFile $csv
cd GLKH-1.1
./runGLKH $csv
cd ..
python NewApproach.py --printSeq 1 --csvFile $csv