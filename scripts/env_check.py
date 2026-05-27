
# STEP 2 - environment check
import scanpy as sc
import squidpy as sq
import pandas as pd
import numpy as np

def check_environment():
    print('scanpy:', sc.__version__)
    print('squidpy:', sq.__version__)
    print('pandas:', pd.__version__)
    print('numpy:', np.__version__)
