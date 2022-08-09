#!/bin/bash

csv=$1
if [csv == ""]; then
  echo "no csv is entered"
  echo "using default param.yaml"
  echo "resulting GLKH file would be named:"
  csv = $$
  echo $csv ".*.tour"
python OCPPP.py --mode 0 --activateTSP 1 --printSeq 0 --csvFile $csv
matlab -nodisplay -nodesktop -r "run OCPPP.m"
python OCPPP.py --mode 1 --activateTSP 1 --printSeq 0 --csvFile $csv
cd GLKH-1.1
./runGLKH $csv
cd ..
