"""
A program that stores the following information about book:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete record
Close the program
"""


from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_tuple
        index = list_1.curselection()[0]
        selected_tuple = list_1.get(index)
        entry_1.delete(0, END)
        entry_1.insert(END, selected_tuple[1])
        entry_2.delete(0, END)
        entry_2.insert(END, selected_tuple[2])
        entry_3.delete(0, END)
        entry_3.insert(END, selected_tuple[3])
        entry_4.delete(0, END)
        entry_4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list_1.delete(0, END)
    for row in backend.view_all():
        list_1.insert(END, row)


def search_command():
    list_1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list_1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_1.delete(0, END)
    list_1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window = Tk()

window.wm_title("Book Store")

label_1 = Label(window, text="Title")
label_1.grid(row=0, column=0)

label_2 = Label(window, text="Author")
label_2.grid(row=0, column=2)

label_3 = Label(window, text="Year")
label_3.grid(row=1, column=0)

label_4 = Label(window, text="ISBN")
label_4.grid(row=1, column=2)

title_text = StringVar()
entry_1 = Entry(window, textvariable=title_text)
entry_1.grid(row=0, column=1)

author_text = StringVar()
entry_2 = Entry(window, textvariable=author_text)
entry_2.grid(row=0, column=3)

year_text = StringVar()
entry_3 = Entry(window, textvariable=year_text)
entry_3.grid(row=1, column=1)

isbn_text = StringVar()
entry_4 = Entry(window, textvariable=isbn_text)
entry_4.grid(row=1, column=3)

list_1 = Listbox(window, height=6, width=35)
list_1.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

# attaching scrollbar to the listbox
list_1.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_1.yview)

list_1.bind('<<ListboxSelect>>', get_selected_row)

view_button = Button(window, text="View all", width=12, command=view_command)
view_button.grid(row=2, column=3)

search_button = Button(window, text="Search entry", width=12, command=search_command)
search_button.grid(row=3, column=3)

add_entry = Button(window, text="Add entry", width=12, command=add_command)
add_entry.grid(row=4, column=3)

update_button = Button(window, text="Update selected", width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete selected", width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)

window.mainloop()
