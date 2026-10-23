import math

x1 = float(input("Enter first input: "))
x2 = float(input("Enter second input: "))

w1 = 0.5
w2 = 0.4
b = 0.2

net = x1 * w1 + x2 * w2 + b

output = 1 / (1 + math.exp(-net))

print("Output of Feed Forward Neural Network =", round(output, 4))
