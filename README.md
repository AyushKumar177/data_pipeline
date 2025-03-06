Brief summary of how I approached the problem:-
    Data Fetching – Collected data from three public APIs (products, users, transactions) with error handling.
    Data Transformation – Standardized and normalised data and metadata while handling  fields.
    Data Enrichment – Joined transactions with products and users, calculated user spending, popular categories, and revenue.
    API Development – Built FastAPI endpoints to serve raw and processed data, including user and product insights.
    Error Handling & Optimization – Used try-except blocks to prevent crashes and optimized dictionary lookups for performance.
    Data Storage – Stored processed data into JSON files for structured and readable output.

Technologies used:

Programming Language: Python

Frameworks & Libraries
    FastAPI – Web framework for building APIs.
    Uvicorn – ASGI server for running FastAPI.
    Requests – Fetching data from public APIs.
    JSON – Data storage and manipulation.
    Datetime – Handling timestamps.
    UUID – Generating unique identifiers.
    Collections (defaultdict) – Optimizing data processing.

Data Storage & Processing
    JSON Files – Storing transformed data.
    Dictionary Lookups – Fast data retrieval.

Development & Deployment
    Virtual Environment – Isolated Python environment.
    Git & GitHub – Version control and code management.
    Swagger UI (FastAPI Docs) – API documentation and testing.

Steps followed to Implement the Solution

Step 1: Setup the Project

Create a project structure:
    data_pipeline/
    ├── main.py  
    ├── fetch_data.py
    ├── transform.py
    ├── insights.py
    ├── requirements.txt
    ├── README.md
    ├── business_rules.py

Follwoing links were used:
    PRODUCTS_API = "https://fakestoreapi.com/products"
    USERS_API = "https://randomuser.me/api/?results=20"
    TRANSACTIONS_API = "https://my.api.mockaroo.com/orders.json?key=e49e6840"

create a virtual environment :
    python -m venv venv
    venv\Scripts\activate     # For Windows

installing dependencies
    writing required libraries on requirements.txt
    pip install -r requirements.txt


Step 2 : Write the entire logic in different files 

Step 1: Data Fetching (fetch_data.py)
    Functions:
        fetch_products
        fetch_users
        fetch_transactions
        fetch_data
    Used functions to fetch products, users, and transactions from different functions.
    Implemented error handling to ensure API failures don’t break the pipeline.

Step 2: Data Transformation (transform.py)
    Functions:
        generate_unique_id
        transform_product
        transform_user
        transform_transaction
        transform_data
    Standardized data into a structured format using transform.py.
    UUIDs were generated for each record to ensure uniqueness.
    Handled missing fields to avoid KeyErrors.

Step 3: Data Enrichment & Business Logic (business_rules.py)
    Functions:
        join_transactions_with_products
        join_transactions_with_users
        calculate_user_spending
        most_popular_categories
        average_transaction_value
    Transactions were linked with users and products for richer insights.
    User spending, popular categories, and revenue calculations were implemented.

Step 4: Data Insights (insights.py)
Functions:
    total_transactions_per_user
    user_with_most_transactions
    users_with_calculate_user_statistics
    top_selling_products
    expensive_and_cheapest_products
    category_wise_revenue
    top_revenue_categories
    most_rated_products
insights.py processes data to generate insights on user transactions and product performance, including spending patterns, top-selling products, revenue calculations, and category popularity for better analytics.

Step 5: API Development (main.py)
    Firstly imported all the libraries and functions.
    Initialised FastApi App
    Implemented  Fetching and transforming data
    Combined product and transaction data and also transaction and user data.
    Calculated user_spending,most_popular_category,average_transaction_values
    Saved all the data in JSON for better understanding

 GET /data/{entity_type} 
 - Retrieve processed data  by type 
 - RESPONSE :
            [
                {
                    "entity_id": "cf95f003-672f-438f-bb23-c6a3f98748a6",
                    "entity_type": "transaction",
                    "timestamp": "2025-03-06T10:50:14.646606",
                    "data": {
                    "transaction_id": 1,
                    "parcel_id": "9181",
                    "status": "delivered",
                    "sender": "Realbuzz",
                    "user_phone": ":46 729478015",
                    "user_name": "Jhon Doe"
                    },
                    "metadata": {
                    "source": "mockaroo",
                    "processed_at": "2025-03-06T10:50:14.646606"
                    }
                },
                .....
                }

 GET /insights/users 
 - User spending patterns and statistics 
 - RESPONSE :
       
            {
            "total user spending": {
                "Jhon Doe": 10
            },
            "user statistics": {
                "total_users": 20,
                "gender_distribution": {
                "male": 16,
                "female": 4
                },
                "age_distribution": {
                "0-18": 0,
                "19-30": 0,
                "31-45": 5,
                "46-60": 10,
                "61+": 5
                }
            },
            "user_with_most_transactions": "Jhon Doe",
            "users_with_no_transactions": [
                "Mehmet Simon",
                "Lumi Salo",
                "پریا زارعی",
                "Chanakya Das",
                "Eugen Gautier",
                "Jason Olson",
                "Paul Laurent",
                "Magdalena Tapia",
                "Elliot Smith",
                "Tony Carpentier",
                "Clarence Woods",
                "Edna Harrison",
                "Cory Nelson",
                "Benjamin Green",
                "Jacob Shaw",
                "حسین صدر",
                "Noa Carpentier",
                "Thomas Li",
                "Gustavo Peña",
                "Ilir Bertrand"
            ]
            } 

 GET /insights/products 
 - Product popularity metrics
 - RESPONSE :
            {
            "most popular category": [
                [
                "electronics",
                1782
                ],
                [
                "women's clothing",
                1675
                ],
                [
                "men's clothing",
                1309
                ],
                [
                "jewelery",
                970
                ]
            ],
            "average transaction values": {
                "men's clothing": 51.057500000000005,
                "jewelery": 220.995,
                "electronics": 332.49833333333333,
                "women's clothing": 26.286666666666665
            },
            "top_selling_products": [
                [
                "Rain Jacket Women Windbreaker Striped Climbing Raincoats",
                679
                ],
                [
                "Mens Cotton Jacket",
                500
                ],
                [
                "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s",
                470
                ],
                [
                "Mens Casual Slim Fit",
                430
                ],
                [
                "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
                400
                ]
            ],
            "expensive_and_cheapest_products details": {
                "cheapest_product": {
                "id": 19,
                "title": "Opna Women's Short Sleeve Moisture",
                "category": "women's clothing",
                "price": 7.95,
                "rating": {
                    "rate": 4.5,
                    "count": 146
                }
                },
                "most_expensive_product": {
                "id": 14,
                "title": "Samsung 49-Inch CHG90 144Hz Curved Gaming Monitor (LC49HG90DMNXZA) – Super Ultrawide Screen QLED ",
                "category": "electronics",
                "price": 999.99,
                "rating": {
                    "rate": 2.2,
                    "count": 140
                }
                }
            },
            "category_wise_revenue": {
                "men's clothing": 204.23000000000002,
                "jewelery": 883.98,
                "electronics": 1994.99,
                "women's clothing": 157.72
            },
            "most_rated_products details": [
                {
                "entity_id": "20e30f95-a54a-44f0-9070-df3c7581d38e",
                "entity_type": "product",
                "timestamp": "2025-03-06T10:50:14.646606",
                "data": {
                    "id": 17,
                    "title": "Rain Jacket Women Windbreaker Striped Climbing Raincoats",
                    "category": "women's clothing",
                    "price": 39.99,
                    "rating": {
                    "rate": 3.8,
                    "count": 679
                    }
                },
                "metadata": {
                    "source": "fakestoreapi",
                    "processed_at": "2025-03-06T10:50:14.646606"
                }
                },
                {
                "entity_id": "1b7d408a-9c90-4608-bdb0-30611b5cab3a",
                "entity_type": "product",
                "timestamp": "2025-03-06T10:50:14.646606",
                "data": {
                    "id": 3,
                    "title": "Mens Cotton Jacket",
                    "category": "men's clothing",
                    "price": 55.99,
                    "rating": {
                    "rate": 4.7,
                    "count": 500
                    }
                },
                "metadata": {
                    "source": "fakestoreapi",
                    "processed_at": "2025-03-06T10:50:14.646606"
                }
                },
                {
                "entity_id": "2637c06d-91ae-4c25-ab18-66fa4fde6933",
                "entity_type": "product",
                "timestamp": "2025-03-06T10:50:14.646606",
                "data": {
                    "id": 10,
                    "title": "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s",
                    "category": "electronics",
                    "price": 109,
                    "rating": {
                    "rate": 2.9,
                    "count": 470
                    }
                },
                "metadata": {
                    "source": "fakestoreapi",
                    "processed_at": "2025-03-06T10:50:14.646606"
                }
                },
                {
                "entity_id": "5a8ef6b7-0035-414a-929c-85c9effdcd3e",
                "entity_type": "product",
                "timestamp": "2025-03-06T10:50:14.646606",
                "data": {
                    "id": 4,
                    "title": "Mens Casual Slim Fit",
                    "category": "men's clothing",
                    "price": 15.99,
                    "rating": {
                    "rate": 2.1,
                    "count": 430
                    }
                },
                "metadata": {
                    "source": "fakestoreapi",
                    "processed_at": "2025-03-06T10:50:14.646606"
                }
                },
                {
                "entity_id": "88a1c87f-3ba2-4ced-8f09-cdd00c1f8718",
                "entity_type": "product",
                "timestamp": "2025-03-06T10:50:14.646606",
                "data": {
                    "id": 5,
                    "title": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
                    "category": "jewelery",
                    "price": 695,
                    "rating": {
                    "rate": 4.6,
                    "count": 400
                    }
                },
                "metadata": {
                    "source": "fakestoreapi",
                    "processed_at": "2025-03-06T10:50:14.646606"
                }
                }
            ],
            "top_revenue_categories": [
                [
                "electronics",
                1994.99
                ],
                [
                "jewelery",
                883.98
                ],
                [
                "men's clothing",
                204.23000000000002
                ],
                [
                "women's clothing",
                157.72
                ]
            ]
            }

Developed FastAPI endpoints to serve raw and processed data.
Provided insights into user behavior and product sales.

Step 6: Error Handling & Optimization
Try-except blocks were added in all functions to handle failures.
Ensured default values were returned for missing data.
Optimized dictionary lookups for faster processing.


Step 3 : running the application to test
    in the terminal put this command to run
    -uvicorn main:app --reload


Future Improvements :
    Database Integration
    UI Dashboard
    Authentication & Authorization 
    Artficial Intelligent system