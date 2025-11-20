######################################################################################
# Dateiname:       02_squareroot.py  [1-2]                                           #
# ---------------------------------------------------------------------------------- #
# Implementierung: https://www.programiz.com/python-programming/examples/square-root #
# Algorithmus:                                                                       #
# Ein-/Ausgabe:    num=9 / num_sqrt=3                                                #
# Beschreibung:    Quadratwurzel                                                     #
# Lernziele:       Formatierung der Ausgabe (f-String, etc.), Benutzereingaben       #
# Anmerkungen:     https://pyformat.info/, https://fstring.help/cheat/               #
#                  (Ausgabe-Formatierung)                                            #
######################################################################################

# User input 
# Version 1: String input must be converted to float first
num_string = input('Enter a number: ')
num = float(num_string)
# Version 2: Beide Befehle in eine Zeilen durch Semikolon getrennt (nicht empfohlen!)
# num_string = input('Enter a number: '); num = float(num_string)
# Version 3: Zusammenfassung beider Befehle in einen geschachtelten Befehl
# num = float(input('Enter a number: '))

# Or we just use a fixed value instead
# num = 9 

num_sqrt = num ** 0.5
# Alternative: Verwendung der sqrt()-Funktion. Hierzu müssen wir zunächst das math-Modul importieren.
# Import-Module werden ausführlicher in 14_ggt_run.py behandelt!
# num_sqrt = sqrt(num)

# This is the newest formatting using the new f-strings (Python 3.6+)
# https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
print(f'The square root of {num} is {num_sqrt}')
# using specific num formatting (see https://fstring.help/cheat/ for details)
print(f'The square root of {num:0.2f} is {num_sqrt:0.2f}')
# The same effect with (omitting leading 0) ...
# print(f'The square root of {num:.2f} is {num_sqrt:.2f}')

# Print statement using slightly older but still valid formatting, see https://pyformat.info/
print('The square root of {:0.3f} is {:0.3f}'.format(num ,num_sqrt))
# omitting specific formatting rules, using system wide formatting instead
print('The square root of {:f} is {:f}'.format(num ,num_sqrt))

# Print statement using old formatting, see https://pyformat.info/
# IMPORTANT NOTICE: Should not be used any longer!
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

# Just for your info: no formatting looks like this
print('The square root of', num, 'is', num_sqrt)