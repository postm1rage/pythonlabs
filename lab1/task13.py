n = int(input())
m = int(input())
symb = input()

print(m * symb)
for i in range(n-2):
    print(symb + (n-2) * ' ' + symb)
print(m * symb)