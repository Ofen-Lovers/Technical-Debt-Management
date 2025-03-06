def compute_deductions(salary):
    sss = 1200
    philhealth = (salary * 0.05) / 2
    pagibig = 100
    tax = 1875 # Assuming fixed value for simplicity

    deductions = sss + philhealth + pagibig + tax 
    net_salary = salary - deductions

def main():
    salary = float(input("Enter your monthly salary: "))    ### Add Error Handling.
    compute_deductions(salary)

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

if __name__ == "__main__":
    main()