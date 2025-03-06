# Technical-Debt-Management
A repository made for the Software Implementations and Management Activity

## Roles
- Javier M. Raut (Project Manager)
- Krystal Heart M. Bacalso (Lead Developer)
- Cyreh M. Bayson (Refactoring Specialist)
- Joseph Jose A. Deysolong (Git Manager)

## Overview
This program calculates the monthly salary deductions for an employee, which include SSS, PhilHealth, Pag-IBIG, and Tax, and computes the net salary after deductions. The program also handles various exemption rules for employees earning below certain thresholds and validates the input to ensure no negative or invalid salary values are entered.


## Changes and Refactors
### Old Code:
The old version directly printed out the deductions and salary without input validation.
It did not handle cases for negative salaries or invalid input.
The deduction computation was simplified and did not include any exemption or validation logic.

### New Code:
Error Handling: The program now raises a ValueError for negative salary values and invalid user input, ensuring proper error management.
Exemption Rules: Added logic to handle SSS exemption for employees earning below 8250 and tax exemption for employees earning below 25000.
Improved Modularity: The computation of deductions is separated into the compute_deductions function, which returns the values, rather than directly printing them within the function. The main function handles the user input and displays the results.
Input Validation: Ensures that only valid numerical input is processed. If the user enters a non-numeric value or a negative salary, an appropriate error message is displayed.

## Unit Tests:
The program includes unit tests to validate that it raises errors for invalid salary inputs (such as negative salaries). Tests can be run using Python's built-in unittest framework.