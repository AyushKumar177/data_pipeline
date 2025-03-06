from fastapi import FastAPI, HTTPException
import uvicorn
import json

# Import functions to fetch and transform data
from fetch_data import fetch_data
from transform import transform_data

# Import user and product insights
from insights import (
    user_with_most_transactions, users_with_no_transactions, calculate_user_statistics,
    top_selling_products, expensive_and_cheapest_products, category_wise_revenue, most_rated_products, top_revenue_categories
)

# Import business logic functions
from business_rules import (
    join_transactions_with_products, join_transactions_with_users, 
    calculate_user_spending, most_popular_categories, average_transaction_value
)

# Initializing FastAPI
app = FastAPI()

# Fetching and transforming data
def pipeline():
    """Runs the data pipeline to fetch and transform data."""
    try:
        raw_data = fetch_data()
        transformed_data = transform_data(raw_data)
        return transformed_data
    except Exception as e:
        print(f"Error in pipeline: {e}")
        return {"products": [], "users": [], "transactions": []}  # Return empty lists on failure

# Loading transformed data
try:
    data = pipeline()
    products = data["products"]
    users = data["users"]
    transactions = data["transactions"]

    # Enrich transactions with product and user details
    transactions_with_products = join_transactions_with_products(transactions, products)
    transactions_with_users = join_transactions_with_users(transactions, users)

    # Compute insights
    user_spending = calculate_user_spending(transactions)
    most_popular_category = most_popular_categories(products)
    average_transaction_values = average_transaction_value(products)

    # Save processed data into JSON files
    try:
        with open("json/transactions.json", "w", encoding="utf-8") as file:
            json.dump(transactions, file, indent=4)
        with open("json/users.json", "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4)
        with open("json/products.json", "w", encoding="utf-8") as file:
            json.dump(products, file, indent=4)
        with open("json/transactions_with_products.json", "w", encoding="utf-8") as file:
            json.dump(transactions_with_products, file, indent=4)
        with open("json/transactions_with_users.json", "w", encoding="utf-8") as file:
            json.dump(transactions_with_users, file, indent=4)
    except Exception as e:
        print(f"Error saving JSON files: {e}")

except Exception as e:
    print(f"Error loading data pipeline: {e}")
    products, users, transactions = [], [], []  # Ensure data is an empty list on failure

# API Endpoint: Fetch stored data (products, users, transactions)
@app.get("/data/{entity_type}")
def get_data(entity_type: str):
    """Fetch stored data by entity type."""
    entity_types = ["product", "user", "transaction"]

    try:
        if entity_type == "product":
            return products
        elif entity_type == "user":
            return users
        elif entity_type == "transaction":
            return transactions
        raise HTTPException(status_code=400, detail=f"Invalid entity type. Choose from: {entity_types}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving data: {e}")

# API Endpoint: User Insights 
@app.get("/insights/users")
def user_spending_insights():
    """Retrieve user insights including spending patterns."""
    try:
        return {
            "total user spending": user_spending,
            "user statistics": calculate_user_statistics(users),
            "user_with_most_transactions": user_with_most_transactions(transactions),
            "users_with_no_transactions": users_with_no_transactions(users, transactions)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving user insights: {e}")

# API Endpoint: Product Insights 
@app.get("/insights/products")
def product_insights():
    """Retrieve product insights including popularity and revenue metrics."""
    try:
        return {
            "most popular category": most_popular_category,
            "average transaction values": average_transaction_values,
            "top_selling_products": top_selling_products(products),
            "expensive_and_cheapest_products details": expensive_and_cheapest_products(products),
            "category_wise_revenue": category_wise_revenue(products),
            "most_rated_products details": most_rated_products(products),
            "top_revenue_categories": top_revenue_categories(products)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving product insights: {e}")

# Running FastAPI Server
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
