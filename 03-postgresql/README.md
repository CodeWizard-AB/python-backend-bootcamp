# 🐘 PostgreSQL

> **CodeForge: Python Backend Engineering Bootcamp — Module 3**
> 📦 12 Classes | ⏱️ 3 Hours per Class | 🎯 Beginner Friendly

You've learned Python — now it's time to give your applications a memory. **PostgreSQL** is one of the most powerful and widely-used databases in the world, and by the end of this module you'll be able to design, build, and query real production-grade databases. Every backend needs a database, and this is the one we'll master. 🗄️🚀

---

## 🎯 What You'll Learn

By the end of this module, you'll be able to:

- ✅ Install, connect to, and navigate PostgreSQL confidently
- ✅ Design tables with the right data types and constraints
- ✅ Perform full CRUD operations (Create, Read, Update, Delete)
- ✅ Filter, sort, and paginate query results
- ✅ Join multiple tables together correctly
- ✅ Write subqueries, CTEs, and advanced queries
- ✅ Use views, indexes, and sequences for performance
- ✅ Manage transactions safely
- ✅ Design a normalized, production-ready database from scratch

---

## 📅 Course Outline

### Class 01 — PostgreSQL Introduction 🐘

> 💡 _Get PostgreSQL installed and take your first steps inside it._

- What is PostgreSQL?
- Key PostgreSQL Features
- PostgreSQL vs SQL
- PostgreSQL vs MySQL
- Understanding PostgreSQL Architecture
- PostgreSQL Database, Server & Client Explained
- Installing PostgreSQL
- Connecting to PostgreSQL
- Using the Command Line (`psql`)
- Popular PostgreSQL GUI Tools
- Creating a Database
- Listing Databases
- Connecting to a Database
- Dropping a Database

---

### Class 02 — Tables & Data Types 📋

> 💡 _Learn how to structure your data correctly from day one._

**Tables**

- What is a Table?
- Creating Tables
- Naming Tables & Columns
- Choosing Column Data Types
- Viewing Tables
- Altering Tables
- Renaming Tables
- Dropping Tables

**Data Types**

- Boolean
- Character Types — `CHAR`, `VARCHAR`, `TEXT`
- Numeric Types — `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `NUMERIC`
- Floating-Point Types — `REAL`, `DOUBLE PRECISION`
- Date & Time Types — `DATE`, `TIME`, `TIMESTAMP`, `TIMESTAMPTZ`, `INTERVAL`
- UUID
- JSON & JSONB
- Arrays

---

### Class 03 — CRUD & Basic Queries ✍️

> 💡 _The four operations every database interaction is built from._

**INSERT**

- Inserting a Single Row
- Inserting Multiple Rows
- Inserting Specific Columns
- `INSERT ... RETURNING`

**SELECT**

- Selecting Columns
- Selecting All Columns
- Column Aliases
- Expressions in `SELECT`
- `DISTINCT`

**UPDATE**

- Updating Columns
- Updating Multiple Rows
- `UPDATE ... RETURNING`

**DELETE**

- Deleting Rows
- `DELETE ... RETURNING`

---

### Class 04 — Filtering & Sorting 🔍

> 💡 _Find exactly the data you need, in the order you want it._

**Filtering with `WHERE`**

- Comparison Operators — `=`, `<>`, `!=`, `>`, `<`, `>=`, `<=`
- Logical Operators — `AND`, `OR`, `NOT`
- Special Operators — `IN`, `NOT IN`, `BETWEEN`, `NOT BETWEEN`, `IS NULL`, `IS NOT NULL`
- Pattern Matching — `LIKE`, `ILIKE`, Wildcards (`%`, `_`)

**Sorting**

- `ORDER BY` — Ascending & Descending
- Multiple Column Sorting
- `NULLS FIRST` / `NULLS LAST`

**Limiting Results**

- `LIMIT`
- `OFFSET`
- Pagination Basics

---

### Class 05 — Constraints 🔒

> 💡 _Protect your data's integrity before problems happen._

**Core Constraints**

- `NOT NULL`
- `UNIQUE`
- `PRIMARY KEY`
- `FOREIGN KEY`
- `CHECK`
- `DEFAULT`

**Primary Keys**

- Single-Column Primary Key
- Composite Primary Key
- UUID Primary Keys
- Identity Columns & Generated Values

**Foreign Keys**

- Understanding Foreign Key Relationships
- Referencing Other Tables
- `ON DELETE` / `ON UPDATE`
- `CASCADE`, `SET NULL`, `RESTRICT`, `NO ACTION`

**Managing Constraints**

- Adding Constraints
- Removing Constraints
- Naming Constraints

---

### Class 06 — Functions & Expressions 🧮

> 💡 _Let PostgreSQL do the calculations for you._

**String Functions**

- `LOWER()`, `UPPER()`, `LENGTH()`, `TRIM()`, `CONCAT()`, `SUBSTRING()`, `REPLACE()`

**Numeric Functions**

- `ROUND()`, `CEIL()`, `FLOOR()`, `ABS()`, `POWER()`

**Conditional Expressions**

- `CASE`
- `COALESCE()`
- `NULLIF()`

**Date & Time Functions**

- `CURRENT_DATE`, `CURRENT_TIME`, `CURRENT_TIMESTAMP`
- Date Arithmetic
- Date Extraction with `EXTRACT()`

---

### Class 07 — Aggregation & GROUP BY 📊

> 💡 _Summarize and analyze your data like a data analyst._

**Aggregate Functions**

- `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`

**Grouping Data**

- `GROUP BY` — Single & Multiple Columns
- Aggregating Groups

**Filtering Groups**

- `HAVING`
- `WHERE` vs `HAVING`

**Practical Aggregation**

- Counting Records
- Calculating Totals & Averages
- Finding Min & Max Values
- Building Group-Based Reports

---

### Class 08 — Joins 🔗

> 💡 _Connect data across multiple tables — the heart of relational databases._

**Join Fundamentals**

- What are Joins?
- Understanding Table Relationships
- Joining Multiple Tables

**Join Types**

- `INNER JOIN`
- `LEFT JOIN`
- `RIGHT JOIN`
- `FULL OUTER JOIN`
- `CROSS JOIN`
- Self Join

**Join Conditions**

- Using `ON`
- Joining with Primary & Foreign Keys
- Multiple Join Conditions

**Practical Relationships**

- One-to-One
- One-to-Many
- Many-to-Many
- Joining Three or More Tables

---

### Class 09 — Advanced Queries 🧠

> 💡 _Write queries within queries — like a database power user._

**Subqueries**

- Subquery in `WHERE`
- Subquery in `SELECT`
- Subquery in `FROM`
- Correlated Subqueries

**Common Table Expressions (CTEs)**

- `WITH` / CTE Basics
- Multiple CTEs
- Recursive CTEs

**Set Operations**

- `UNION` / `UNION ALL`
- `INTERSECT`
- `EXCEPT`

**Query Techniques**

- Nested Queries
- Complex Filtering
- Combining Aggregation & Joins
- Query Composition

---

### Class 10 — Views, Indexes & Sequences ⚡

> 💡 _Make your database faster and easier to work with._

**Views**

- Creating, Querying, Updating & Dropping Views

**Materialized Views**

- Creating Materialized Views
- Refreshing Materialized Views
- Dropping Materialized Views

**Indexes**

- Why Indexes Matter
- Creating & Dropping Indexes
- Unique, Composite, Partial & Expression Indexes

**Sequences**

- What is a Sequence?
- Creating Sequences
- `nextval()` / `currval()`
- Identity Columns

---

### Class 11 — Transactions & Advanced Data 💾

> 💡 _Keep your data safe and consistent, even when things go wrong._

**Transactions**

- `BEGIN`, `COMMIT`, `ROLLBACK`
- The ACID Properties — Atomicity, Consistency, Isolation, Durability

**Transaction Control**

- Savepoints
- `SAVEPOINT`, `ROLLBACK TO`, `RELEASE SAVEPOINT`

**JSON & JSONB**

- Creating & Querying JSON Data
- JSON Operators & Functions
- Updating JSON Data
- JSONB Indexing

**Arrays**

- Creating Arrays
- Array Elements & Operators
- Array Functions & Querying

---

### Class 12 — Database Design & Production Basics 🏭

> 💡 _Design databases the way real companies do — and prepare for your capstone project._

**Database Design**

- Entities, Attributes & Relationships
- Primary & Foreign Keys
- Normalization — 1NF, 2NF, 3NF
- Denormalization

**Schema Design**

- Creating & Organizing Schemas
- Naming Conventions
- Database Structure

**Performance**

- `EXPLAIN` / `EXPLAIN ANALYZE`
- Query Planning
- Index Optimization
- Common Performance Problems

**Security**

- Users & Roles
- `GRANT` / `REVOKE`
- Database, Table & Schema Privileges

**Backup & Maintenance**

- `pg_dump` / `pg_restore`
- `VACUUM` / `ANALYZE`

**Project Preparation**

- Identifying Requirements & Entities
- Relationship & Schema Design
- Table Creation, Constraints & Indexes
- Seed Data & Complex Queries
- Database Testing
- Building a Production-Ready Database

---

## 🗺️ Complete PostgreSQL Topic Map

```text
🐘 PostgreSQL Introduction
│
├── Installation & Connection
└── psql & GUI Tools
        │
        ▼
📋 Tables & Data Types
        │
        ▼
✍️ CRUD (Insert / Select / Update / Delete)
        │
        ▼
🔍 Filtering, Sorting & Pagination
        │
        ▼
🔒 Constraints (Primary Key / Foreign Key / Checks)
        │
        ▼
🧮 Functions & Expressions
        │
        ▼
📊 Aggregation & GROUP BY
        │
        ▼
🔗 Joins (Inner / Left / Right / Full)
        │
        ▼
🧠 Advanced Queries (Subqueries / CTEs / Set Ops)
        │
        ▼
⚡ Views, Indexes & Sequences
        │
        ▼
💾 Transactions & JSON/Array Data
        │
        ▼
🏭 Database Design & Production Basics
```

---

## ✅ Module Checklist

- [ ] I can install PostgreSQL and connect using `psql`
- [ ] I can create tables with correct data types and constraints
- [ ] I can perform full CRUD operations confidently
- [ ] I can filter, sort, and paginate results
- [ ] I can join two or more tables together
- [ ] I can write subqueries and CTEs
- [ ] I can use transactions safely
- [ ] I can design a normalized database from scratch

---

🎉 **Congratulations on completing the PostgreSQL module!** You now know how to store, organize, and query real data like a backend engineer. Next up: **FastAPI** — where we'll connect this database to a real web API! ⚡🚀
