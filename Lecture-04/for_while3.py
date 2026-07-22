keep_going = 'y'

while keep_going == 'y':
    wholesale_cost = float(input('Enter the wholesale cost: '))
    retail_price = wholesale_cost * 2.5
    print(f'The retail price is ${retail_price:.2f}')
    keep_going = input('Do you want to calculate another' + \
                       ' retail price (Enter y for yes  ): ')