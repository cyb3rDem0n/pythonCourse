variable_1 = 1
variable_2 = 5
print(f"INITIAL STATE: \nMEM Index_1: {id(variable_1)} \nMEM Index_2: {id(variable_2)}")
variable_1, variable_2 = variable_2, variable_1
print(f"\n\nEDITED STATE: \nMEM Index_1: {id(variable_1)} \nMEM Index_2: {id(variable_2)} \nThe MEM INDEX has been SWAPPED")

print(variable_1, variable_2, sep="\n")

print(30*"##############")
# questo non funziona, la var 1 avrebbe un indirizzo di mem errato
variable_3 = 1
variable_4 = 5
print(f"INITIAL STATE: \nMEM Index_3: {id(variable_3)} \nMEM Index_4: {id(variable_4)}")

# l'indirizzo di memoria della variabile 3 viene sovrascritto da quello della var3, quindi
# nello swap var3 var4 l'indirizzo della 4 è gia quello della 3 quindi swappiamo lo stesso indirizzo
variable_4 = variable_3
variable_3 = variable_4

print(f"\n\nEDITED STATE: \nMEM Index_3: {id(variable_3)} \nMEM Index_4: {id(variable_4)} \nThe MEM INDEX IS EQUAL, VAR3 has the same initial index ")
print(variable_3, variable_4, sep="\n")

# posso usare anche una variabile temporanea come soluzione
