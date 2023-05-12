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

```

**Response:**
```

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

```

### Customers 
**Request:**
```
GET "customers/"
```

**Response:**
```

```

### Subscriptions
**Request:**
```
GET "subscriptions/"
```

**Response:**
```

```
