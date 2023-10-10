# Johnson, Hugo - Massey Overnighter Service (V2)
# Booking service for buses between Auckland and Palmerston North
# 27.8.2023

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
        self.name_label.grid(row=2, column=0, pady=10, padx=10, sticky = 'e')

        # Name entry box
        self.name_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', bg=secondary_color)
        self.name_entry.grid(row=2, column=1)

        # Phone number entry (row 3)

        # Phone number Label
        self.phone_label = Label(self.booking_frame, font='Arial 14 bold', text='Phone number:', fg=font_color, bg=background_color)
        self.phone_label.grid(row=3, column=0, pady=10, padx=10, sticky = 'e')

        # Phone number entry box
        self.phone_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', text="Phone number:", bg=secondary_color)
        self.phone_entry.grid(row=3, column=1, pady=10, padx=10)

        # City headings (row 4)

        # To Auckland heading
        self.to_auckland = Label(self.booking_frame, text="To Auckland", font= ("Arial", "14", 'bold'), 
        bg=background_color, wrap=290, padx=10, pady=10, fg=font_color)
        self.to_auckland.grid(row=4, column=0)

        # To Palmerston North heading
        self.to_palmerston_north = Label(self.booking_frame,text="To Palmerston North",
        font= ("Arial", "14", 'bold'), bg=background_color,wrap=290, padx=10, pady=10, fg=font_color)
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

        # Reciept button (row 9)
        self.preview_button = Button(self.booking_frame, width=150, font='Arial 14 bold',text='Preview', bg='green', fg=font_color, command=self.create_booking)
        self.preview_button.grid(row=9, columnspan=2, pady=10, padx=10)

        self.preview_button.config(state=NORMAL)
    
    def create_booking(self):
        
        error = 'pale red'
        preview_booking = {}

        # Retrieve amount entered into entry field and store
        preview_booking['name'] = self.name_entry.get()

        # Retrieve amount entered into entry field and store
        preview_booking['phone'] = self.phone_entry.get()

        # Retrieve amount entered into entry field and store
        preview_booking['seats_akl'] = self.seats_auckland_entry.get()

        # Retrieve amount entered into entry field and store
        preview_booking['seats_pn'] = self.seats_palmerston_north_entry.get()

        # Retrieve amount entered into entry field and store
        preview_booking['bunks_akl'] = self.bunks_auckland_entry.get()

        # Retrieve amount entered into entry field and store
        preview_booking['bunks_pn'] = self.bunks_palmerston_north_entry.get()

        print(preview_booking)
        Preview(self, preview_booking)

class Preview:
    def __init__(self, partner, preview_booking):

        # Formatting variables
        background_color = "light blue"
        secondary_color ="gold"
        font_color = "black"

        # Disable preview button
        partner.preview_button.config(state=DISABLED)

        # Sets up child window 
        self.preview_box = Toplevel()

        # Destroys window when closing
        self.preview_box.protocol('WM_DELETE_WINDOW', partial(self.close_preview, partner))

        # Main window frame
        self.preview_frame = Frame(self.preview_box, bg=background_color, pady=10)
        self.preview_frame.grid()

        # Preview heading (row 0)
        self.preview_heading = Label(self.preview_frame, text="Preview Booking",
        font= ("Arial", "19", "bold"), bg=background_color, padx=10, pady=10)
        self.preview_heading.grid(row=0)

        # Preview instructions
        self.preview_instructions = Label(self.preview_frame, text='Here is a preview of your booking:', font='arial 10 italic', justify=LEFT, bg=background_color, padx=10, pady=10)
        self.preview_instructions.grid(row=1)

        # Preview name
        self.name_preview = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Name: {preview_booking['name']}", bg=background_color)
        self.name_preview.grid(row=2, column=0, pady=10, padx=10)

        # Preview phone
        self.phone_preview = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Phone: {preview_booking['phone']}", bg=background_color)
        self.phone_preview.grid(row=3, column=0, pady=10, padx=10)

        # No. of seats to Auckland preview
        self.seats_akl_preview = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Seats to Auckland: {preview_booking['seats_akl']}", bg=background_color)
        self.seats_akl_preview.grid(row=4, column=0, pady=10, padx=10)

        # No. of seats to Palmerston North preview
        self.seats_pn_preview = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Seats to Palmerston North: {preview_booking['seats_pn']}", bg=background_color)
        self.seats_pn_preview.grid(row=5, column=0, pady=10, padx=10)

        # No. of bunks in Auckland preview
        self.seats_pn_preview = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Bunks in Auckland: {preview_booking['seats_pn']}", bg=background_color)
        self.seats_pn_preview.grid(row=6, column=0, pady=10, padx=10)

        # No. of bunks in Palmerston North preview
        self.seats_pn_preview = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Bunks in Palmerston North: {preview_booking['seats_pn']}", bg=background_color)
        self.seats_pn_preview.grid(row=7, column=0, pady=10, padx=10)

        # Confirm booking button 
        self.confirm_button = Button(self.preview_frame, width=150, font='Arial 14 bold',text='Confirm', bg='green', fg=font_color)
        self.confirm_button.grid(row=8, column=0, pady=10, padx=10)

    
    def close_preview(self, partner):
        # Put history button back to normal
        partner.preview_button.config(state=NORMAL)
        self.preview_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Massey Overnighter Service")
    something = Booking()
    root.mainloop()

