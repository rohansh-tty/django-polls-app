
Assignment 1: Bank Account Management System

Develop a Python program to create a banking application. The program should have the following classes:

1. `BankAccount` class: This class should represent a basic bank account. It should have attributes such as account number, account holder's name, and balance. It should also have methods to deposit and withdraw money.

2. `SavingsAccount` class: This class should inherit from the `BankAccount` class and represent a savings account. It should have an additional attribute to store the interest rate. It should also have a method to calculate and add the interest to the account balance annually.

3. `CheckingAccount` class: This class should inherit from the `BankAccount` class and represent a checking account. It should have an additional attribute to store the overdraft limit. It should also have a method to deduct an overdraft fee if the balance goes below zero.

4. `Bank` class: This class should have a list of bank accounts (instances of `BankAccount`, `SavingsAccount`, and `CheckingAccount` classes). It should have methods to add a new account, remove an existing account, and display information about all accounts.


5.  Add a `Transaction` class to represent various types of transactions (deposit, withdrawal, transfer, etc.). Each transaction should have attributes like transaction ID, date, amount, and type.

6. Modify the `BankAccount` class to have a list of transactions and methods to add new transactions and calculate the current balance based on the transactions.

7. In the `SavingsAccount` class, implement a method to calculate and add compound interest to the account balance based on the interest rate and a given period (e.g., monthly, quarterly, or annually).

8. Add a `CreditAccount` class that inherits from `BankAccount`. It should have additional attributes like credit limit and interest rate for outstanding balances. Implement methods to handle credit transactions and calculate interest on outstanding balances.

9. Modify the `Bank` class to have methods to generate reports for various accounts, such as transaction history, interest accrued, and outstanding balances.

```
# Create a bank
bank = Bank()

# Create different types of accounts
savings_account = SavingsAccount(123, "John Doe", 5000, 0.05)
checking_account = CheckingAccount(456, "Jane Smith", 10000, 500)
credit_account = CreditAccount(789, "Michael Johnson", 0, 5000, 0.18)

# Add accounts to the bank
bank.add_account(savings_account)
bank.add_account(checking_account)
bank.add_account(credit_account)

# Perform transactions
savings_account.deposit(1000)
checking_account.withdraw(2500)
credit_account.withdraw(3000)  # Adds to outstanding balance

# Calculate interest and update balances
savings_account.calculate_interest(period="yearly")
credit_account.calculate_interest()

# Generate reports
print(bank.get_account_report(123))
print(bank.get_transaction_history(456))
print(bank.get_outstanding_balances())
```
 
Assignment 2: Employee Management System

Develop a Python program to manage employee records in a company. The program should have the following classes:

1. `Employee` class: This class should be an abstract base class with attributes such as employee ID, name, age, and base salary. It should have an abstract method to calculate the monthly salary.

2. `SalariedEmployee` class: This class should inherit from the `Employee` class and represent a salaried employee. It should have an attribute to store the annual salary, and a method to calculate the monthly salary based on the annual salary.

3. `HourlyEmployee` class: This class should inherit from the `Employee` class and represent an hourly employee. It should have attributes to store the hourly rate and the number of hours worked per month, and a method to calculate the monthly salary based on the hourly rate and hours worked.

4. `CommissionEmployee` class: This class should inherit from the `SalariedEmployee` class and represent a commission-based employee. It should have an additional attribute to store the commission rate, and a method to calculate the monthly salary by adding the commission to the base salary.

5. `Company` class: This class should have a list of employees (instances of `SalariedEmployee`, `HourlyEmployee`, and `CommissionEmployee` classes). It should have methods to add a new employee, remove an existing employee, and display information about all employees, including their monthly salaries.

6. Introduce a `Payroll` class to handle payroll calculations for all employees. It should have methods to calculate the total payroll cost for the company, generate pay slips, and handle tax deductions.

7. Add a `PerformanceReview` class to manage employee performance reviews. It should have attributes like review date, rating, and comments. Implement methods to calculate performance-based bonuses or salary increments.

8. Create a `Manager` class that inherits from `SalariedEmployee`. It should have additional attributes like department and a list of subordinates (instances of other employee classes).

9. Implement a `Contractor` class that represents a contracted employee. It should have attributes like contract duration, hourly rate, and methods to calculate the payment based on the contract terms.

10. Modify the `Company` class to have methods to generate reports for payroll, performance reviews, and organizational hierarchies (managers and their subordinates).

```
# Create a company
company = Company()

# Hire employees
manager = Manager(1001, "John Doe", 45, 8000)
salaried_employee = SalariedEmployee(1002, "Jane Smith", 32, 6000)
hourly_employee = HourlyEmployee(1003, "Michael Johnson", 28, 25, 160)
contractor = Contractor(1004, "Emily Davis", 35, 50, 80)

# Add employees to the company
company.add_employee(manager)
company.add_employee(salaried_employee)
company.add_employee(hourly_employee)
company.add_employee(contractor)

# Conduct performance reviews
salaried_employee.performance_review = PerformanceReview("2023-05-01", 4.5, "Excellent work!")
hourly_employee.performance_review = PerformanceReview("2023-06-15", 3.0, "Needs improvement.")

# Calculate payroll
payroll = Payroll()
payroll.calculate_payroll(company.employees)

# Generate reports
print(company.get_employee_report(1001))
print(payroll.generate_payslips())
print(company.get_organizational_hierarchy())
```


Assignment 3: Vehicle Rental System

Create a Python program to manage a vehicle rental system. The program should have the following classes:

1. `Vehicle` class: This class should be an abstract base class with attributes such as vehicle ID, make, model, and year of manufacture. It should have an abstract method to calculate the daily rental rate.

2. `Car` class: This class should inherit from the `Vehicle` class and represent a car. It should have an additional attribute to store the number of seats, and a method to calculate the daily rental rate based on the vehicle's make and model.

3. `Truck` class: This class should inherit from the `Vehicle` class and represent a truck. It should have additional attributes to store the payload capacity and number of axles, and a method to calculate the daily rental rate based on the payload capacity.

4. `Motorcycle` class: This class should inherit from the `Vehicle` class and represent a motorcycle. It should have an additional attribute to store the engine displacement, and a method to calculate the daily rental rate based on the engine displacement.

5. `RentalCompany` class: This class should have a list of vehicles (instances of `Car`, `Truck`, and `Motorcycle` classes). It should have methods to add a new vehicle, remove an existing vehicle, rent a vehicle to a customer (based on availability and customer's requirements), and display information about all available vehicles and their rental rates.

6. Introduce a `Reservation` class to handle vehicle rental reservations. It should have attributes like reservation ID, customer details, pickup and return dates, and the reserved vehicle.

7. Create a `FleetManagement` class to manage the company's fleet of vehicles. It should have methods to track vehicle availability, schedule maintenance, and handle vehicle acquisitions and disposals.

8. Implement a `Rental` class that represents an active rental agreement. It should have attributes like rental ID, reservation details, and methods to calculate the rental cost based on the rental duration and any additional charges (e.g., late fees, damage fees).

9. Add a `Customer` class to store customer information like name, contact details, and rental history.

10. Modify the `RentalCompany` class to have methods to handle reservations, process rentals, manage customer accounts, and generate reports on rental activities and fleet utilization.
critically about class design, inheritance, and object interactions in more complex scenarios.

```
# Create a rental company
rental_company = RentalCompany()

# Add vehicles to the fleet
car1 = Car(1, "Toyota", "Camry", 2020, 5)
truck1 = Truck(2, "Ford", "F-150", 2018, 1500, 2)
motorcycle1 = Motorcycle(3, "Honda", "CBR600RR", 2022, 599)

rental_company.add_vehicle(car1)
rental_company.add_vehicle(truck1)
rental_company.add_vehicle(motorcycle1)

# Create customers
customer1 = Customer("John Doe", "john.doe@email.com")
customer2 = Customer("Jane Smith", "jane.smith@email.com")

# Make reservations
reservation1 = Reservation(1, customer1, car1, "2023-07-01", "2023-07-07")
reservation2 = Reservation(2, customer2, truck1, "2023-08-15", "2023-08-20")

# Process rentals
rental1 = Rental(reservation1)
rental2 = Rental(reservation2)

# Manage fleet
fleet_management = FleetManagement(rental_company.vehicles)
fleet_management.schedule_maintenance(car1, "2023-09-01")
fleet_management.acquire_vehicle(Car(4, "Honda", "Civic", 2021, 5))

# Generate reports
print(rental_company.get_available_vehicles())
print(rental_company.get_rental_report(rental1.rental_id))
print(fleet_management.get_maintenance_schedule())
```