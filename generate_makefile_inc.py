import distutils.sysconfig
import numpy

makefile_code = '''
# Copyright (c) 2015-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the CC-by-NC license found in the
# LICENSE file in the root directory of this source tree.

# -*- makefile -*-
# tested on CentOS 7, Ubuntu 16 and Ubuntu 14, see below to adjust flags to distribution.


CC=g++

CFLAGS=-fPIC -m64 -Wall -g -O3  -msse4 -mpopcnt -fopenmp -Wno-sign-compare -Dnullptr=NULL -Doverride= -fopenmp
LDFLAGS=-g -fPIC  -fopenmp

# common linux flags
SHAREDEXT=so
SHAREDFLAGS=-shared
FAISSSHAREDFLAGS=-shared


##########################################################################
# Uncomment one of the 4 BLAS/Lapack implementation options
# below. They are sorted # from fastest to slowest (in our
# experiments).
##########################################################################

#
# 2. Openblas
#
# The library contains both BLAS and Lapack. About 30% slower than MKL.

BLASCFLAGS=-DFINTEGER=int

# This is for Centos:
# BLASLDFLAGS=/usr/lib64/libopenblas.so.0

# for Ubuntu 16: 
# sudo apt-get install libopenblas-dev python-numpy python-dev
# BLASLDFLAGS=/usr/lib/libopenblas.so.0

# for Ubuntu 14: 
# sudo apt-get install libopenblas-dev liblapack3 python-numpy python-dev
BLASLDFLAGS=/usr/lib/libopenblas.so.0 /usr/lib/lapack/liblapack.so.3.0


##########################################################################
# SWIG and Python flags
##########################################################################

# SWIG executable. This should be at least version 3.x
SWIGEXEC=swig

PYTHONCFLAGS=-I{python_path} -I{numpy_path}



###########################################################################
# Cuda GPU flags
###########################################################################


# a C++ compiler that supports c++11
CC11=g++

# root of the cuda 8 installation
CUDAROOT=/usr/local/cuda-8.0/

CUDACFLAGS=-I$(CUDAROOT)/include

NVCC=$(CUDAROOT)/bin/nvcc

NVCCFLAGS= $(CUDAFLAGS) \
   -I $(CUDAROOT)/targets/x86_64-linux/include/ \
   -Xcompiler -fPIC \
   -Xcudafe --diag_suppress=unrecognized_attribute \
   -gencode arch=compute_35,code="compute_35" \
   -gencode arch=compute_52,code="compute_52" \
   -gencode arch=compute_60,code="compute_60" \
   --std c++11 -lineinfo \
   -ccbin $(CC11) -DFAISS_USE_FLOAT16

# BLAS LD flags for nvcc (used to generate an executable)
# if BLASLDFLAGS contains several flags, each one may 
# BLAS LD flags for nvcc (used to generate an executable)
BLASLDFLAGSNVCC=-Xlinker /usr/lib/libopenblas.so.0 -Xlinker /usr/lib/lapack/liblapack.so.3.0

# Same, but to generate a .so
BLASLDFLAGSSONVCC=-Xlinker  /usr/lib/libopenblas.so.0 -Xlinker /usr/lib/lapack/liblapack.so.3.0
'''.format(python_path=distutils.sysconfig.get_python_inc(),
           numpy_path=numpy.get_include())


with open('makefile.inc', 'w') as f:
    f.write(makefile_code)
