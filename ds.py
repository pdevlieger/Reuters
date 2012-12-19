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

#  => length of texts variation: day of the month/week, hour.

def body_len(x):
	if x:
		if len(x)==0:
			return None
		return len(x)
	else:
		return None

df2['BODYlen'] = df['BODY'].map(body_len)

df_daymon = df2.groupby('DAY_M').mean()
df_dayyear = df2.groupby('DAY_Y').mean()
df_hour = df2.groupby('HOUR').mean()

# figure
fig = plt.figure()
# panel 1
ax = fig.add_subplot(3,1,1)
len_mon = df_daymon.BODYlen.plot()
ax.set_title('Over the month')
ax.set_xlabel('Day')
# panel 2
ax = fig.add_subplot(3,1,2)
len_year = df_dayyear.BODYlen.plot()
ax.set_title('Over the year')
ax.set_xlabel('Day')
# panel 3
ax = fig.add_subplot(3,1,3)
len_hour = df_hour.BODYlen.plot()
ax.set_title('Over the day')
ax.set_xlabel('Hour')
fig.tight_layout()
savefig('body_length.png')
plt.show()

#  => hour at which article is posted. TODO: makes this a bit nicer!
# figure
fig = plt.figure()
# panel 1
ax = fig.add_subplot(2,1,1)
len_mon = df_daymon.HOUR.plot()
ax.set_title('Over the month')
# panel 2
ax = fig.add_subplot(2,1,2)
len_year = df_dayyear.HOUR.plot()
ax.set_title('Over the month')
savefig('hour_posted.png')
plt.show()

