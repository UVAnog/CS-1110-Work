import copy

for i in range(1,101):
    if not i % 3:
        print(i, end=' ')

print()

for letter in "Guess what I do!":
    if letter > 'k':
        print(letter, end='')

print()

def count_fruits(fruits):
    count = 0
    fruit_found = False
    for i in "banana pineapple orange grapefruit":
            if i == 'n' and not fruit_found:
                fruit_found == True
                count += 1
            elif i == ' ':
                fruit_found = False
    print(count)

print()

sum = 0
for i in (-10, -5, 0, 5, 10):
    if i < 0:
        sum += i
print(sum)


a_list = ['one', 'two']
x = ['three']
a_list += [x]
x[0] = 3
print(a_list)

def what_fruits(a_list):
    a_list[0] = 'apple'

fruits = ['banana', 'orange']
what_fruits(fruits)
print(fruits + ['kiwi'])



def operate(a,b):
    c = a + b
    return a, b, c
print (list(operate(5,6)))

my_list = [5,6,7,8,9]
double_list = [i*2 for i in my_list]
print(double_list)





