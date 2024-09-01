# Shane Hendrickson
#CBIS 4210
#Assignment 2
#9/1/2024

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    """Calculate the simple interest based on principal, rate, and time."""
    return (principal * rate * time) / 100

# Main function
def main():
    principal = 1000  # Example principal amount
    rate = 5          # Example interest rate in percentage
    time = 2          # Example time in years

    interest = calculate_simple_interest(principal, rate, time)
    print(f"Simple Interest: ${interest:.2f}")

# Call the main function
if __name__ == "__main__":
    main()
