import numpy as np

with open("data_3.txt") as f:
    data = [list(map(int, list(line))) for line in f.read().split()]
    
    # Part 1
    gamma = np.sum(data, axis=0) > len(data)/2
    gamma = [int(n) for n in gamma]

    epsilon = [int(not n) for n in gamma]

    # back to string for the bin2dec conversion
    gamma_str = "".join(map(str, gamma))
    epsilon_str = "".join(map(str, epsilon))

    bin2dec = lambda x: int(x, 2)

    print("Part 1: ", bin2dec(gamma_str)*bin2dec(epsilon_str))

  
    # Part 2
    data_o2 = data
    data_co2 = data

    i = 0
    while len(data_o2) > 1:
        # sum cols and get the i-col max value
        max = int(np.sum(data_o2, axis=0)[i] >= len(data_o2)/2.)
        data_o2 = [elem for elem in data_o2 if elem[i] != max]
        i += 1
    
    i = 0
    while len(data_co2) > 1:
        # get the min per col
        min = int(not (np.sum(data_co2, axis=0)[i] >= len(data_co2)/2))
        data_co2 = [elem for elem in data_co2 if elem[i] != min]
        i += 1
        
        

    data_o2_str = "".join(map(str, data_o2[0]))
    data_co2_str = "".join(map(str, data_co2[0]))

    data_o2_dec = bin2dec(data_o2_str)
    data_co2_dec = bin2dec(data_co2_str)

    print("Part 2: ", data_o2_dec*data_co2_dec)

