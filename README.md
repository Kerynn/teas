# Tea Subscription
The goal of this project is to create a backend API service built with Python and Django that will be used by a frontend team to create a web application. The app will allow users to manage and view their tea subscriptions. This backend service will expose several endpoints for the frontend team to use that includes creating a new tea subscription, cancelling a subscription, and viewing all subscriptions (both currently active and cancelled).

## Getting Started
### Prerequisites
* Python 3.9.6
* Django 4.2.1

### Setup


## DB Schema

## Endpoints
All endpoints start with url: http://127.0.0.1:8000

### Teas 
**Create tea request:**
```
POST "teas/"
Content-Type: application/json
Accept: application/json

{
    "name": "Sunshine Spice",
    "description": "Sunny morning joy!",
    "temperature": 160,
    "brew_time": "25 minutes"
}
```

**Response:**
```
{
    "success": "Tea created successfully"
}
```

**Get all teas request:**
```
GET "teas/"
```

**Response:**
```
{
  "teas": [
      {
        "id": 1,
        "name": "Sunshine Spice",
        "description": "Sunny morning joy!",
        "temperature": 160,
        "brew_time": "25 minutes"
      },
      {...}
  ]
}
```

**Get tea details request:**
```
GET "teas/<tea_id>"
```

**Response:**
```
{
  "tea": 
      {
        "id": 1,
        "name": "Sunshine Spice",
        "description": "Sunny morning joy!",
        "temperature": 160,
        "brew_time": "25 minutes"
      }
}
```

**Delete tea request:**
```
DELETE "teas/<tea_id>"
```

**Response:**
```
  "success": "Tea deleted successfully"
```

### Customers 
**Request:**
```
POST "customers/"
Content-Type: application/json
Accept: application/json

{
    "first_name": "Kamee",
    "last_name": "Nev",
    "email": "kamnev@fakeemail.com",
    "address": "1234 Happy Ln"
}
```

**Response:**
```
{
    "success": "Customer created successfully"
}
```

### Subscriptions
**Create a subscription request:**
```
POST "subscriptions/"
Content-Type: application/json
Accept: application/json

{
    "customer": 2,
    "tea": 2,
    "title": "Morning Fog",
    "frequency": "monthly",
    "price": 28.50
}
```

**Response:**
```
{
    "success": "Subscription created successfully"
}
```

**Get all existing subscriptions request:**
```
GET "subscriptions/"
```

**Response:**
```
{
  "subscriptions": [
      {
        "id": 1,
        "title": "Sunshine Spice",
        "price": "24.24",
        "status": "Active",
        "frequency": "Annually",
        "tea": 1,
        "customer": 2
      },
      {...}
  ]
}
```

**Get subscriptions belonging to a customer request:**
``` 
GET "customers/<customer_id>/subscriptions"
```

**Response:**
```
{
  "subscriptions": [
      {
        "id": 1,
        "title": "Sunshine Spice",
        "price": "24.24",
        "status": "Active",
        "frequency": "Annually",
        "tea": 1,
        "customer": 2
      },
      {
        "id": 3,
        "title": "Morning Fog",
        "price": "28.50",
        "status": "Active",
        "frequency": "monthly",
        "tea": 2,
        "customer": 2
      }
  ]
}
```

**Update status of a subscription request:**
```
PATCH "subscriptions/<subscrption_id>"
Content-Type: application/json
Accept: application/json

{
  "status": "cancelled"
}
```

**Response:**
```
{
  "success": "Subscription status updated successfully"
}
```
