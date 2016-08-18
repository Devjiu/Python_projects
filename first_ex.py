import numpy as np
import pandas
import re

data = pandas.read_csv('D:\\Downloads\\titanic.csv')
print data.head()


print '---------------------------------------------------'
print data['Name']
print '---------------------------------------------------'
base = np.vstack((data['Name'], data['Sex']))
names = []
for i in range(len(base[0])):
    if base[1][i] == 'female':
        names.append(base[0][i])
first_names = []
for name in names:
    m = re.search('\(\w+', name)
    if m is not None:
        first_names.append(m.group()[1:])
    else:
        n = re.search('\. \w+', name)
        first_names.append(n.group()[2:])
print "wtf"
print pandas.Series(first_names).value_counts()