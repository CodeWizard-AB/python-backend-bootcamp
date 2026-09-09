# 🏗️ Project Building

> **CodeForge: Python Backend Engineering Bootcamp — Module 5 (Final Module)**
> 📦 12 Classes | ⏱️ 3 Hours per Class | 🎯 Capstone Module

This is where everything comes together. 🎉 You've learned **Git & GitHub**, **Python**, **PostgreSQL**, and **FastAPI** — now it's time to prove you can build real backend systems from scratch. In this module, you won't just learn new topics — you'll **build actual projects**, step by step, class by class, until you have a portfolio-ready backend application by the end.

> 💡 **Don't worry about "what to build" — that confusion ends here.** This module gives you a clear, guided project path so you always know exactly what to work on each class.

---

## 🎯 What You'll Achieve

By the end of this module, you'll have:

- ✅ Built 3 progressively harder backend projects
- ✅ Applied Python, PostgreSQL, and FastAPI together in real applications
- ✅ Implemented authentication, relationships, and clean architecture
- ✅ Deployed a working project that's live on the internet
- ✅ A polished GitHub portfolio with real, working backend projects
- ✅ The confidence to design and build your _own_ backend ideas after the bootcamp

---

## 🗂️ The Project Path (Big Picture)

Instead of one giant confusing project, we build **three projects of increasing difficulty** — each one teaches you something new, and each one becomes a portfolio piece.

```text
🟢 Project 1: Task Manager API        (Classes 1–4)   → Core CRUD + Auth
🟡 Project 2: Blog & Comments API     (Classes 5–8)   → Relationships + Roles
🔴 Project 3: Mini E-Commerce API     (Classes 9–12)  → Full Capstone + Deployment
```

> 📌 Each project is fully guided — you'll never be stuck wondering "what do I build next?"

---

## 📅 Course Outline

### 🟢 PROJECT 1 — Task Manager API

> _A simple, focused project to lock in your CRUD + Auth fundamentals._

### Class 01 — Planning & Project Setup

- Understanding the Project Requirements
- Identifying Core Features (Tasks, Users)
- Designing the Database Schema
- Setting Up the FastAPI Project Structure
- Setting Up PostgreSQL Database
- Creating Your GitHub Repository
- Writing Your First `README.md` for the Project
- Committing Initial Project Setup

### Class 02 — Building the Task Model & Database

- Designing the `Task` Table
- Creating SQLAlchemy Models
- Connecting FastAPI to PostgreSQL
- Creating Database Tables
- Writing Pydantic Schemas for Tasks
- Testing Database Connection

### Class 03 — Task CRUD API

- Creating a Task (`POST /tasks`)
- Listing All Tasks (`GET /tasks`)
- Getting a Single Task (`GET /tasks/{id}`)
- Updating a Task (`PUT /tasks/{id}`)
- Deleting a Task (`DELETE /tasks/{id}`)
- Testing All Endpoints with Swagger UI

### Class 04 — Adding User Authentication

- Designing the `User` Table
- User Registration Endpoint
- Password Hashing
- Login Endpoint & JWT Tokens
- Protecting Task Routes with Authentication
- Linking Tasks to Logged-In Users
- 🎉 **Project 1 Complete — Push to GitHub!**

---

### 🟡 PROJECT 2 — Blog & Comments API

> _A more realistic project with relationships between multiple tables and user roles._

### Class 05 — Planning the Blog API

- Understanding the Project Requirements
- Identifying Entities (Users, Posts, Comments)
- Designing Table Relationships
- Planning API Endpoints
- Setting Up a Fresh Project Structure
- Creating the GitHub Repository

### Class 06 — Users, Posts & Relationships

- Building the `User` and `Post` Models
- One-to-Many Relationship (User → Posts)
- Foreign Keys in SQLAlchemy
- Post CRUD Endpoints
- Filtering Posts by Author

### Class 07 — Comments & Nested Data

- Building the `Comment` Model
- One-to-Many Relationship (Post → Comments)
- Creating & Listing Comments
- Returning Nested Data (Post with Comments)
- Deleting Comments (Author-Only Permission)

### Class 08 — Roles, Permissions & Clean Structure

- Adding User Roles (Admin vs Regular User)
- Role-Based Route Protection
- Refactoring into Routers, Services & Schemas
- Error Handling Improvements
- Writing Basic Tests with `TestClient`
- 🎉 **Project 2 Complete — Push to GitHub!**

---

### 🔴 PROJECT 3 — Mini E-Commerce API (Capstone)

> _Your final capstone project — the one that goes on your resume and portfolio._

### Class 09 — Capstone Planning & Database Design

- Understanding Capstone Requirements
- Identifying Entities (Users, Products, Orders, Order Items, Categories)
- Designing a Normalized Database Schema
- Planning One-to-Many & Many-to-Many Relationships
- Sketching Out All API Endpoints
- Setting Up the Capstone Repository

### Class 10 — Core Models & Product Catalog

- Building `Category` & `Product` Models
- Product CRUD Endpoints
- Filtering, Searching & Pagination for Products
- Image/Field Validation with Pydantic
- Seeding Sample Data

### Class 11 — Orders, Cart Logic & Authentication

- Building the `Order` & `OrderItem` Models
- Linking Orders to Users & Products
- Creating an Order (Checkout Flow)
- Calculating Order Totals
- Full JWT Authentication Integration
- Admin-Only Product Management Routes

### Class 12 — Testing, Deployment & Final Polish

- Writing Automated Tests for Key Endpoints
- Environment Variables & `.env` Configuration
- Preparing for Deployment (Uvicorn/Gunicorn)
- Deploying Your API (Render / Railway / VPS)
- Final README, API Documentation & Project Presentation
- 🎉🎉 **Capstone Complete — Bootcamp Finished!**

---

## 🗺️ Complete Project Building Roadmap

```text
🟢 Project 1: Task Manager API
│
├── Class 1 → Planning & Setup
├── Class 2 → Models & Database
├── Class 3 → CRUD Endpoints
└── Class 4 → Authentication
        │
        ▼
🟡 Project 2: Blog & Comments API
│
├── Class 5 → Planning & Relationships Design
├── Class 6 → Users, Posts & Relationships
├── Class 7 → Comments & Nested Data
└── Class 8 → Roles, Permissions & Clean Structure
        │
        ▼
🔴 Project 3: Mini E-Commerce API (Capstone)
│
├── Class 9  → Database Design
├── Class 10 → Product Catalog
├── Class 11 → Orders & Auth
└── Class 12 → Testing, Deployment & Launch 🚀
```

---

## 🧠 Skills Applied From Previous Modules

| Skill        | Where You'll Use It                                   |
| ------------ | ----------------------------------------------------- |
| Git & GitHub | Every class — commits, branches, PRs for each feature |
| Python       | Writing all business logic, classes, and utilities    |
| PostgreSQL   | Designing schemas, relationships, and queries         |
| FastAPI      | Building every API endpoint across all 3 projects     |

---

## ✅ Module Checklist

- [ ] I completed Project 1: Task Manager API
- [ ] I completed Project 2: Blog & Comments API
- [ ] I completed Project 3: Mini E-Commerce API (Capstone)
- [ ] I used Git & GitHub properly throughout (commits, branches, PRs)
- [ ] I deployed at least one project live
- [ ] I wrote a clean `README.md` for each project
- [ ] I can explain my project's architecture in an interview

---

## 🎓 Final Words

You started this bootcamp not knowing how to save code with Git. You're finishing it having **designed databases, built secure APIs, and deployed a real e-commerce backend.** That's not a small achievement — that's the foundation of a real backend engineering career. 💪

🎉 **Welcome to backend engineering, CodeForge graduate!** 🚀
