print('KPH\tMPH')
print('-----------------')
for mph in range(0,140,10):
    kph = mph * 0.6214
    print(mph, '\t', f"{kph:.2f}")
    
print('-----------------')
print('MPH\tKPH')
print('-----------------')
for kph in range(0, 140, 10):
    mph = kph / 0.6214
    print(kph, '\t', f"{mph:.2f}")