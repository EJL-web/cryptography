#Cracking Codes Ceaser cipher

import pyperclip

#the string to be encrypted/decryted
message = 'Mai Shiranui is the hottest woman in fiction'

#The encryption/decryption key
key = 13

#wether the the program encrypts or decrypts
mode = 'encrypt' #Set to either 'encrypt' or 'decrypt'

#Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #perform eyncryption/decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wraparound id needed
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        #Append the symbol without enycrpting/decrypting
        translated = translated + symbol

#Output the translated string
print(translated)
pyperclip.copy(translated)
