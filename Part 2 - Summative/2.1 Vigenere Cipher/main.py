# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  word = ""
  text = text.upper()
  text = text.replace(" ", "")
  for i in range(len(text)):
    index = (alpha.index(text[i]) + alpha.index(keyword[i % len(keyword)])) % 26
    word += alpha[index]
  return word


def vig_decode(text, keyword):
  word = ""
  text = text.upper()
  text = text.replace(" ", "")
  for i in range(len(text)):
    index = (alpha.index(text[i]) - alpha.index(keyword[i % len(keyword)])) % 26
    word += alpha[index]
  return word


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!