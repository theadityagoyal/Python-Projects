year=int(input('enter a year\n'))

if year%4==0 or year%100==0 or year%400==0:
    print("{0} leap year".format(year))
else:
    print('{0} is not leap year'.format(year))