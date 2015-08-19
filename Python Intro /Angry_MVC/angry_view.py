__author__ = 'TheOneTAR'


class AngryView:

    def show_instructions(self):
        text = "Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!\n" \
             "Stage 1 you need to roll 1 & 2\n" \
             "Stage 2 you need to roll ANGRY & 4\n" \
             "Stage 3 you need to roll 5 & 6\n" \
             "You can lock a die needed for your current stage \n" \
             "and just roll the other one, but beware!\n" \
             "If you ever get 2 ANGRY's at once, you have to restart to Stage 1!\n" \
             "Also, you can never lock a 6! That's cheating!\n\n" \
             "To roll the dice, simply input the name of the die you want to roll.\n" \
             "Their names are a and b.\n"
        print(text)