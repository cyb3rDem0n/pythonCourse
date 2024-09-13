# 2 (starting number) → 5 (2 increment by 3 equals 5 - the number is within the range from 2 to 8) → 8 
# (5 increment by 3 equals 8 - the number is not within the range from 2 to 8, 
# because the stop parameter is not included in the sequence of numbers generated by the function.)
for i in range(2, 8, 3):
    print("The value of i is currently", i)
# cicla da 0 a 8 con step di 1
for i in range(0, 8, 1):
    print("The value of i is currently", i)

#####################################################

# 16 cicli, expo contiene semplicemente l'indice
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

# utilizzo di print(f" mi chiamo {var}")
import time

# Loop to count from 1 to 5 "Mississippily"
for i in range(1, 6):
    print(f"{i} Mississippi")
    time.sleep(1)  # Sleep for 1 second to simulate a real-time delay

# Final message
print("Ready or not, here I come!")

# BRACK e CONTINUE
# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

###########################################
# la differenza è che BREAK ci fa uscire subito e
# completamente dal loop, mentre CONTINUE salta solo
# un ciclo a seconda della logica che vogliamo,
# ma non esce dal loop, è un salto condizionale.

# break usato per interrompere il loop assieme al counter
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1: # mi serve per fermare/pilotare il loop
        break
    counter += 1 # se quando interrompo è 0 vuol dire che non arrivo mai qui 
                    # e non ho mai messo alcun valore eccetto -1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


# alternativa con continue
# OCCHIO, al primo inserimento l'input è fuori,
# quindi se metto -1 esco subito
# se invece entro nel loop, allora l'input viene pilotato dal
# controllo =>  if number == -1: continue, che saltera l'unica iterazione
# e in questo caso chiude il loop
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue # se metto un print prima non verrà stampato xke continue ha "priorità"
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

