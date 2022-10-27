divisors = []
number = int(input("Enter a number to find its divisor."))
for element in range (1, (number+1)):
    if number % element == 0:
        divide = int(number/element)
        divisors.append(element)
print(divisors)
