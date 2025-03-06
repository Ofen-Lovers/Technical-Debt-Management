def compute_deductions(salary):
### Have a Separate function for the values or separate it from the computation function.
### Let the User decide if they want a specific value of the sss, philhealth, pagibig, and tax. make the current values the default values.
    sss = 1200
    philhealth = (salary * 0.05) / 2
    pagibig = 100
    tax = 1875 # Assuming fixed value for simplicity

    deductions = sss + philhealth + pagibig + tax 
    net_salary = salary - deductions

### Have a separate function for output.
    print("Gross Salary:", salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

### Add a main Function
salary = float(input("Enter your monthly salary: "))    ### Add Error Handling.
compute_deductions(salary)