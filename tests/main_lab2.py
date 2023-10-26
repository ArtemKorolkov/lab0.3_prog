#1
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext.upper():
        #проверка для последних букв
        if i == 'X':
            ciphertext += 'A'
        elif i == 'Y':
            ciphertext += 'B'
        elif i == 'Z':
            ciphertext += 'C'
        #проверка на строку или знак = запись без изменений
        elif i.isnumeric() or i in '.,^-/:;"%$#@&*?№! ':
            ciphertext+=i
        else:
            ciphertext += chr(ord(i) + shift)

    #приведение к определенному формату
    if plaintext.isupper():
        return ciphertext
    elif plaintext.islower():
        return ciphertext.lower()
    else:
        return ciphertext.title()



def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext.upper():
        # проверка для первых букв
        if i=='A':
            plaintext+='X'
        elif i=='B':
            plaintext+='Y'
        elif i=='C':
            plaintext+='Z'
        # проверка на строку или знак = запись без изменений
        elif i.isnumeric() or i in '.,^-/:;"%$#@&*?№ !':
            plaintext+=i
        else:
            plaintext += chr(ord(i) - shift)

    # приведение к определенному формату
    if ciphertext.isupper():
        return plaintext
    elif ciphertext.islower():
        return plaintext.lower()
    else:
        return plaintext.title()

print(encrypt_caesar('Python3.6'))
print(decrypt_caesar(encrypt_caesar('Python3.6')))

#2
#создание 2-ух словарей для шифрования
sl_byk={'A': 0, 'B': 1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12,
    'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
sl_ch={0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M',
    13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    #увеличение ключа в случае несовпадания с длиной шифруемого слова
    while len(keyword)<len(plaintext):
        keyword+=keyword
    if keyword>plaintext:
        keyword=keyword[0:len(plaintext)]
    keyword=keyword.upper()
    #задание ключей для определения формата слова
    if plaintext.isupper():
        f='U'
    elif plaintext.islower():
        f='L'
    else:
        f='T'
    plaintext=plaintext.upper() #преобразование в капс для удобства

    for i in range(len(plaintext)):
        #проверка на строку и знак = запись без преобразований
        if plaintext[i].isnumeric() or plaintext[i] in '.,^- /:;"%$#@&*?№!':
            ciphertext += plaintext[i]
        else:
            #проверка на индекс словаря
            if sl_byk[plaintext[i]]+sl_byk[keyword[i]] > 25:
                ciphertext += sl_ch[sl_byk[plaintext[i]]+sl_byk[keyword[i]]-26]
            else:
                ciphertext += sl_ch[sl_byk[plaintext[i]] + sl_byk[keyword[i]]]
    #приведение к нужному формату
    if f=='U':
        return ciphertext
    elif f=='L':
        return ciphertext.lower()
    else:
        return ciphertext.title()

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    # увеличение ключа в случае несовпадания с длиной шифруемого слова
    while len(keyword) < len(ciphertext):
        keyword += keyword
    if keyword > ciphertext:
        keyword = keyword[0:len(ciphertext)]
    keyword=keyword.upper()
    # задание ключей для определения формата слова
    if ciphertext.isupper():
        f = 'U'
    elif ciphertext.islower():
        f = 'L'
    else:
        f = 'T'
    ciphertext = ciphertext.upper() #преобразование в капс для удобства

    for i in range(len(ciphertext)):
        #проверка на строку и знак = запись без преобразований
        if ciphertext[i].isnumeric() or ciphertext[i] in '.,^-/:;"%$#@&*?№! ':
            plaintext += ciphertext[i]
        else:
            #проверка на индекс словаря
            if sl_byk[ciphertext[i]] - sl_byk[keyword[i]] < 0:
                plaintext += sl_ch[sl_byk[ciphertext[i]] - sl_byk[keyword[i]] + 26]
            else:
                plaintext += sl_ch[sl_byk[ciphertext[i]] - sl_byk[keyword[i]]]
    #приведение к нужному формату
    if f == 'U':
        return plaintext
    elif f == 'L':
        return plaintext.lower()
    else:
        return plaintext.title()

print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))

#3
import random

# функция проверки на простоту
def is_prime(n: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    f=True
    if str(n).isnumeric():
        for i in range(2,int(n*0.5)+1):
            if n % i == 0:
                f=False
                break
            else:
                f=True
        return f
    else:
        return "It's not a number"

def generate_keypair(p: int, q: int): #-> Tuple[Tuple[int, int], Tuple[int, int]]
    if str(p).isnumeric() and str(q).isnumeric():
        if not (is_prime(p) and is_prime(q)):
            raise ValueError('Both numbers must be prime.')
        elif p == q:
            raise ValueError('p and q cannot be equal')

        n = p*q #произведение протых числе
        phi = (p-1)*(q-1) #функция эйлера

        # рандомное число е<phi и взаимнопростое с ним
        e = random.randrange(1, phi)

        # проверка на взаимно простое число и поиск подходящего ключа
        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)

        # Расширенный алгоритм евклида для поиска d: d * e mod phi = 1
        d = multiplicative_inverse(e, phi)
        return ((e, n), (d, n))
    else:
        return 'Incorrect input'

def gcd(a: int, b: int) -> int: #поиск НОД
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if str(a).isnumeric() and str(b).isnumeric():
        while (a):
            b, a = a, b % a
        return b
    else:
        return 'Incorrect input'

def multiplicative_inverse(e: int, phi: int) -> int: #Расширенный алгоритм Евклида
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
    if str(e).isnumeric() and str(phi).isnumeric():
        a = 0
        if phi > e:
            a = phi
        elif phi <= e:
            a = e

        for d in range(a):
            if ((d * e) % phi) == 1:
                return d
    else:
        return 'Incorrect input'

print(multiplicative_inverse(7,40))
print(generate_keypair(7,5))