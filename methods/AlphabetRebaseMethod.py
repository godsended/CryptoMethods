from methods.CryptoMethod import CryptoMethod

class AlphabetRebaseMethod(CryptoMethod):

    def __init__(self):
        self.__lang = CryptoMethod.DEFAULT_LANGUAGE

    def encrypt(self, text: str, key: str):
        if sorted(self.__lang) != sorted(key):
            raise Exception('Key must contains all the alphabet letters and vice verca!')

        result: str = ''
        for char in text:
            result += key[self.__lang.index(char)]

        return result
    
    def decrypt(self, text: str, key: str):
        if sorted(self.__lang) != sorted(key):
            raise Exception('Key must contains all the alphabet letters and vice verca!')

        result: str = ''
        for char in text:
            result += self.__lang[key.index(char)]

        return result
    
    def setLanguage(self, language: str):
        self.__lang = language