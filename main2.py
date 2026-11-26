n = int(input("enter a number (try 5 or 12)"))
guess = input("Left shift doubles it. guess: " + str(n) + " << 1 =?")

input("NOT flips every bit. press enter")
print("  12 =", bin(12)[2:])
print("  NOT 12 =", ~12 & 0xFF)

input("XOR gives bits give 1. Press enter")
print("  12 ^ 10 =", 12 ^ 10)

input('LEft shift multiplies by 2. press enter')
print(f'   ', n , " << 1 =", n << 1, "  your guess:", guess)

input('RIght shift divides by 2. press enter')
print(f'   ', n , " >> 1 =", n >> 1)
