
import uuid
import datetime

# Generate a unique ID for each transformed entity
def generate_unique_id():
    return str(uuid.uuid4())

# Transform raw product data into a standardized format
def transform_product(product):
    try:
        return {
            "entity_id": generate_unique_id(),
            "entity_type": "product",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "data": {
                "id": product["id"],
                "title": product["title"],
                "category": product["category"],
                "price": product["price"],
                "rating": product.get("rating", {})  # Handle missing rating field
            },
            "metadata": {
                "source": "fakestoreapi",
                "processed_at": datetime.datetime.utcnow().isoformat()
            }
        }
    except Exception as e:
        print(f"Error in transform_product: {e}")
        return {}

# Transform raw user data into a standardized format
def transform_user(user):
    try:
        return {
            "entity_id": generate_unique_id(),
            "entity_type": "user",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "data": {
                "id": user["login"]["uuid"],
                "name": f"{user['name']['first']} {user['name']['last']}",
                "gender": user.get("gender", "Unknown"),
                "email": user.get("email", "Unknown"),
                "location": f"{user['location'].get('state', 'Unknown')} , {user['location'].get('country', 'Unknown')}",
                "user_name": user["login"]["username"],
                "password": user["login"]["password"],
                "dob": user["dob"]["date"],
                "phone": user.get("phone", "Unknown")
            },
            "metadata": {
                "source": "randomuserapi",
                "processed_at": datetime.datetime.utcnow().isoformat()
            }
        }
    except Exception as e:
        print(f"Error in transform_user: {e}")
        return {}

# Transform raw transaction data into a standardized format
def transform_transaction(transaction, users, products):
    try:
        user_id = transaction.get("user_id")
        product_id = transaction.get("product_id")

        user = next((u for u in users if u["data"].get("id") == user_id), None) if user_id else None
        product = next((p for p in products if p["data"].get("id") == product_id), None) if product_id else None

        return {
            "entity_id": generate_unique_id(),
            "entity_type": "transaction",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "data": {
                "transaction_id": transaction.get("id"),
                "parcel_id": transaction.get("parcel_id", "Unknown"),
                "status": transaction.get("status", "Unknown"),
                "sender": transaction.get("sender", "Unknown"),
                "user_phone": transaction.get("user_phone", "Unknown"),
                "user_name": transaction.get("user_name", "Unknown")
            },
            "metadata": {
                "source": "mockaroo",
                "processed_at": datetime.datetime.utcnow().isoformat()
            }
        }
    except Exception as e:
        print(f"Error in transform_transaction: {e}")
        return {}

# Transform all raw data into standardized format
def transform_data(raw_data):
    try:
        transformed_products = [transform_product(p) for p in raw_data["products"]]
        transformed_users = [transform_user(u) for u in raw_data["users"]]
        transformed_transactions = [transform_transaction(t, transformed_users, transformed_products) for t in raw_data["transactions"]]

        return {
            "products": transformed_products,
            "users": transformed_users,
            "transactions": transformed_transactions
        }
    except Exception as e:
        print(f"Error in transform_data: {e}")
        return {"products": [], "users": [], "transactions": []}  # Return empty lists on failure
