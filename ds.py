from reut import get_data
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig

data = get_data()

df = pd.DataFrame(data)
df = df.dropna(axis=1, how='all')

d = {'YEAR':pd.Series(df.YEAR, index=df.ID),'MONTH':pd.Series(df.MONTH, index=df.ID),
'DAY_M':pd.Series(df.DAY_M, index=df.ID),'HOUR':pd.Series(df.HOUR, index=df.ID),
'DAY_Y':pd.Series(df.DAY_Y, index=df.ID),'TITLE':pd.Series(df.TITLE, index=df.ID),
'PEOPLE':pd.Series(df.PEOPLE, index=df.ID),'EXCHANGES':pd.Series(df.EXCHANGES, index=df.ID),
'ORGS':pd.Series(df.ORGS, index=df.ID),'BODY':pd.Series(df.BODY, index=df.ID)}

df2 = pd.DataFrame(d)

## We have all the data. Now look at some trends.

def body_len(x):
	if x:
		if len(x)==0:
			return None
		return len(x)
	else:
		return None	

x = df2.groupby('DAY').mean()

fig = x.HOUR.plot()
savefig('foo.png')
plt.show(x.HOUR.plot())

