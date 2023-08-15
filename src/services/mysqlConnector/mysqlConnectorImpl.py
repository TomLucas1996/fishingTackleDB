import mysql.connector

# Replace these values with your actual database credentials
host = "localhost"
user = "root"
password = "root"
database = "XXX"

# Establish a connection to the database
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("Connected to the database")

    # Perform database operations here
    if connection.is_connected():
        cursor = connection.cursor()

    # Example: Execute a SELECT query
    query = "SELECT * FROM your_table_name"
    cursor.execute(query)

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed")


except mysql.connector.Error as err:
    print(f"Error: {err}")
