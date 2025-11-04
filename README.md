# 🛒 Hoodcart (Django Backend)

The **Hoodcart Backend** powers the eCommerce platform’s API, handling product data, cart management, and payment processing through **Flutterwave**.

It is built with **Django** and **Django REST Framework**, exposing RESTful endpoints consumed by the React frontend.

---

## 🚀 Features

* Product CRUD management
* User cart creation and tracking
* Transaction logging and verification
* Flutterwave Standard payment integration
* API responses optimized for React frontend
* Admin dashboard for product management

---

## 🏗️ Tech Stack

| Component   | Technology                       |
| ----------- | -------------------------------- |
| Framework   | Django 5.x                       |
| API         | Django REST Framework            |
| Database    | SQLite (dev) / PostgreSQL (prod) |
| Payment     | Flutterwave API                  |
| Environment | Python 3.12+, Virtualenv         |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/hoodcart.git
cd hoodcart
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment variables

Create a `.env` file in the root directory and add:

```
DJANGO_SECRET_KEY=your_django_secret
FLUTTERWAVE_PUBLIC_KEY=your_test_public_key
FLUTTERWAVE_SECRET_KEY=your_test_secret_key
DEBUG=True
```

### 5️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Start the development server

```bash
python manage.py runserver
```

Now visit the API at
➡️ `http://127.0.0.1:8000/`

---

## 🔌 API Endpoints (Summary)

| Endpoint             | Method | Description               |
| -------------------- | ------ | ------------------------- |
| `/products/`         | `GET`  | List all products         |
| `/get_cart/`         | `GET`  | Retrieve user cart        |
| `/add_to_cart/`      | `POST` | Add item to cart          |
| `/get_cart_stat/`    | `GET`  | Get cart summary          |
| `/initiate_payment/` | `POST` | Start Flutterwave payment |
| `/payment_callback/` | `GET`  | Verify transaction        |

---

## 💳 Flutterwave Test Setup

Use Flutterwave’s test cards from
🔗 [https://developer.flutterwave.com/docs/testing-requests](https://developer.flutterwave.com/docs/testing-requests)

Set redirect URL in Flutterwave dashboard to:

```
http://127.0.0.1:8000/payment_callback/
```

---

## 🧩 Project Structure

```
hoodcart/
├── hoodcart/             # Core project files
├── shop_app/             # Main Django app
├── manage.py
└── requirements.txt
```

---

## 🧑‍💻 Developer

**Tayo Popoola** — Backend Developer (Django & REST Framework)
📧 https://github.com/tmp-cloud7
