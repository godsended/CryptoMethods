import random
import unittest
from methods.AffineMethod import AffineMethod
from methods.CryptoMethod import CryptoMethod

method: CryptoMethod = AffineMethod()

class AffineMethod_test(unittest.TestCase):
    def testEncryption(self):
        inputs = ['БГУ', 'МАМА МЫЛА', 'ЛЕСНАЯ ОПУШКА']
        keys = ['ГА', 'ГБ', 'Ю ']
        espected = ['ГИЩ', 'ЁБЁБЯЁРГБ', 'ЮСМШ ЕВХТЖЩА '] 

        for i in range(len(inputs)):
            self.assertEqual(method.encrypt(inputs[i], keys[i]), espected[i])

    def testDecryption(self):
        inputs = ['ГИЩ', 'ЁБЁБЯЁРГБ', 'ЮСМШ ЕВХТЖЩА '] 
        keys = ['ГА', 'ГБ', 'Ю ']
        espected = ['БГУ', 'МАМА МЫЛА', 'ЛЕСНАЯ ОПУШКА']

        for i in range(len(inputs)):
            self.assertEqual(method.decrypt(inputs[i], keys[i]), espected[i])

    def testRandomCycle(self):
        for _ in range(10):
            key = 'Г '
            word = ''.join(random.choices(population=method.DEFAULT_LANGUAGE, k=10))
            self.assertEqual(word, method.decrypt(method.encrypt(word, key), key))

    def testNegativeKey(self):
        with self.assertRaises(Exception) as context:
            method.encrypt('БАБА ЯГА', 'Б')
        with self.assertRaises(Exception) as context:
            method.encrypt('БАБА ЯГА', 'БАБ')

    def testNegativeAlphabet(self):
        with self.assertRaises(Exception) as context:
            method.encrypt('abc', 'АБ')
        with self.assertRaises(Exception) as context:
            method.encrypt('А', '11')