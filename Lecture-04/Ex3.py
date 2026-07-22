column = int(input("Enter the number of columns: "))
for i in range(1, 101):
    print(i, end="\t")
    if i % column == 0:
        print()