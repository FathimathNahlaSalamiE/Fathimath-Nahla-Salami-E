list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,8,9,12,46,76,82,15,20,30]
output = {}

for i in list1:
    count = 0
    for j in list2:
        if j % i == 0:
            count += 1
    output[i] = count

print(output)