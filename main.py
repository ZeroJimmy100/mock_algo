A = [100, 200, 0, 300, 400, 0, 200, 200]
arr = []
right = 0
left = 0
result = 0
for index, number in enumerate(A):

    arr.append(number)
    print(arr)
    if (len(arr) == 4):
        left = sum(arr[:2])
        print("left:", left)
        right = sum(arr[2:])
        print("right", right)
        if (right == left):
            result += 1
            left = 0
            right = 0
            arr = []
        else:
            left = 0
            right = 0
            arr = []
print(result)
