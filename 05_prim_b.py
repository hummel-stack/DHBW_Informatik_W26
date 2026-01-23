DEBUG_INFO = False

def prime_num(num):
    '''
    Berechnet Primzahl
    '''
    # Rückgabe: True wenn num Primzahl ist, sonst False
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    import math
    max_div = int(math.isqrt(num))
    i = 3
    while i <= max_div:
        if num % i == 0:
            return False
        i += 2
    return True




max_num = 10
prime_nums = {}

if __name__ == "__main__":
    import sys
    # Kommandozeilen-Argument bevorzugen
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Bitte eine gültige ganze Zahl als Argument angeben.")
            sys.exit(1)
        print(prime_num(n))
    else:
        # Interaktive Eingabe (einmalig)
        try:
            s = input("Gib eine Zahl ein (oder ENTER, um Primzahlen bis max_num zu sehen): ").strip()
        except EOFError:
            s = ''
        if s:
            try:
                n = int(s)
            except ValueError:
                print("Bitte eine gültige ganze Zahl eingeben.")
            else:
                print(prime_num(n))
        else:
            # Standardverhalten: Primzahlen bis max_num ausgeben
            for z in range(0, max_num + 1):
                if prime_num(z):
                    print("                Ich bin eine Primzahl: ", z)
            #print(prime_nums)
