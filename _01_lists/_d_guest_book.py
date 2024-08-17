"""
* Create an app like the one shown in the pictures in this package,
  'guest_book_add.png' and 'guest_book_print'
"""
from tkinter import messagebox, simpledialog, Tk
import tkinter as tk

# TODO 1) Complete the function by:
#         a. Asking for the name of the guest to add
#         b. Add the guest to list_of_guests
#         c. Return the list_of_guests
def add_guest(list_of_guests):
    guest_name = simpledialog.askstring(title='llllllkjsdlsadf', prompt="what is ur name????????????")
    list_of_guests.append(guest_name)
    return list_of_guests

# TODO 2) Complete the function by:
#         a. Asking for the name of the guest to remove
#         b. Remove the guest from list_of_guests. Do not change the list if
#            the guest isn't in the list.
#         c. Return the list_of_guests
def remove_guest(list_of_guests):
    remove_guest_name = simpledialog.askstring(title='lkjlhguyftytgyt', prompt='please remove a guest')
    list_of_guests.remove(remove_guest_name)
    return list_of_guests

# TODO 3) Complete the function by:
#         a. Display the names of the guests in the following format:
#            Guest 1. Peppa Pig
#            Guest 2. Amogus
#            Guest 3. Shrek
#         b. If there are no guests, print "There are no guests"
def print_guests(list_of_guests):
    for i in range(len(list_of_guests)):
        print("guest " + str(i+1) + ". " + list_of_guests[i])


# ======================= DO NOT EDIT THE CODE BELOW =========================

class GuestBook(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)

        self.guests = list()

        self.geometry('260x50')

        self.grid()

        button_add = tk.Button(self, text='Add Guest', command=self.add_guest)
        button_add.grid(padx=5, pady=10, row=0, column=0)

        button_remove = tk.Button(self, text='Remove Guest', command=self.remove_guest)
        button_remove.grid(padx=5, pady=10, row=0, column=1)

        button_print_guests = tk.Button(self, text='View Guests', command=self.print_guests)
        button_print_guests.grid(padx=5, pady=10, row=0, column=2)

    def add_guest(self):
        self.guests = add_guest(self.guests)

    def remove_guest(self):
        self.guests = remove_guest(self.guests)

    def print_guests(self):
        print_guests(self.guests)


if __name__ == '__main__':
    gb = GuestBook(None)
    gb.title('Guest Book')
    gb.mainloop()
