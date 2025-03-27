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


import pandas as pd
import numpy as np

# Creating the DataFrame
df = pd.DataFrame(
    np.random.randint(0, 101, (5, 5)),  # Random marks between 0 and 100
    index=['Math', 'Science', 'English', 'History', 'Computer Science'],  # Row labels (Subjects)
    columns=['Alice', 'Bob', 'Charlie', 'David', 'Emma']  # Column labels (Students)
)

df.loc['Math':'English', 'Alice':'Charlie']

df.loc['Math':'English', 'Alice':]

df.loc['Math':'English', 'Alice']

df.loc['Math':, 'Alice':'Charlie']

df.loc['Math', 'Alice':'Charlie']

df['Alice':'Charlie']

df['Math':'English', 'Alice':'Charlie']

df['Math':'English']

df['Math']

df['Alice':'Charlie']

df['Alice']

df.iloc[[2,3,4], [1,2,4]]

df.loc[['Math','English','History'], ['Alice','Charlie']]

df.loc[['History', 'Math', 'English'], ['Alice','Charlie']]

df.loc[['Alice','Charlie'], ['History', 'Math', 'English']]

df[['Math','English','History'], ['Alice','Charlie']]

df[['Alice','Charlie'], ['History', 'Math', 'English']]

df.iloc[[2,False,4], : ]
