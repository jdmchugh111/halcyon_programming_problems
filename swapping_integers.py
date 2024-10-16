# I ordered these solutions from best to worst.
# Solution 1:
# The first solution using tuples seems to be the best because it's a single line, concise solution.
# It doesn't require any extra memory (like assigning a new variable), and it doesn't require any unnecessary mathematical operations like Solution 2.
# Solution 2:
# This solution is decent, but it does add new math operations (even though they're small and simple) to the stack unnecessarily.
# Solution 3:
# This solution is probably the least optimal since you're requiring more memory when you asign a new variable.

# Solution 1: Using tuples
a = 3
b = 7

a, b = b, a

print(a, b)

# Solution 2: Using simple arithmetic
a = 3
b = 7

a = a + b
b = a - b
a = a - b

print(a, b)

# Solution 3: Using a third variable
a = 3
b = 7

c = a
a = b
b = c

print(a, b)