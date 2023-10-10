# Johnson, Hugo - Massey Overnighter Service
# Booking service for buses between Auckland and Palmerston North
# 23.8.2023

# Importing
from tkinter import *
from functools import partial # to prevent unwanted windows
from tkmacosx import Button
import random

class Booking:
    def __init__(self):

        # Formatting variables
        background_color = "blue"
        secondary_color ="light goldenrod"
        font_color = "white"

        # Main window frame
        self.booking_frame = Frame(root, bg=background_color, pady=10)
        self.booking_frame.grid()

        # Booking service heading (row 0)
        self.booking_heading = Label(self.booking_frame, text="Massey Overnighter Service",
        font= ("Arial", "19", "bold"), fg='gold', bg=background_color, padx=10, pady=10)
        self.booking_heading.grid(row=0, columnspan=2)

        # User instuctions (row 1)
        self.booking_instructions = Label(self.booking_frame, text="Welcome to Massey Overnighter Bus Service, book tickets below", 
        font= ("Arial", "10", 'italic'), bg=background_color, fg=font_color, padx=10, pady=10)
        self.booking_instructions.grid(row=1, columnspan=2)

        # Name entry (row 2)

        # Name Label
        self.name_label = Label(self.booking_frame, font='Arial 14 bold', fg=font_color, text='Name:', bg=background_color)
        self.name_label.grid(row=2, column=0, pady=10, padx=10, sticky='e')

        # Name entry box
        self.name_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', bg=secondary_color)
        self.name_entry.grid(row=2, column=1)

        # Phone number entry (row 3)

        # Phone number Label
        self.phone_label = Label(self.booking_frame, font='Arial 14 bold', text='Phone number:', fg=font_color, bg=background_color)
        self.phone_label.grid(row=3, column=0, pady=10, padx=10, sticky='e')

        # Phone number entry box
        self.phone_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', text="Phone number:", bg=secondary_color)
        self.phone_entry.grid(row=3, column=1, pady=10, padx=10)

        # City headings (row 4)

        # To Auckland heading
        self.to_auckland = Label(self.booking_frame, text="To Auckland", font= ("Arial", "10", 'italic'), 
        bg=background_color, wrap=290, padx=10, pady=10, fg=font_color)
        self.to_auckland.grid(row=4, column=0)

        # To Palmerston North heading
        self.to_palmerston_north = Label(self.booking_frame,text="To Palmerston North",
        font= ("Arial", "10", 'italic'), bg=background_color,wrap=290, padx=10, pady=10, fg=font_color)
        self.to_palmerston_north.grid(row=4, column=1)

        # Book seats label (row 5)

        # Seats to Auckland
        self.seats_auckland_label = Label(self.booking_frame, font= ("Arial", "10", 'italic'), text='How many seats would you like to book?:', bg=background_color, fg=font_color)
        self.seats_auckland_label.grid(row=5, column=0)

        # Seats to Palmerston North
        self.seats_palmerston_north_label = Label(self.booking_frame, font= ("Arial", "10", 'italic'), text='How many seats would you like to book?:', bg=background_color, fg=font_color)
        self.seats_palmerston_north_label.grid(row=5, column=1)

        # Book seats entry (row 6)

        # Entry to Auckland
        self.seats_auckland_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', bg=secondary_color)
        self.seats_auckland_entry.grid(row=6, column=0, pady=10, padx=10)

        # Entry to Palmerston North
        self.seats_palmerston_north_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', bg=secondary_color)
        self.seats_palmerston_north_entry.grid(row=6, column=1, pady=10, padx=10)

        # Book bunks label (row 7)

        # Bunks in Auckland
        self.bunks_auckland_label = Label(self.booking_frame, font= ("Arial", "10", 'italic'), text='How many bunks would you like to book?:', bg=background_color, fg=font_color)
        self.bunks_auckland_label.grid(row=7, column=0)

        # Bunks in Palmerston North
        self.bunks_palmerston_north_label = Label(self.booking_frame, font= ("Arial", "10", 'italic'), text='How many bunks would you like to book?:', bg=background_color, fg=font_color)
        self.bunks_palmerston_north_label.grid(row=7, column=1)

        # Book bunks entry (row 8)

        # Entry in Auckland
        self.bunks_auckland_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', bg=secondary_color)
        self.bunks_auckland_entry.grid(row=8, column=0, pady=10, padx=10)

        # Entry in Palmerston North
        self.bunks_palmerston_north_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', bg=secondary_color)
        self.bunks_palmerston_north_entry.grid(row=8, column=1, pady=10, padx=10)

        # Bunks in Palmerston North

        # Bunks in Auckland





# Main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Massey Overnighter Service")
    something = Booking()
    root.mainloop()

