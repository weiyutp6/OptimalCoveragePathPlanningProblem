# OptimalCoveragePathPlanningProblem

## Prerequisites

### Python

```bash
pip install numpy
pip install matplotlib
pip install scipy
pip install pandas
```

### Matlab

Optimization Toolbox(https://www.mathworks.com/help/optim/)

### GNU C

gcc 11.3.0

**Disclaimer**

All code from folder GLKH-1.1 is not original. Everything is based on http://webhotel4.ruc.dk/~keld/research/GLKH/ with only changes being compatibility changes in the original code to run on the current setup. If you want to use the original GLKH follow the download instructions on the website and replace GLKKH-1.1 with the compiled folder.

**Note**
If you are running this on Windows OS mingw compiler is tested and doesn't work. GLKH is ported to this version of gcc with cygwin 3.3.5 and is primarily tested and run on this version.

## Code workings

### Run unfinished GTSP version

Go to the bottom of OCPPP.py
Change desired start, end and unpassable areas or read a .csv file which is a heat map
Which can be changed in the section
```bash
g = Grid(start = start10, end = end10, unpassable = unpassable10, threshold = 0)
g = Grid(csv_file=csv_file, threshold=0)
```bash
Change mode = 0
```bash
python OCPPP.py
```
Go to Matlab command line and the main repository directory
```bash
OCPPP
```
The following xh.csv would be the results of line segmentation of the workspace
Go back to OCPPP.py and change mode = 1, activate_tsp = 0
```bash
python OCPPP.py
```
Creates the transition segments and relative cost for GTSP and plots the line segments to segment.png
Go to Matlab again
```bash
GTSP
```
The following GTSP_result.csv would be the results of GTSP w.r.t the line segments and transition segments
To plot the results go back to OCPPP.py again and change mode = 2
```bash
python OCPPP.py
``` 
#### plot
Go back to the bottom of OCPPP.py
Change mode = 0
```bash
python OCPPP.py
```

### Run with Ramesh et al. configurations

Go to the bottom of OCPPP.py
Change desired start, end and unpassable areas or read a .csv file which is a heat map.
Edit the section bellow accordingly at the bottom of OCPPP.py
```bash
g = Grid(start = start10, end = end10, unpassable = unpassable10, threshold = 0)
g = Grid(csv_file=csv_file, threshold=0)
```bash
Change mode = 0
```bash
python OCPPP.py
```
Go to Matlab command line and the main repository directory
```bash
OCPPP
```
The following xh.csv would be the results of line segmentation of the workspace
Go back to OCPPP.py and change mode = 1, activate_tsp = 1
```bash
python OCPPP.py
```
You would get the files
```bash
edge_weight_section.txt
set_section.txt
```
These files would be used to create the .gtsp file for GLKH. a template .gtsp used is OCPPP3.gtsp.

Open .gtsp file with text editor

Change the tags accordingly. The important ones are replace content under EDGE_WEIGHT_SECTION tag with the contents from edge_weight_section.txt and replace GTSP_SET_SECTION tag contents with content from set_section.txt.

Then change the DIMENSION and GTSP_SETS to match that of GTSP_SET_SECTION.

Don't forget to change the NAME tag to the filename of the .gtsp file.

(I know this is very annoying and I promise I will include code to do this automatically on the next update QwQ)

After the .gtsp file is saved run GLKH
```bash
./$(workspace_dir)/GLKH-1.1/runSmall $(workspace_dir)/(filename without .gtsp at the end)
```
Your results should be saved in the following format
```bash
(filename).(optimal cost).tour
```
To compile the results the file
```bash
line_segment.mat
```
Contains a dictionary with the set number defined in GLKH to the line segment and direction with the set number as the key and line segment as the value.
Then you can find the resulting trajectory when you match the results together.

## test
the other files are the results using
```bash
unpassable = [[1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5], [5, 7], [5, 8], [6, 7], [6, 8]]
```
![](segment.png)

Fig.1 result of workspace segmentation(red lines) and transition segments(yellow lines)

![](GTSP.png)

Fig.2 result of GTSP

## Reference:

@INPROCEEDINGS{7743548,
  author={Bochkarev, Stanislav and Smith, Stephen L.},
  booktitle={2016 IEEE International Conference on Automation Science and Engineering (CASE)},
  title={On minimizing turns in robot coverage path planning},
  year={2016},
  volume={},
  number={},
  pages={1237-1242},
  doi={10.1109/COASE.2016.7743548}}
  
@misc{https://doi.org/10.48550/arxiv.2109.08185,
  doi = {10.48550/ARXIV.2109.08185},
  url = {https://arxiv.org/abs/2109.08185},
  author = {Ramesh, Megnath and Imeson, Frank and Fidan, Baris and Smith, Stephen L.},
  title = {Optimal Partitioning of Non-Convex Environments for Minimum Turn Coverage Planning},
  publisher = {arXiv},
  year = {2021},
  copyright = {arXiv.org perpetual, non-exclusive license}}

@Article{Helsgaun2015,
author={Helsgaun, Keld},
title={Solving the equality generalized traveling salesman problem using the Lin--Kernighan--Helsgaun Algorithm},
journal={Mathematical Programming Computation},
year={2015},
month={Sep},
day={01},
volume={7},
number={3},
pages={269-287},
abstract={The equality generalized traveling salesman problem (E-GTSP) is an extension of the traveling salesman problem (TSP) where the set of cities is partitioned into clusters, and the salesman has to visit every cluster exactly once. It is well known that any instance of E-GTSP can be transformed into a standard asymmetric instance of the TSP, and therefore solved with a TSP solver. This paper evaluates the performance of the state-of-the art TSP solver Lin--Kernighan--Helsgaun (LKH) on transformed E-GTSP instances. Although LKH is used without any modifications, the computational evaluation shows that all instances in a well-known library of benchmark instances, GTSPLIB, could be solved to optimality in a reasonable time. In addition, it was possible to solve a series of new very-large-scale instances with up to 17,180 clusters and 85,900 vertices. Optima for these instances are not known but it is conjectured that LKH has been able to find solutions of a very high quality. The program's performance has also been evaluated on a large number of instances generated by transforming arc routing problem instances into E-GTSP instances. The program is free of charge for academic and non-commercial use and can be downloaded in source code.},
issn={1867-2957},
doi={10.1007/s12532-015-0080-8},
url={https://doi.org/10.1007/s12532-015-0080-8}
}
