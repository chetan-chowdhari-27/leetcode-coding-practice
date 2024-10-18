# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = int(input())
m = int(input())

# Calculate a^b mod m
x = pow(a, b)
x1 = pow(a, b, m)

# Print the result
print(x)
print(x1)
