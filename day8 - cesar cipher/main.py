# def greet():
#     print('hello')
    
# greet()

alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabeth.index(letter)
#         new_position = (position + shift_amount) % len(alphabeth)
#         new_letter = alphabeth[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabeth.index(letter) 
#         new_position = (position - shift_amount) % len(alphabeth)
#         new_letter = alphabeth[new_position]
#         plain_text += new_letter
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
    

def cesar(text, shift, direction):
    output = ""
    for letter in text:
        if letter in alphabeth:
            position = alphabeth.index(letter)
            if direction == "decode":
                new_position = (position - shift) % len(alphabeth)
            else:
                new_position = (position + shift) % len(alphabeth)
            new_letter = alphabeth[new_position]
            # print(new_letter)
        else:
            new_letter = letter
        output += new_letter
    print(f"Here is the {direction}d result: {output}")

cont = True
while cont:
    cesar(text=text, shift=shift, direction=direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if again == "no":
        cont = False
