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
