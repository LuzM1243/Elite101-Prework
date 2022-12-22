#use jira and whiteboard for todo list
from datetime import date
import datetime
now = datetime.datetime.now()
now=(now.hour,now.minute)
date= date.today()
#use f string
dateq= ('What is todays date?')
timeq=('What is the time?')
print('Hi, how are you doing today?')
input()
print('what would you like me to do for you?')
question=print(f'You could say, {dateq}, or {timeq}')
ask= input()
if ask== dateq:
  print("Today's date is: ", date)
  print(f'You could say, {dateq}, or {timeq}')
  ask= input()
if ask ==timeq:
   print(f'The time is {now}')
   print(f'You could say, {dateq}, or {timeq}')
   ask= input()
if ask!= ['dateq','timeq']:
  print(f'Invalid response. Make sure to type in question exactally as written.You could say, {dateq}, or {timeq}')
  ask= input()
#almost finished
#While loops didnt work