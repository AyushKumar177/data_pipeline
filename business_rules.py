from collections import defaultdict

# Join Transactions with Product Details
def join_transactions_with_products(transactions, products):
    """Enrich transactions by adding product details based on parcel_id."""
    try:
        # Create a mapping of product IDs to product details for fast lookup
        product_lookup = {str(product["data"]["id"]): product["data"] for product in products}
        enriched_transactions = []

        for transaction in transactions:
            parcel_id = str(transaction["data"].get("parcel_id", ""))  # Convert to string for lookup
            product = product_lookup.get(parcel_id)  # Find product by parcel_id

            # Append transaction with product details
            enriched_transactions.append({
                "transaction_id": transaction["data"].get("transaction_id", "Unknown"),
                "user_name": transaction["data"].get("user_name", "Unknown"),
                "user_phone": transaction["data"].get("user_phone", "Unknown"),
                "status": transaction["data"].get("status", "Unknown"),
                "sender": transaction["data"].get("sender", "Unknown"),
                "product": product.get("title", "Product Not Found") if product else "Product Not Found"
            })

        return enriched_transactions

    except Exception as e:
        print(f"Error in join_transactions_with_products: {e}")
        return []  # Return empty list on failure


# Join Transactions with User Details
def join_transactions_with_users(transactions, users):
    """Enrich transactions by adding user details."""
    try:
        enriched_transactions = []
        # Create a dictionary mapping user names to user details for fast lookup
        user_lookup = {u["data"]["name"]: u["data"] for u in users}

        for transaction in transactions:
            transaction_data = transaction.get("data", {})
            user_name = transaction_data.get("user_name")

            # Fetch user details using the lookup table
            user_details = user_lookup.get(user_name, None)

            enriched_transactions.append({
                "transaction_id": transaction_data.get("transaction_id", "Unknown"),
                "user": user_details if user_details else "User Not Found",
                "user_phone": transaction_data.get("user_phone", "Unknown"),
                "status": transaction_data.get("status", "Unknown"),
                "sender": transaction_data.get("sender", "Unknown"),
                "parcel_id": transaction_data.get("parcel_id", "Unknown"),
            })

        return enriched_transactions

    except Exception as e:
        print(f"Error in join_transactions_with_users: {e}")
        return []  # Return empty list on failure


# Calculate Total Spending per User
def calculate_user_spending(transactions):
    """Counts the number of transactions per user."""
    try:
        user_transactions = defaultdict(int)

        for transaction in transactions:
            user_name = transaction["data"].get("user_name", "Unknown")
            user_transactions[user_name] += 1

        return dict(user_transactions)

    except Exception as e:
        print(f"Error in calculate_user_spending: {e}")
        return {}  # Return empty dictionary on failure


# Identify Most Popular Product Categories
def most_popular_categories(products):
    """Finds the most popular product categories based on rating count."""
    try:
        category_count = defaultdict(int)

        for product in products:
            category = product["data"].get("category", "Unknown")
            rating_count = product["data"].get("rating", {}).get("count", 0)

            if category:
                category_count[category] += rating_count

        # Return categories sorted by popularity (highest rating count first)
        return sorted(category_count.items(), key=lambda x: x[1], reverse=True)

    except Exception as e:
        print(f"Error in most_popular_categories: {e}")
        return []  # Return empty list on failure


# Calculate Average Transaction Value
def average_transaction_value(products):
    """Calculates the average price of products within each category."""
    try:
        category_prices = defaultdict(list)

        for product in products:
            category = product["data"].get("category", "Unknown")
            price = product["data"].get("price", 0)

            if category:
                category_prices[category].append(price)

        # Compute the average price per category
        return {category: sum(prices) / len(prices) for category, prices in category_prices.items() if prices}

    except Exception as e:
        print(f"Error in average_transaction_value: {e}")
        return {}  # Return empty dictionary on failure
