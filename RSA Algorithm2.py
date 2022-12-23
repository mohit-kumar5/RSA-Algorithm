def mohit(message):
    n = 3
    chunks = [message[i: i + n]
              for i in range(0, len(message), n)]
    list = len(chunks)
    d = 0
    pHex = []
    hexaList = []
    while (d < list):
        s = list(chunks[d])
        l3 = []
        for c in s:
            l3.append(hex(ord(c))[2:])
        pHex = ''.join(map(str, l3))
        hexaList.append(pHex)
        d = d + 1
        print(" ")
    print("Message is devided into three bytes : ", chunks)
    print(" ")
    print("Hexa Decimal Value is : ", hexaList)
    print(" ")
    dec = []
    decList = []
    d = 0
    le = len(hexaList)
    while (d < le):
        x = d
        abc = hexaList[x]
        d = d + 1
        dec = int(abc, 16)
        decList.append(dec)
    print("Decimal Value of the bytes is : ", decList)
    return decList


def Merge(ctext):
    hexa = []
    text_ascii = []
    l = len(ctext)
    u = 0
    while (u < l):
        hexa.append(hex(ctext[u]))
        text_ascii.append(bytearray.fromhex(hexa[0]))
        u = u + 1
    print(hexa)
    print(text_ascii)
    x = ".join(text_ascii)"
    print(x)
    return x

def initEncryption():
    print("Enter Your Partner's Public Key N:")
    publicKeyN = int(input())
    print("Enter Your Partner's Public Key e:")
    publicKeyE = int(input())
    print("Please enter the message you want to encrypt")
    message = str(input())
    List1 = []
    messages = []
    sb = ''
    for i in range(0, len(message), 3):
        if (len(message) - i > 3):
            substring = message[i:i + 3]
            List1.append(substring)
        else:
            substring = message[i:]
            List1.append(substring)
    print(List1)
    for x in List1:
        messageChunk = Encryption(x, publicKeyN, publicKeyE)
        messages.append(messageChunk)
    for i in messages:
        sb = sb + str(i) + ','
    sb = sb[0:-1]
    print('[' + sb + ']')


def Encryption(str, N, e):
    sb = ''
    for i in str:
        ascii = ord(i)
        hexString = hex(ascii)
        sb += hexString.replace('0x', '')
    value = int(sb, 16)
    enc_message = Squareandmultiply(value, e, N)
    return enc_message

def initDecryption():
    print("Enter Your Public Key N:")
    publicKeyN = int(input())
    print("Enter Your Private key d:")
    PrivateKeyD = int(input())
    print("Please enter the message you want to Decrypt")
    message = str(input())
    message = message.replace('[', '')
    message = message.replace(']', '')
    messages = []
    values = message.split(",")
    for i in values:
        chunk = int(i)
        messageChunk = Decryption(chunk, PrivateKeyD, publicKeyN)
        messages.append(messageChunk)
    print(messages)
    concat = ''.join(messages)
    print(concat)


def Decryption(str, D, N):
    sb = ''
    decryptedMessage = Squareandmultiply(str, D, N)
    hexString = hex(decryptedMessage)
    sb += hexString.replace('0x', '')
    bytesFormat = bytes.fromhex(sb)
    dec_message = bytesFormat.decode("ASCII")
    return dec_message




def Squareandmultiply(str, e, N):
    Dict = {}
    binarystring = bin(e).replace("0b", "")
    reversebinarystring = binarystring[::-1]
    result = 0
    endresult = 1
    for i in range(len(binarystring)):
        if (i == 0):
            result = str
        else:
            result = result * result
            if (result >= N):
                quotient = result // N
                result = quotient * N
        Dict[i] = result
    for j in range(0, len(reversebinarystring)):
        if (reversebinarystring[j] == '1'):
            endresult *= Dict[j]
            if (endresult >= N):
                quotient = endresult // N
                endresult = quotient * N

    if (endresult >= N):
        quotient = endresult // N
        endresult -= quotient * N
    return endresult


def Signature():
    sb = ''
    print("Please enter the your Public key N")
    publicKeyN = int(input())
    print("Please enter the your Private key D")
    publicKeyE = int(input())
    print("Please enter Your Signature to be encrypted")
    message = str(input())
    List1 = []
    messages = []
    for i in range(0, len(message), 3):
        if (len(message) - i > 3):
            substring = message[i:i + 3]
            List1.append(substring)
        else:
            substring = message[i:]
            List1.append(substring)
    print(List1)
    for x in List1:
        messageChunk = Encryption(x, publicKeyN, publicKeyE)
        messages.append(messageChunk)
    for i in messages:
        sb = sb + str(i) + ','
    sb = sb[0:-1]
    print('The encryption of my signature is as below : ')
    print('[' + sb + ']')


def Verification():
    print("Please enter the Partner's Public key N")
    publicKeyN = int(input())
    print("Please enter the Partner's Public key e")
    PrivateKeyD = int(input())
    print("Please enter the patners sign : ")
    sign = str(input())
    print("Please enter the patners encrypted signature : ")
    message = str(input())
    message = message.replace('[', '')
    message = message.replace(']', '')
    messages = []
    values = message.split(",")
    for i in values:
        chunk = int(i)
        messageChunk = Decryption(chunk, PrivateKeyD, publicKeyN)
        messages.append(messageChunk)
    concat = ''.join(messages)
    if (sign == concat):
        print('Signature verification is: True')
    else:
        print('Signature verification is: False')
    print(concat)


print('This is the program for RSA Encryption && Decryption!')
print(
    'select: \n Enter 1 for Encryption \n Enter 2 for Decryption \n Enter 3 for Signature \n Enter 4 for verifying signature')
selection = int(input())
if selection == 1:
    initEncryption()
if selection == 2:
    initDecryption()
if selection == 3:
    Signature()
if selection == 4:
    Verification()
else:
    print('select a valid option')
