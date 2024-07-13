#Date: 22/08/24
#Author: Arnav Kumar
#Purpose: To create a program that can keep track of the items hired and can refund them.

#Imports tkinter
from tkinter import*
import random

#Creates a function for the reciept number
def generate_reciept():
    #Creates a global variable for reciept_number
    global reciept_number
    #Random number generator
    reciept_number = random.randint(1000, 9999)

#Creates a quit function which can be used for the quit button
def quit():
    main_window.destroy()

#Creates a submit function which can be used for the quit button
def submit():
    #Creates a global variable for current row
    global current_row
    customer_name = entry_customer_name.get()
    item_name = entry_item_name.get()
    number_of_items = entry_number_of_items.get()

    #Runs the random number generator
    generate_reciept()
    
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
        Label(main_window, font=("Times New Roman", 14), text = reciept_number, bg = "light blue", fg = "#084772", width = 10).grid(column = 0, row = current_row)
        Label(main_window, font=("Times New Roman", 14), text = customer_name, bg = "light blue", fg = "#084772", width = 10).grid(column = 1, row = current_row)
        Label(main_window, font=("Times New Roman", 14), text = item_name, bg = "light blue", fg = "#084772", width = 10).grid(column = 2, row = current_row)
        Label(main_window, font=("Times New Roman", 14), text = number_of_items, bg = "light blue", fg = "#084772", width = 10).grid(column = 3, row = current_row)
        Label(main_window, font=("Times New Roman", 14), text = current_row - 4, bg = "light blue", fg = "#084772", width = 10).grid(column = 4, row = current_row)
        #Increases the variable current row by 1
        current_row += 1
    
#Creates a function for the labels
def labels():
    #Labels for the text for the inputs
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Customer Full Name:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 0, sticky = E)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Item Name:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 1, sticky = E)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Number Of Items:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 0, row = 2, sticky = E)

    #Labels for the other headers
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Row:", bg = "light blue", fg = "#084772", width = 20, anchor = "e").grid(column = 2, row = 2, sticky = E)

    #Blank row for aesthetics
    Label(main_window, bg = "light blue").grid(column = 0, row = 3)

    #Labels for the headers for the printed details
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Receipt Number:", bg = "light blue", fg = "#084772", width = 20).grid(column = 0, row = 4)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Customer Full Name:", bg = "light blue", fg = "#084772", width = 20).grid(column = 1, row = 4)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Item Name:", bg = "light blue", fg = "#084772", width = 20).grid(column = 2, row = 4)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Number Of Items:", bg = "light blue", fg = "#084772", width = 20).grid(column = 3, row = 4)
    Label(main_window, font = ("Times New Roman", 14, "bold"), text = "Row:", bg = "light blue", fg = "#084772", width = 20).grid(column = 4, row = 4)

#Creates a function for the buttons
def buttons():
    #Buttons for quit, sumbit, and delete row
    Button(main_window, font = ("Times New Roman", 14, "bold"), text = "Quit", command = quit, fg = "#084772", width = 10).grid(column = 4, row = 0)
    Button(main_window, font=("Times New Roman", 14, "bold"), text = "Submit", command = submit, fg = "#084772", width = 10).grid(column = 4, row = 1)
    Button(main_window, font=("Times New Roman", 14, "bold"), text = "Delete Row", fg = "#084772", width = 10).grid(column = 4, row = 2)

#Creates a fucntion for the entries
def entries():
    #Creates these global variables
    global entry_customer_name, entry_item_name, entry_number_of_items

    #Creates the input box for customer name
    entry_customer_name = Entry(main_window, width = 15)
    entry_customer_name.grid(column = 1, row = 0)

    #Creates the input box for item name
    entry_item_name = Entry(main_window, width = 15)
    entry_item_name.grid(column = 1, row = 1)

    #Creates the input box for the number of items
    entry_number_of_items = Entry(main_window, width = 15)
    entry_number_of_items.grid(column = 1, row = 2)

    #Creates the input box for delete row
    entry_delete_row = Entry(main_window, width = 15)
    entry_delete_row.grid(column = 3, row = 2)

#Creates the main function
def main():
    main_window.title("Party Hire Store")
    main_window.configure(bg = "light blue")
    global current_row
    current_row = 5
    labels()
    buttons()
    entries()

#Other necessary lines of code for the program to run
main_window = Tk()
main()
main_window.mainloop()
    
