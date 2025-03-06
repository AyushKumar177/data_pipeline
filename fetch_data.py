import requests

# API Endpoints for fetching data
PRODUCTS_API = "https://fakestoreapi.com/products"  # E-commerce product data
USERS_API = "https://randomuser.me/api/?results=20"  # User profiles
TRANSACTIONS_API = "https://my.api.mockaroo.com/orders.json?key=e49e6840"  # Transaction data

# Fetch Product Data
def fetch_products():
    """Fetches product data with error handling."""
    try:
        response = requests.get(PRODUCTS_API, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching products: {e}")
        return []  # Return empty list on failure

# Fetch User Data
def fetch_users():
    """Fetches user data with error handling."""
    try:
        response = requests.get(USERS_API, timeout=10)
        response.raise_for_status()
        return response.json().get("results", [])  # Extract user list
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users: {e}")
        return []

# Fetch Transaction Data
def fetch_transactions():
    """Fetches transaction data with error handling."""
    try:
        response = requests.get(TRANSACTIONS_API, timeout=10)
        response.raise_for_status()
        return response.json()  # Return transaction records
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transactions: {e}")
        return []

# Fetch All Data
def fetch_data():
    """Fetches all data sources and returns as a dictionary."""
    return {
        "products": fetch_products(),
        "users": fetch_users(),
        "transactions": fetch_transactions()
    }
