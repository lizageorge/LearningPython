"""
This was my response to my mom's challenge to find the average of the numbers 0 - 9
"""
digits = []
for x in range(0, 10, 1):
    digits.append(x)
print(digits)

sum_of_digits = 0
for value in digits:
    sum_of_digits = sum_of_digits + value

print(f"The sum is {sum_of_digits}")
average = sum_of_digits / len(digits)
print(f"The average is {average}")
