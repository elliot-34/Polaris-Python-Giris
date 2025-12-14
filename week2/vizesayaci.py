import time
import datetime
from datetime import datetime, date, time, timezone

def main():
     dt=datetime.now()
     daylist=[0,31,28,31,30,31,30,31,31,30,31,30,31]
     while True:
        exam=input("Enter Your Exam Date In This Format DD.MM.YYYY:")
        if len(exam)!=10:
             print("You need to enter full details, please try again.")
             continue
        if exam[2]=="." and exam[5]==".":
            try:
                day=(int(exam[0])*10)+int(exam[1])
                month=(int(exam[3])*10)+int(exam[4])
                year=(int(exam[6])*1000)+(int(exam[7])*100)+(int(exam[8])*10)+int(exam[9])
            except ValueError:
                print("Please try again.")
            else:
                 if year<dt.year:
                      print("We cant count to past.Try again.")
                      continue
                 elif year==dt.year:
                      if month<dt.month:
                           print("We cant count to past.Try again.")
                           continue
                      elif month==dt.month and day<dt.day:
                           print("We cant count to past.Try again.")
                           continue
                 if month>12 or month==0:
                      print("Only 12 months exist.Try again.")
                      continue
                 else:
                      if year%400==0:
                           daylist[2]=29
                      elif year%100==0:
                           daylist[2]=28
                      elif year%4==0:
                           daylist[2]=29
                      if daylist[month]<day or day==0:
                           print("Problem with day of the month.Try again.")
                           daylist[2]=28
                           continue
                      else:
                           break
        else:
             print("Please try again.")
     while True:
          examh=input("Enter Your Exam Hour In This Format HH.MM:")
          if len(examh)!=5:
               print("We need full details, try again.")
               continue
          if examh[2]!='.':
               print("Use format as expected.Try again.")
          else:
               try:
                    hour=(int(examh[0])*10)+int(examh[1])
                    minute=(int(examh[3])*10)+int(examh[4])
               except ValueError:
                    print("Enter numbers.Try again.")
               else:
                    if day==dt.day and month==dt.month and year==dt.year:
                         if hour<dt.hour:
                              print("We cant go back to past,try again.")
                              continue
                         elif hour==dt.hour and minute<dt.minute:
                              print("We cant go back to past,try again.")
                              continue
                         else:
                              break
                    else:
                         if hour>23 or minute>59:
                              print("Problem with hour or minute,try again.")
                         else:
                              break     
     userdt=datetime(year,month,day,hour,minute)
     delta=userdt-dt
     deltahour=int(delta.seconds/3600)
     deltaminu=int(delta.seconds/60)-int((deltahour*60))
     print(f"{delta.days}days,{deltahour}hours,{deltaminu}minutes left till exam")

main()
#biraz c kafasi oldu 