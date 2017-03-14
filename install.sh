#!/usr/bin/env bash


echo "start generating make_file_inc"
python generate_makefile_inc.py

echo "start installation of CPU faiss"
make
make py

echo "start installation of GPU faiss"
cd gpu
make
make py
