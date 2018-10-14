#!/bin/bash

python getSearch.py && python getCount.py '2018-10-15 00:15' && python createGraph.py && python s3uploader.py
