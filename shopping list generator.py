import tkinter as tk
from tkinter import messagebox

class GroceryListGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Shopping List Generator")

        self.products = {
            "Apples": 80.0,  # Price in Indian Rupees
            "Bananas": 40.0,
            "Milk": 60.0,
            "Bread": 40.0,
            "Eggs": 70.0,
            "Cheese": 180.0,
            "Chicken": 250.0,
            "Potatoes": 40.0,
        }

        self.selected_items = {}
        self.total_price = 0.0

        self.create_gui()

    def create_gui(self):
        product_label = tk.Label(self.root, text="Select a product:")
        product_label.pack()

        product_var = tk.StringVar()
        product_var.set(list(self.products.keys())[0])  # Set the default product
        product_dropdown = tk.OptionMenu(self.root, product_var, *self.products.keys())
        product_dropdown.pack()

        quantity_label = tk.Label(self.root, text="Enter quantity:")
        quantity_label.pack()

        quantity_entry = tk.Entry(self.root)
        quantity_entry.pack()

        add_button = tk.Button(self.root, text="Add to List", command=lambda: self.add_to_list(product_var, quantity_entry))
        add_button.pack()

        shopping_list_label = tk.Label(self.root, text="Shopping List:")
        shopping_list_label.pack()

        self.shopping_list = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        self.shopping_list.pack()

        remove_button = tk.Button(self.root, text="Remove Item", command=self.remove_item)
        remove_button.pack()

        calculate_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        calculate_button.pack()

        self.total_label = tk.Label(self.root, text="Total Price: ₹0.00")
        self.total_label.pack()

    def add_to_list(self, product_var, quantity_entry):
        product = product_var.get()
        quantity = quantity_entry.get()
        
        if not quantity.isdigit():
            messagebox.showerror("Error", "Please enter a valid quantity.")
            return
        
        quantity = int(quantity)
        if product in self.selected_items:
            self.selected_items[product] += quantity
        else:
            self.selected_items[product] = quantity
        
        self.shopping_list.delete(0, tk.END)
        for item, qty in self.selected_items.items():
            self.shopping_list.insert(tk.END, f"{item} x{qty}")
        
        quantity_entry.delete(0, tk.END)
    
    def remove_item(self):
        selected_indices = self.shopping_list.curselection()
        for index in selected_indices:
            item = self.shopping_list.get(index)
            product, _ = item.split(" x")
            product = product.strip()
            del self.selected_items[product]
        self.shopping_list.delete(0, tk.END)
        for item, qty in self.selected_items.items():
            self.shopping_list.insert(tk.END, f"{item} x{qty}")
    
    def calculate_total(self):
        self.total_price = sum(self.products[product] * quantity for product, quantity in self.selected_items.items())
        self.total_label.config(text=f"Total Price: ₹{self.total_price:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryListGenerator(root)
    root.mainloop()
