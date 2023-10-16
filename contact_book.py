import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []
        self.current_contact = None

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        # Labels
        tk.Label(root, text="Name:").grid(row=0, column=0)
        tk.Label(root, text="Phone:").grid(row=1, column=0)
        tk.Label(root, text="Email:").grid(row=2, column=0)
        tk.Label(root, text="Address:").grid(row=3, column=0)

        # Entry fields
        tk.Entry(root, textvariable=self.name_var).grid(row=0, column=1)
        tk.Entry(root, textvariable=self.phone_var).grid(row=1, column=1)
        tk.Entry(root, textvariable=self.email_var).grid(row=2, column=1)
        tk.Entry(root, textvariable=self.address_var).grid(row=3, column=1)

        # Listbox for displaying contacts
        self.contact_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.contact_listbox.grid(row=0, column=2, rowspan=9)

        # Bind a selection event to the listbox
        self.contact_listbox.bind('<<ListboxSelect>>', self.on_contact_select)

        # Buttons
        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2)
        tk.Button(root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2)
        tk.Button(root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2)
        tk.Button(root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if name and phone:
            contact_info = (name, phone, email, address)
            self.contacts.append(contact_info)
            self.update_contact_listbox()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showwarning("Warning", "Name and phone are required.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "Contact List:\n"
            for contact in self.contacts:
                contact_list += f"Name: {contact[0]}, Phone: {contact[1]}\n"
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts found.")

    def search_contact(self):
        search_term = self.name_var.get()
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term in contact[0]]
            if found_contacts:
                contact_list = "Search Results:\n"
                for contact in found_contacts:
                    contact_list += f"Name: {contact[0]}, Phone: {contact[1]}\n"
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showwarning("Warning", "Enter a search term (name or phone).")

    def on_contact_select(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.current_contact = self.contacts[selected_index[0]]
            self.display_current_contact()

    def update_contact(self):
        if not self.current_contact:
            messagebox.showwarning("Warning", "Select a contact to update.")
            return

        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        updated_contact = (name, phone, email, address)

        index = self.contacts.index(self.current_contact)
        self.contacts[index] = updated_contact

        self.update_contact_listbox()
        self.clear_entries()
        messagebox.showinfo("Success", "Contact updated successfully")

    def delete_contact(self):
        if not self.current_contact:
            messagebox.showwarning("Warning", "Select a contact to delete.")
            return

        confirmation = messagebox.askquestion("Confirm Deletion", "Are you sure you want to delete this contact?")
        if confirmation == 'yes':
            self.contacts.remove(self.current_contact)
            self.update_contact_listbox()
            self.clear_entries()
            self.current_contact = None  # Reset the current contact
            messagebox.showinfo("Success", "Contact deleted.")

    def clear_entries(self):
        self.name_var.set('')
        self.phone_var.set('')
        self.email_var.set('')
        self.address_var.set('')

