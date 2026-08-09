import mysql.connector
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()


class MySQLDB:

    # Connect to MySQL
    def __init__(self):

        self.connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )

        self.create_table()

        print("MySQL database connected successfully!")

    # Create expenses table
    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            category VARCHAR(100) NOT NULL,
            amount DECIMAL(10,2) NOT NULL
        )
        """

        cursor = self.connection.cursor()

        cursor.execute(query)

        self.connection.commit()

        cursor.close()

    # Add expense
    def add_expense(self, name, category, amount):

        query = """
        INSERT INTO expenses (name, category, amount)
        VALUES (%s, %s, %s)
        """

        cursor = self.connection.cursor()

        # Parameterized query
        cursor.execute(query, (name, category, amount))

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

    # Search expenses by category
    def search_expenses(self, category):

        query = """
        SELECT id, name, category, amount
        FROM expenses
        WHERE LOWER(category) = LOWER(%s)
        """

        cursor = self.connection.cursor()

        cursor.execute(query, (category,))

        rows = cursor.fetchall()

        cursor.close()

        return rows

    # Update expense
    def update_expense(self, expense_id, name, category, amount):

        query = """
        UPDATE expenses
        SET name = %s,
            category = %s,
            amount = %s
        WHERE id = %s
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

    # Delete expense
    def delete_expense(self, expense_id):

        query = """
        DELETE FROM expenses
        WHERE id = %s
        """

        cursor = self.connection.cursor()

        cursor.execute(query, (expense_id,))

        self.connection.commit()

        affected_rows = cursor.rowcount

        cursor.close()

        return affected_rows

    # Calculate total expense
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

    # Find highest expense
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

    # Close database connection
    def close(self):

        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed.")

db = MySQLDB()

result = db.update_expense(
    1,
    "Burger",
    "Food",
    500
)

if result > 0:
    print("Expense updated successfully!")
else:
    print("Expense not found.")

rows = db.view_expenses()

for row in rows:
    print(row)

db.close()