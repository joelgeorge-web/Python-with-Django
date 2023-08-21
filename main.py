list1 = list(map(int, input("Enter the list: ").split()))

#assign first element as smallest
smallest = list1[0]

for i in range(1, len(list1)):
    if list1[i] < smallest:
        smallest = list1[i]

print("Smallest element is:", smallest)
