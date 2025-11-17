class Employee:
    """Represents an employee with a name and salary."""

    def __init__(self, name, salary):
        """
        Initialize the Employee object.

        Parameters:
        name (str): Employee's name.
        salary (float): Employee's salary.
        """
        self._name = name
        self._salary = salary

    def increase_salary(self, percentage):
        """
        Increase employee salary by a given percentage.

        Parameters:
        percentage (float): Percentage to increase salary.
        """
        self._salary += self._salary * (percentage / 100)

    def display_info(self):
        """Display the employee's name and formatted salary."""
        print(f"Employee Name: {self._name} | Salary: {self._salary:.2f}")


# ---- User Input ----
name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))
percentage = float(input("Enter increment percentage: "))

# Create employee object
emp = Employee(name, salary)

# Apply increment
emp.increase_salary(percentage)

# Display result
emp.display_info()
