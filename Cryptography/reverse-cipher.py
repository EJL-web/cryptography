#Reverse cipher again

message = 'for the need of a nail the horseshoe was lost'
translated = ''

i = len(message)- 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
