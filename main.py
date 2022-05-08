import random


ALPHABET = "abcdefghijklmnopqrstuvwxyz"
random.seed(199)


def replacespace(text_list):
    for character in range(0, len(text_list)):
        random_number = str(random.randint(0, 9))
        if text_list[character] == " ":
            text_list[character] = random_number
    return text_list


def replacenumber(text_list):
    for character in range(0, len(text_list)):
        if text_list[character] in "0123456789":
            text_list[character] = " "
    return text_list


def getkey():
    key = input("Please enter the key: ")
    iskeyvalid = False
    while iskeyvalid == False:
        if (len(key) % 2 == 1) and (key.islower() == True):
            for character in key:
                if character not in ALPHABET:
                    break
            break
        print("Invalid Key!")
        print()
        key = input("Please enter the key: ")
    return key


def encrypt(text, key):
    text = text.lower()
    textlist = list(text)
    first_letter = text[0]
    third_letter = text[2]
    textlist[0] = third_letter
    textlist[2] = first_letter
    textlist = replacespace(textlist)
    alphabetlist = list(ALPHABET)
    keylength = len(key)
    magicnumberindex = int((keylength-1)/2)
    magicnumber = ALPHABET.index(key[magicnumberindex])
    for evenindex in range(0, len(textlist), 2):
        if textlist[evenindex].isalpha() == True:
            characterindex1 = alphabetlist.index(textlist[evenindex])
            textlist[evenindex] = alphabetlist[int(characterindex1+keylength)%26]
    for oddindex in range(1, len(textlist), 2):
        if textlist[oddindex].isalpha() == True:
            characterindex2 = alphabetlist.index(textlist[oddindex])
            textlist[oddindex] = alphabetlist[int(characterindex2+magicnumber)%26]
    text = "".join(textlist)
    return text


def decrypt(encryptedtext, key):
    encryptedtextlist = list(encryptedtext)
    first_letter = encryptedtext[0]
    third_letter = encryptedtext[2]
    encryptedtextlist[0] = third_letter
    encryptedtextlist[2] = first_letter
    textlist = replacenumber(encryptedtextlist)
    alphabetlist = list(ALPHABET)
    keylength = len(key)
    magicnumberindex = int((keylength - 1) / 2)
    magicnumber = ALPHABET.index(key[magicnumberindex])
    for evenindex in range(0, len(textlist), 2):
        if textlist[evenindex].isalpha() == True:
            characterindex1 = alphabetlist.index(encryptedtextlist[evenindex])
            encryptedtextlist[evenindex] = alphabetlist[int(characterindex1 - keylength) % 26]
    for oddindex in range(1, len(textlist), 2):
        if textlist[oddindex].isalpha() == True:
            characterindex2 = alphabetlist.index(encryptedtextlist[oddindex])
            encryptedtextlist[oddindex] = alphabetlist[int(characterindex2 - magicnumber) % 26]
    text = "".join(textlist)
    return text


textinput = input("Please enter the text you want to encrypt: ")
keyinput = getkey()
encryptedtextinput = encrypt(textinput, keyinput)
print()
print("Input message:", textinput)
print("Encrypted message:", encrypt(textinput, keyinput))
print("Decrypted message:", decrypt(encryptedtextinput, keyinput))