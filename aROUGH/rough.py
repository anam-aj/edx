import pandas as pd

# Creating the DataFrame
data = {
    "Name": ["Raman", "Raman", "Raman", "Zuhaire", "Zuhaire", "Zuhaire",
             "Ashravy", "Ashravy", "Ashravy", "Mishti", "Mishti", "Mishti"],
    "UT": [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    "Maths": [22, 21, 14, 20, 23, 22, 23, 24, 12, 15, 18, 17],
    "Science": [21, 20, 19, 17, 15, 18, 19, 22, 25, 22, 21, 18],
    "S.St": [18, 19, 15, 22, 21, 19, 20, 24, 19, 25, 25, 20],
    "Hindi": [20, 24, 24, 24, 25, 23, 15, 17, 21, 22, 24, 25],
    "Eng": [21, 23, 23, 19, 15, 13, 22, 21, 23, 22, 23, 20]
}

df = pd.DataFrame(data)


       Name  UT  Maths  Science  S.St  Hindi  Eng
0     Raman   1     22       21    18     20   21
1     Raman   2     21       20    19     24   23
2     Raman   3     14       19    15     24   23
3   Zuhaire   1     20       17    22     24   19
4   Zuhaire   2     23       15    21     25   15
5   Zuhaire   3     22       18    19     23   13
6   Ashravy   1     23       19    20     15   22
7   Ashravy   2     24       22    24     17   21
8   Ashravy   3     12       25    19     21   23
9    Mishti   1     15       22    25     22   22
10   Mishti   2     18       21    25     24   23
11   Mishti   3     17       18    20     25   20


filter = df.loc[ :, 'Name'] == 'Mishti'
df['Name'] == 'Mishti'


df[df['Name'] == 'Mishti']
df.loc[df['Name'] == 'Mishti']


dfmishti = df[df['Name'] == 'Mishti']

df.aggregate(['max', 'min', 'count'])

df.aggregate(['max', 'min', 'count'], axis = 1)

dfUT1 = df[df.UT == 1].copy()

dfUT1.reset_index(inplace=True)

dfUT1.drop(columns=['index'], inplace=True)

dfUT1.set_index('Name', inplace=True)

dfUT1.reset_index('Name', inplace = True)

dfUT1.reset_index(inplace = True)

dfUT1.reset_index('UT', inplace = True)
