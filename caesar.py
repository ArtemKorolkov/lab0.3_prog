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
