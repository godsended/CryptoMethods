import random
import unittest
from methods.CaesarMethod import CaesarMethod
from methods.CryptoMethod import CryptoMethod

method: CryptoMethod = CaesarMethod()

class CaesarMethod_test(unittest.TestCase):
    def testEncryption(self):
        inputs = ['БГУ', 'МАМА МЫЛА', 'ЛЕСНАЯ ОПУШКА']
        keys = ['Г', 'А', 'Я']
        espected = ['ДЁЦ', 'МАМА МЫЛА', 'ЙГПЛЯЭЮМНСЦИЯ'] 

        for i in range(len(inputs)):
            self.assertEqual(method.encrypt(inputs[i], keys[i]), espected[i])

    def testDecryption(self):
        inputs = ['ДЁЦ', 'МАМА МЫЛА', 'ЙГПЛЯЭЮМНСЦИЯ'] 
        keys = ['Г', 'А', 'Я']
        espected = ['БГУ', 'МАМА МЫЛА', 'ЛЕСНАЯ ОПУШКА']

        for i in range(len(inputs)):
            self.assertEqual(method.decrypt(inputs[i], keys[i]), espected[i])

    def testRandomCycle(self):
        for _ in range(10):
            key = random.choice(method.DEFAULT_LANGUAGE)
            word = ''.join(random.choices(population=method.DEFAULT_LANGUAGE, k=10))
            self.assertEqual(word, method.decrypt(method.encrypt(word, key), key))

    def testNegativeAlphabet(self):
        with self.assertRaises(Exception) as context:
            method.encrypt('abc', 'А')
        with self.assertRaises(Exception) as context:
            method.encrypt('А', 'abc')