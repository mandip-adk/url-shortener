# URL Shortener - Django

## Overview

A URL Shortener web application built with Django that allows authenticated users to create, manage, and track shortened URLs.

The application provides user authentication, URL management, click analytics, custom short aliases, and optional expiration dates.

This project was developed as part of a Django Backend Developer technical assessment.

---

## Features

### Authentication

* User Registration
* User Login
* User Logout
* Protected routes for authenticated users

### URL Management

* Create shortened URLs
* View all created URLs
* Edit existing URLs
* Delete URLs
* User-specific URL ownership

### URL Shortening

* Automatic unique short code generation
* Custom short aliases (optional)
* Redirect short URLs to original URLs

### Analytics

* Track click counts for each shortened URL
* Display creation date and time

### Expiration Support

* Optional expiration date for shortened URLs
* Expired links display an expiration page instead of redirecting

### User Interface

* Responsive design using Bootstrap
* Dashboard for managing URLs
* Mobile-friendly layout

---

## Tech Stack

* Python
* Django
* SQLite
* Bootstrap 5
* HTML
* CSS

---

## Project Structure

```text
url_shortener/
│
├── accounts/          # Authentication app
├── shortner/          # URL shortening functionality
├── templates/         # HTML templates
├── static/            # Static files
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## Database Design

### ShortURL Model

| Field        | Description              |
| ------------ | ------------------------ |
| user         | Owner of the URL         |
| original_url | Original long URL        |
| short_code   | Unique short identifier  |
| created_at   | Creation timestamp       |
| click_count  | Number of redirects      |
| expires_at   | Optional expiration date |

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/mandip-adk/url-shortener.git
cd url-shortener
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Usage

### Create a Short URL

1. Register an account
2. Login
3. Click "Create New"
4. Enter the original URL
5. Optionally:

   * Provide a custom short code
   * Set an expiration date
6. Save

### Redirect

Visiting a short URL automatically:

* Increments the click counter
* Redirects to the original URL

### Expired Links

If a URL has passed its expiration date, an expiration page is shown instead of redirecting.

---

## Security Considerations

* Only authenticated users can manage URLs.
* Users can only edit or delete their own URLs.
* Duplicate custom short codes are prevented through validation.
* Invalid short codes return a 404 response.

---

## Future Improvements

* QR Code Generation
* Advanced Analytics Dashboard
* REST API Support
* Password Reset Functionality
* URL Categories and Tags

---

## Author

Mandip Adhikari

