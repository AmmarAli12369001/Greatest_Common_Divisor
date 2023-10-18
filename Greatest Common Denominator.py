"""
Greatest Common Divisor
We say that an integer D is a divisor of another integer A if the fraction A/D is also an integer.
Given two positive integers A and B, compute the largest number which is a divisor of both A and B.

Standard input
The first line contains the two integers A and B.

Standard output
Output a single number representing the greatest common divisor.
"""


def input_value():
    while True:
        input_list = list(input().split(" "))
        if len(input_list) > 0:
            for value in input_list:
                yield value


input_values = input_value()


def valid_input_generator():
    global input_values
    data = next(input_values)

    try:
        return int(data)
    except ValueError:
        try:
            return float(data)
        except:
            return str(data)


a = valid_input_generator()
b = valid_input_generator()

if a > b:
    max_v, min_v = a, b
else:
    max_v, min_v = b, a

v = 0
for i in range(min_v, 0, -1):
    if max_v % i == 0 and min_v % i == 0:
        v = i
        break

print(v)
