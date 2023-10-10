from methods.CaesarMethod import CaesarMethod
from methods.CryptoMethod import CryptoMethod

class VigenereMethod(CryptoMethod):

    def __init__(self):
        self.__lang = CryptoMethod.DEFAULT_LANGUAGE

    def encrypt(self, text: str, key: str):
        currInd = 0
        keyLen = len(key)
        affine = CaesarMethod()
        affine.setLanguage(self.__lang)

        result: str = ''
        for char in text:
            result += affine.encrypt(char, key[currInd])
            currInd += 1
            currInd %= keyLen

        return result
    
    def decrypt(self, text: str, key: str):
        currInd = 0
        keyLen = len(key)
        affine = CaesarMethod()
        affine.setLanguage(self.__lang)

        result: str = ''
        for char in text:
            result += affine.decrypt(char, key[currInd])
            currInd += 1
            currInd %= keyLen

        return result
    
    def setLanguage(self, language: str):
        self.__lang = language