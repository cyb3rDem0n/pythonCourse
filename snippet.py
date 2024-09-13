


print ("Hello Py")

# un unico print per rappresentare la freccia usando sep

print("    *", "   * *","  *   *"," *     *","***   ***","  *   *","  *   *","  *****", sep = "\n")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# print di un numero in base ottale / base 8 quindi possiamo usare da 0 a 7
# 7  => 07 => 0x8^1 + 7x8^0 = 0+7
# 8  => 10 => 1x8^1 + 0x8^0 = 8+0
# 9  => 11 => 1x8^1 + 1x8^0 = 8+1
# 15 => 17 => 1x8^1 + 7x8^0 = 8+7
# 16 => 20 => 2x8^0 + 0x8^0 = 16+0

print(0o11)


# esadecimale (o base 16) utilizza 16 simboli per rappresentare i numeri: 
# i numeri da 0 a 9 e le lettere da a ad f
# A (che vale 10), B (che vale 11), C (che vale 12), D (che vale 13), 
# E (che vale 14), e F (che vale 15).
# 0xa = 10
# 0x9 = 9
# 0x11 = 17
# 0xf = 15
# 0x10 = 16
# 0x10 => 1x16^1 + 0x16^0 = 16+0 

print(0x10)
print("0x123 ==>","1x16^2 + 2x16^1 + 3x16^0", "256 + 32 + 3", "= 291")
print("0x123 ==>", 0x123)

# esponenziali
# usiamo la e o E per indicarlo
print(0.0000000000000000000001)
print(1E-22)
print(6.62607E-34)
print(1e10)

# ancora stringhe
print('I like "Monty Python"')

#BINARIO
# 00001011 => 0x2^7 + 0x2^6 + 0x2^5 + 0x2^4 + 1x2^3 + 0x2^2 + 1x2^1 + 1x2^0
# 1x2^3 + 0x2^2 + 1x2^1 + 1x2^0 = 8 + 0 + 2 + 1 = 11
#gli zeri a SX sono trascurabili
numero_binario = "1011"
numero_decimale = int(numero_binario, 2)
print(numero_decimale)

# MATH OPERATOR +, -, *, /, // divisione tra integer, % resto, **
# An expression is a combination of values
# Most of Python's operators have left-sided binding, which means that the 
# calculation of the expression is conducted from left to right.
# The exponentiation operator uses right-sided binding
# parentheses are always calculated first,

# RESERVED KEYWORDS IN PY
print('False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 
      'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 
      'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 
      'while', 'with', 'yield')

# The square of the hypotenuse is equal to the sum of the squares of the other two sides.
# 0.5 equivale alla radice

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

# per concatenare stringhe e interi usa la virgola
john = 5
mary = 10
adam = 15
print(john, mary, adam, sep = ",")
total_apples = john + adam + mary
print(total_apples)
print('"Total number of apples:"' , total_apples)

# shortcut operator
x = 2
x *= 5
print(x)

# input function
# the result of the input() function is a string
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

# casting
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# replication operator - 10 * "-" => decuplica -
print("+" + 10 * "-" + "+")
XX = "3"
YY=6
print(XX*YY)

# convert a number into a string
str(100)


# test con anno gregoriano e resto

year = int(input("Enter a year: "))
what = ""

if year < 1582:
    what = "not greg"
else:
    if (year % 4) != 0:
        what = "common year"
    elif (year % 100) != 0:
        what = "leap year"
    elif (year % 400) != 0:
        what = "common year"
    else:
        what = "leap year"

print(what)

# in python anche il FOR puo avere un ELSE
# il for salta viene printato direttamente l'else
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

"""
RANGE() METHOD - crea una sequenza
start: is an optional parameter specifying the starting number of the sequence (0 by default)
stop:  is an optional parameter specifying the end of the sequence generated (it is not included),
step: is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)
"""
for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2 contiamo al contrario


n = range(4)

for num in n: # range genera al volo 0,1,2,3
    print(num - 1) # quindi -1,0,1,2,3
else:
    print(num)


for i in range(0, 6, 3):
    print(i) # stamperà 0 e 3, ricorda che l'estremo è escluso