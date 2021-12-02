''' 
PART 1 
******
- forward 5 adds 5 to your horizontal position, a total of 5.
- down 5 adds 5 to your depth, resulting in a value of 5.
- forward 8 adds 8 to your horizontal position, a total of 13.
- up 3 decreases your depth by 3, resulting in a value of 2.
- down 8 adds 8 to your depth, resulting in a value of 10.
- forward 2 adds 2 to your horizontal position, a total of 15.

PART 2
******
- forward 5 adds 5 to your horizontal position, a total of 5. 
Because your aim is 0, your depth does not change.
- down 5 adds 5 to your aim, resulting in a value of 5.
- forward 8 adds 8 to your horizontal position, a total of 13. 
Because your aim is 5, your depth increases by 8*5=40.
- up 3 decreases your aim by 3, resulting in a value of 2.
- down 8 adds 8 to your aim, resulting in a value of 10.
- forward 2 adds 2 to your horizontal position, a total of 15. 
Because your aim is 10, your depth increases by 2*10=20 to a 
total of 60.

What do you get if you multiply your final horizontal 
position by your final depth?
'''


with open("data_2.txt") as f:
    data = [line for line in f.read().split()]

    h = 0
    d = 0 

# PART 1
    for i in range(len(data)):
        if data[i] == "forward":
            h += int(data[i+1])
            

        if data[i] == "up":
            d -= int(data[i+1])

        if data[i] == "down":
            d += int(data[i+1])
    
    print(10*'-', 'Part 1', 10*'-')
    print(f'Horizontal: {h}\nDepth: {d}\nHoriz*Depth: {d*h}\n')
  
# PART 2
    h = 0
    d = 0
    aim = 0

    for i in range(len(data)):
        if data[i] == "forward":
            h += int(data[i+1])
            d += int(data[i+1]) * aim

        if data[i] == "up":
            aim -= int(data[i+1])

        if data[i] == "down":
            aim += int(data[i+1])

    print(10*'-', 'Part 2', 10*'-')
    print(f'Horizontal: {h}\nDepth: {d}\nHoriz*Depth: {d*h}')


    
