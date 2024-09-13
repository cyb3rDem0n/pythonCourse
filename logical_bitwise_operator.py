"""
##

Key takeaways

1. Python supports the following logical operators:

and → if both operands are true, the condition is true, e.g., (True and True) is True,
or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.
2. You can use bitwise operators to manipulate single bits of data. The following sample data:

x = 15, which is 0000 1111 in binary,
y = 16, which is 0001 0000 in binary.
will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

& does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
| does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
>> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
<< does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary,

AND
0 0 0 1
OR
0 1 1 1
XOR
0 1 1 0




"""






"""
A SX gli operatori logici a destra i Bitwise Op.
AND => & (ampersand) - bitwise conjunction
OR  => | (bar) - bitwise disjunction
NOT => ~ (tilde) - bitwise negation
XOR => ^ (caret) - bitwise exclusive

Logical values vs. single bits

LOGICAL operators take their arguments as a whole regardless 
of how many bits they contain. 

The operators are aware only of the value: 
- zero (when all the bits are reset) means False; 
- not zero (when at least one bit is set) means True.

The result of their operations is one of these values: False or True. 

This means that this snippet will assign the value True to the j variable if i is not zero; 
otherwise, it will be False.
"""

# i = 1
# j = not not i

# print(i, "--", j)

"""
Let us add an important remark: the arguments of these operators must be integers; 
we must not use floats here.

The difference in the operation of the logical and bit operators is important: 
the logical operators do not penetrate into the bit level of its argument. 
They're only interested in the final integer value.

Bitwise operators are stricter: they deal with every bit separately.
 If we assume that the integer variable occupies 64 bits (which is common in modern computer systems), 
 you can imagine the bitwise operation as a 64-fold evaluation of the logical operator for each pair 
 of bits of the arguments. This analogy is obviously imperfect, as in the real world all 
 these 64 operations are performed at the same time (simultaneously).
"""

"""

# h e k sono TRUE perchè il loro valore è != 0
h = bool(15)
k = bool(22)
m = bool(0)
# h: 00000000000000000000000000001111
# k: 00000000000000000000000000010110

logicResult = h and k
print(f"risultato AND= {logicResult} valore m=  {m}")



# i =   00000000000000000000000000001111
# j =   00000000000000000000000000010110
# AND = 00000000000000000000000000000110

# facciamo la AND dei bit non trascurabili
i = 15
j = 22
bit = i & j	# 00000000000000000000000000000110

print(bin(i))
print(bin(j))
print(bin(bit))

print(f"bitwise operation is: {bit}") #stamperà 6 perchè la nad dei due valori, IN BIT, da 0110 ovvero 6

#print(f"negazione bit= {~m}")


###############
print("/*"*15)

myNumber = 8
print("my Number In Bit: ",bin(8))

myNumber = 8
myNumberInBit = format(myNumber, '032b')
print(f"Rappresentazione a 8 bit: {myNumberInBit}")


tot = 0
num = 45
print(bin(num))
for posizione in range(31):  # Controlla i bit da 0 a 31
    bit = num & (1 << posizione)
    if bit:
        tot += 2**posizione
        print(tot)

if bin(tot) & bin(12):
    print("true")


numero = 128
lunghezza_bit = numero.bit_length()

for i in range(lunghezza_bit):
        bit = (numero & (1 << i)) >> i
        print(f"Bit alla posizione {i}: {bit}")  
        if bit == 1:
                print(f"FOUND in position {i} so the number is => {2**i}")  

"""

def scansiona_bit(numero):
    # Otteniamo il numero di bit necessario per rappresentare il numero
    lunghezza_bit = numero.bit_length()

    # Cicliamo su ciascuna posizione di bit
    for posizione in range(lunghezza_bit):
        # Creiamo una maschera con 1 spostato a sinistra nella posizione desiderata
        bit = (numero & (1 << posizione)) >> posizione
        if bit == 1:
            print(f"There's a 1 in position {posizione}")
        #print(f"Bit alla posizione {posizione}: {bit}")

# Esempio di utilizzo
numero = 5124  # In binario: 00001000
scansiona_bit(numero)


"""
var = 8
var_right = var >> 1
var_left = var << 1
print(var, var_right, var_left)


8 => 00001000 -> 2^3
8 >> 00000100 -> 2^2
8 >> 00010000 -> 2^4

"""

x = 4
y = 1

a = x & y # 0100 and 0001 = 0 xke false
b = x | y # 0100 or 0001 = 0101
c = ~x  # NOT 0100 -> 1011 -> gli zeri a sx diventano uni 11111011 -> -5?
d = x ^ 5 # 0100 XOR 0101 ->  0001
e = x >> 2 # 0100 -> 0001 -> 2^0
f = x << 2 # 0010 -> 10000 -> 2^4

print(a, b, c, d, e, f)