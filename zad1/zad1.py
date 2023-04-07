from zad1testy import runtests

def ceasar( s ):
    """
    Michal Kawa
    Algorytm szuka palindromow od srodka napisu s i zapamietuje dlugosc najdluzszego
    z tych co znalazl do tej pory. Jezeli algorytm stwierdzi ze znaleziona dlugosc
    palindrmu jest wieksza niz dlugosc pozostalej czesci napisu do sprawdzenia
    algorytm konczy dzialanie.
    zlozonosz: n^2 
    """
    leng = len(s)
    steps = int(leng / 2)
    max_s = 0
    for i in range(steps):
        for n in [1, 2]:
            start = steps - i * (-1) ** n
            j = 0
            while start + j < leng and 0 <= start - j and s[start - j] == s[start + j]:
                j += 1
            max_s = max(max_s, (j - 1) * 2 + 1)
        if max_s > (steps-i)*2:
            break
    return max_s

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
