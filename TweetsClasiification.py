import pandas as pd
import numpy as np
import re

#Pass the Dictionaries generated from the DictGen File and increase the number of labels according to your use
Label1DF=pd.read_csv('Dict1.csv')
Label2DF=pd.read_csv('Dict2.csv')
Label3DF=pd.read_csv('Dict3.csv')
Label4DF=pd.read_csv('Dict4.csv')
Label5DF=pd.read_csv('Dict5.csv')
Test=pd.read_csv('test3.csv')

#Clean the Test set/ Data to be labelled
Test = Test.dropna(axis = 0, how ='any')



#Convert the Dictionaries to Numpy Arrays for processing
Label1NumpyArray=np.array(Label1DF)
Label2NumpyArray=np.array(Label2DF)
Label3NumpyArray=np.array(Label3DF)
Label4NumpyArray=np.array(Label4DF)
Label5NumpyArray=np.array(Label5DF)

#variable for your reference to see which row is being labelled
number=0

TweetsAfter=[]
LabelAfter=[]
for row in Test.itertuples(index = True, name ='Pandas'): 
  number+=1
  print(number)

  #Initialise the label values for the words in the row 
  Label1Count=0
  Label2Count=0
  Label3Count=0
  Label4Count=0
  Label5Count=0
  text_type=getattr(row,"type")

  #Check the row whether it is a tweet or a reply
  if(text_type=='post'):
    print('Post')
    continue
  
  #Extract the row to be labelled, clean and spilt into words for processing
  test_temp=getattr(row, "text")
  TweetsAfter.append(test_temp)
  print(test_temp)
  res= re.sub(r'[^\w\s]', '', test_temp) 
  test_t1=res.strip()
  test_t2 = test_t1.rsplit(' ')

  #Labelling starts
  for i in range(0,len(test_t2)):

    #Incase the scrapped data has the names of the people who tweeted in the row
    if(i==0 or i==1):
      a=1+1
      continue

    #Start Labelling
    else:
      lower_test=test_t2[i].lower()
      lower_test= re.sub(r'[^\w\s]', '', lower_test)

      #check for values if they are not relevant
      if(lower_test=='reply\n' or lower_test.startswith('#') or lower_test.startswith('"')  or lower_test.startswith(',') or lower_test.startswith('@') or lower_test.startswith('/') or lower_test.startswith('[') or lower_test.startswith(']') or lower_test.startswith('http') or lower_test.startswith('\n') or lower_test.startswith('!') or lower_test.startswith('$') or lower_test.startswith('%') or lower_test.startswith('&') or lower_test.startswith('(') or lower_test.startswith('*') or lower_test.startswith('+') or lower_test.startswith('-') or lower_test.startswith('.') or lower_test.startswith('-') or lower_test.startswith('?') or lower_test.startswith('>') or lower_test.startswith(':') or lower_test.startswith(';') or lower_test.startswith('=') or lower_test.startswith(')') or lower_test.startswith('0') or lower_test.startswith('1') or lower_test.startswith('2') or lower_test.startswith('3') or lower_test.startswith('4') or lower_test.startswith('5') or lower_test.startswith('6') or lower_test.startswith('7') or lower_test.startswith('8') or lower_test.startswith('9')):
        a=1+1  
        continue

      #The data is ready for labelling and is clean
      else:
          #Flags the words if they are present in the corresponding dictionary

        flag_Label1=0
        for j in range(0,len(Label1NumpyArray)):
          if(lower_test==Label1NumpyArray[j]):
            flag_Label1=flag_Label1+1
          else:
            flag_Label1=flag_Label1

        flag_Label2=0
        for k in range(0,len(Label2NumpyArray)):
          if(lower_test==Label2NumpyArray[k]):
            flag_Label2=flag_Label2+1
          else:
            flag_Label2=flag_Label2

        flag_Label3=0
        for l in range(0,len(LabelNumpyArray)):
          if(lower_test==Label3NumpyArray[l]):
            flag_Label3=flag_Label3+1
          else:
            flag_Label3=flag_Label3

        flag_Label4=0
        for m in range(0,len(Label4NumpyArray)):
          if(lower_test==Label4NumpyArray[m]):
            flag_Label4=flag_Label4+1
          else:
            flag_Label4=flag_Label4

        flag_Label5=0
        for n in range(0,len(Label5NumpyArray)):
          if(lower_test==Label5NumpyArray[n]):
            flag_Label5=flag_Label5+1
          else:
            flag_Label5=flag_Label5
        
        #Comapre the occurance of the words and clasiify them

        flag=[flag_Label1,flag_Label2,flag_Label3,flag_Label4,flag_Label5]
        max_flag=max(flag)
        if(max_flag==0):
          Label1Count+=1

        #If the word is present in two or more dictionaries we calssify them which is most appropriate and this requires you to have some knowledge about the data
        
        elif(flag_Label1==flag_Label2):
          Label1Count+=1
        elif(flag_Label1==flag_Label3):
          Label3Count+=1
        elif(flag_Label1==flag_Label4):
          Label4Count+=1
        elif(flag_Label1==flag_Label5):
          Label5Count+=1

        elif(flag_Label2==flag_Label3):
          Label2Count+=1
        elif(flag_Label2==flag_Label4):
          Label4Count+=1
        elif(flag_Label2==flag_Label5):
          Label5Count+=1

        elif(flag_Label3==flag_Label4):
          Label4Count+=1
        elif(flag_Label3==flag_Label5):
          Label5Count+=1

        elif(flag_Label4==flag_Label5):
          Label5Count+=1
 
        elif(max_flag==flag_Label1):
          Label1Count+=1
        elif(max_flag==flag_Label2):
          Label2Count+=1
        elif(max_flag==flag_Label3):
          Label3Count+=1
        elif(max_flag==flag_Label4):
          Label4Count+=1
        elif(max_flag==flag_Label5):
          Label5Count+=1

  #Classify the senetence based on the occurances of the number of corresponding labels in it
  WordCount=[Label1GeneralCount,Label2Count,Label3Count,Label4Count,Label5Count]

  max_WordCount=max(WordCount)

  if(max_WordCount==0):
    LabelAfter.append('Label1')

  elif(max_WordCount==1):
    if(Label1Count==1):
      LabelAfter.append('Label1')

    elif(Label2Count==1):
      LabelAfter.append('Label2')

    elif(Label3Count==1):
      LabelAfter.append('Label3')

    elif(Label4Count==1):
      LabelAfter.append('Label4')
 
    elif(Label5Count==1):
      print('Label5')
    
  
  elif(Label1Count==max_WordCount):
    LabelAfter.append('Label1')

  elif(Label2Count==max_WordCount):
    LabelAfter.append('Label2')

  elif(Label3Count==max_WordCount):
    LabelAfter.append('Label3')

  elif(Label4Count==max_WordCount):
    LabelAfter.append('Label4')

  elif(Label5Count==max_WordCount):
    LabelAfter.append('Label5')

#Gives the labelled tweets as CSV files

TweetDF = pd.DataFrame(TweetsAfter)


LabelsDF=pd.DataFrame(LabelAfter)


LabelledTweets= pd.concat([TweetDF, LabelsDF], axis=1, sort=False)
LabelledTweets.to_csv('LabelledTweets.csv', index=False)



