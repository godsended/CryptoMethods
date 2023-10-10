import random
import unittest
from methods.ReplacementsMethod import ReplacementsMethod
from methods.CryptoMethod import CryptoMethod

method: CryptoMethod = ReplacementsMethod()

class VigenereMethod_test(unittest.TestCase):
    def testEncryption(self):
        inputs = ['БГУ', 'МАМА МЫЛА', 'ЛЕСНАЯ ОПУШКА']
        keys = ['ЛОБ', 'БЕГ', 'ПРЫЖОК ВУХ']
        espected = ['ГУБ', 'ММААМ ЫАЛ', 'Я УСАНЛЕОПВГЁАБАШКДЕ'] 

        for i in range(len(inputs)):
            self.assertEqual(method.encrypt(inputs[i], keys[i]), espected[i])

    def testDecryption(self):
        inputs = ['ГУБ', 'ММААМ ЫАЛ', 'Я УСАНЛЕОПВГЁАБАШКДЕ'] 
        keys = ['ЛОБ', 'БЕГ', 'ПРЫЖОК ВУХ']
        espected = ['БГУ', 'МАМА МЫЛА', 'ЛЕСНАЯ ОПУШКААБВГДЕЁ']

        for i in range(len(inputs)):
            self.assertEqual(method.decrypt(inputs[i], keys[i]), espected[i])

    def testRandomCycle(self):
        for _ in range(10):
            key = ''.join(random.choices(population=method.DEFAULT_LANGUAGE, k=5))
            keyIsBad = False
            sortedKey = sorted(key)
            for i in range(len(key) - 1):
                if sortedKey[i] == sortedKey[i + 1]:
                    keyIsBad = True
                    break
            
            if keyIsBad:
                continue

            word = ''.join(random.choices(population=method.DEFAULT_LANGUAGE, k=10))
            self.assertEqual(word, method.decrypt(method.encrypt(word, key), key))

    def testNegativeKey(self):
        with self.assertRaises(Exception) as context:
            method.encrypt('БАБА ЯГА', '')