from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random


# users choose 3, 5 or 10 rounds
class ChooseRounds:

    def __init__(self):
        # invoke play class with three rounds for testing purposes.
        self.to_play(3)

    def to_play(self, num_rounds):
        Play(num_rounds)

        # hide root window (ie: hide rounds choice window)
        root.Withdraw()

class Play:

    def __init__(self, how_many):

        self.play_box = Toplevel()

        # if users press cross at top, closes help  and
        # 'releases' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        # variables used to work out statistics, when game ends etc
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        # initially set rounds played and rounds won to 0
        self.rounds_player = IntVar()
        self.rounds_player.set(0)

        self.rounds_won = IntVar()
        self.rounds_won.set(0)

        # lists to hold user score/s and computer score/s
        # used to work statistics

        user_scores = []
        computer_scores = []

        # get all the colours for use in game
        self.all_colours = self.get_all_colours()

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quest_frame, text=rounds_heading,
                                    font=("Arial", "16", "bold")
                                    )
        self.choose_heading.grid(row=0)

        instructions = "Choose one of the colours below. When you choose " \
                       "a colour, the computer's choice and the results"



