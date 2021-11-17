import pandas as pd
import zipfile

zf_calgary = zipfile.ZipFile('calgary_crime.zip') 
df_calgary = pd.read_csv(zf_calgary.open('calgary_crime.csv'))


zf_toronto = zipfile.ZipFile('Toronto_crime.zip') 
df_toronto = pd.read_csv(zf_toronto.open('Toronto_crime.csv'))

print(df_toronto)


