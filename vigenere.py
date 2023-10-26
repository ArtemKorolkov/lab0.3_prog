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
