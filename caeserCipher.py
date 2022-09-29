l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

i="ghansham"

# the ascii codes for the values inside the 
# english alphabets 
# A=65
# Z=91
# a=97
# z=122

def giveCipherBit(ch):
    ch=ch.lower()
    if(ord(ch)>=97 and ord(ch)<=121):
        return chr(ord(ch)+1-32)
    if(ord(ch)==122):
        return  chr(65)
    if(ord(ch)==32):
        return chr(32)

def CaesercipherEncryption(plaintext,changeBits):

    ciphertext=""
    z=changeBits
    if(changeBits<0):
        changeBits= 26-changeBits
    for j in range(changeBits):
        ciphertext=""
        for i in plaintext:
            ciphertext+=str(giveCipherBit(i))
        plaintext=ciphertext
    # print(ciphertext)
    return ciphertext

def caeserCipherDecryption(ciphertext,changeBits):
    if changeBits>0:
        return CaesercipherEncryption(ciphertext,26-changeBits).lower()
    else:
        return CaesercipherEncryption(ciphertext,26+changeBits).lower()


print(caeserCipherDecryption(CaesercipherEncryption("ghansham",2),2))
