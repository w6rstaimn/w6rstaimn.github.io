take in the number
n = input()  # Input: space-separated numbers

calculate answer
numbers = n.split()  # Split input into a list of strings
seen = set()  # Set to track seen numbers
unique_numbers = []  # List to store unique numbers in order

for num in numbers:
    if num not in seen:
        seen.add(num)
        unique_numbers.append(num)

print answer
print(" ".join(unique_numbers))  # Output: space-separated unique numbers