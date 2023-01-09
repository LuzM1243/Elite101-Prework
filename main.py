#use jira and whiteboard for todo list
from datetime import date
import datetime
now = datetime.datetime.now()
now=(now.hour,now.minute)
date= date.today()
#use f string
dateq= ('What is todays date?')
timeq=('What is the time?')
bdq=('when is your bithday?(yyyy-mm-dd)')
#start
print('How are you doing today?')
input()
#name
print('what is your name?')
name=input()
print(f'Hello, {name}')
#birthday
bdq=print(f'{bdq}')
userbirthday=input()
#what do?
print('what would you like me to do for you?')
question=print(f'You could say, {dateq}, or {timeq}')
ask= input()
if userbirthday == date:
  print('Happy Birthday!')
if ask== dateq:
  print("Today's date is: ", date)
  print(f'You could say, {timeq}')
  ask= input()
 
if ask ==timeq:
   print(f'The time is {now}')
   print(f'You could say, {dateq}')
   ask= input()
  #list
if ask!= ['dateq','timeq']:
  print(f'Invalid response. Make sure to type in question exactly as written.You could say, {dateq}, or {timeq}')
  ask= input()

#almost finished
#While loops didnt work