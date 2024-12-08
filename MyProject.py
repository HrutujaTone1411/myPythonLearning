import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib.inline

url = "https://docs.google.com/document/d/1TSMaIE5a3doyOuB_hXjXGShoC8Pl4YwVr8nKdtjsuQE/edit?usp=sharing"
data = pd.read_csv(url)
print("Data Successfully Loaded")