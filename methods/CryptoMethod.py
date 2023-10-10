class CryptoMethod:
    DEFAULT_LANGUAGE: str = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    
    def encrypt(self, text: str, key: str):
        Exception('Is abstract method')

    def decrypt(self, text: str, key: str):
        Exception('Is abstract method')
    
    def setLanguage(self, language: str):
        Exception('Is abstract method')