from methods.CryptoMethod import CryptoMethod

class CaesarMethod(CryptoMethod):

    def __init__(self):
        self.__lang = CryptoMethod.DEFAULT_LANGUAGE

    def encrypt(self, text: str, key: str):
        result: str = ''
        for char in text:
            ind = self.__lang.index(char)
            ind += self.__lang.index(key)
            ind %= len(self.__lang)
            result += self.__lang[ind]

        return result
    
    def decrypt(self, text: str, key: str):
        result: str = ''
        for char in text:
            ind = self.__lang.index(char)
            ind -= self.__lang.index(key)
            ind %= len(self.__lang)
            result += self.__lang[ind]

        return result
    
    def setLanguage(self, language: str):
        self.__lang = language