import math
from typing import Any
from methods.CryptoMethod import CryptoMethod

class AffineMethod(CryptoMethod):

    def __init__(self):
        self.__lang = CryptoMethod.DEFAULT_LANGUAGE

    def encrypt(self, text: str, key: str):
        if len(key) != 2:
            raise Exception('Key must consist from 2 letters!')

        a = self.__lang.index(key[0]) 
        b = self.__lang.index(key[1]) 
        l = len(self.__lang)

        if math.gcd(a, l) != 1:
            raise Exception('GCD of a and alphabet must be 1!')

        result: str = ''
        for char in text:
            ind = (self.__lang.index(char) * a + b) % l
            result += self.__lang[ind]

        return result
    
    def decrypt(self, text: str, key: str):
        if len(key) != 2:
            raise Exception('Key must consist from 2 letters')

        a = self.__lang.index(key[0]) 
        b = self.__lang.index(key[1]) 
        l = len(self.__lang)

        ma = 0
        for i in range(len(self.__lang)):
            if (a * i) % l == 1:
                ma = i
                break

        result: str = ''
        for char in text:
            ind = (ma * (self.__lang.index(char) - b)) % l
            result += self.__lang[ind]

        return result
    
    def setLanguage(self, language: str):
        self.__lang = language