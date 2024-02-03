import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.window = tk.Tk()
        self.window.title("Contact Manager")

        # Labels and Entry widgets for contact details
        self.name_label = tk.Label(self.window, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(self.window, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.window)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(self.window, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.window)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(self.window, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.window)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for actions
        self.add_button = tk.Button(self.window, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(self.window, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.search_button = tk.Button(self.window, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(self.window, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(self.window, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.window.mainloop()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
        else:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            results = [contact for contact in self.contacts if
                       search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']]
            if results:
                result_str = "\n".join([f"{result['Name']}: {result['Phone']}" for result in results])
                messagebox.showinfo("Search Results", result_str)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showwarning("Error", "Please enter a search term.")

    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter name or phone number:")
        if search_term:
            results = [contact for contact in self.contacts if
                       search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']]
            if results:
                selected_contact = results[0]
                new_name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=selected_contact['Name'])
                new_phone = simpledialog.askstring("Update Phone", "Enter new phone number:",
                                                   initialvalue=selected_contact['Phone'])
                new_email = simpledialog.askstring("Update Email", "Enter new email:",
                                                   initialvalue=selected_contact['Email'])
                new_address = simpledialog.askstring("Update Address", "Enter new address:",
                                                     initialvalue=selected_contact['Address'])

                if new_name:
                    selected_contact['Name'] = new_name
                if new_phone:
                    selected_contact['Phone'] = new_phone
                selected_contact['Email'] = new_email
                selected_contact['Address'] = new_address

                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showwarning("Error", "Please enter a search term.")

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete Contact", "Enter name or phone number:")
        if search_term:
            results = [contact for contact in self.contacts if
                       search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']]
            if results:
                confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete this contact?")
                if confirmed:
                    self.contacts.remove(results[0])
                    messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showwarning("Error", "Please enter a search term.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    ContactManager()
