from methods.AffineMethod import AffineMethod
from methods.AlphabetRebaseMethod import AlphabetRebaseMethod
from methods.CaesarMethod import CaesarMethod
from methods.CryptoMethod import CryptoMethod
from methods.ReplacementsMethod import ReplacementsMethod
from methods.VigenereMethod import VigenereMethod

with open('alphabet.txt') as alphabetFile, open('in.txt') as inFile, open('key.txt') as keyFile:
    alphabet = alphabetFile.readline()
    method: CryptoMethod
    methodId = input('1 - Caesar, 2 - Affine, 3 - Rebase, 4 - Hill, 5 - Replacements, Other - Vigenere')
    match methodId:
        case '1':
            method = CaesarMethod()
        case '2':
            method = AffineMethod()
        case '3':
            method = AlphabetRebaseMethod()
        case '4':
            method = VigenereMethod()
        case '5':
            method = ReplacementsMethod()
        case other:
            method = VigenereMethod()  
    
    processId = input('0 - encrtypt, Other - decrypt')

    method.setLanguage(alphabet)

    text = ''
    isFirst = True
    for line in inFile.readlines():
        if not isFirst:
            text += '\n'
        text += line
        isFirst = False

    key = keyFile.readline()
    outputFileName = ''
    output = ''
    match processId:
        case '0':
            outputFileName = 'encrypt.txt'
            output = method.encrypt(text=text, key=key)
        case other:
            outputFileName = 'decrypt.txt'
            output = method.decrypt(text=text, key=key)

    outputFile = open(outputFileName, 'w')
    outputFile.write(output)
    outputFile.close()