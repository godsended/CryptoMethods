import random
import unittest
from methods.VigenereMethod import VigenereMethod
from methods.CryptoMethod import CryptoMethod

method: CryptoMethod = VigenereMethod()

class VigenereMethod_test(unittest.TestCase):
    def testEncryption(self):
        inputs = ['БГУ', 'МАМА МЫЛА', 'ЛЕСНАЯ ОПУШКА']
        keys = ['ЛОЖКА', 'БЕГ', 'ПРЫЫЖОК']
        espected = ['МСЪ', 'НЕПБДПЬРГ', 'ЫХЛЗЖМЙЮ НТСО'] 

        for i in range(len(inputs)):
            self.assertEqual(method.encrypt(inputs[i], keys[i]), espected[i])

    def testDecryption(self):
        inputs = ['МСЪ', 'НЕПБДПЬРГ', 'ЫХЛЗЖМЙЮ НТСО'] 
        keys = ['ЛОЖКА', 'БЕГ', 'ПРЫЫЖОК']
        espected = ['БГУ', 'МАМА МЫЛА', 'ЛЕСНАЯ ОПУШКА']

        for i in range(len(inputs)):
            self.assertEqual(method.decrypt(inputs[i], keys[i]), espected[i])

    def testRandomCycle(self):
        for _ in range(10):
            key = ''.join(random.choices(population=method.DEFAULT_LANGUAGE, k=5))
            word = ''.join(random.choices(population=method.DEFAULT_LANGUAGE, k=10))
            self.assertEqual(word, method.decrypt(method.encrypt(word, key), key))

    def testNegativeKey(self):
        with self.assertRaises(Exception) as context:
            method.encrypt('БАБА ЯГА', '')

    def testNegativeAlphabet(self):
        with self.assertRaises(Exception) as context:
            method.encrypt('abc', 'АБ')
        with self.assertRaises(Exception) as context:
            method.encrypt('А', '11')