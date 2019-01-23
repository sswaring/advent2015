floor = 0
position = 0

# save route to a variable
with open ("input.txt") as f:
    route = f.read().strip()

# if the character is "(" then Santa goes up one floor
# if the character is ")" then Santa goes down one floor
for x in route: 
    if x == "(":
        floor += 1
    elif x == ")":
        floor -= 1
   
# What floor does Santa end up on?
print("Part 1 answer:", floor)

# initialize variables
floor = 0
position = 0

# run until floor < 0
# add to position variable after every move
for x in route:
    if x == "(":
        floor += 1
        position += 1
        if floor < 0:
            break
    elif x == ")":
        floor -= 1
        position += 1
        if floor < 0:
            break

# At what position does Santa arrive at floor -1?
print("Part 2 answer:", position)

