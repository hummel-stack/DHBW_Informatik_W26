#####################################################################################
# Dateiname:       01_summe.py  [1-1]                                               #
# --------------------------------------------------------------------------------- #
# Implementierung: https://www.programiz.com/python-programming/examples/add-number #
# Algorithmus:                                                                      #
# Ein-/Ausgabe:                                                                     #
# Beschreibung:    Addition zweier (Fließkomma-/ganze)Zahlen                        #
# Lernziele:       Überlagerung des + Operators (Addition/String-Konkatenation)     #
# Anmerkungen:                                                                      #
#####################################################################################


# Store input numbers
# int cast (i.e. int()) must be used to transfer strings to integer numbers
# the same is valid for float cast float()
# FRAGE: Was passiert, wenn die beiden int()-Casts weggelassen werden?
# ANTWORT: String-Konkatenation anstatt Addition
num1_string = input('Enter first number: ')
num1 = int(num1_string)
num2_string = input('Enter second number: ')
num2 = int(num2_string)

# Or fixed values instead
# num1 = 3
# num2 = 6

# Add two numbers (fixed values)
sum = num1 + num2
# This schema below is useful when only the sum is shown (optional)
# sum = int(num1_string) + int(num2_string)

# Display the sum (2 versions)
# First with no formatting of input and output numbers
print("Die Summe von", num1, "und" , num2, "ist:", sum)

# The next versions uses the newest f-string formatting, see https://pyformat.info/ for details
# IMPORTANT: works only in Python 3.6 or newer!
print(f"Die Summe von {num1} und {num2} ist: {sum}")

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print('The sum of {} and {} is {}'.format(num1, num2, sum))
print('The sum of {:06.2f} and {:06.2f} is {:06.2f}'.format(num1, num2, sum))
print('The sum of {1:07.4f} and {0:06.2f} is {2:06.2f}'.format(num1, num2, sum))

tt="""
Weitere Formatierungsarten werden in 02_squareroot.py ausführlicher behandelt:

This next formatting is slightly older than the first one
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
The identifier may be omitted
print('The sum of {} and {} is {}'.format(num1, num2, sum))

The floating point numbers may be characterized specifically
(here: 6 digits overall, 2 digits after point; valid with f-string formats as well)
print('The sum of {:06.2f} and {:06.2f} is {:06.2f}'.format(num1, num2, sum))
With turning of the first two terms
print('The sum of {1:06.2f} and {0:06.2f} is {2:06.2f}'.format(num1, num2, sum))
"""
#print(tt)