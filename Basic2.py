
#this is a comment


num1=13
key = False

if num1 == 12:
    if key:
        print('Num1 is equal to 12 and key is true.')
    else:
        print('Num1 is equal to 12 and key is false.')
elif num1 < 12:
    print('Num1 is less than 12 and key is ' + str(bool(key)) +
    '.')
else:
    print('Num1 is NOT equal to 12. Also, num1 being an integer is '+str(isinstance(num1,int))+'.')
    
