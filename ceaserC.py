#defines function for ceaser cipher
def encyption_method()->str:
    encrypted_data = ""
   #asks users what message they want to encrypt, and what the shift of the cypher 
    message = input("what message would you like to encrypt?: ")
    shift = int(input("what is the shift of your message?:(enter as number) "))
    #for every character of message loop once
    for char in message:
 
        # we must covert to ascii using ord
        #declares the ascii version of char as a variable
        char_code = ord(char) 
        

        #adds number to ascii so when ascii is coverted back to letter the value will be different
        new_char_code = char_code + shift

        #converts shifted ascii back into normal letters 
        new_char = chr(new_char_code)
        # sets result equal to itself plus the new charater generated 
        encrypted_data = encrypted_data + new_char
    
    print("message sucsessfully encrypted")
    users_choice = input("would you like to see encrypted message? (y/n)")
    if users_choice == "y":
        print(encrypted_data)
    else:
        print("data will not be printed")

#to decrypt data use the same logic as encryption, just subtract by the shift instead of add
def decryption_method():
    decrypted_data = ""
    message = input("what message you would like to decrypt?: ")
    shift= int(input("what is the shift of your message?:(enter as number) "))
    for char in message:
        char_code = ord(char)
        new_char_code = char_code - shift
        new_char = chr(new_char_code)
        decrypted_data = decrypted_data + new_char
    print("message sucsessfully encrypted")
    users_choice = input("would you like to see encrypted message? (y/n) ")
    if users_choice == "y":
        print(decrypted_data)
    else:
        print("data will not be printed")



#full function 
def encrypt_decrypt():
    encryptORdecrypt = input("would you like to encrypt or decrypt?:(en/de) ")
    if encryptORdecrypt == "en":
        encyption_method()
    elif encryptORdecrypt == "de":
        decryption_method()
    else:
        print("invalid input")
    exit
encrypt_decrypt()




