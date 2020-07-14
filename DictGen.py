

import pandas as pd
import numpy as np
import re



#We can add more data. More the data more the accuracy and performance

PrevData1=pd.read_csv('Data1.csv')
PrevData2=pd.read_csv('Data2.csv')
PrevData3= pd.read_csv('Data3.csv')



#Concating the trainig data to form dictionaries

Train_t=pd.concat([PrevData1, PrevData2, PrevData3])
Train = Train_t.dropna(axis = 0, how ='any')





#Dictionary creation

Label1=[]
Label2=[]
Label3=[]
Label4=[]
Label5=[]
for row in Train.itertuples(index = True, name ='Pandas'): 
    text_temp=getattr(row, "tweets")
    tag_temp=getattr(row, "Tags")
    res= re.sub(r'[^\w\s]', '', text_temp) 
    text_t1=res.strip()

    text_t2 = text_t1.rsplit(' ')

    newtext=[]
    for i in range(0,len(text_t2)):
      lower=text_t2[i].lower()
      if(lower=='reply\n'or lower.startswith('#') or lower.startswith('"')  or lower.startswith(',') or lower.startswith('@') or lower.startswith('/') or lower.startswith('[') or lower.startswith(']') or lower.startswith('http') or lower.startswith('\n') or lower.startswith('!') or lower.startswith('$') or lower.startswith('%') or lower.startswith('&') or lower.startswith('(') or lower.startswith('*') or lower.startswith('+') or lower.startswith('-') or lower.startswith('.') or lower.startswith('-') or lower.startswith('?') or lower.startswith('>') or lower.startswith(':') or lower.startswith(';') or lower.startswith('=') or lower.startswith(')') or lower.startswith('0') or lower.startswith('1') or lower.startswith('2') or lower.startswith('3') or lower.startswith('4') or lower.startswith('5') or lower.startswith('6') or lower.startswith('7') or lower.startswith('8') or lower.startswith('9')):
        a=1+1
      else:
        if(tag_temp=='Label1'):
          Label1.append(lower)
        if(tag_temp=='Label2'):
          Label2.append(lower)
        if(tag_temp=='Label3'):
          Label3.append(lower)
        if(tag_temp=='Label4'):
          Label5.append(lower)
        if(tag_temp=='Label5'):
          Label5.append(lower)





x = np.array(Label1) 
Label1Unique=np.unique(x)
print(len(Label1Unique))

y = np.array(Label2) 
Label2Unique=np.unique(y)
print(len(Label2Unique)) 

z = np.array(Label3) 
Label3Unique=np.unique(z)
print(len(Label3Unique))

f = np.array(Label4) 
Label4Unique=np.unique(f)
print(len(Label4Unique)) 

g = np.array(Label5) 
Label5Unique=np.unique(g)
print(len(Label5Unique))

Label1Unique=list(Label1Unique)
Label2Unique=list(Label2Unique)
Label3Unique=list(Label3Unique)
Label4Unique=list(Label4Unique)
Label5Unique=list(Label5Unique)



#Cleaning the Dictinary to have unique values in all the Dictionaries
result12 = set(Label1Unique).intersection(Label2Unique)
result13= set(Label1Unique).intersection(Label3Unique)
result14 = set(Label1Unique).intersection(Label4Unique)
result15= set(Label1Unique).intersection(Label5Unique)


result23 = set(Label2Unique).intersection(Label3Unique)
result24= set(Label2Unique).intersection(Label4Unique)
result25 = set(Label2Unique).intersection(Label5Unique)


result34 = set(Label3Unique).intersection(Label4Unique)
result35= set(Label3Unique).intersection(Label5Unique)


result45= set(Label4Unique).intersection(Label5Unique)

#Intersection Label1
Res12=list(result12)
Label1Unique=list(Label1Unique)
for i in Label1Unique:
  for j in result12:
    if(i==j):
      Label1Unique.remove(i)
      Label2Unique.remove(j)

Res13=list(result13)
Label1Unique=list(Label1Unique)
for i in Label1Unique:
  for j in result13:
    if(i==j):
      Label1Unique.remove(i)
      Label3Unique.remove(j)

Res14=list(result14)
Label1Unique=list(Label1Unique)
for i in Label1Unique:
  for j in result14:
    if(i==j):
      Label1Unique.remove(i)
      Label4Unique.remove(j)


Res15=list(result15)
Label1Unique=list(Label1Unique)
for i in Label1Unique:
  for j in result15:
    if(i==j):
      Label1Unique.remove(i)
      Label15Unique.remove(j)

type(GeneralUnique)
Label1UniqueDictC= pd.DataFrame(Label1Unique) 
Label1UniqueDictC.head()
Label1UniqueDictC.to_csv('Dict1.csv', index=False)


#Intersection Label2
Res23=list(result23)
Label2Unique=list(Label2Unique)
for i in Label2Unique:
  for j in result23:
    if(i==j):
      Label2Unique.remove(i)
      try:
        Label3Unique.remove(j)
      except ValueError:
        a=1+1


Res24=list(result24)
Label2Unique=list(Label2Unique)
for i in Label2Unique:
  for j in result24:
    if(i==j):
      Label2Unique.remove(i)
      try:
        Label4Unique.remove(j)
      except ValueError:
        a=1+1


Res25=list(result25)
Label2Unique=list(Label2Unique)
for i in Label2Unique:
  for j in result25:
    if(i==j):
      Label2Unique.remove(i)
      try:
        Label2Unique.remove(j)
      except ValueError:
        a=1+1



Label2UniqueDictC= pd.DataFrame(Label2Unique) 
Label2UniqueDictC.head()
Label2UniqueDictC.to_csv('Dict2.csv', index=False)



#Intersection Label3
Res34=list(result34)
Label3Unique=list(Label3Unique)
for i in Label3Unique:
  for j in result34:
    if(i==j):
      Label3Unique.remove(i)
      try:
        Label4Unique.remove(j)
      except ValueError:
        a=1+1

Res35=list(result35)
Label3Unique=list(Label3Unique)
for i in Label3Unique:
  for j in result35:
    if(i==j):
      Label3Unique.remove(i)
      try:
        Label5Unique.remove(j)
      except ValueError:
        a=1+1

Label3UniqueDictC= pd.DataFrame(Label3Unique) 
Label3UniqueDictC.head()
Label3UniqueDictC.to_csv('Dict3.csv', index=False)


#Intersection Label4
Res45=list(result45)
Label4Unique=list(Label4Unique)
for i in Label4Unique:
  for j in result45:
    if(i==j):
      Label4Unique.remove(i)
      try:
        Label5Unique.remove(j)
      except ValueError:
        a=1+1

print(len(AgainstUnique))

Label4UniqueDictC= pd.DataFrame(Label4Unique) 
Label4UniqueDictC.head()
Label4UniqueDictC.to_csv('Dict4.csv', index=False)

Label5UniqueDictC= pd.DataFrame(Label5Unique) 
Label5UniqueDictC.head()
Label5UniqueDictC.to_csv('Dict5.csv', index=False)




