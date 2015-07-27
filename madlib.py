# This script will take input from the user in the form of various words,
# then output a hopefully amusing intrductory news paragraph.
#########################################################################

# First, we start the article.
article = "A "

# Next, we collect the first piece of input to add to the article
theInput = input("Please type the name of a state. >> ")

# we add it to the article, along with the setup for the next piece
article += theInput + " man and his family, who collected $"

# we continue this process until the article is complete
theInput = input("Please enter a large number. >> ")
article += theInput + " through charities promising to help "

theInput = input("Please type in a group of people. >> ")
article += theInput + ", spent much of the money on themselves. Expenses ranged from "

theInput = input("Please type in something expensive. >> ")
article += theInput + " to "

theInput = input("Please type in another opulent object. >> ")
article += theInput + ", according to "

theInput = input("Please type in a type of document (e.g. 'federal lawsuit') >> ")
article += theInput + "."

# finally, we print the article to the screen, after a few new lines.
print("\n\n")
print(article)
print("\n\n")