def compute_deductions(salary):
    sss = 1200
    philhealth = (salary * 0.05) / 2
    pagibig = 100
    tax = 1875 # Assuming fixed value for simplicity

    # SSS Exemption for minimum wage earners (salary below 8250)
    if salary < 8250:
        sss = 0
    if salary < 25000:
        tax = 0
    # Deductions and net salary computations
    deductions = sss + philhealth + pagibig + tax
    net_salary = salary - deductions

    return sss, philhealth, pagibig, tax, deductions, net_salary 

def main():
    try:
        salary = float(input("Enter your monthly salary: ")) # User input for salary
        if salary < 0:
            print("Salary cannot be negative. Please enter a valid salary.")
            return
        print("Gross Salary:", salary)
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Function call to compute deductions and net salary
    sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(salary)

    print("\n-----Deductables-----")
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("\nNet Salary:", net_salary)


if __name__ == "__main__":
    main()