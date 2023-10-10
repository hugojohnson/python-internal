# Johnson, Hugo - Massey Overnighter Service (V3)
# Booking service for buses between Auckland and Palmerston North
# 30.8.2023

# Importing
from tkinter import *
from functools import partial # to prevent unwanted windows
from tkmacosx import Button
import random

background_color = "blue"
secondary_color ="light goldenrod"
font_color = "white"

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


    # Input validation
    
    def create_booking(self):
        
        error = '#ffafaf'
        preview_booking = {}
        has_error = 'no'

        # Retrieve amount entered into entry field and store
        preview_booking['name'] = self.name_entry.get().capitalize()

        if any(char.isdigit() for char in preview_booking['name']):
            self.name_entry.config(bg=error)
            self.name_label.config(text='Name cannot contain digits', fg='red')
            has_error = 'yes'   
        elif 0 == len(str(preview_booking['name'])):
            self.name_entry.config(bg=error)
            self.name_label.config(text='Enter a name', fg='red')
            has_error = 'yes'
        elif 300 < len(str(preview_booking['name'])):
            self.name_entry.config(bg=error)
            self.name_label.config(text='Name is too long', fg='red')
            has_error = 'yes'
        else:
            self.name_label.config(text='Name', fg=font_color)
            self.name_entry.config(bg=secondary_color)

        # Retrieve amount entered into entry field and store
        preview_booking['phone'] = self.phone_entry.get()
        try:
            if int(preview_booking['phone'])<=0:
                self.phone_entry.config(bg=error)
                self.phone_label.config(text='Enter positve number', fg='red')
                has_error = 'yes'
            elif len(str(int(preview_booking['phone']))) <= 8:
                self.phone_entry.config(bg=error)
                self.phone_label.config(text='Number too short', fg='red')
                has_error = 'yes'
            elif len(str(int(preview_booking['phone']))) >= 15:
                self.phone_entry.config(bg=error)
                self.phone_label.config(text='Number too long', fg='red')
                has_error = 'yes'
            else:
                self.phone_label.config(text='Phone number', fg=font_color)
                self.phone_entry.config(bg=secondary_color)
        except ValueError:
            self.phone_entry.config(bg=error)
            self.phone_label.config(text='Enter digits', fg='red')
            has_error = 'yes'
            
        # Retrieve amount entered into entry field and store
        try:
            preview_booking['seats_akl'] = int(self.seats_auckland_entry.get())

            if preview_booking['seats_akl'] > 15:
                self.seats_auckland_label.config(text="Maximum 15 seats per booking", fg='red')
                self.seats_auckland_entry.config(bg=error)
                has_error='yes'
            else: 
                preview_booking['seats_akl'] = f"{preview_booking['seats_akl']} seat(s) (${(preview_booking['seats_akl'])*25})"
                self.seats_auckland_label.config(text="How many seats would you like to book?", fg=font_color)
                self.seats_auckland_entry.config(bg=secondary_color)
        except ValueError or KeyError:
            has_error = 'yes'
            self.seats_auckland_label.config(text="Enter a number", fg="red")
            self.seats_auckland_entry.config(bg=error)

        # Retrieve amount entered into entry field and store
        try:
            preview_booking['seats_pn'] = int(self.seats_palmerston_north_entry.get())

            if preview_booking['seats_pn'] > 15:
                self.seats_palmerston_north_label.config(text="Maximum 15 seats per booking", fg='red')
                self.seats_palmerston_north_entry.config(bg=error)
                has_error='yes'
            else: 
                preview_booking['seats_pn'] = f"{preview_booking['seats_pn']} seat(s) (${(preview_booking['seats_pn'])*25})"
                self.seats_palmerston_north_label.config(text="How many seats would you like to book?", fg=font_color)
                self.seats_palmerston_north_entry.config(bg=secondary_color)
        except ValueError or KeyError:
            has_error = 'yes'
            self.seats_palmerston_north_label.config(text="Enter a number", fg="red")
            self.seats_palmerston_north_entry.config(bg=error)

        # Retrieve amount entered into entry field and store
        try:
            preview_booking['bunks_akl'] = int(self.bunks_auckland_entry.get())

            if preview_booking['bunks_akl'] > 15:
                self.bunks_auckland_label.config(text="Maximum 15 bunks per booking", fg='red')
                self.bunks_auckland_entry.config(bg=error)
                has_error='yes'
            else: 
                preview_booking['bunks_akl'] = f"{preview_booking['bunks_akl']} bunks(s) (${(preview_booking['bunks_akl'])*50})"
                self.bunks_auckland_label.config(text="How many bunks would you like to book?", fg=font_color)
                self.bunks_auckland_entry.config(bg=secondary_color)
        except ValueError or KeyError:
            has_error = 'yes'
            self.bunks_auckland_label.config(text="Enter a number", fg="red")
            self.bunks_auckland_entry.config(bg=error)

        # Retrieve amount entered into entry field and store
        try:
            preview_booking['bunks_pn'] = int(self.bunks_palmerston_north_entry.get())

            if preview_booking['bunks_pn'] > 15:
                self.bunks_palmerston_north_label.config(text="Maximum 15 bunks per booking", fg='red')
                self.bunks_palmerston_north_entry.config(bg=error)
                has_error='yes'
            else: 
                preview_booking['bunks_pn'] = f"{preview_booking['bunks_pn']} bunks(s) (${(preview_booking['bunks_pn'])*50})"
                self.bunks_palmerston_north_label.config(text="How many bunks would you like to book?", fg=font_color)
                self.bunks_palmerston_north_entry.config(bg=secondary_color)
        except ValueError or KeyError:
            has_error = 'yes'
            self.bunks_palmerston_north_label.config(text="Enter a number", fg="red")
            self.bunks_palmerston_north_entry.config(bg=error)

        if has_error == 'no':
            Preview(self, preview_booking)

# Preview 
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
        self.preview_heading.grid(row=0, columnspan=2)

        # Preview instructions (row 1)
        self.preview_instructions = Label(self.preview_frame, text='Here is a preview of your booking:', font='arial 10 italic', justify=LEFT, bg=background_color, padx=10, pady=10)
        self.preview_instructions.grid(row=1, columnspan=2)

        # Preview name (row 2)
        self.name_preview_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text="Name: ", bg=background_color)
        self.name_preview_label.grid(row=2, column=0, pady=10, padx=10, sticky = 'e')

        self.name_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=preview_booking['name'], bg=background_color)
        self.name_preview_value.grid(row=2, column=1, pady=10, padx=10)

        # Preview phone (row 3)
        self.phone_preview_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Phone: ", bg=background_color)
        self.phone_preview_label.grid(row=3, column=0, pady=10, padx=10, sticky = 'e')

        self.phone_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=preview_booking['phone'], bg=background_color)
        self.phone_preview_value.grid(row=3, column=1, pady=10, padx=10)

        # No. of seats to Auckland preview (row 4)
        self.seats_akl_preview_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Seats to Auckland: ", bg=background_color)
        self.seats_akl_preview_label.grid(row=4, column=0, pady=10, padx=10, sticky = 'e')

        self.seats_akl_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=preview_booking['seats_akl'], bg=background_color)
        self.seats_akl_preview_value.grid(row=4, column=1, pady=10, padx=10)

        # No. of seats to Palmerston North preview (row 5)
        self.seats_pn_preview_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Seats to Palmerston North: ", bg=background_color)
        self.seats_pn_preview_label.grid(row=5, column=0, pady=10, padx=10, sticky = 'e')

        self.seats_pn_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=preview_booking['seats_pn'], bg=background_color)
        self.seats_pn_preview_value.grid(row=5, column=1, pady=10, padx=10)

        # No. of bunks in Auckland preview (row 6)
        self.bunks_akl_preview_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Bunks in Auckland: ", bg=background_color)
        self.bunks_akl_preview_label.grid(row=6, column=0, pady=10, padx=10, sticky = 'e')

        self.bunks_akl_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=preview_booking['bunks_akl'], bg=background_color)
        self.bunks_akl_preview_value.grid(row=6, column=1, pady=10, padx=10)

        # No. of bunks in Palmerston North preview (row 7)
        self.bunks_pn_preview_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Bunks in Palmerston North: ", bg=background_color)
        self.bunks_pn_preview_label.grid(row=7, column=0, pady=10, padx=10, sticky = 'e')

        self.bunks_pn_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=preview_booking['bunks_pn'], bg=background_color)
        self.bunks_pn_preview_value.grid(row=7, column=1, pady=10, padx=10)

        # Confirm booking button (row 8)
        self.confirm_button = Button(self.preview_frame, width=150, font='Arial 14 bold',text='Confirm', bg='green', fg=font_color)
        self.confirm_button.grid(row=8, column = 0, pady=30, padx=5)

        # Cancel button
        self.cancel_button = Button(self.preview_frame, width=150, font='Arial 14 bold',text='Cancel', bg='red', fg=font_color, command=partial(self.close_preview, partner))
        self.cancel_button.grid(row=8, column = 1, pady=30, padx=5)
    
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