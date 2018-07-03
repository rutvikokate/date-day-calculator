def day(j):
    m=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    for i in range(2018,n+1):
        if (j==7):
            j=0
        
        if (( i%400 == 0)or (( i%4 == 0 ) and ( i%100 != 0))):
            if (j==6):
                j=0
                print date,'/',month,'/',i,'is',m[j]
                j=j+1
            else:
                print date,'/',month,'/',i,'is',m[j+1]
                j=j+2
    
        else:
            print date,'/',month,'/',i,'is',m[j]
            j=j+1

restart='yes'
while(restart=='yes'):
    print ' 1.jan\n 2.feb\n 3.mar\n 4.apr\n 5.may\n 6.jun\n 7.jul\n 8.aug\n 9.sep\n 10.oct\n 11.nov\n 12.dec\n'
    month=int(raw_input('Enter month no. '))
    date=int(raw_input('Enter date '))
    n=int(raw_input('Enter the year upto which day must be displayed, year must be greater than 2018 '))
    if(n<2018):
        print 'Enter year more than 2018'
        n=int(raw_input('Enter the year upto which day must be displayed, year must be greater than 2018 '))
    else:
        continue
    
    if(month==1):
        if(date>31):
            print 'invalid date'
        if(date%7==0):
            day(6)
        if(date%7==1):
            day(0)
        if(date%7==2):
            day(1)
        if(date%7==3):
            day(2)
        if(date%7==4):
            day(3)
        if(date%7==5):
            day(4)
        if(date%7==6):
            day(5)

    if(month==2):
        if(date>29):
            print 'invalid date'
        if(date%7==0):
            j=2
        if(date%7==1):
            j=3
        if(date%7==2):
            j=4
        if(date%7==3):
            j=5
        if(date%7==4):
            j=6
        if(date%7==5):
            j=0
        if(date%7==6):
            j=1
        
        m=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        for i in range(2018,n+1):
            if (j==7):
                j=0
        
            if (( i%400 == 0)or (( i%4 == 0 ) and ( i%100 != 0))):
                if (j==6):
                    j=0
                    print date,'/',month,'/',i,'is',m[j]
                    j=j+1
                else:
                    print date,'/',month,'/',i,'is',m[j]
                    j=j+2
    
            else:
                if(date==29):
                    j=j+1
                    print'day exist only in leap year'
                    continue
                print date,'/',month,'/',i,'is',m[j]
                j=j+1
  

    if(month==3):
        if(date>31):
            print 'invalid date'
        if(date%7==0):
            day(2)
        if(date%7==1):
            day(3)
        if(date%7==2):
            day(4)
        if(date%7==3):
            day(5)
        if(date%7==4):
            day(6)
        if(date%7==5):
            day(0)
        if(date%7==6):
            day(1)

    if(month==4):
        if(date>30):
            print 'invalid date'
        if(date%7==0):
            day(5)
        if(date%7==1):
            day(6)
        if(date%7==2):
            day(0)
        if(date%7==3):
            day(1)
        if(date%7==4):
            day(2)
        if(date%7==5):
            day(3)
        if(date%7==6):
            day(4)

    if(month==5):
        if(date>31):
            print 'invalid date'
        if(date%7==0):
            day(0)
        if(date%7==1):
            day(1)
        if(date%7==2):
            day(2)
        if(date%7==3):
            day(3)
        if(date%7==4):
            day(4)
        if(date%7==5):
            day(5)
        if(date%7==6):
            day(6)

    if(month==6):
        if(date>30):
            print 'invalid date'
        if(date%7==0):
            day(3)
        if(date%7==1):
            day(4)
        if(date%7==2):
            day(5)
        if(date%7==3):
            day(6)
        if(date%7==4):
            day(0)
        if(date%7==5):
            day(1)
        if(date%7==6):
            day(2)

    if(month==7):
        if(date>31):
            print 'invalid date'
        if(date%7==0):
            day(6)
        if(date%7==1):
            day(0)
        if(date%7==2):
            day(1)
        if(date%7==3):
            day(2)
        if(date%7==4):
            day(3)
        if(date%7==5):
            day(4)
        if(date%7==6):
            day(5)

    if(month==8):
        if(date>31):
            print 'invalid date'
        if(date%7==0):
            day(1)
        if(date%7==1):
            day(2)
        if(date%7==2):
            day(3)
        if(date%7==3):
            day(4)
        if(date%7==4):
            day(5)
        if(date%7==5):
            day(6)
        if(date%7==6):
            day(0)

    if(month==9):
        if(date>30):
            print 'invalid date'
        if(date%7==0):
            day(4)
        if(date%7==1):
            day(5)
        if(date%7==2):
            day(6)
        if(date%7==3):
            day(0)
        if(date%7==4):
            day(1)
        if(date%7==5):
            day(2)
        if(date%7==6):
            day(3)

    if(month==10):
        if(date>31):
            print 'invalid date'
        if(date%7==0):
            day(6)
        if(date%7==1):
            day(0)
        if(date%7==2):
            day(1)
        if(date%7==3):
            day(2)
        if(date%7==4):
            day(3)
        if(date%7==5):
            day(4)
        if(date%7==6):
            day(5)

    if(month==11):
        if(date>30):
            print 'invalid date'
        if(date%7==0):
            day(2)
        if(date%7==1):
            day(3)
        if(date%7==2):
            day(4)
        if(date%7==3):
            day(5)
        if(date%7==4):
            day(6)
        if(date%7==5):
            day(0)
        if(date%7==6):
            day(1)

    if(month==12):
        if(date>31):
            print 'invalid date'
        if(date%7==0):
            day(4)
        if(date%7==1):
            day(5)
        if(date%7==2):
            day(6)
        if(date%7==3):
            day(0)
        if(date%7==4):
            day(1)
        if(date%7==5):
            day(2)
        if(date%7==6):
            day(3)

    print
    restart=raw_input('enter yes to run again no to end: ')
    print
    
