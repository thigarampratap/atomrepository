import pandas as pd
import os
import sys

print(os.getcwd().replace('\\','/'))

pdf = pd.read_csv('busidx.csv')
print(pdf.iloc[0:1])
print(pdf.columns)

f1  = pdf['Indx'] == 'K135'
print(pdf[f1])

print(pdf[3:6])
# end.
