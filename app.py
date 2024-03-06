# Import the necessary libraries
from flask import Flask, render_template, request, jsonify
import sqlite3

# Create a Flask app
app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('food_delivery.db')
c = conn.cursor()

# Define the route to render the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for the user registration
@app.route('/api/user/register', methods=['POST'])
def register_user():
    # Get the user data from the request
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Check if the username is already taken
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    if c.fetchone():
        return jsonify({'error': 'Username already taken'}), 400

    # Insert the new user into the database
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

    # Return a success message
    return jsonify({'message': 'User registered successfully'}), 200

# Define the route for the user login
@app.route('/api/user/login', methods=['POST'])
def login_user():
    # Get the user data from the request
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Check if the user exists in the database
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    if not user:
        return jsonify({'error': 'Invalid username or password'}), 400

    # Return a success message and the user ID
    return jsonify({'message': 'User logged in successfully', 'user_id': user[0]}), 200

# Define the route for the restaurant registration
@app.route('/api/restaurant/register', methods=['POST'])
def register_restaurant():
    # Get the restaurant data from the request
    data = request.get_json()
    name = data['name']
    address = data['address']
    phone_number = data['phone_number']

    # Check if the restaurant name is already taken
    c.execute("SELECT * FROM restaurants WHERE name = ?", (name,))
    if c.fetchone():
        return jsonify({'error': 'Restaurant name already taken'}), 400

    # Insert the new restaurant into the database
    c.execute("INSERT INTO restaurants (name, address, phone_number) VALUES (?, ?, ?)", (name, address, phone_number))
    conn.commit()

    # Return a success message
    return jsonify({'message': 'Restaurant registered successfully'}), 200

# Define the route for the restaurant login
@app.route('/api/restaurant/login', methods=['POST'])
def login_restaurant():
    # Get the restaurant data from the request
    data = request.get_json()
    name = data['name']
    phone_number = data['phone_number']

    # Check if the restaurant exists in the database
    c.execute("SELECT * FROM restaurants WHERE name = ? AND phone_number = ?", (name, phone_number))
    restaurant = c.fetchone()
    if not restaurant:
        return jsonify({'error': 'Invalid restaurant name or phone number'}), 400

    # Return a success message and the restaurant ID
    return jsonify({'message': 'Restaurant logged in successfully', 'restaurant_id': restaurant[0]}), 200

# Define the route for creating a new order
@app.route('/api/orders/create', methods=['POST'])
def create_order():
    # Get the order data from the request
    data = request.get_json()
    user_id = data['user_id']
    restaurant_id = data['restaurant_id']
    items = data['items']

    # Calculate the total price of the order
    total_price = 0
    for item in items:
        c.execute("SELECT price FROM menu_items WHERE item_id = ?", (item['item_id'],))
        price = c.fetchone()[0]
        total_price += price * item['quantity']

    # Insert the new order into the database
    c.execute("INSERT INTO orders (user_id, restaurant_id, total_price) VALUES (?, ?, ?)", (user_id, restaurant_id, total_price))
    order_id = c.lastrowid

    # Insert the order items into the database
    for item in items:
        c.execute("INSERT INTO order_items (order_id, item_id, quantity) VALUES (?, ?, ?)", (order_id, item['item_id'], item['quantity']))

    conn.commit()

    # Return a success message and the order ID
    return jsonify({'message': 'Order created successfully', 'order_id': order_id}), 200

# Define the route for getting the status of an order
@app.route('/api/orders/status', methods=['GET'])
def get_order_status():
    # Get the order ID from the query string
    order_id = request.args.get('order_id')

    # Check if the order exists in the database
    c.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
    order = c.fetchone()
    if not order:
        return jsonify({'error': 'Invalid order ID'}), 400

    # Return the status of the order
    return jsonify({'status': order[3]}), 200

# Define the route for getting the menu of a restaurant
@app.route('/api/restaurants/menu', methods=['GET'])
def get_restaurant_menu():
    # Get the restaurant ID from the query string
    restaurant_id = request.args.get('restaurant_id')

    # Retrieve the menu items from the database for the specified restaurant
    c.execute("SELECT * FROM menu_items WHERE restaurant_id = ?", (restaurant_id,))
    menu_items = c.fetchall()

    # Format the menu items as a list of dictionaries
    menu = [{'item_id': item[0], 'name': item[2], 'description': item[3], 'price': item[4]} for item in menu_items]

    # Return the restaurant menu
    return jsonify({'menu': menu}), 200

if __name__ == '__main__':
    app.run()
