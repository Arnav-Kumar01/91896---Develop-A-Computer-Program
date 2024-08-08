# Date: 22/08/24 (Deadline).
# Author: Arnav Kumar.
# Purpose: To create a program which can print a list of purchase and allows the user to remove items from that list.

# Imports tkinter and all the other things needed for this program.
from tkinter import*
from tkinter.ttk import Combobox
import random
import re

# Shows the quit screen.
def quit_window():
    quit_screen.deiconify()

# Quits all the windows if the user has confirmed it.
def quit():
    main_window.destroy()
    error_message_window.destroy()
    quit_screen.destroy()
    delete_row_window.destroy()

# Hides the quit screen if the user doesn't confirm the quit.
def cancel_quit():
    quit_screen.withdraw()

# Hides the error message screen if the user presses ok.
def ok_button():
    # Hides the error message screen.
    error_message_window.withdraw()

# Hides the delete row screen if the user presses ok.
def delete_row_ok():
    # Hides the delete row screen.
    delete_row_window.withdraw()

# Creates a function which holds all the labels for the main window.
def labels():
    # Labels for the text for the inputs.
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Customer Full Name:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 0, sticky = E, pady = 5)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Item Name:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 1, sticky = E, pady = 5)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Number Of Items:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 2, sticky = E, pady = 5)

    # Label for the delete row entry.
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Row:", bg = "light blue", fg = "#084772", width = 20).grid(column = 3, row = 0, pady = 5)

    # Blank row for aesthetics with a horizontal line.
    Label(main_window, bg = "light blue", fg = "#084772", text = "_–"*75).grid(column = 0, row = 3, columnspan = 4)

    # Labels for the headers for the printed details.
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Receipt Number:", bg = "light blue", fg = "#084772", width = 20).grid(column = 0, row = 4)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Customer Full Name:", bg = "light blue", fg = "#084772", width = 20).grid(column = 1, row = 4)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Item Name:", bg = "light blue", fg = "#084772", width = 20).grid(column = 2, row = 4)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Number Of Items:", bg = "light blue", fg = "#084772", width = 20).grid(column = 3, row = 4)

    # Asks the user if they are sure they want to quit the program, this label is on the quit screen.
    Label(quit_screen, font = ("Times New Roman", 14), text = "Are you sure you want to quit?", bg = "light blue", fg = "#084772").grid(column = 0, row = 0, columnspan = 2, padx = 10, pady = 5)

    # Error message if the user types a wrong input into delete row.
    Label(delete_row_window, font = ("Times New Roman", 14), text = "Please enter a valid row number that exists.", bg = "pink", fg = "red").grid(column = 0, row = 0, padx = 10, pady = 5)

# Creates a function for the buttons.
def buttons():
    # Buttons for quit, sumbit, delete row, and clear items.
    Button(main_window, font = ("Times New Roman", 14, "bold"), text = "Quit", command = quit_window, bg = "#084772", fg = "light blue", width = 10).grid(column = 2, row = 0, pady = 5)
    Button(main_window, font = ("Times New Roman", 14, "bold"), text = "Clear Items", command = clear_items, bg = "#084772", fg = "light blue", width = 10).grid(column = 2, row = 1, pady = 5)
    Button(main_window, font = ("Times New Roman", 14, "bold"), text = "Submit", command = submit, bg = "#084772", fg = "light blue", width = 10).grid(column = 2, row = 2, pady = 5)
    Button(main_window, font = ("Times New Roman", 14, "bold"), text = "Delete Row", command = delete_row, bg = "#084772", fg = "light blue", width = 10).grid(column = 3, row = 2, pady = 5)
    
    # Buttons for yes and no for the quit screen.
    Button(quit_screen, font = ("Times New Roman", 14, "bold"), text = "Yes", command = quit, bg = "#084772", fg = "light blue", width = 10).grid(column = 0, row = 1, padx = 10, pady = 5)
    Button(quit_screen, font = ("Times New Roman", 14, "bold"), text = "No", command = cancel_quit, bg = "#084772", fg = "light blue", width = 10).grid(column = 1, row = 1, padx = 10, pady = 5)

    # Ok button for delete row.
    Button(delete_row_window, font = ("Times New Roman", 14, "bold"), text = "Ok", command = delete_row_ok, bg = "red", fg = "pink", width = 10).grid(column = 0, row = 1, pady = 5)

# Creates a function for the entries.
def entries():
    # Creates global variables for each entry to be used in another function.
    global entry_customer_name, entry_item_name, entry_number_of_items, entry_delete_row

    # Creates the input box for customer name.
    entry_customer_name = Entry(main_window, font = ("Times New Roman", 14), width = 16)
    entry_customer_name.grid(column = 1, row = 0, pady = 5)

    # Creates a combobox to have a multichoice list for item name.
    entry_item_name = Combobox(main_window, font = ("Times New Roman", 14), values = ["", "Balloons", "Candles", "Paper Plates", "Paper Cups", "Napkins", "Streamers", "Confetti", "Party Hats", "Glitter"], width = 14)
    entry_item_name.grid(column = 1, row = 1, pady = 5)
    entry_item_name.current(0)

    # Creates the input box for the number of items.
    entry_number_of_items = Entry(main_window, font = ("Times New Roman", 14), width = 16)
    entry_number_of_items.grid(column = 1, row = 2, pady = 5)

    # Creates the input box for delete row.
    entry_delete_row = Entry(main_window, font = ("Times New Roman", 14), width = 13)
    entry_delete_row.grid(column = 3, row = 1, pady = 5)

# Creates a function to clear the items.
def clear_items():
    # Resets all the entries including the combobox.
    entry_customer_name.delete(0, END)
    entry_item_name.current(0)
    entry_number_of_items.delete(0, END)

# Creates a function for the receipt number.
def generate_receipt():
    # Creates a global variable to be used in another function.
    global receipt_number

    # Random number generator but it ensures that the same receipt number can't be printed twice.
    while True:
        receipt_number = random.randint(1000000000, 9999999999)
        if receipt_number not in generated_receipt_numbers:
            generated_receipt_numbers.add(receipt_number)
            break

# Creates a submit function which can be used for the submit button.
def submit():
    # Creates global variables to be used in other functions.
    global current_row, rows

    # Assigns a variable to each of the entries so we know what each entry is.
    customer_name = entry_customer_name.get()
    item_name = entry_item_name.get()
    number_of_items = entry_number_of_items.get()

    # Runs the random number generator.
    generate_receipt()

    # Clear previous error messages.
    for error_messages in error_message_window.winfo_children():
        error_messages.destroy()

    # Sets the error to false so that if an error occurs it changes to true.
    error_occurred = False

    
    # Changes the colour of the border to red and prints an error message on a seperate window if an error has occurred.
    if customer_name == "" or not re.match("^[A-Za-z- ]+$", customer_name):
        error_message_window.deiconify()
        Label(error_message_window, font = ("Times New Roman", 14), text = "Please enter your full name with letters only, you cannot leave it blank.", bg = "pink", fg = "red").grid(column = 0, row = 0, padx = 10, pady = 5)
        Button(error_message_window, font = ("Times New Roman", 14, "bold"), text = "Ok", command = ok_button, bg = "red", fg = "pink", width = 10).grid(column = 0, row = 3, pady = 5)
        error_occurred = True


    # Sets the allowed items for item name to these.
    allowed_items = ["Balloons", "Candles", "Paper Plates", "Paper Cups", "Napkins", "Streamers", "Confetti", "Party Hats", "Glitter"]
 
    # Changes the colour of the combobox to red and prints an error message on a seperate window if an error has occurred.
    if item_name not in allowed_items:
        error_message_window.deiconify()
        Label(error_message_window, font = ("Times New Roman", 14), text = "Please choose an item from the list, you cannot leave it blank.", bg = "pink", fg = "red").grid(column = 0, row = 1, padx = 10, pady = 5)
        Button(error_message_window, font = ("Times New Roman", 14, "bold"), text = "Ok", command = ok_button, bg = "red", fg = "pink", width = 10).grid(column = 0, row = 3, pady = 5)
        error_occurred = True


    # Changes the colour of the border to red and prints an error message on a seperate window if an error has occurred.
    try:
        if number_of_items == "" or int(number_of_items) <= 0 or int(number_of_items) > 500:
            error_message_window.deiconify()
            Label(error_message_window, font = ("Times New Roman", 14), text = "Please enter the number of items, must be a number between 1 and 500.", bg = "pink", fg = "red").grid(column = 0, row = 2, padx = 10, pady = 5)
            Button(error_message_window, font = ("Times New Roman", 14, "bold"), text = "Ok", command = ok_button, bg = "red", fg = "pink", width = 10).grid(column = 0, row = 3, pady = 5)
            error_occurred = True


    # Prints an error message on a seperate window if theres a value error such as a word being written.
    except ValueError:
        error_message_window.deiconify()
        Label(error_message_window, font = ("Times New Roman", 14), text = "Please enter the number of items, must be a number between 1 and 500.", bg = "pink", fg = "red").grid(column = 0, row = 2, padx = 10, pady = 5)
        Button(error_message_window, font = ("Times New Roman", 14, "bold"), text = "Ok", command = ok_button, bg = "red", fg = "pink", width = 10).grid(column = 0, row = 3, pady = 5)
        error_occurred = True

 
    # Prints the details if no error has occurred.
    if error_occurred == False:
        # Hide the error messages window.
        error_message_window.withdraw()

        # Resets all the entries including the combobox.
        entry_customer_name.delete(0, END)
        entry_item_name.current(0)
        entry_number_of_items.delete(0, END)
        
        # Prints the receipt number.
        receipt_label = Label(main_window, font = ("Times New Roman", 14), text = receipt_number, bg = "light blue", fg = "#084772", width = 20)
        receipt_label.grid(column = 0, row = current_row)

        # Prints the customer's name.
        customer_label = Label(main_window, font = ("Times New Roman", 14), text = customer_name, bg = "light blue", fg = "#084772", width = 20)
        customer_label.grid(column = 1, row = current_row)

        # Prints the item name.
        item_label = Label(main_window, font = ("Times New Roman", 14), text = item_name, bg = "light blue", fg = "#084772", width = 20)
        item_label.grid(column = 2, row = current_row)

        # Prints number of items.
        number_label = Label(main_window, font = ("Times New Roman", 14), text = number_of_items, bg = "light blue", fg = "#084772", width = 20)
        number_label.grid(column = 3, row = current_row)

        # Appends all the labels to the rows variable so that it can be deleted by the user.
        rows.append((receipt_label, customer_label, item_label, number_label))

        # Increases the variable current row by 1.
        current_row += 1

# Creates a function to delete a specific row.
def delete_row():
    try:
        # Checks that the entry is a number.
        row_to_delete = int(entry_delete_row.get()) - 1

        # Ensures that the row exists.
        if 0 <= row_to_delete < len(rows):
            for widget in rows[row_to_delete]:
                widget.destroy()

            # Deletes the row.
            del rows[row_to_delete]

            # Hides the delete row window.
            delete_row_window.withdraw()
            
        # Prints an error message if it is not a number that exists.
        else:
            # Makes the delete row window appear.
            raise ValueError
            
    # Prints an error message if there is an error.
    except ValueError:
        delete_row_window.deiconify()

    # Clears the entry box.
    entry_delete_row.delete(0, END)

# Creates the main function.
def main():
    # Gives the main window a title and colour.
    main_window.title("Party Hire Store")
    main_window.configure(bg = "light blue")
    
    # Gives the error messages window a title, colour and hides it to begin with.
    error_message_window.title("Error Messages")
    error_message_window.configure(bg = "pink")
    error_message_window.withdraw()

    # Gives the quit window a title, colour and hides it to begin with.
    quit_screen.title("Quit Window")
    quit_screen.configure(bg = "light blue")
    quit_screen.withdraw()

    # Gives the delete row window a title, colour and hides it to begin with.
    delete_row_window.title("Delete Row")
    delete_row_window.configure(bg = "pink")
    delete_row_window.withdraw()
    
    # Creates global variables to be used in other functions.
    global current_row, rows, generated_receipt_numbers
    
    # Sets current row to be 6.
    current_row = 6

    # Set up to store receipt numbers so it is not repeated.
    generated_receipt_numbers = set()
    
    # Creates a list of the rows variable.
    rows = []
    
    # Starts all these functions.
    labels()
    buttons()
    entries()

# Other necessary lines of code for the program to run.
main_window = Tk()
error_message_window = Tk()
quit_screen = Tk()
delete_row_window = Tk()

# Starts the main function.
main()

# Keeps the main window open.
main_window.mainloop()
