# create a variable for the puzzle input
with open ("input.txt") as f:
    puzzle_input = f.readlines()

puzzle_list = []
for x in puzzle_input:
    puzzle_list.append(x.split('x'))

# grab the first digit and save it in a list of lengths
lengths = []
for i in puzzle_list:
    lengths.append(i[0])

# grab the second digit and save it in a list of widths
widths = []
for i in puzzle_list:
    widths.append(i[1])

# grab the third digit in each mini list and save it in a list of heights
heights = []
for i in puzzle_list:
    heights.append(i[2])

# do calc1 = l*w
calc1 = 0
# do calc2 = w*h
calc2 = 0
# do calc3 = h*l
calc3 = 0

# create a list to save these 
deminsions_step1 = []
for x in puzzle_list:
    calc1 = int(x[0]) * int(x[1])
    calc2 = int(x[1]) * int(x[2])
    calc3 = int(x[2]) * int(x[0])
    deminsions_step1.append([calc1, calc2, calc3])

# find the minimum in each set
deminsions_step2 = []
for i in deminsions_step1:
    minimum = min(i)
    deminsions_step2.append(minimum)

# do 2* each number in puzzle_list
deminsions_step3 = []
for x in puzzle_list:
    new_calc1 = 2* int(x[0]) * int(x[1])
    new_calc2 = 2* int(x[1]) * int(x[2])
    new_calc3 = 2* int(x[2]) * int(x[0])
    deminsions_step3.append([new_calc1, new_calc2, new_calc3])

# get sum of each list in deminsions_step3
sum_list = []
for x in deminsions_step3:
    sum = int(x[0]) + int(x[1]) + int(x[2])
    sum_list.append(sum)

# find total of sums + deminsions_step2 (slack needed)
totals = [deminsions_step2[i] + sum_list[i] for i in range(len(deminsions_step2))]

# calculate the puzzle answer as sum of all elements in list totals
puzzle_answer = 0
for x in totals:
    puzzle_answer = puzzle_answer + x
    
print("Part 1 answer is:", puzzle_answer)

# Part 2 starts here
# calculate perimeter of smallest side
# order the numbers in each inner list to be smallest to largest
for x in puzzle_list:
    x.sort(key=int)

# do calculation x[0] + x[0] + x[1] + x[1]
# save to list
perimeters_list = []
perimeter = 0
for x in puzzle_list:
    perimeter = int(x[0]) + int(x[0]) + int(x[1]) + int(x[1])
    perimeters_list.append(perimeter)

#calculate ribbon needed for bow by doing index[0] * index[1] * index[2]
ribbons_list = []
ribbon = 0
for x in puzzle_list:
    ribbon = int(x[0]) * int(x[1]) * int(x[2])
    ribbons_list.append(ribbon)

# add the elements of the perimeters list and the ribbons list
totals = 0
totals = [perimeters_list[i] + ribbons_list[i] for i in range(len(perimeters_list))]

# initialize variable for puzzle answer
puzzle_answer = 0

for x in totals:
    puzzle_answer = puzzle_answer + x
    
print("Part 2 answer is:", puzzle_answer)
