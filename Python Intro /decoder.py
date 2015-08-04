"""A Decoder module that takes a file name, opens the file, 
retrieves the encoded message, decodes it, and then prints that.
"""

def main(filename = 'secrets'):
   secret = getSecret(filename)
   message = decodeSecret(secret)
   print(message)

def getSecret(filename):
   #Open the file, and read the message in
   secret = ""
   return secret

def decodeSecret(secret):
   #Decode the file
   message = ""

   return message


