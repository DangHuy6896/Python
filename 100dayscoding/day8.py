import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

want_continue = True

while want_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction != "encode" and direction != "decode":
    print("Please enter one of the two options correctly")
    sys.exit()
  shift = int(input("Type the shift number:\n"))
  f_shift = shift % 26
  text = input("Type your message:\n").lower()  
  text_list = list(text)
  if direction == "encode":
    for letter in range(len(text)):
      if text_list[letter] in alphabet:
        text_list[letter] = alphabet[alphabet.index(text_list[letter]) - 26 + f_shift]
    text = ''.join(text_list)
    print(f"Here is the encode result: {text}")
  elif direction == "decode":
    for letter in range(len(text)):
      if text_list[letter] in alphabet:
        text_list[letter] = alphabet[alphabet.index(text_list[letter]) - f_shift]
    text = ''.join(text_list)
    print(f"Here is the decode result: {text}")

  again = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
  if again == "yes":
    want_continue = True
  elif again == "no":
    want_continue = False
    print("Goodbye!")
  else:
    want_continue = False
    print("Please enter one of the two options correctly")