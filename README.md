## ROSSL

This repository contains the author's implementation Pytorch in  paper "Robust Structural Sequence Learning from Open-world Graph Streams Using Laplace Approximation".


## Dependencies

- Python (>=3.6)
- torch:  (>= 1.7.0)
- numpy (>=1.17.4)
- sklearn



## Implementation

Here we provide the implementation of ROSSL, along with the default dataset (DBLP5). The repository is organised as follows:

 - `data/` contains the necessary dataset files and config files;
 - `code/` contains the implementation of the ROSSL and the basic utils;

 Finally, `main.py` puts all of the above together and can be used to execute a full training run on the datasets.

## Process
 - Place the datasets in `data/`
 - Training/Testing:
 ```bash
 python main.py
 ```
 
