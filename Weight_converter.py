weight=int(input('Weight: '))
unit=input('(L)bs or (K)g: ')

if unit.upper()=="L":
    convertor=weight*0.45
    print(f'You are {convertor} Kilos')
else:
    converted=weight/0.45
    print(f'You are {converted} Lbs')