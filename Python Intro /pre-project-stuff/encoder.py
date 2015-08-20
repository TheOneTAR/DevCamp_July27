"""An Encoder module that takes a string and encodes it into
a secret message, which it then writes to a file.
"""

def main(message = None):
   if message == None:
      message = input("Enter a message to encode. >>> ")

   transcodedMessage = transcode_message(message)
   make_secret(transcodedMessage)


def transcode_message(message):
   transcodedMessage = ""
   for i in message:
      transcodedMessage += str(ord(i)) + " "

   return transcodedMessage

def make_secret(secret):
   with open('secrets.txt', 'w') as f:
      f.write(secret)
