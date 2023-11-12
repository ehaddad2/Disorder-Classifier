import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

symptomsDF = pd.read_csv('MD_symptoms.csv')

corr = symptomsDF.corr()
print(symptomsDF.keys())
print(symptomsDF['anger'].drop())

print(corr)

