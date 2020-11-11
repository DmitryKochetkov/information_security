# Practice 1: Caesar cipher

print("Enter text to decode:", end=' ')
encoded = input()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'

unknown_char_flag = False
for key in range(27):
    decoded = ""
    for c in encoded:
        index = alphabet.find(c.upper())
        if index == -1:
            unknown_char_flag = True
            decoded += c
        else:
            decoded += alphabet[(index - key) % len(alphabet)]

    print("Key ", key, ": ", decoded, sep = '')

if unknown_char_flag:
        print("Warning: unknown characters detected!")