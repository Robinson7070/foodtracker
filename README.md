# Food Delivery App

The Food Delivery App is a web application built with Flask that allows users to place orders from restaurants and track the status of their orders in real-time. Restaurant owners can also manage their menus, view orders, and update order statuses.

## Features

- **User Registration and Authentication**: Users can register for an account and log in to place orders.
- **Order Placement**: Users can create orders by selecting items from restaurant menus.
- **Real-time Order Tracking**: Users can track the status of their orders in real-time, from preparation to delivery.
- **Restaurant Management**: Restaurant owners can manage their menus, view orders, and update order statuses.
- **Responsive Design**: The application is optimized for both desktop and mobile devices.

## Installation

1. Clone the repository:
   git clone https://github.com/Robinson7070/food-delivery-app.git

2. Navigate to the project directory
   cd food-delivery-app


3. Install dependencies:
   pip install -r requirements.txt


4. Set up the database:
   Create a new SQLite database file named `food_delivery.db`.
   Run the SQL commands in `schema.sql` to create the necessary tables.

5. Run the Flask application:
   python app.py:

6. Access the application in your web browser at `http://localhost:5000`.

## Usage

- **User Registration**: Navigate to the registration page (`/register`) to create a new user account.
- **User Login**: Log in with your username and password on the login page (`/login`).
- **Order Placement**: Browse the restaurants and menus, select items, and place orders.
- **Order Tracking**: Track the status of your orders on the order tracking page (`/orders`).
- **Restaurant Management**: Log in as a restaurant owner to manage menus, view orders, and update order statuses.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
