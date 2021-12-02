with open("data_1.txt") as f:
    data = [int(line) for line in f.read().split()]
    
    count_1 = 0
    count_2 = 0

    for i in range(0, len(data)): 
        count_1 += data[i] > data[i-1]
        
    for i in range(2, len(data)):
        count_2 += sum(data[i-2:i+1]) < sum(data[i-1:i+2])

print(count_1)
print(count_2)

