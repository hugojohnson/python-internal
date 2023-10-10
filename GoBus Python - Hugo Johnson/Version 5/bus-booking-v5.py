# Johnson, Hugo - Massey Overnighter Service (V5)
# Booking service for buses between Auckland and Palmerston North
# 30.9.2023

# Importing
from tkinter import *
from functools import partial # to prevent unwanted windows
from tkmacosx import Button
import random

# Formatting variables
background_color = "blue"
secondary_color ="light goldenrod"
font_color = "white"

booking_history = [] # List for all bookings

# Inital avaliable seats/bunks
seats_akl_free = 20 
seats_pn_free = 20
bunks_akl_free = 15
bunks_pn_free = 15

class Booking:
    def __init__(self, parent):
        # Main window frame
        self.booking_frame = Frame(root, bg=background_color, pady=10)
        self.booking_frame.grid()

        # Booking service heading (row 0)
        self.booking_heading = Label(self.booking_frame, text="Go Student Bus Service",
        font= ("Arial", "19", "bold"), fg='gold', bg=background_color, padx=10, pady=10)
        self.booking_heading.grid(row=0, columnspan=2)

        # User instuctions (row 1)
        self.booking_instructions = Label(self.booking_frame, text="Welcome to Massey Overnighter Bus Service, book tickets below", font= ("Arial", "10", 'italic'), bg=background_color, fg=font_color, padx=10, pady=10)
        self.booking_instructions.grid(row=1, columnspan=2)

        # Name entry (row 2)
        # Name Label
        self.name_label = Label(self.booking_frame, font='Arial 14 bold', fg=font_color, text='Full name:', bg=background_color)
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
        self.to_auckland = Label(self.booking_frame, text="To / In Auckland", font= ("Arial", "14", 'bold'), 
        bg=background_color, wrap=290, padx=10, pady=10, fg=font_color)
        self.to_auckland.grid(row=4, column=0)
        # To Palmerston North heading
        self.to_palmerston_north = Label(self.booking_frame,text="To / In Palmerston North",
        font= ("Arial", "14", 'bold'), bg=background_color,wrap=290, padx=10, pady=10, fg=font_color)
        self.to_palmerston_north.grid(row=4, column=1)

        # Book seats label (row 5)
        # Seats to Auckland
        self.seats_akl_label = Label(self.booking_frame, font= ("Arial", "10", 'italic'), text=f"How many seats would you like to book?\n({seats_akl_free} avaliable):", bg=background_color, fg=font_color, wraplength=200)
        self.seats_akl_label.grid(row=5, column=0)
        # Seats to Palmerston North
        self.seats_pn_label = Label(self.booking_frame, font= ("Arial", "10", 'italic'), text=f"How many seats would you like to book?\n({seats_pn_free} avaliable):", bg=background_color, fg=font_color, wraplength=200)
        self.seats_pn_label.grid(row=5, column=1)

        # Book seats entry (row 6)
        # Entry to Auckland
        self.seats_akl_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', bg=secondary_color)
        self.seats_akl_entry.grid(row=6, column=0, pady=10, padx=10)
        # Entry to Palmerston North
        self.seats_pn_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', bg=secondary_color)
        self.seats_pn_entry.grid(row=6, column=1, pady=10, padx=10)

        # Book bunks label (row 7)
        # Bunks in Auckland
        self.bunks_akl_label = Label(self.booking_frame, font= ("Arial", "10", 'italic'), text=f"How many bunks would you like to book?\n({bunks_akl_free} avaliable):", bg=background_color, fg=font_color, wraplength=200)
        self.bunks_akl_label.grid(row=7, column=0)
        # Bunks in Palmerston North
        self.bunks_pn_label = Label(self.booking_frame, font= ("Arial", "10", 'italic'), text=f'How many bunks would you like to book?({bunks_pn_free} avaliable):', bg=background_color, fg=font_color, wraplength=200)
        self.bunks_pn_label.grid(row=7, column=1)

        # Book bunks entry (row 8)
        # Entry in Auckland
        self.bunks_akl_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', bg=secondary_color)
        self.bunks_akl_entry.grid(row=8, column=0, pady=10, padx=10)
        # Entry in Palmerston North
        self.bunk_pn_entry = Entry(self.booking_frame, width=20, font='Arial 14 bold', bg=secondary_color)
        self.bunk_pn_entry.grid(row=8, column=1, pady=10, padx=10)

        # Reciept button (row 9)
        self.preview_button = Button(self.booking_frame, width=150, font='Arial 14 bold',text='Preview', bg='green', fg=font_color, command=self.create_booking)
        self.preview_button.grid(row=9, columnspan=2, pady=10, padx=10)

        self.preview_button.config(state=NORMAL)

    def create_booking(self): # Input validation
        
        error = '#ffafaf'
        booked = {}
        has_error = 'no'

        # Retrieve name entry field & error check
        booked['name'] = self.name_entry.get()

        # Checks for non-integer character
        if any(char.isdigit() for char in booked['name']): 
            self.name_entry.config(bg=error)
            self.name_label.config(text='Name cannot contain digits', fg='red')
            has_error = 'yes'             
        # Checks for empty box
        elif 0 == len(str(booked['name'])):
            self.name_entry.config(bg=error)
            self.name_label.config(text='Enter a name', fg='red')
            has_error = 'yes'
        # Length limit
        elif 300 < len(str(booked['name'])):
            self.name_entry.config(bg=error)
            self.name_label.config(text='Name is too long', fg='red')
            has_error = 'yes'
        else:
            self.name_label.config(text='Name', fg=font_color)
            self.name_entry.config(bg=secondary_color)

        # Retrieve phone entry field & error check
        booked['phone'] = self.phone_entry.get()
        try:
            # Checks for empty box
            if int(booked['phone'])<=0:
                self.phone_entry.config(bg=error)
                self.phone_label.config(text='Enter positve number', fg='red')
                has_error = 'yes'
                # Checks length
            elif len(str(int(booked['phone']))) <= 5:
                self.phone_entry.config(bg=error)
                self.phone_label.config(text='Number too short', fg='red')
                has_error = 'yes'
            elif len(str(int(booked['phone']))) >= 14:
                self.phone_entry.config(bg=error)
                self.phone_label.config(text='Number too long', fg='red')
                has_error = 'yes'
            else:
                self.phone_label.config(text='Phone number', fg=font_color)
                self.phone_entry.config(bg=secondary_color)
        # Stops non-int values being input
        except ValueError:
            self.phone_entry.config(bg=error)
            self.phone_label.config(text='Phone number can only contain digits', fg='red')
            has_error = 'yes'
            
        # Error checking Auckland seats
        try:
            booked['seats_akl'] = int(self.seats_akl_entry.get())
            if booked['seats_akl'] > seats_akl_free: # Checks avaliablity 
                self.seats_akl_label.config(text=f"Only {seats_akl_free} seats remaining", fg='red')
                self.seats_akl_entry.config(bg=error)
                has_error='yes'
            elif booked['seats_akl'] <= 0: # Checks for empty
                self.seats_akl_label.config(text="Enter positive number", fg='red')
                self.seats_akl_entry.config(bg=error)
                has_error='yes'
            else: 
                self.seats_akl_label.config(text=f"How many seats would you like to book?\n({seats_akl_free} avaliable):", fg=font_color)
                self.seats_akl_entry.config(bg=secondary_color)
        except ValueError or KeyError: # Stops non-integer values
            has_error = 'yes'
            self.seats_akl_label.config(text="Enter a number", fg="red")
            self.seats_akl_entry.config(bg=error)

        # Error checking Palmerston North seats
        try:
            booked['seats_pn'] = int(self.seats_pn_entry.get())
            if booked['seats_pn'] > seats_pn_free: # Checks avaliablity 
                self.seats_pn_label.config(text=f"Only {seats_pn_free} seats remaining", fg='red')
                self.seats_pn_entry.config(bg=error)
                has_error='yes'
            elif booked['seats_pn'] <= 0: # Checks for empty
                self.seats_pn_label.config(text="Enter positive number", fg='red')
                self.seats_pn_entry.config(bg=error)
                has_error='yes'
            else: 
                self.seats_pn_label.config(text=f"How many seats would you like to book?\n({seats_pn_free} avaliable):", fg=font_color)
                self.seats_pn_entry.config(bg=secondary_color)
        except ValueError or KeyError: # Stops non-integer values
            has_error = 'yes'
            self.seats_pn_label.config(text="Enter a number", fg="red")
            self.seats_pn_entry.config(bg=error)

        # Error checking Auckland bunks
        try:
            booked['bunks_akl'] = int(self.bunks_akl_entry.get())
            if booked['bunks_akl'] > bunks_akl_free: # Checks avaliablity 
                self.bunks_akl_label.config(text=f"Only {bunks_akl_free} seats remaining", fg='red')
                self.bunks_akl_entry.config(bg=error)
                has_error='yes'
            elif booked['bunks_akl'] <= 0: # Checks for empty
                self.bunks_akl_label.config(text="Enter positive number", fg='red')
                self.bunks_akl_entry.config(bg=error)
                has_error='yes'
            else: 
                self.bunks_akl_label.config(text=f"How many bunks would you like to book?\n({bunks_akl_free} avaliable):", fg=font_color)
                self.bunks_akl_entry.config(bg=secondary_color)
        except ValueError or KeyError: # Stops non-integer values
            has_error = 'yes'
            self.bunks_akl_label.config(text="Enter a number", fg="red")
            self.bunks_akl_entry.config(bg=error)

        # Error checking Palmerston North bunks
        try:
            booked['bunks_pn'] = int(self.bunk_pn_entry.get())
            if booked['bunks_pn'] > bunks_pn_free: # Checks avaliablity 
                self.bunks_pn_label.config(text=f"Only {bunks_pn_free} avaliable", fg='red')
                self.bunk_pn_entry.config(bg=error)
                has_error='yes'
            elif booked['bunks_pn'] <= 0: # Checks for empty
                self.bunks_pn_label.config(text="Enter positive number", fg='red')
                self.bunk_pn_entry.config(bg=error)
                has_error='yes'
            else: 
                self.bunks_pn_label.config(text=f"How many bunks would you like to book?\n({bunks_pn_free} avaliable):", fg=font_color)
                self.bunk_pn_entry.config(bg=secondary_color)
        except ValueError or KeyError: # Stops non-integer values
            has_error = 'yes'
            self.bunks_pn_label.config(text="Enter a number", fg="red")
            self.bunk_pn_entry.config(bg=error)

        if has_error == 'no': # If no errors, preview displayed
            Preview(self, booked)

# Preview 
class Preview:
    def __init__(self, partner, booked):

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

        self.name_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=booked['name'], bg=background_color)
        self.name_preview_value.grid(row=2, column=1, pady=10, padx=10)

        # Preview phone (row 3)
        self.phone_preview_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Phone: ", bg=background_color)
        self.phone_preview_label.grid(row=3, column=0, pady=10, padx=10, sticky = 'e')

        self.phone_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=booked['phone'], bg=background_color)
        self.phone_preview_value.grid(row=3, column=1, pady=10, padx=10)

        # No. of seats to Auckland preview (row 4)
        self.seats_akl_preview_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Seats to Auckland: ", bg=background_color)
        self.seats_akl_preview_label.grid(row=4, column=0, pady=10, padx=10, sticky = 'e')

        self.seats_akl_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"{booked['seats_akl']} seat(s) (${(booked['seats_akl'])*25})", bg=background_color)
        self.seats_akl_preview_value.grid(row=4, column=1, pady=10, padx=10)

        # No. of seats to Palmerston North preview (row 5)
        self.seats_pn_preview_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Seats to Palmerston North: ", bg=background_color)
        self.seats_pn_preview_label.grid(row=5, column=0, pady=10, padx=10, sticky = 'e')

        self.seats_pn_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"{booked['seats_pn']} seat(s) (${(booked['seats_pn'])*25})", bg=background_color)
        self.seats_pn_preview_value.grid(row=5, column=1, pady=10, padx=10)

        # No. of bunks in Auckland preview (row 6)
        self.bunks_akl_preview_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Bunks in Auckland: ", bg=background_color)
        self.bunks_akl_preview_label.grid(row=6, column=0, pady=10, padx=10, sticky = 'e')

        self.bunks_akl_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"{booked['bunks_akl']} bunks(s) (${(booked['bunks_akl'])*50})", bg=background_color)
        self.bunks_akl_preview_value.grid(row=6, column=1, pady=10, padx=10)

        # No. of bunks in Palmerston North preview (row 7)
        self.bunks_pn_preview_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Bunks in Palmerston North: ", bg=background_color)
        self.bunks_pn_preview_label.grid(row=7, column=0, pady=10, padx=10, sticky = 'e')

        self.bunks_pn_preview_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"{booked['bunks_pn']} seat(s) (${(booked['bunks_pn'])*50})", bg=background_color)
        self.bunks_pn_preview_value.grid(row=7, column=1, pady=10, padx=10)

        # Total price (row 8)
        self.total_label = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, text=f"Total price: ", bg=background_color)
        self.total_label.grid(row=8, column=0, pady=10, padx=10, sticky = 'e')
        # 'total' variable
        total = int(booked['seats_akl']*25)+int(booked['seats_pn']*25)+int(booked['bunks_akl']*50)+int(booked['bunks_pn']*50)
        self.total_value = Label(self.preview_frame, font='Arial 14 bold', fg=font_color, bg=background_color, text=f"${total}")
        self.total_value.grid(row=8, column=1, pady=10, padx=10)

        # GST portion of total cost (row 9)
        gst = round(total-(total/1.15),2)
        self.gst_label = Label(self.preview_frame, font = 'Arial 14 bold', fg=font_color, bg=background_color, text='GST (Included in total):')
        self.gst_label.grid(row=9, column=0, pady=10, padx=10)
        self.gst_value = Label(self.preview_frame, font = 'Arial 14 bold', fg=font_color, bg=background_color, text=f"${gst}")
        self.gst_value.grid(row=9, column=1, pady=10, padx=10)

        # Confirm booking button (row 10)
        self.confirm_button = Button(self.preview_frame, width=150, font='Arial 14 bold',text='Confirm', bg='green', fg=font_color, command=lambda: self.confirm_preview(booked, partner, total, gst))
        self.confirm_button.grid(row=10, column = 0, pady=30, padx=5)

        # Cancel button
        self.cancel_button = Button(self.preview_frame, width=150, font='Arial 14 bold',text='Cancel', bg='red', fg=font_color, command=partial(self.close_preview, partner))
        self.cancel_button.grid(row=10, column = 1, pady=30, padx=5)

    def confirm_preview(self, booked, partner, total, gst):

        self.close_preview(partner) # Closes window

        booking_statement = f"Name: {booked['name']}, Phone number: {booked['phone']}, Seat(s) to Auckland: {booked['seats_akl']}, Seat(s) to Palmerston North: {booked['seats_pn']}, Bunk(s) in Auckland: {booked['bunks_akl']}, Bunk(s) in Palmerston North: {booked['bunks_pn']}, Total price: ${total}, GST:${gst}"
        booking_history.append(booking_statement)
        print(booking_history)

        # Clears entry fields
        partner.name_entry.delete(0,'end')
        partner.phone_entry.delete(0,'end')
        partner.seats_pn_entry.delete(0,'end')
        partner.seats_akl_entry.delete(0,'end')
        partner.bunk_pn_entry.delete(0,'end')
        partner.bunks_akl_entry.delete(0,'end')
        # Allows access outside of local scope
        global seats_akl_free
        global seats_pn_free 
        global bunks_pn_free
        global bunks_akl_free
        # Updates avaliability
        seats_akl_free-=int(booked['seats_akl'])
        seats_pn_free-=int(booked['seats_pn'])
        bunks_akl_free-=int(booked['bunks_akl'])
        bunks_pn_free-=int(booked['bunks_pn'])
        # Updates displayed amount of avaliable seats
        partner.seats_akl_label.config(text=f'How many bunks would you like to book?({seats_akl_free} avaliable):')
        partner.seats_pn_label.config(text=f'How many bunks would you like to book?({seats_pn_free} avaliable):')
        partner.bunks_akl_label.config(text=f'How many bunks would you like to book?({bunks_akl_free} avaliable):')
        partner.bunks_pn_label.config(text=f'How many bunks would you like to book?({bunks_pn_free} avaliable):')

        booked={} # Empties dictionary

    def close_preview(self, partner):
        # Put preview button back to normal
        partner.preview_button.config(state=NORMAL)
        self.preview_box.destroy() # Closes preview window
# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Go Student Bus Service")
    something = Booking(root)
    root.mainloop()