# Faiss 

Faiss is a library for efficient similarity search and clustering of dense vectors.

See more description on the package at [faiss](https://github.com/facebookresearch/faiss).


# Installation

Please follow the following installation instructions after satisfying the requirements.

This is only tested on Ubuntu 14.04. Also, CUDA needs to be 8.0 and stored at the standard location.

This command will automatically create makefile.inc and run installation of faiss.

```
python setup.py install
pip installl -e .
```

Please test and see that it is installed

```python
import numpy as np
d = 64                           # dimension
nb = 100000                      # database size
nq = 10000                       # nb of queries
np.random.seed(1234)             # make reproducible
xb = np.random.random((nb, d)).astype('float32')
xb[:, 0] += np.arange(nb) / 1000.
xq = np.random.random((nq, d)).astype('float32')
xq[:, 0] += np.arange(nq) / 1000.

import faiss                   # make faiss available
index = faiss.IndexFlatL2(d)   # build the index
print index.is_trained
index.add(xb)                  # add vectors to the index
print index.ntotal
```

# Requirements

```
sudo apt-get install libopenblas-dev liblapack3
```
