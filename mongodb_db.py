from pymongo import MongoClient
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

load_dotenv()


class MongoDB:

    # Connect to MongoDB
    def __init__(self):

        self.client = MongoClient(
            os.getenv("MONGODB_URI")
        )

        self.database = self.client[
            os.getenv("MONGODB_DATABASE")
        ]

        self.collection = self.database["expenses"]

        # Test connection
        self.client.admin.command("ping")

        print("MongoDB database connected successfully!")

    # Add expense
    def add_expense(self, name, category, amount):

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        self.collection.insert_one(expense)

        print("Expense added successfully!")

    # View all expenses
    def view_expenses(self):

        documents = self.collection.find().sort("_id", 1)

        rows = []

        for document in documents:

            rows.append(
                (
                    str(document["_id"]),
                    document["name"],
                    document["category"],
                    document["amount"]
                )
            )

        return rows

    # Search expenses by category
    def search_expenses(self, category):

        documents = self.collection.find(
            {
                "category": {
                    "$regex": f"^{category}$",
                    "$options": "i"
                }
            }
        )

        rows = []

        for document in documents:

            rows.append(
                (
                    str(document["_id"]),
                    document["name"],
                    document["category"],
                    document["amount"]
                )
            )

        return rows

    # Update expense
    def update_expense(
        self,
        expense_id,
        name,
        category,
        amount
    ):

        result = self.collection.update_one(
            {
                "_id": ObjectId(expense_id)
            },
            {
                "$set": {
                    "name": name,
                    "category": category,
                    "amount": amount
                }
            }
        )

        return result.modified_count

    # Delete expense
    def delete_expense(self, expense_id):

        result = self.collection.delete_one(
            {
                "_id": ObjectId(expense_id)
            }
        )

        return result.deleted_count

    # Total expenses
    def total_expense(self):

        result = self.collection.aggregate(
            [
                {
                    "$group": {
                        "_id": None,
                        "total": {
                            "$sum": "$amount"
                        }
                    }
                }
            ]
        )

        result = list(result)

        if result:
            return result[0]["total"]

        return 0

    # Highest expense
    def highest_expense(self):

        document = self.collection.find_one(
            sort=[
                ("amount", -1)
            ]
        )

        if document:

            return (
                str(document["_id"]),
                document["name"],
                document["category"],
                document["amount"]
            )

        return None

    # Close MongoDB connection
    def close(self):

        self.client.close()

        print("MongoDB connection closed!")


# Test MongoDB
if __name__ == "__main__":

    db = MongoDB()

    db.close()