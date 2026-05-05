lst = [10, 20, 30, 40]
key = int(input("Enter number to search: "))

for i in range(len(lst)):
    if lst[i] == key:
        print("Found at position", i)
        break
else:
    print("Not found")