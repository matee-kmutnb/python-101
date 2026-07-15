workH = int(input("work hour: "))
payrate = int(input("payrate: "))


if workH >= 40:
    grosspay = workH * payrate
else:
    regularpay = 40 * payrate
    overtimepay = (workH - 40) * payrate * 1.5
    grosspay = regularpay + overtimepay
print("the gross pay is: " ,grosspay)