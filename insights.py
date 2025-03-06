from collections import defaultdict
from datetime import datetime

### ---- USER INSIGHTS ---- ###

# Total Transactions Per User
def total_transactions_per_user(transactions):
    """Counts the number of transactions for each user."""
    try:
        user_transactions = defaultdict(int)
        for transaction in transactions:
            user_name = transaction["data"].get("user_name", "Unknown")
            user_transactions[user_name] += 1  # Increment transaction count per user
        return dict(user_transactions)
    except Exception as e:
        print(f"Error in total_transactions_per_user: {e}")
        return {}

# User with Most Transactions
def user_with_most_transactions(transactions):
    """Finds the user who made the most transactions."""
    try:
        user_transactions = total_transactions_per_user(transactions)
        return max(user_transactions, key=user_transactions.get, default=None)
    except Exception as e:
        print(f"Error in user_with_most_transactions: {e}")
        return None

# Users with No Transactions
def users_with_no_transactions(users, transactions):
    """Finds users who haven't made any transactions."""
    try:
        user_names = {user["data"]["name"] for user in users}
        users_with_transactions = {transaction["data"].get("user_name", "Unknown") for transaction in transactions}
        return list(user_names - users_with_transactions)
    except Exception as e:
        print(f"Error in users_with_no_transactions: {e}")
        return []

# User Statistics (Total, Gender, Age Distribution)
def calculate_user_statistics(users):
    """Calculates total users, gender distribution, and age distribution."""
    try:
        total_users = len(users)
        gender_count = defaultdict(int)
        age_categories = {"0-18": 0, "19-30": 0, "31-45": 0, "46-60": 0, "61+": 0}
        current_year = datetime.utcnow().year

        for user in users:
            user_data = user.get("data", {})
            gender = user_data.get("gender", "Unknown")
            dob = user_data.get("dob", "")

            # Calculate age
            birth_year = int(dob[:4]) if dob and len(dob) >= 4 else current_year  # Extract year safely
            age = current_year - birth_year

            # Categorize age
            if age <= 18:
                age_categories["0-18"] += 1
            elif age <= 30:
                age_categories["19-30"] += 1
            elif age <= 45:
                age_categories["31-45"] += 1
            elif age <= 60:
                age_categories["46-60"] += 1
            else:
                age_categories["61+"] += 1

            # Count gender
            gender_count[gender] += 1

        return {
            "total_users": total_users,
            "gender_distribution": dict(gender_count),
            "age_distribution": age_categories
        }
    except Exception as e:
        print(f"Error in calculate_user_statistics: {e}")
        return {"total_users": 0, "gender_distribution": {}, "age_distribution": {}}

### ---- PRODUCT INSIGHTS ---- ###

# Top-Selling Products
def top_selling_products(products, top_n=5):
    """Finds the top N best-selling products based on rating count."""
    try:
        product_sales = {}

        for product in products:
            title = product["data"].get("title", "Unknown")
            sales_count = product["data"].get("rating", {}).get("count", 0)  # Use rating count as sales metric

            if title:
                product_sales[title] = sales_count

        return sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:top_n]  # Return top N products
    except Exception as e:
        print(f"Error in top_selling_products: {e}")
        return []

# Most Expensive & Cheapest Products
def expensive_and_cheapest_products(products):
    """Finds the most expensive and cheapest products."""
    try:
        sorted_products = sorted(products, key=lambda x: x["data"].get("price", 0))
        return {
            "cheapest_product": sorted_products[0]["data"] if sorted_products else None,
            "most_expensive_product": sorted_products[-1]["data"] if sorted_products else None
        }
    except Exception as e:
        print(f"Error in expensive_and_cheapest_products: {e}")
        return {"cheapest_product": None, "most_expensive_product": None}

# Category-Wise Revenue
def category_wise_revenue(products):
    """Calculates total revenue generated per product category."""
    try:
        category_revenue = defaultdict(float)

        for product in products:
            category = product["data"].get("category", "Unknown")
            price = product["data"].get("price", 0)

            if category:
                category_revenue[category] += price  # Sum revenue per category

        return dict(category_revenue)
    except Exception as e:
        print(f"Error in category_wise_revenue: {e}")
        return {}

# Top Revenue-Generating Categories
def top_revenue_categories(products, top_n=5):
    """Finds the top N revenue-generating product categories."""
    try:
        revenue_data = category_wise_revenue(products)
        sorted_categories = sorted(revenue_data.items(), key=lambda x: x[1], reverse=True)
        return sorted_categories[:top_n]
    except Exception as e:
        print(f"Error in top_revenue_categories: {e}")
        return []

# Most Rated Products
def most_rated_products(products):
    """Finds the top 5 most rated products based on customer reviews."""
    try:
        return sorted(products, key=lambda x: x["data"].get("rating", {}).get("count", 0), reverse=True)[:5]
    except Exception as e:
        print(f"Error in most_rated_products: {e}")
        return []
