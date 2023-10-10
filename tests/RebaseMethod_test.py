from ctypes import Array
import random
import unittest
from methods.AlphabetRebaseMethod import AlphabetRebaseMethod
from methods.CryptoMethod import CryptoMethod

method: CryptoMethod = AlphabetRebaseMethod()

class AffineMethod_test(unittest.TestCase):
    def testEncryption(self):
        inputs = ['БГУ', 'МАМА МЫЛА', 'ЛЕСНАЯ ОПУШКА']
        key = 'ВУЁБЕПЛТЗРХЯЭШОЙЖЪЫЦАМ ДЩЬСКИНЮЧФГ'
        espected = ['УБА', 'ШВШВГШИЭВ', 'ЭПЫОВФГЙЖАЬЯВ'] 

        for i in range(len(inputs)):
            self.assertEqual(method.encrypt(inputs[i], key), espected[i])

    def testDecryption(self):
        inputs = ['УБА', 'ШВШВГШИЭВ', 'ЭПЫОВФГЙЖАЬЯВ']
        key = 'ВУЁБЕПЛТЗРХЯЭШОЙЖЪЫЦАМ ДЩЬСКИНЮЧФГ'
        espected = ['БГУ', 'МАМА МЫЛА', 'ЛЕСНАЯ ОПУШКА']

        for i in range(len(inputs)):
            self.assertEqual(method.decrypt(inputs[i], key), espected[i])

    def testRandomCycle(self):
        for _ in range(10):
            key = list(method.DEFAULT_LANGUAGE)
            random.shuffle(key)
            key = ''.join(key)
            word = ''.join(random.choices(population=method.DEFAULT_LANGUAGE, k=10))
            self.assertEqual(word, method.decrypt(method.encrypt(word, key), key))

    def testNegativeKey(self):
        with self.assertRaises(Exception) as context:
            method.encrypt('БАБА ЯГА', '')
        with self.assertRaises(Exception) as context:
            method.encrypt('БАБА ЯГА', 'БАБ')

    def testNegativeAlphabet(self):
        with self.assertRaises(Exception) as context:
            method.encrypt('abc', 'АБ')
        with self.assertRaises(Exception) as context:
            method.encrypt('А', '11')