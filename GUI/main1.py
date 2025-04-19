import pandas as pd
import numpy as np
import GUI.adm1 as ad
import matplotlib.pyplot as plt
import seaborn as sns
language=1

data = ad.read_preprocessing('GlobalElectricityStatistics.csv')
selected_countries = ['China', 'United States', 'India', 'Russia', 'Japan']