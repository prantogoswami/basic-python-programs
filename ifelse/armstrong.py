#An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its digits raised to the power of the number of digits. For example, 153 is an Armstrong number
num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")