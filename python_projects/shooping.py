# Create the item_list
item_list = ["Laptop", "Headset", "Second Monitor", "Mousepad", "USB drive", "External Drive"]

# Assign the spending limit value to a variable called limit
limit = 50000

# Create a dictionary that contains each item and its price
price_sheet = {
    "Laptop": 1500,
    "Headset": 100,
    "Second Monitor": 200,
    "Mousepad": 50,
    "USB drive": 70,  # "USB Driver" yerine doğru isim
    "External Drive": 250  # "Extrenal drive" yerine doğru isim
}

# Initialize the cart list
cart = []

# Define the "add_to_cart" function
def add_to_cart(item, quantity):  # "quantitiy" yerine "quantity"
    if item in item_list:
        cart.append((item, quantity))
        item_list.remove(item)
    else:
        print(f"{item} isimli ürün bulunamadı veya zaten sepette!")

# Define the "create_invoice" function
def create_invoice():
    total_amount_inc_tax = 0
    print("\n---- Fatura ----")
    for item, quantity in cart:
        if item in price_sheet:
            price = price_sheet[item]
            tax = 0.18 * price
            total = (tax + price) * quantity
            total_amount_inc_tax += total
            print(f"Item: {item}\t Price: {price}\t Quantity: {quantity}\t Tax: {tax}\t Total: {total}")
        else:
            print(f"Hata: {item} için fiyat bulunamadı!")

    print("\nAfter the taxes are applied, the total amount is:", total_amount_inc_tax)
    return total_amount_inc_tax

# Define the "checkout" function
def checkout():
    global limit
    total_amount = create_invoice()
    
    if total_amount > limit:
        print("The amount you have to pay is above the spending limit. You have to drop some items.")
    else:
        limit -= total_amount
        print(f"The total amount (incl. taxes) you've paid is {total_amount}. You have {limit} dollars left.")

# Call the "add_to_cart" function for each item

# Add first item to cart
add_to_cart("Laptop", 1)

# Add second item to cart
add_to_cart("Headset", 8)

# Add third item to cart
add_to_cart("Second Monitor", 1)

# Add fourth item to cart
add_to_cart("Mousepad", 1)

# Add fifth item to cart
add_to_cart("USB drive", 2)

# Add last item to cart
add_to_cart("External Drive", 4)

# Call the create "checkout" function to pay for all your items
checkout()
