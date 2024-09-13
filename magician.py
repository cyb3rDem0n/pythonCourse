print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

secret_number = 666

inputNumber = int(input("magic num: "))

while inputNumber != 666:
    print("Ha ha! You're stuck in my loop!")
    inputNumebr = int(input("magic num: "))
print("Well done, muggle! You are free now.")

