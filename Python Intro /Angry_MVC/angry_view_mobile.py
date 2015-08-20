__author__ = 'TheOneTAR'

class AngryMobileView:
    """Ideal view for smaller screen sizes, such as Mobile screens."""

    def show_instructions(self):
        text = "Welcome to Angry Dice! Roll the 2 dice until you win\n" \
             "Stage 1 – 1 & 2\n" \
             "Stage 2 – ANGRY & 4\n" \
             "Stage 3 – 5 & 6\n" \
             "You can lock one die each stage, but beware!\n" \
             "If you get 2 ANGRY's, you have to restart!\n" \
             "Also, you can never lock a 6! That's cheating!\n\n" \
             "Input the name of the die you want to roll.\n" \
             "Their names are a and b.\n"
        print(text)