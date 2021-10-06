# Problema 7: Sa se verifice daca un numar este antipalindrom


def is_antipalindrome(n):
    """
    Introducem intr-un vector cifrele numarului n
    Verificam daca cifrele egal departate de mijlocul numarului sunt egale, iar daca gasim vreo pereche atunci programul
    va returna False
    In caz contrar, acesta va returna True
    :param n: numarul de verificat
    :return: True sau False in functie de proprietatea numarului de a fi antipalindrom
    """
    v = []
    while n > 0:
        v.append(n % 10)
        n //= 10
    for i in range(len(v)//2):
        if v[i] == v[len(v)-i-1]:
            return False
    return True


# Problema 8: Sa se treaca un numar din baza 10 in baza 2;


def get_base_2(n):
    """
    Transformam string-ul citit in numar intreg pentru a ne putea folosi de functia bin() care converteste un numar
    intreg din baza 10 in baza 2
    Mai apoi transformam numarul gasit inapoi intr-un string, iar apoi stergem prefix '0b' care va aparea inaintea
    numarului dorit din cauza folosirii functiei bin()
    :param n: numarul de convertit
    :return: numarul n scris in baza 2
    """
    return str(bin(int(n))).removeprefix('0b')


# Problema 5: Sa se verifice daca un numar e palindrom (problema rezolvata in timpul laboratorului 2)


def is_palindrome(n):
    """
    Introducem intr-un vector cifrele numarului n
    Verificam daca cifrele egal departate de mijlocul numarului sunt diferite, iar daca gasim vreo astfel de
    pereche atunci programul va returna False
    In caz contrar, acesta va returna True
    :param n: numarul de verificat
    :return: True sau False in functie de proprietatea numarului de a fi palindrom
    """
    v = []
    while n > 0:
        v.append(n % 10)
        n //= 10
    for i in range(len(v)//2):
        if v[i] != v[len(v)-i-1]:
            return False
    return True


def test_is_antipalindrome():
    assert not is_antipalindrome(2773)
    assert not is_antipalindrome(23532)
    assert is_antipalindrome(2783)


def test_get_base_2():
    assert get_base_2(4) == "100"
    assert get_base_2(7) == "111"


def test_is_palindrome():
    assert not is_palindrome(2773)
    assert is_palindrome(23532)
    assert not is_palindrome(2783)


def print_menu():
    print('1. Problema 7')
    print('2. Problema 8')
    print('3. Problema 5')
    print('4. Exit')

    n = input('Alegeti o optiune: ')

    if n == '1':
        nr = input('Introduceti un numar: ')
        nr = int(nr)
        if is_antipalindrome(nr):
            print(nr, ' este antipalindrom')
        else:
            print(nr, ' nu este antipalindrom')
    elif n == '2':
        nr = input('Introduceti un numar: ')
        nr = int(nr)
        print('Numrul', nr, 'in bazza 2 este', get_base_2(nr))
    elif n == '3':
        nr = input('Introduceti un numar: ')
        nr = int(nr)
        if is_palindrome(nr):
            print(nr, ' este palindrom')
        else:
            print(nr, ' nu este palindrom')
    elif n == '4':
        exit(0)


def main():
    test_is_antipalindrome()
    test_get_base_2()
    test_is_palindrome()

    while True:
        print_menu()


if __name__ == "__main__":
    main()
