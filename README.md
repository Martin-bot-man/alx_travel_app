
<img width="1248" height="908" alt="image" src="https://github.com/user-attachments/assets/ebef4111-4837-4596-936f-91371f71243c" />

# Property Management API

A production-ready REST API for managing property listings built with Django REST Framework. Features comprehensive CRUD operations, advanced filtering, and interactive API documentation.

## 🚀 Features

- **Full CRUD Operations** - Create, Read, Update, Delete property listings
- **Advanced Filtering** - Filter by property type, price range, location, and guest capacity
- **Interactive API Documentation** - Swagger UI and ReDoc integration
- **Data Validation** - Comprehensive input validation and error handling
- **Timestamps** - Automatic tracking of creation and modification times
- **Availability Management** - Track property availability status
- **RESTful Design** - Follows REST API best practices
- **Pagination** - Efficient handling of large datasets
- **OpenAPI Specification** - Standards-compliant API schema

## 🛠️ Tech Stack

- **Framework:** Django 5.2.9
- **API:** Django REST Framework 3.16.1
- **Documentation:** drf-yasg (Swagger/OpenAPI)
- **Database:** SQLite (Development) / PostgreSQL (Production-ready)
- **Python:** 3.12+

## 📋 Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd alx_travel_app_0x01
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Activate on Linux/Mac
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:

```bash
pip install django djangorestframework django-cors-headers drf-yasg
```

### 4. Navigate to Project Directory

```bash
cd alx_travel_app
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Documentation

### Interactive Documentation

- **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

### Schema Files

- **JSON:** [http://127.0.0.1:8000/swagger.json](http://127.0.0.1:8000/swagger.json)
- **YAML:** [http://127.0.0.1:8000/swagger.yaml](http://127.0.0.1:8000/swagger.yaml)

## 🔌 API Endpoints

### Listings

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/listings/` | List all listings (with filters) |
| POST | `/api/listings/` | Create a new listing |
| GET | `/api/listings/{id}/` | Retrieve a specific listing |
| PUT | `/api/listings/{id}/` | Update a listing (full) |
| PATCH | `/api/listings/{id}/` | Partial update a listing |
| DELETE | `/api/listings/{id}/` | Delete a listing |
| GET | `/api/listings/property_types/` | Get available property types |

### Query Parameters (Filtering)

- `property_type` - Filter by type (apartment, house, villa, condo)
- `min_price` - Minimum price per night
- `max_price` - Maximum price per night
- `location` - Search by location (case-insensitive)
- `max_guests` - Minimum guest capacity
- `is_available` - Filter by availability (true/false)

## 📝 Usage Examples

### Create a Listing

```bash
curl -X POST http://127.0.0.1:8000/api/listings/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Luxury Beach Villa",
    "description": "Beautiful villa with ocean views",
    "property_type": "villa",
    "price_per_night": "250.00",
    "location": "Malibu, California",
    "max_guests": 6,
    "amenities": ["WiFi", "Pool", "Beach Access", "Parking"],
    "is_available": true
  }'
```

### Get All Listings

```bash
curl http://127.0.0.1:8000/api/listings/
```

### Filter Listings

```bash
# By property type
curl "http://127.0.0.1:8000/api/listings/?property_type=villa"

# By price range
curl "http://127.0.0.1:8000/api/listings/?min_price=100&max_price=300"

# By location
curl "http://127.0.0.1:8000/api/listings/?location=california"

# Combined filters
curl "http://127.0.0.1:8000/api/listings/?property_type=apartment&max_price=150&location=nairobi"
```

### Update a Listing

```bash
curl -X PATCH http://127.0.0.1:8000/api/listings/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "price_per_night": "275.00",
    "is_available": false
  }'
```

### Delete a Listing

```bash
curl -X DELETE http://127.0.0.1:8000/api/listings/1/
```

## 🗂️ Project Structure

```
alx_travel_app_0x01/
├── alx_travel_app/
│   ├── alx_travel_app/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py          # Main URL configuration
│   │   └── wsgi.py
│   ├── hotel_management/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py         # Listing model
│   │   ├── serializers.py    # DRF serializers
│   │   ├── views.py          # API viewsets
│   │   └── urls.py           # App URL routing
│   ├── manage.py
│   └── db.sqlite3
└── venv/
```

## 🔒 Security Features

- **Input Validation** - Comprehensive validation on all fields
- **URL Pattern Validation** - Regex-based route protection for schema endpoints
- **CORS Configuration** - Controlled cross-origin access
- **SQL Injection Protection** - Django ORM prevents SQL injection
- **XSS Protection** - Built-in Django security features

### Schema Endpoint Security

Instead of accepting any format:
```python
path('swagger<format>/', ...)  # ❌ Accepts anything
```

We use explicit validation:
```python
re_path(r'^swagger(?P<format>\.json|\.yaml)$', ...)  # ✅ Only .json and .yaml
```

This prevents malicious requests like `/swagger.hack` or `/swagger<script>`.

## 🧪 Testing with Postman

1. Import the OpenAPI schema: `http://127.0.0.1:8000/swagger.json`
2. Postman will auto-generate all endpoints
3. Start testing CRUD operations

## 📊 Data Model

### Listing Model

```python
{
  "id": 1,
  "title": "Luxury Beach Villa",
  "description": "Beautiful villa with ocean views",
  "property_type": "villa",
  "property_type_display": "Villa",
  "price_per_night": "250.00",
  "location": "Malibu, California",
  "max_guests": 6,
  "amenities": ["WiFi", "Pool", "Beach Access"],
  "amenities_count": 3,
  "is_available": true,
  "created_at": "2025-12-07T03:00:00Z",
  "updated_at": "2025-12-07T03:00:00Z"
}
```

### Property Types

- `apartment` - Apartment
- `house` - House
- `villa` - Villa
- `condo` - Condo

## 🚧 Future Enhancements

- [ ] User authentication and authorization
- [ ] Booking system integration
- [ ] Image upload for properties
- [ ] Reviews and ratings
- [ ] Payment integration
- [ ] Advanced search with Elasticsearch
- [ ] Caching with Redis
- [ ] Rate limiting
- [ ] Email notifications
- [ ] Admin dashboard

## 🐛 Troubleshooting

### Import Error: 'premissions'

**Error:**
```
ImportError: cannot import name 'premissions' from 'rest_framework'
```

**Solution:** Fix typo in `urls.py`:
```python
# Wrong
from rest_framework import premissions

# Correct
from rest_framework import permissions
```

### Migration Issues

```bash
# Reset migrations (development only)
rm db.sqlite3
rm hotel_management/migrations/0*.py
python manage.py makemigrations
python manage.py migrate
```

### Server Won't Start

```bash
# Check if port 8000 is in use
lsof -i :8000

# Use different port
python manage.py runserver 8080
```

## 📄 License

This project is licensed under the MIT License.


## 🙏 Acknowledgments

- Django REST Framework documentation
- drf-yasg for excellent API documentation
- The Django community

## 📞 Support

For issues, questions, or contributions, please open an issue on GitHub or reach out via LinkedIn.

---

**Happy Coding! 🚀**
