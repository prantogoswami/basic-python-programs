Inp=eval(input('Enter first number'))
Inp2=eval(input('Enter Second number'))
Inp3=eval(input('Enter Third number'))

if Inp<Inp2 and Inp2>Inp3:
    print('Second number is the largest number')
elif Inp2<Inp and Inp>Inp3:
    print('First number is the largest number')
elif Inp2==Inp and Inp2==Inp3:
    print('all numbers are equal')
else:
    print('third number id the largest number') 