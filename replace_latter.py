user_input = input("Enter your phase : ")
start_latter = (input("Enter the starting latter : ").lower())[0]

alphabet = []

for i in range(97, 122 + 1):
    alphabet += chr(i)


user_alphabet = []
for i in range((ord(start_latter)), 122 + 1):
    user_alphabet += chr(i)

firt_latter = user_alphabet[0]
if len(user_alphabet) < 26:
    for i in range(97, ord(firt_latter)):
        user_alphabet += chr(i)


output = ""
for latter in user_input:
    if latter in alphabet:
        num = alphabet.index(latter)
        output += (user_alphabet[num])
    else:
        output += latter

print(output)
