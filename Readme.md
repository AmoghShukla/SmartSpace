# Project

SmartSpace : Workspace Booking & Resource Management API

## Installation

Use the package manager [poetry](https://https://python-poetry.org/) to install Project.

```bash
poetry install
```

## Usage

```python
poetry run uvicorn main:app --reload
```

## About the Project



a) Overview
Built a backend system for managing co-working spaces where users can:

    -Register and log in
    -Book Meeting Rooms, Auditoriums
    -Managed availability
    -Handled approvals (admin flow)
    -Tracked usage and limits

b) Roles Based Responsibilities

1) Admin
```
    -Manages workspace resources
    -Approves/rejects bookings
    -Views analytics
```

2) User
```
    -Books Meeting Rooms, Auditoriums
    -Views own bookings
    -Cancels bookings
```
3)Workspace Manager
```
    -Creates Resources 
    -Manages Meeting Rooms, Auditoriums
    -Views assigned Workspace bookings
    -Approves Cancels bookings
```
c) User Management
```
    -Register
    -Login
    -Get profile (protected)
    -Role-based access
```
Uses:
```
    -Password hashing
    -JWT
    -Dependency Injection for current user
```

d) Users can:
```
    -Book a resource for a time slot
    -Cancel booking
Constraints:

    No overlapping bookings
    Capacity rules enforced
    Booking must be within working hours
```

e) Admin can:
```
    -Approve/reject bookings (for rooms)

Constraints:

    -Max booking hours per day/week
    System should:
        -Prevent overbooking

List bookings with:

    -Date filters
    -Status filters
    -Pagination
```
## Env Setup(Reference)
```python
DB_USER='DB_USER'
DB_PORT=DB_PORT
DB_NAME='DB_NAME'
DB_PASSWORD='DB_PASSWORD'
DB_HOST='DB_HOST'

ADMIN_NAME='ADMIN_NAME'
ADMIN_PASSWORD="ADMIN_PASSWORD"
ADMIN_CONTACT_NO='ADMIN_CONTACT_NO'
ADMIN_EMAIL_ID='ADMIN_EMAIL_ID'

SECRET_KEY="SECRET_KEY"
ALGORITHM="ALGORITHM"
ACCESS_TOKEN_EXPIRE_MINUTES=ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS=REFRESH_TOKEN_EXPIRE_DAYS
```