score=float(input("Youscore:"))


#ifelse
if score>=80:
     grade=('"A"')
elif score>=75:
    grade=('B+')
elif score>=70:
     grade=('"B"')
elif score>=65:
     grade=('"C+"')
elif score>=60:
     grade=('"C"')
elif score>=55:
     grade=('"D+"')
elif score>=50:
     grade=('"D"')
else:
     grade=('"F"')


#output
print('Yougrade:', grade) 