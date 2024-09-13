# usando IN per ogni lettera della stringa passata, mi stanpo le singole lettere
# stessa cosa per trovare AEIOU dentro la stringa passata in input

user_word = input("insert your word: ")

for letter in user_word.upper():
    if letter in "AEIOU":
        continue
    
    print(letter)