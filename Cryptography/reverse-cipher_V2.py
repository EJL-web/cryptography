#Improved reverse cipher

message = input('Write message here --  ')
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
