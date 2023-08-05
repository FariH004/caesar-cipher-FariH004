alphabet = "abcdefghijklmnopqrstuvwxyz"
user_plaintext = input("Enter your plaintext: ")
key = int(input("Enter a key: "))

encrypted_text = ""
for char in user_plaintext:
    if char in alphabet:
       position = alphabet.find(char)
       new_position = (position + key) % 26
       new_char = alphabet[new_position]
       encrypted_text += new_char
    else:
        # If the character is not in the alphabet (e.g., space or punctuation), keep it as is.
        encrypted_text += char

print("The encrypted sentence is: " + encrypted_text)


    