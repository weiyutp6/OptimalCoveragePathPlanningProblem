#!/bin/bash

csv=$1
python OCPPP.py --mode 0 --activateTSP 1 --printSeq 0 --csvFile csv
matlab -nodisplay -nodesktop -r "run OCPPP.m"
python OCPPP.py --mode 1 --activateTSP 1 --printSeq 0 --csvFile csv
cd GLKH-1.1
./runGLKH csv
cd ..
