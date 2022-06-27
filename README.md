# OptimalCoveragePathPlanningProblem

## Prerequisites

### Python

```bash
pip install numpy
pip install matplotlib
pip install scipy
```

### Matlab

Optimization Toolbox(https://www.mathworks.com/help/optim/)

## Code workings

run
```bash
# go to the bottom of OCPPP.py
# change desired start, end and unpassable areas
# change mode = 1
python OCPPP.py
# go to Matlab command line and the main repository directory
OCPPP
# the following xh.csv would be the results
``` 
plot
```bash
# go back to the bottom of OCPPP.py
# change mode = 0
python OCPPP.py
```
##Ref:

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
