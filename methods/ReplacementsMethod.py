from functools import cmp_to_key
from multiprocessing import process
from methods.CryptoMethod import CryptoMethod

class ReplacementsMethod(CryptoMethod):

    def __init__(self):
        self.__lang = CryptoMethod.DEFAULT_LANGUAGE

    def __processKey(self, key: str):
        sortedKey = sorted(key)
        for i in range(len(sortedKey)):
            if (i < len(sortedKey) - 1 and sortedKey[i] == sortedKey[i + 1]) or sortedKey[i] not in self.__lang:
                Exception('All characters in key must be in alphabet and unique!')

        return list(map(lambda char: sortedKey.index(char), key))

    def encrypt(self, text: str, key: str):
        newKey = self.__processKey(key)
        keyLen = len(key)
        miss = len(text) % keyLen
        if miss > 0:
            for i in range(keyLen - miss):
                text += self.__lang[i]

        result: str = ''
        for i in range(int(len(text) / keyLen)):
            for j in range(keyLen):
                result += text[i * keyLen + newKey[j]]

        return result
    
    def decrypt(self, text: str, key: str):
        newKey = self.__processKey(key)
        keyLen = len(key)

        miss = len(text) % keyLen
        for i in range(miss):
            text += self.__lang[i]

        result: str = ''
        for i in range(int(len(text) / keyLen)):
            for j in range(keyLen):
                result += text[i * keyLen + newKey.index(j)]

        return result
    
    def setLanguage(self, language: str):
        self.__lang = language