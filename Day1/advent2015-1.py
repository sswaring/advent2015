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

floor = 0
position = 0

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

print("Part 2 answer:", position)

