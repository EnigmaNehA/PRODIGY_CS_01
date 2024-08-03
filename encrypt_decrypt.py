def Encryptmessage(input_str, key1):
    encstring = ''
    for i in input_str:
        if (ord(i) >= 65 and ord(i) <= 90):  # Uppercase letters
            tempstr = (ord(i) + key1)
            if tempstr > 90:
                tempstr = tempstr % 90 + 64
            encstring += chr(tempstr)
        elif (ord(i) >= 97 and ord(i) <= 122):  # Lowercase letters
            tempstr = (ord(i) + key1)
            if tempstr > 122:
                tempstr = tempstr % 122 + 96
            encstring += chr(tempstr)
        else:
            encstring += i  # Non-alphabetic characters remain unchanged
    return encstring

def Decryptmessage(input_str, key1):
    string2 = Encryptmessage(input_str, key1)
    dncstring = ''
    for i in string2:
        if (ord(i) >= 65 and ord(i) <= 90):  # Uppercase letters
            dncstring += chr((ord(i) - key1 - 65) % 26 + 65)
        elif (ord(i) >= 97 and ord(i) <= 122):  # Lowercase letters
            dncstring += chr((ord(i) - key1 - 97) % 26 + 97)
        else:
            dncstring += i  # Non-alphabetic characters remain unchanged
    return dncstring

print("Enter the string to encrypt and decrypt:")
string1 = input()
print("Enter the key (Eg. 2):")
keyp = int(input()) % 26  # Ensure key is within the range 0 to 25
print("Encrypted message is:", Encryptmessage(string1, keyp))
print("Decrypted message is:", Decryptmessage(string1, keyp))
