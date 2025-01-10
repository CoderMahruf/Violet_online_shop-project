# Violet Online Store

## Project Overview

The **Violet Online Store** is an e-commerce web application developed using the Django framework. This platform provides users with a seamless shopping experience, allowing them to browse products, view categories, and complete purchases using PayPal or a debit/credit card.

---

## Features

### 1. Homepage
- A clean and elegant homepage with a "Lookbook" section showcasing featured clothing items.

### 2. Product Categories
- Featured categories are displayed on the homepage, such as:
  - Electronics
  - Jewelry
  - Men's Clothing
  - Women's Clothing

### 3. Product Listings
- Each product is displayed with an image, title, price, and brief description.

### 4. Checkout System
- A fully integrated checkout system with multiple payment options:
  - PayPal
  - Pay Later
  - Debit/Credit Card (powered by PayPal)

### 5. Responsive Design
- The application is mobile-friendly and responsive, ensuring usability across various devices.

### 6. Admin Dashboard
- Built-in Django admin interface for managing products, categories, and orders.

---

## Technologies Used

- **Backend:** Django Framework (Python)
- **Frontend:** HTML, CSS, JavaScript (for interactivity)
- **Database:** SQLite (default Django database)
- **Payment Integration:** PayPal API

---

## Installation Guide

### Prerequisites
- Python 3.8 or later
- pip (django,pillow)
- Virtualenv (env)

### Steps
1. Clone the repository:
   ```bash
   git clone <https://github.com/CoderMahruf/Violet_online_shop-project.git>
   cd config/
   ```

2. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for the admin interface:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open the application in your web browser at `http://127.0.0.1:8000`.

---

## Usage

1. Access the homepage to browse featured products and categories.
2. Navigate through product categories to find specific items.
3. Add desired products to the cart.
4. Proceed to the checkout page and select a payment option to complete your purchase.

---

## Project Structure

```
project-root/
|
|-- violet/
|   |-- settings.py      # Django settings file
|   |-- urls.py          # URL routing configuration
|   |-- wsgi.py          # WSGI entry point
|
|-- templates/           # HTML templates
|-- static/              # Static files (CSS, JS, images)
|-- media/               # Uploaded media files
|-- requirements.txt     # Python dependencies
|-- manage.py            # Django management script
```

---

## Future Enhancements

- Add user authentication and profile management.
- Implement advanced product filters (e.g., price range, ratings).
- Integrate additional payment gateways.
- Add product reviews and ratings.
- Deploy the application to a cloud platform.

---

## Credits

Developed by [Mahruful Alam].

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

