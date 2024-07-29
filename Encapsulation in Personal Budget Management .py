# File: budget_category.py (module name follows lowercase with underscores convention)

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self._category_name = category_name
        self._allocated_budget = allocated_budget

    def get_category_name(self):
        """Get the category name."""
        return self._category_name

    def get_allocated_budget(self):
        """Get the allocated budget."""
        return self._allocated_budget

    def set_category_name(self, new_name):
        """Set the category name (with validation)."""
        if new_name:
            self._category_name = new_name
        else:
            print("Category name cannot be empty.")

    def set_allocated_budget(self, new_budget):
        """Set the allocated budget (with validation)."""
        if new_budget >= 0:
            self._allocated_budget = new_budget
        else:
            print("Budget must be a positive number.")

    def add_expense(self, amount):
        """Add an expense to the category (with validation)."""
        if amount >= 0:
            if amount <= self._allocated_budget:
                self._allocated_budget -= amount
            else:
                print("Expense exceeds allocated budget.")
        else:
            print("Expense amount must be non-negative.")

    def display_category_summary(self):
        """Display the budget category details."""
        print(f"Category: {self._category_name}")
        print(f"Allocated Budget: ${self._allocated_budget:.2f}")

# Example usage
if __name__ == "__main__":
    food_category = BudgetCategory(category_name="Food", allocated_budget=500)
    food_category.add_expense(100)
    food_category.display_category_summary()
