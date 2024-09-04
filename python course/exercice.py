#Write a function sum_of_digits(number) that takes an integer and returns the sum of its digits.Hint: Use a loop to process each digit.




def sum_of_digits(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print("sum of digits =",sum_of_digits((1, 2, 3, 4))) # output : 10
print("sum of digits =",sum_of_digits((5, 6, 7, 8)))  # output :26
print("sum of digits =",sum_of_digits((9, 1, 0, 1,1)))  # output :12
print("sum of digits =",sum_of_digits((1, 2, 3, 4,5)))  # output : 15
print("sum of digits =",sum_of_digits(()))  # output : 0
#2
def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result
    #3:
    def factorial(n):
    # Handle the base cases
     if n == 0 or n == 1:
        return 1
    
    # Initialize result
    result = 1
    
    # Loop from 1 to n and compute the factorial
    for i in range(2, n + 1):
        result *= i
    
    return result
#4
def pascals_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Start with the first row

    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Start each row with 1

        # Compute the values for the new row based on the previous row
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # End each row with 1
        triangle.append(new_row)
    
    return triangle 
