import os
import cfg_target
import pickle
import numpy as np
from utils import *
import argparse
import evaluation

# from random_cv import best_hyperparameter

model_names = ['FNN']#cfg_target.model_names  # ['EncoderFNN_AllSeq', 'EncoderDecoder', 'EncoderFNN']
test_years = cfg_target.test_years  # [2017, 2018]
month_range = cfg_target.month_range
rootpath = cfg_target.forecast_rootpath


for model_name in model_names:
    if model_name in ['EncoderFNN_AllSeq_AR_CI', 'EncoderFNN_AllSeq_AR', 'EncoderFNN_AllSeq', 'EncoderDecoder', 'EncoderFNN']:
        file_name = 'run_encoder_decoder.py'
    elif model_name in ['XGBoost', 'Lasso']:
        file_name = 'run_non_dl.py'
    elif model_name in ['FNN', 'CNN_FNN', 'CNN_LSTM']:
        file_name = 'run_dl.py'
    for year in test_years:
        for month in month_range:
            cmd = "{} {} --model_name {} --year {} --month {}".format("python", file_name, model_name, year, month)
            print(cmd)
            os.system(cmd)
