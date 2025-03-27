import pandas as pd
import numpy as np

seriesA = pd.Series(
    [1,2,3,4,5],
    index = ['a', 'b', 'c', 'd', 'e']
)

seriesB = pd.Series(
    [1000,2000,-1000,-5000,1000],
    index = ['a', 'b', 'c', 'd', 'e']
)

seriesC = pd.Series(
    [10,20,-10,-50,100],
    index = ['z', 'y', 'a', 'c', 'e']
)

df1 = pd.DataFrame(seriesA)

df2 = pd.DataFrame(seriesA, seriesB)

df3 = pd.DataFrame([seriesA, seriesB])

df4 = pd.DataFrame([seriesA, seriesC])

df5 = pd.DataFrame([seriesA, seriesB, seriesC])
