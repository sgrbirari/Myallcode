# Dict

marks={'history':45,'geography':78, 'hindi':79}
print(marks)
print(marks['geography'])

marks['english']=70
print(marks)
## update

# dict2={'suresh':[150,48],'ramesh':[149,49]}
# dict2.update({'sunil':[148,46], 'sahil':[134,40]})
# print(dict2)
# ## del
# del dict2['ramesh']
# print(dict2)

# a=dict()
# a[1]
# print(a)
#########################################

# modules & Packeges

# from operator.arithmatic import addition_____ addition(3,5)
# from operator import arithmatic_______________ariyhmatic.addition(3,5)
################################################

#Pandas
# reading filtering, manipulating, 
'''
reading variety od daata
'''
# reading csv file

import pandas as pd
df= pd.read_csv('data.csv')
df=head() # to read first few rows

df1=pd.read_excel('data.xlsx')
df1.head()


