import pandas as pd
import numpy as np
import joblib

def load_pickle(file_path):

    return joblib.load(file_path)

def dump_pickle(data, file_path):
    
    joblib.dump(data, file_path)