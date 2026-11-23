expenses = []


def add_expense(amount, category, description):
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
    }
    expenses.append(expense)
    return expense


def list_expenses():
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['amount']} | {expense['category']} | {expense['description']}")


if __name__ == "__main__":
    list_expenses()
    add_expense(12.5, "food", "lunch")
    add_expense(40, "transport", "bus pass")
    list_expenses()