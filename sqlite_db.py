import sqlite3


class SQLiteDB:

    # Connect to the SQLite database
    def __init__(self, db_name="expenses.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    # Create expenses table
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL
        )
        """

        cursor = self.connection.cursor()

        cursor.execute(query)

        self.connection.commit()

        cursor.close()

    # Add an expense
    def add_expense(self, name, category, amount):
        query = """
        INSERT INTO expenses (name, category, amount)
        VALUES (?, ?, ?)
        """

        cursor = self.connection.cursor()

        # Parameterized query
        cursor.execute(query, (name, category, amount))

        # Save the change permanently
        self.connection.commit()

        cursor.close()

        print("Expense added successfully!")

    # View all expenses
    def view_expenses(self):
        query = """
        SELECT id, name, category, amount
        FROM expenses
        ORDER BY id
        """

        cursor = self.connection.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()

        return rows
    def search_expenses(self, category):

      query = """
      SELECT id, name, category, amount
      FROM expenses
      WHERE LOWER(category) = LOWER(?)
      """

      cursor = self.connection.cursor()

      cursor.execute(query, (category,))

      rows = cursor.fetchall()

      cursor.close()

      return rows
    
    def update_expense(self, expense_id, name, category, amount):

      query = """
      UPDATE expenses
      SET name = ?, category = ?, amount = ?
      WHERE id = ?
      """

      cursor = self.connection.cursor()

      cursor.execute(
          query,
          (name, category, amount, expense_id)
      )

      self.connection.commit()

      affected_rows = cursor.rowcount

      cursor.close()

      return affected_rows

    def delete_expense(self, expense_id):

      query = """
      DELETE FROM expenses
      WHERE id = ?
      """

      cursor = self.connection.cursor()

      cursor.execute(query, (expense_id,))

      self.connection.commit()

      affected_rows = cursor.rowcount

      cursor.close()

      return affected_rows
    
    def total_expense(self):

      query = """
      SELECT SUM(amount)
      FROM expenses
      """

      cursor = self.connection.cursor()

      cursor.execute(query)

      result = cursor.fetchone()

      cursor.close()

      return result[0] if result[0] is not None else 0
    
    def highest_expense(self):

      query = """
      SELECT id, name, category, amount
      FROM expenses
      ORDER BY amount DESC
      LIMIT 1
      """

      cursor = self.connection.cursor()

      cursor.execute(query)

      result = cursor.fetchone()

      cursor.close()

      return result
    
db = SQLiteDB()


# Total Expense
total = db.total_expense()

print("Total Expense:", total)


# Highest Expense
highest = db.highest_expense()

if highest:
    print("\nHighest Expense")
    print("ID:", highest[0])
    print("Name:", highest[1])
    print("Category:", highest[2])
    print("Amount:", highest[3])
else:
    print("No expenses found.")