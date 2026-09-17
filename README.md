# 📱 TechZone - Single Vendor E-commerce Website

A modern Single Vendor E-commerce Website built with **Django** that allows customers to browse technology products, search and filter products, view product details, manage a shopping cart, provide delivery information, place orders, and receive order confirmation.

---

## Features

- Home Page
- Product Listing
- Product Details
- Product Categories
- Product Search
- Category Filtering
- Dynamic Product Loading from Database
- Product Image Management
- Product Stock Management
- Automatic Product Slug Generation
- Automatic Category Slug Generation
- Add to Cart
- Increase Cart Quantity
- Decrease Cart Quantity
- Remove from Cart
- Dynamic Cart Item Count
- Session-Based Shopping Cart
- In Cart Button State
- Checkout
- Customer Information
- Delivery Address
- Cash on Delivery
- Order Creation
- Multiple Order Items
- Automatic Stock Reduction
- Order Status Management
- Order Success Page
- Django Admin Panel
- Responsive UI
- Bootstrap
- Custom CSS
- JavaScript Interactions
- Modular Django Applications

---

## Technology Stack

- Python 3
- Django
- PostgreSQL
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Pillow
- python-dotenv
- Boxicons

---

## Project Structure

```text
TechZone/
│
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── customers/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── products/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── cart/
│   ├── migrations/
│   ├── __init__.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── orders/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── payments/
│   ├── migrations/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   │
│   └── js/
│
├── templates/
│   ├── base.html
│   │
│   ├── accounts/
│   │
│   ├── customers/
│   │   └── checkout.html
│   │
│   ├── products/
│   │   ├── product_list.html
│   │   └── product_detail.html
│   │
│   ├── cart/
│   │   └── cart.html
│   │
│   └── orders/
│       └── order_success.html
│
├── media/
│   ├── products/
│   └── screenshots/
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation Guide

### Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Go to Project Directory

```bash
cd TechZone
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root directory.

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=techzone
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

---

## Database

Database: **PostgreSQL**

Create a PostgreSQL database:

```text
techzone
```

Configure the database credentials inside `.env`.

### Run Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

Enter:

```text
Username
Email
Password
```

---

## Run Server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

---

## Django Admin Panel

Open:

```text
http://127.0.0.1:8000/admin/
```

---

## UI Screenshots

### Home Page

<p align="center">
<img src="media/screenshots/home.png" width="800">
</p>

<p align="center">
<b>Figure 1: TechZone Home Page</b>
</p>

---

### Product List

<p align="center">
<img src="media/screenshots/products.png" width="800">
</p>

<p align="center">
<b>Figure 2: Product Listing Page</b>
</p>

---

### Product Details

<p align="center">
<img src="media/screenshots/product_details.png" width="800">
</p>

<p align="center">
<b>Figure 3: Product Details Page</b>
</p>

---

### Empty Cart

<p align="center">
<img src="media/screenshots/cart_empty.png" width="800">
</p>

<p align="center">
<b>Figure 4: Empty Shopping Cart</b>
</p>

---

### Shopping Cart

<p align="center">
<img src="media/screenshots/cart.png" width="800">
</p>

<p align="center">
<b>Figure 5: Shopping Cart</b>
</p>

---

### Checkout

<p align="center">
<img src="media/screenshots/checkout.png" width="800">
</p>

<p align="center">
<b>Figure 6: Checkout Page</b>
</p>

---

### Order Success

<p align="center">
<img src="media/screenshots/order_success.png" width="800">
</p>

<p align="center">
<b>Figure 7: Order Success Page</b>
</p>

---

## Functionalities

- ✔ Home Page
- ✔ Navigation Bar
- ✔ Footer
- ✔ Product Listing
- ✔ Product Details
- ✔ Product Categories
- ✔ Product Search
- ✔ Category Filtering
- ✔ Automatic Product Slug Generation
- ✔ Automatic Category Slug Generation
- ✔ Product Image Upload
- ✔ Product Stock Management
- ✔ Add to Cart
- ✔ AJAX Add to Cart
- ✔ In Cart State
- ✔ Increase Quantity
- ✔ Decrease Quantity
- ✔ Remove Product
- ✔ Session-Based Cart
- ✔ Dynamic Cart Count
- ✔ Cart Total Calculation
- ✔ Checkout
- ✔ Customer Information
- ✔ Delivery Address
- ✔ Cash on Delivery
- ✔ Order Creation
- ✔ Multiple Order Items
- ✔ Stock Reduction
- ✔ Cart Clearing
- ✔ Order Status Management
- ✔ Order Success Page
- ✔ Django Admin
- ✔ PostgreSQL Database
- ✔ Bootstrap
- ✔ Custom CSS
- ✔ JavaScript
- ✔ Responsive UI

---

## Future Improvements

### Authentication

- User Registration
- User Login
- User Logout
- Password Reset
- Customer Profile
- Customer Dashboard

### Products

- Product Reviews
- Product Ratings
- Wishlist
- Product Comparison
- Advanced Filtering
- Product Sorting
- Related Products

### Orders

- Order History
- Order Tracking
- Order Cancellation
- Order Invoice
- Email Order Confirmation

### Payments

- bKash Integration
- Nagad Integration
- SSLCommerz Integration
- Stripe Integration
- Online Payment Verification

### Administration

- Admin Dashboard
- Sales Analytics
- Revenue Reports
- Inventory Reports
- Low Stock Alerts
- Customer Management
- Order Management

---

## Author

**Maksuda Parvin**

Department of Computer Science & Engineering

Bangladesh University of Business and Technology (BUBT)

---

## License

This project is developed for learning purposes.