from art import logo
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(logo)




def ceasor(start_text, shift_amount, ceasor_direction):
    end_text = ''
    if ceasor_direction == "decode":
            shift_amount *=-1
    for char in start_text:
        if char in alphabet:             
            position = alphabet.index(char)
            new_position = position + shift_amount
            changed_text = alphabet[new_position]
            end_text += changed_text
        else:
             end_text += char
    print(f"The {direction}d text is {end_text}")


should_run_again = True
while should_run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt \n").lower()
    message = input("Type your message: \n").lower()
    shift = int(input("Type your shift number: \n"))

    shift = shift % 25
    ceasor(message, shift, direction)

    result = input("Type 'yes' if you wanna go again, otherwise 'no'.\n")
    if result == 'no':
         should_run_again = False
         print('Goodbye') 

