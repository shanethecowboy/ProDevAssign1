# Shane Hendrickson
#CBIS 4210
#Assignment 2
#9/1/2024

# Function to calculate sales tax
def calculate_sales_tax(amount, tax_rate):
    """Calculate sales tax based on the amount and tax rate."""
    return amount * (tax_rate / 100)

# Function to calculate total amount after tax
def calculate_total_amount(amount, tax):
    """Calculate the total amount after adding the tax."""
    return amount + tax

# Main function
def main():
    amount = 250         # Example amount
    tax_rate = 7.5       # Example tax rate in percentage

    tax = calculate_sales_tax(amount, tax_rate)
    total_amount = calculate_total_amount(amount, tax)

    print(f"Total Amount after Tax: ${total_amount:.2f}")

# Call the main function
if __name__ == "__main__":
    main()
