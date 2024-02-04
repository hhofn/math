# Define a class to represent an employee
class Employee:
    def __init__(self, id, name, hours_worked, hourly_rate):
        self.id = id
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    
    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate

# Initialize sets for employees in different restaurants
restaurant_a_employees = {
    Employee('001', 'Alice', 40, 15),
    Employee('002', 'Bob', 35, 12),
    Employee('003', 'Charlie', 45, 18),
}

restaurant_b_employees = {
    Employee('004', 'Dave', 38, 14),
    Employee('002', 'Bob', 30, 12),  # Note: Bob works in both restaurants
    Employee('005', 'Eve', 42, 17),
}

# Use set operations to find unique employees across both restaurants
all_employees = restaurant_a_employees.union(restaurant_b_employees)

# Calculate total payroll
total_payroll = sum(employee.calculate_pay() for employee in all_employees)

# Print the total number of unique employees and total payroll
print(f'Total unique employees: {len(all_employees)}')
print(f'Total payroll: ${total_payroll}')

# Additionally, demonstrating other set operations
# Intersection: Employees working in both restaurants
common_employees = restaurant_a_employees.intersection(restaurant_b_employees)
print(f'Employees working in both restaurants: {len(common_employees)}')

# Difference: Employees in Restaurant A not in Restaurant B
exclusive_a_employees = restaurant_a_employees.difference(restaurant_b_employees)
print(f'Exclusive employees in Restaurant A: {len(exclusive_a_employees)}')

# Symmetric Difference: Employees in one restaurant but not both
unique_employees = restaurant_a_employees.symmetric_difference(restaurant_b_employees)
print(f'Employees working in just one restaurant: {len(unique_employees)}')
