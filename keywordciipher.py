def keyword_cipher(message,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newMessage = message+ "".join([letter for letter in alphabet if letter not in message])
    newerMessage = ""
    for keyLetter in key:
        newerMessage = newerMessage + newMessage[alphabet.find(keyLetter)]
    print(newerMessage)

keyword_cipher("keyword","abchij")
# output = "keyabc"

keyword_cipher("purplepineapple","abc")
# output = "pur"

keyword_cipher("mubashir","edabit")
# output = "samucq"

keyword_cipher("etaoinshrdlucmfwypvbgkjqxz","abc")
# output = "eta"

keyword_cipher("etaoinshrdlucmfwypvbgkjqxz","xyz")
# output = "qxz"

keyword_cipher("etaoinshrdlucmfwypvbgkjqxz","aeiou")
# output = "eirfg"
