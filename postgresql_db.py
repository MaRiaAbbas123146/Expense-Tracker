import psycopg #driver
from dotenv import load_dotenv
import os

load_dotenv()


class PostgreSQLDB:

    # Connect to PostgreSQL
    def __init__(self):

        self.connection = psycopg.connect(
            host=os.getenv("POSTGRES_HOST"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            dbname=os.getenv("POSTGRES_DATABASE"),
            port=os.getenv("POSTGRES_PORT")
        )

        self.create_table()

        print("PostgreSQL database connected successfully!")

    # Create expenses table
    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
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
        SET name = %s, category = %s, amount = %s
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

    # Total expenses
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

    # Highest expense
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

        self.connection.close()
        print("PostgreSQL connection closed.")


db = PostgreSQLDB()

db.close()