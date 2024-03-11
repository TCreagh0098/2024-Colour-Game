from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random


# users choose 3, 5 or 10 rounds
class ChooseRounds:

    def __init__(self):

        button_font = ("Arial", "13", "bold")
        button_fg = "#FFFFFF"

        # set up GUI frame
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()

        # heading and brief instructions
        self.temp_heading = Label(self.intro_frame,
                                  text="Colour Quest",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        choose_instruction_txt = "In each round you will be given " \
                                 "six different colours to choose " \
                                 "from.  Pick a colour and see if " \
                                 "you can beat the computer's " \
                                 "score!\n\n" \
                                 "To begin, choose how many rounds " \
                                 "you'd like to play..."
        self.choose_instructions_label = Label(self.intro_frame,
                                               text=choose_instruction_txt,
                                               wraplength=300,
                                               justify="left")
        self.choose_instructions_label.grid(row=1)

        # rounds buttons...
        self.how_many_frame = Frame(self.intro_frame)
        self.how_many_frame.grid(row=2)

        self.three_button = Button(self.how_many_frame, fg=button_fg,
                                   bg="#CC0000", text="3 Rounds",
                                   font=button_font, width=10)
        self.three_button.grid(row=0, column=0, padx=5, pady=5)

        self.five_button = Button(self.how_many_frame, fg=button_fg,
                                  bg="#009900", text="5 Rounds",
                                  font=button_font, width=10)
        self.five_button.grid(row=0, column=1, padx=5, pady=5)

        self.ten_button = Button(self.how_many_frame, fg=button_fg,
                                 bg="#000099", text="10 Rounds",
                                 font=button_font, width=10)
        self.ten_button.grid(row=0, column=2, padx=5, pady=5)


class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()

        # If users press cross at top, closes help and
        # 'releases' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quest_frame, text=rounds_heading,
                                    font=("Arial", "16", "bold")
                                    )
        self.choose_heading.grid(row=0)

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        self.start_over_button = Button(self.control_frame, text="Start Over",
                                        command=self.close_play)
        self.start_over_button.grid(row=0, column=2)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    ChooseRounds()
    root.mainloop()
