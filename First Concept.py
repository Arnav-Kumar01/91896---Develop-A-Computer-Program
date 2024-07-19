#Date: 22/08/24
#Author: Arnav Kumar
#Purpose: To create a program that can keep track of the items hired and can refund them.

#Imports tkinter
from tkinter import*
from tkinter.ttk import Combobox
import random

#Creates a function for the receipt number
def generate_receipt():
    #Creates a global variable for receipt_number
    global receipt_number
    #Random number generator
    receipt_number = random.randint(100000, 999999)

#Creates a quit function which can be used for the quit button
def quit():
    main_window.destroy()

#Creates a submit function which can be used for the quit button
def submit():
    #Creates a global variable for current row
    global current_row, rows
    customer_name = entry_customer_name.get()
    item_name = entry_item_name.get()
    number_of_items = entry_number_of_items.get()

    #Runs the random number generator
    generate_receipt()
    
    #Changes the colour of the text is the user has put an invalid input
    if customer_name == "":
        Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Customer Full Name:", bg = "light blue", fg = "red", width = 20, anchor = "e").grid(column = 0, row = 0, sticky = E)
    #Keeps the text black is there is a correct input
    else:
        Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Customer Full Name:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 0, sticky = E)

    #Changes the colour of the text is the user has put an invalid input
    if item_name == "":
        Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Item Name:", bg = "light blue", fg = "red", width = 20, anchor = "e").grid(column = 0, row = 1, sticky = E)
    #Keeps the text black is there is a correct input
    else:
        Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Item Name:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 1, sticky = E)

    #Changes the colour of the text is the user has put an invalid input
    if number_of_items == "" or 0 > int(number_of_items) or 500 <= int(number_of_items):
        Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Number Of Items:", bg = "light blue", fg = "red", width = 20, anchor = "e").grid(column = 0, row = 2, sticky = E)
    #Keeps the text the same colour is there is a correct input
    else:
        Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Number Of Items:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 2, sticky = E)

    #Prints the details if the input is valid
    if customer_name and item_name and 0 < int(number_of_items) <= 500:

        #Prints the receipt number
        receipt_label = Label(main_window, font = ("Times New Roman", 14), text = receipt_number, bg = "light blue", fg = "#084772", width = 10)
        receipt_label.grid(column = 0, row = current_row)

        #Prints the customer's name
        customer_label = Label(main_window, font = ("Times New Roman", 14), text = customer_name, bg = "light blue", fg = "#084772", width = 10)
        customer_label.grid(column = 1, row = current_row)

        #Prints the item name
        item_label = Label(main_window, font = ("Times New Roman", 14), text = item_name, bg = "light blue", fg = "#084772", width = 10)
        item_label.grid(column = 2, row = current_row)

        #Prints number of items
        number_label = Label(main_window, font = ("Times New Roman", 14), text = number_of_items, bg = "light blue", fg = "#084772", width = 10)
        number_label.grid(column = 3, row = current_row)

        #Appends all the labels to the rows variable so that it can be deleted by the user
        rows.append((receipt_label, customer_label, item_label, number_label))

        #Increases the variable current row by 1
        current_row += 1

#Creates a function to clear the items
def clear_items():
    entry_customer_name.delete(0, END)
    entry_item_name.current(0)
    entry_number_of_items.delete(0, END)

#Creates a function to delete a specific row
def delete_row():
    #Finds the row to delete by adding 4 to the user's input as thats how many non changable rows there are
    row_to_delete = int(entry_delete_row.get()) + 4
    #Ensures that the row to delete actually exists
    if row_to_delete < current_row:
        for widget in rows[row_to_delete - 5]:
            widget.destroy()
        #Deletes the row
        del rows[row_to_delete - 5]

#Creates a function for the labels
def labels():
    #Labels for the text for the inputs
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Customer Full Name:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 0, sticky = E)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Item Name:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 1, sticky = E)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Number Of Items:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 2, sticky = E)

    #Blank row for aesthetics
    Label(main_window, bg = "light blue", text = "_"*75).grid(column = 0, row = 3, columnspan = 4)

    #Labels for the headers for the printed details
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Receipt Number:", bg = "light blue", fg = "#084772", width = 20).grid(column = 0, row = 4)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Customer Full Name:", bg = "light blue", fg = "#084772", width = 20).grid(column = 1, row = 4)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Item Name:", bg = "light blue", fg = "#084772", width = 20).grid(column = 2, row = 4)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Number Of Items:", bg = "light blue", fg = "#084772", width = 20).grid(column = 3, row = 4)

#Creates a function for the buttons
def buttons():
    #Buttons for quit, sumbit, and delete row
    Button(main_window, font = ("Times New Roman", 14, "bold"), text = "Quit", command = quit, fg = "#084772", width = 10).grid(column = 3, row = 0)
    Button(main_window, font = ("Times New Roman", 14, "bold"), text = "Submit", command = submit, fg = "#084772", width = 10).grid(column = 2, row = 1)
    Button(main_window, font = ("Times New Roman", 14, "bold"), text = "Delete Row", command = delete_row, fg = "#084772", width = 10).grid(column = 2, row = 2)
    Button(main_window, font = ("Times New Roman", 14, "bold"), text = "Clear Items", command = clear_items, fg = "#084772", width = 10).grid(column = 2, row = 0)

#Creates a fucntion for the entries
def entries():
    #Creates these global variables
    global entry_customer_name, entry_item_name, entry_number_of_items, entry_delete_row

    #Creates the input box for customer name
    entry_customer_name = Entry(main_window, width = 15)
    entry_customer_name.grid(column = 1, row = 0)

    #Creates a combobox to have a multichoice list for item name
    entry_item_name = Combobox(main_window, values=["", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5"], width = 13)
    entry_item_name.grid(column = 1, row = 1)
    entry_item_name.current(0)

    #Creates the input box for the number of items
    entry_number_of_items = Entry(main_window, width = 15)
    entry_number_of_items.grid(column = 1, row = 2)

    #Creates the input box for delete row
    entry_delete_row = Entry(main_window, width = 10)
    entry_delete_row.grid(column = 3, row = 2)

#Creates the main function
def main():
    main_window.title("Party Hire Store")
    main_window.configure(bg = "light blue")
    global current_row, rows
    current_row = 5
    rows = []
    labels()
    buttons()
    entries()

#Other necessary lines of code for the program to run
main_window = Tk()
main()
main_window.mainloop()
