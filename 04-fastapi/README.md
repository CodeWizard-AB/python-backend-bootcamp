# ⚡ FastAPI

> **CodeForge: Python Backend Engineering Bootcamp — FastAPI Module**

## Class 01 — FastAPI Introduction & First API

- What is FastAPI?
- Why FastAPI?
- FastAPI Features
- FastAPI vs Flask
- FastAPI vs Django
- ASGI
- Uvicorn
- Installing FastAPI
- Creating a FastAPI Project
- Running a FastAPI Application
- First FastAPI Application
- `FastAPI()`
- Path Operations
- `@app.get()`
- `@app.post()`
- `@app.put()`
- `@app.delete()`
- Running with Uvicorn
- Development Server
- Automatic Reload
- Interactive API Documentation
- Swagger UI
- ReDoc
- OpenAPI

---

## Class 02 — Path Operations & Parameters

### Path Operations

- Path Operation Functions
- HTTP Methods
- GET
- POST
- PUT
- PATCH
- DELETE
- Path Operation Decorators
- Path Operation Naming
- Operation IDs
- Tags

### Path Parameters

- Path Parameters
- Declaring Path Parameters
- Typed Path Parameters
- Path Parameter Validation
- Path Parameter Documentation

### Query Parameters

- Query Parameters
- Optional Query Parameters
- Default Values
- Required Query Parameters
- Boolean Query Parameters
- Multiple Query Parameters
- Query Parameter Validation

---

## Class 03 — Request Body & Pydantic Models

### Request Body

- Request Body
- JSON Request Body
- POST Request Body
- PUT Request Body
- PATCH Request Body

### Pydantic

- Pydantic Models
- `BaseModel`
- Model Fields
- Field Types
- Optional Fields
- Default Values
- Nested Models
- List Models
- Dictionary Models
- Model Validation

### Request Data

- Path Parameters + Request Body
- Query Parameters + Request Body
- Multiple Body Parameters
- Body Field Metadata

---

## Class 04 — Data Validation & Response Models

### Validation

- Automatic Data Validation
- Type Validation
- Required Fields
- Default Values
- `Field()`
- Minimum Values
- Maximum Values
- String Length
- Regular Expressions
- Numeric Constraints
- List Constraints

### Response Models

- Response Models
- `response_model`
- Response Validation
- Response Serialization
- Filtering Response Data
- Nested Response Models
- List Response Models

### Status Codes

- HTTP Status Codes
- `status_code`
- `200 OK`
- `201 Created`
- `204 No Content`
- `400 Bad Request`
- `404 Not Found`
- `422 Unprocessable Entity`

---

## Class 05 — Error Handling & HTTP Exceptions

### HTTP Exceptions

- `HTTPException`
- Raising HTTP Exceptions
- Custom Status Codes
- Custom Error Messages
- Headers in Exceptions

### Error Handling

- Request Validation Errors
- Response Validation Errors
- Exception Handlers
- Custom Exception Handlers
- Handling Application Errors
- Handling Database Errors

### Headers

- Request Headers
- Header Parameters
- Optional Headers
- Multiple Headers
- Response Headers

### Cookies

- Cookie Parameters
- Reading Cookies
- Setting Cookies
- Deleting Cookies

---

## Class 06 — Dependencies & Application Structure

### Dependencies

- Dependency Injection
- `Depends()`
- Dependency Functions
- Dependency Parameters
- Dependency Chains
- Reusable Dependencies
- Class-Based Dependencies
- Dependencies with `yield`

### Global Dependencies

- Router Dependencies
- Application-Level Dependencies
- Dependency Overrides

### Project Structure

- FastAPI Project Structure
- Application Entry Point
- Routers
- Services
- Schemas
- Models
- Dependencies
- Configuration
- Utilities

### APIRouter

- `APIRouter`
- Creating Routers
- Including Routers
- Router Prefixes
- Router Tags
- Router Dependencies

---

## Class 07 — Security & Authentication

### Security Fundamentals

- Authentication
- Authorization
- Authentication vs Authorization
- Password Security
- Security Dependencies

### OAuth2

- OAuth2
- OAuth2 Password Flow
- `OAuth2PasswordBearer`
- Login Endpoint
- Access Tokens
- Bearer Tokens

### JWT

- JSON Web Tokens
- JWT Structure
- JWT Payload
- JWT Signature
- Creating JWT Tokens
- Verifying JWT Tokens
- Token Expiration
- Protected Routes

### Passwords

- Password Hashing
- Password Verification
- Secure Password Storage
- Login Flow
- Current User
- Authenticated User

---

## Class 08 — Middleware, CORS & Background Tasks

### Middleware

- What is Middleware?
- FastAPI Middleware
- HTTP Middleware
- Request Processing
- Response Processing
- Custom Middleware

### CORS

- Cross-Origin Resource Sharing
- CORS Configuration
- `CORSMiddleware`
- Allowed Origins
- Allowed Methods
- Allowed Headers
- Credentials

### Background Tasks

- Background Tasks
- `BackgroundTasks`
- Adding Background Tasks
- Sending Emails
- Processing Tasks
- Post-Response Tasks

### Application Events

- Startup Events
- Shutdown Events
- Lifespan Events
- Application Lifecycle

---

## Class 09 — Database Integration

### Database Fundamentals

- FastAPI + Database
- Database Connection
- Database Sessions
- Database Dependencies
- CRUD Operations

### SQLAlchemy

- SQLAlchemy
- SQLAlchemy Models
- Database Engine
- Sessions
- ORM
- Queries
- Relationships

### PostgreSQL Integration

- FastAPI + PostgreSQL
- PostgreSQL Connection
- Environment-Based Database Configuration
- Database Models
- Database Tables
- CRUD with PostgreSQL

### Database Operations

- Create Records
- Read Records
- Update Records
- Delete Records
- Transactions
- Rollback
- Database Error Handling

---

## Class 10 — Advanced API Development

### Async Programming

- `async`
- `await`
- Async Path Operations
- Async Dependencies
- Async Database Operations
- Synchronous vs Asynchronous Code

### File Handling

- File Uploads
- `UploadFile`
- `File()`
- Multiple File Uploads
- File Metadata
- File Validation

### Forms

- Form Data
- `Form()`
- Form Parameters
- Combining Forms and Files

### Static Files

- Static Files
- `StaticFiles`
- Serving Static Content

### Streaming

- Streaming Responses
- `StreamingResponse`
- Large Responses

---

## Class 11 — Advanced FastAPI Features & Testing

### API Documentation

- OpenAPI
- Automatic Documentation
- Swagger UI
- ReDoc
- API Metadata
- Tags
- Examples
- Documentation Customization

### Advanced Responses

- JSON Responses
- HTML Responses
- Redirect Responses
- File Responses
- Streaming Responses
- Custom Response Classes

### Testing

- API Testing
- `TestClient`
- Testing GET Endpoints
- Testing POST Endpoints
- Testing PUT Endpoints
- Testing DELETE Endpoints
- Testing Authentication
- Testing Dependencies
- Test Fixtures
- Automated Tests

### Configuration

- Environment Variables
- Configuration Management
- `.env`
- Application Settings
- Secrets Management

---

## Class 12 — Production-Ready FastAPI

### API Architecture

- Layered Architecture
- Router Layer
- Schema Layer
- Service Layer
- Repository Layer
- Model Layer
- Dependency Layer
- Configuration Layer

### API Design

- REST API Principles
- Resource-Based URLs
- HTTP Methods
- Status Codes
- Pagination
- Filtering
- Sorting
- Searching
- API Versioning

### Production

- Environment Configuration
- Development Environment
- Testing Environment
- Production Environment
- Logging
- Error Handling
- Security
- CORS
- Database Connection Pooling

### Deployment

- Uvicorn
- Gunicorn
- ASGI
- Reverse Proxy
- Docker
- Environment Variables
- Production Server
- Health Check Endpoint

### FastAPI Project Preparation

- Project Requirements
- API Architecture
- Database Integration
- Authentication
- Authorization
- CRUD APIs
- Validation
- Error Handling
- API Documentation
- Testing
- Environment Configuration
- Production Configuration
- Deployment