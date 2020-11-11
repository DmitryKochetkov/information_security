# Practice 1: Caesar cipher

print("Enter text to encode:", end=' ')
plaintext = input()
print("Enter encryption key:", end=' ')
key = int(input())

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'

unknown_char_flag = False
encoded = ""
for c in plaintext:
    index = alphabet.find(c.upper())
    if index == -1:
        unknown_char_flag = True
        encoded += c
    else:
        encoded += alphabet[(index + key) % len(alphabet)]

if unknown_char_flag:
    print("Warning: unknown characters detected!")
print("Encoded text:")
print(encoded)
