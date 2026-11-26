n = int(input("Enter a number  (try 5 or 12):  "))
guess = input("guess its binry")


input("binary. press enter")
print("  decimal", n, "-> binary", bin(n)[2:])
print("  your guess: ", guess)

input('AND - both bits must be 1. Press Enter')
print('  12 =', bin(12)[2:])
print('  10 =', bin(10)[2:])
print('12 & 10', bin(12 & 10)[2:])

input('or - atleast one bit must be 1. press enter  ')
print   ('  12 | 10 =', bin(12 | 10)[2:])