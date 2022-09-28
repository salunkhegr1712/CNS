def Encryption(plaintext, key_val):
    ciphertext = ''
    for i in range(len(plaintext)):
        word = plaintext[i]
        new_word = word.lower()
        if new_word == " ":
            ciphertext += ' '
        elif word.isalpha():
            ciphertext += chr((ord(new_word) + key_val - 97) % 26 + 97)

    return ciphertext


def Decryption(ciphertext, key_val):
    plaintext = ''
    for i in range(len(ciphertext)):
        word = ciphertext[i]
        new_word = word.lower()
        if new_word == " ":
            plaintext += ' '
        elif word.isalpha():
            plaintext += chr((ord(new_word) - key_val - 97) % 26 + 97)
    return plaintext


while True:

    print('Wlcm to Caeser Cipher Encryption-Decryption\n Press 1 for Encryption \n Press 0 for Decryption \n Press 01 to exit.. ')

    choice = input(' >>>>')

    if choice.isdigit():

        if choice == '1':

            sen = input('Insert the plaintext : ')
            key = int(input('Insert shift value(Only integer values) : '))
            print(50 * '-')
            print(f'Your ciphertext ---> {Encryption(sen, key)}')
            print(50 * '-')
            print('word symbols (!,# etc and numbers) are deleted..')
            con = input('Type any Key to continue &  no to exit')

            if con == 'no':

                print('Exiting..')
                break
            else:

                pass
        
        elif choice == '0':

            csen = input('Insert the ciphertext : ')
            key = int(input('Insert shift value(Only integer values) : '))
            print(50 * '-')
            print(f'Your plaintext --->{Decryption(csen, key)}')
            print(50 * '-')
            print('word symbols (!,# etc and numbers) are deleted..')
            con = input('Shall we continue ? [Any Key/no]')

            if con == 'no':

                print('Exiting..')
                break

            else:

                pass

        elif choice == '-1':

            print('Exiting out of code ')
            break

        else:

            print('Exception error  \n' + 'Please insert 0 or 1 ')