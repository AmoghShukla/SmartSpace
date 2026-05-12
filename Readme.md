# SmartSpace : Resource Booking & Workspace Management System

**SmartSpace** is a scalable, backend-driven workspace and resource management platform inspired by modern coworking ecosystems like WeWork.
It is designed to streamline the **entire lifecycle of workspace operations** — from resource onboarding and availability management to booking workflows, payment handling, scheduling, and operational tracking.

Traditional workspace management often relies on spreadsheets, disconnected tools, and manual coordination, leading to booking conflicts, inefficient utilization, and poor operational visibility.
SmartSpace solves this by introducing a **centralized booking engine**, structured resource allocation logic, and a modular backend architecture built for scalability, maintainability, and real-world operational constraints.

This is not just a CRUD application — it is a **system-oriented workspace infrastructure platform**, engineered using backend design principles, layered architecture, and business-rule-driven workflows.

---

# Core Highlights

* **Resource Booking Engine**
  Book workspaces, meeting rooms, desks, cabins, and shared resources with conflict prevention.

* **Real-Time Availability Management**
  Dynamically tracks resource occupancy and booking status.

* **Conflict-Free Scheduling System**
  Prevents overlapping bookings and invalid time-slot allocations.

* **Workspace & Resource Management**
  Manage different workspace types, capacities, pricing, and availability.

* **User & Role Management**
  Supports administrators, workspace managers, and end users.

* **Payment Workflow Support**
  Designed to integrate booking payments, transaction tracking, and billing workflows.

* **Modular Layered Architecture**
  Structured separation between routers, services, repositories, schemas, and database layers.

* **Scalable Backend Design**
  Built with modern backend engineering practices using FastAPI and PostgreSQL.

---

# System Design Philosophy

SmartSpace is built around **real-world workspace management constraints**, not just database operations.

Typical booking systems focus only on:

* Creating reservations
* Managing users
* Storing booking data

SmartSpace goes further by handling:

* **Scheduling validation**
* **Resource allocation logic**
* **Concurrency-safe booking workflows**
* **Availability enforcement**
* **Operational scalability**
* **Clean architecture principles**

The platform is engineered to simulate how real coworking and office management systems function in production environments.

---

# Tech Stack

| Category           | Technologies               |
| ------------------ | -------------------------- |
| Backend Framework  | FastAPI                    |
| Database           | PostgreSQL                 |
| ORM                | SQLAlchemy                 |
| Database Migration | Alembic                    |
| Validation         | Pydantic                   |
| Authentication     | JWT (Planned / Extendable) |
| API Testing        | Postman                    |
| Package Management | Poetry / pip               |
| Language           | Python                     |

---

# Project Structure

```bash
SmartSpace/
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── src/
│   ├── core/              # Application configuration & constants
│   ├── database/          # DB connection & session management
│   ├── dependencies/      # Dependency injection utilities
│   ├── exceptions/        # Custom exception handling
│   ├── logs/              # Application logs
│   ├── models/            # SQLAlchemy ORM models
│   ├── repository/        # Database access layer
│   ├── router/            # FastAPI route handlers
│   ├── schema/            # Pydantic request/response schemas
│   ├── service/           # Core business logic layer
│   └── utils/             # Helper utilities
│
├── .env
├── alembic.ini
├── main.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

---

# Core Modules

| Module                | Description                                               |
| --------------------- | --------------------------------------------------------- |
| User Management       | Handles authentication, authorization, and user workflows |
| Workspace Management  | Manages rooms, desks, cabins, and shared resources        |
| Booking Engine        | Handles booking creation, scheduling, and validation      |
| Availability System   | Tracks real-time workspace availability                   |
| Payment Module        | Manages booking payments and transaction workflows        |
| Admin Dashboard Logic | Controls workspace operations and management              |
| Notification System   | Planned support for alerts and reminders                  |

---

# Business Rules Enforced

* A workspace/resource **cannot be double-booked** for overlapping time slots
* Booking requests must respect **resource availability constraints**
* Users can only access actions allowed by their roles
* Resource occupancy updates dynamically after successful bookings
* Payment validation can be enforced before booking confirmation
* Booking cancellations and modifications maintain scheduling consistency

---

# Booking Workflow (Conceptual)

The booking engine follows the following workflow:

1. User selects a workspace/resource
2. System checks:

   * Availability
   * Time-slot conflicts
   * Resource constraints
3. Booking request is validated
4. Payment workflow is triggered (if applicable)
5. Booking is confirmed
6. Resource occupancy is updated dynamically
7. Booking details are stored and returned to the user

---

# Features

* User registration & authentication
* Workspace/resource management
* Real-time booking system
* Conflict-free scheduling
* Availability tracking
* Booking history management
* Role-based access control
* Payment integration support
* RESTful API architecture
* Structured exception handling
* Scalable layered backend architecture

---

# API Architecture

SmartSpace follows a **layered backend architecture**:

```text
Client Request
      ↓
FastAPI Router Layer
      ↓
Service Layer (Business Logic)
      ↓
Repository Layer (Database Access)
      ↓
PostgreSQL Database
```

This architecture ensures:

* Maintainability
* Scalability
* Separation of concerns
* Cleaner testing workflows
* Easier feature expansion

---

# Setup & Installation

## 1. Clone the Repository

```bash
git clone https://github.com/AmoghShukla/SmartSpace.git
cd SmartSpace
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

---

## 3. Install Dependencies

### Using pip

```bash
pip install -r requirements.txt
```

### Using Poetry

```bash
poetry install
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/smartspace
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 5. Run Database Migrations

```bash
alembic upgrade head
```

---

## 6. Run the Application

```bash
uvicorn main:app --reload
```

---

# Example Workflow

1. Admin creates workspace resources
2. Users register/login
3. User checks workspace availability
4. User books a resource
5. System validates booking conflicts
6. Payment is processed (optional/integrated)
7. Booking confirmation is generated
8. Admin monitors bookings and occupancy

---

# Future Enhancements

* JWT-based authentication & refresh tokens
* Razorpay / Stripe payment integration
* Real-time booking updates using WebSockets
* Workspace analytics dashboard
* Booking recommendation engine
* Calendar integration (Google Calendar / Outlook)
* QR-based workspace check-in system
* Email & push notifications
* AI-based occupancy prediction
* Multi-branch workspace management

---

# Why SmartSpace?

SmartSpace is not just a workspace booking API.

It is an attempt to engineer a backend system that reflects how real coworking ecosystems operate — balancing:

* Scalability
* Scheduling accuracy
* Operational efficiency
* Maintainability
* Clean backend architecture

The project demonstrates:

* Backend system design
* API engineering
* Database modeling
* Business-rule implementation
* Scalable architecture patterns

---

# Contributing

1. Fork the repository
2. Create a feature branch:

```bash
git checkout -b feature/your-feature
```

3. Commit your changes:

```bash
git commit -m "Add your feature"
```

4. Push to GitHub:

```bash
git push origin feature/your-feature
```

5. Open a Pull Request

---

# License

This project is open source and available under the **MIT License**.

---

# Final Note

SmartSpace isn’t just about booking workspaces —
it’s about engineering a system that can efficiently manage shared infrastructure at scale.

From scheduling logic and resource allocation to modular architecture and backend scalability, the project is designed to reflect real-world engineering practices used in modern workspace management platforms.
