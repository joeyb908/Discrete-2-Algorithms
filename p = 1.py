# 

p = 1
s = int(input("Enter the integer you will raise: "))
r = int(input("Enter your exponent: "))
n = int(input("Enter your modulo: "))

while (r > 0):
    if (r % 2 == 1):
        p = p * s % n
    
    s = s * s % n
    r = r // 2

print(p)