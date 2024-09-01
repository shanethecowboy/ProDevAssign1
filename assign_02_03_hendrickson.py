# Shane Hendrickson
#CBIS 4210
#Assignment 2
#9/1/2024

# Function to calculate gross salary
def calculate_gross_salary(basic_salary, allowances):
    """Calculate gross salary by adding basic salary and allowances."""
    return basic_salary + allowances

# Function to calculate net salary
def calculate_net_salary(gross_salary, deductions):
    """Calculate net salary by subtracting deductions from gross salary."""
    return gross_salary - deductions

# Main function
def main():
    basic_salary = 3000      # Example basic salary
    allowances = 500         # Example allowances
    deductions = 300         # Example deductions

    gross_salary = calculate_gross_salary(basic_salary, allowances)
    net_salary = calculate_net_salary(gross_salary, deductions)

    print(f"Net Salary: ${net_salary:.2f}")

# Call the main function
if __name__ == "__main__":
    main()
