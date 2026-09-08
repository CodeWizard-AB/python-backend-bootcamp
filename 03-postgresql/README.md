# 🐘 PostgreSQL

> **CodeForge: Python Backend Engineering Bootcamp — PostgreSQL Module**

## Class 01 — PostgreSQL Introduction

- What is PostgreSQL?
- PostgreSQL Features
- PostgreSQL vs SQL
- PostgreSQL vs MySQL
- PostgreSQL Architecture
- PostgreSQL Database
- PostgreSQL Server
- PostgreSQL Client
- Installing PostgreSQL
- Connecting to PostgreSQL
- PostgreSQL Command Line
- `psql`
- PostgreSQL GUI Tools
- Creating a Database
- Listing Databases
- Connecting to a Database
- Dropping a Database

---

## Class 02 — PostgreSQL Tables & Data Types

### Tables

- What is a Table?
- Creating Tables
- Table Names
- Column Names
- Column Data Types
- Viewing Tables
- Altering Tables
- Renaming Tables
- Dropping Tables

### Data Types

- Boolean
- Character Types
- `CHAR`
- `VARCHAR`
- `TEXT`
- Numeric Types
- `SMALLINT`
- `INTEGER`
- `BIGINT`
- `DECIMAL`
- `NUMERIC`
- Floating-Point Types
- `REAL`
- `DOUBLE PRECISION`
- Date and Time Types
- `DATE`
- `TIME`
- `TIMESTAMP`
- `TIMESTAMPTZ`
- `INTERVAL`
- UUID
- JSON
- JSONB
- Arrays

---

## Class 03 — PostgreSQL CRUD & Basic Queries

### INSERT

- `INSERT`
- Insert a Single Row
- Insert Multiple Rows
- Insert Specific Columns
- `INSERT ... RETURNING`

### SELECT

- `SELECT`
- Selecting Columns
- Selecting All Columns
- Column Aliases
- Expressions
- `DISTINCT`

### UPDATE

- `UPDATE`
- Updating Columns
- Updating Multiple Rows
- `UPDATE ... RETURNING`

### DELETE

- `DELETE`
- Deleting Rows
- `DELETE ... RETURNING`

---

## Class 04 — PostgreSQL Filtering & Sorting

### Filtering

- `WHERE`
- Comparison Operators
- `=`
- `<>`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

### Logical Operators

- `AND`
- `OR`
- `NOT`

### Special Operators

- `IN`
- `NOT IN`
- `BETWEEN`
- `NOT BETWEEN`
- `IS NULL`
- `IS NOT NULL`

### Pattern Matching

- `LIKE`
- `ILIKE`
- Wildcards
- `%`
- `_`

### Sorting

- `ORDER BY`
- Ascending Order
- Descending Order
- Multiple Column Sorting
- `NULLS FIRST`
- `NULLS LAST`

### Limiting Results

- `LIMIT`
- `OFFSET`
- Pagination Basics

---

## Class 05 — PostgreSQL Constraints

### Constraints

- What are Constraints?
- `NOT NULL`
- `UNIQUE`
- `PRIMARY KEY`
- `FOREIGN KEY`
- `CHECK`
- `DEFAULT`

### Primary Keys

- Single-Column Primary Key
- Composite Primary Key
- UUID Primary Keys
- Identity Columns
- Generated Values

### Foreign Keys

- Foreign Key Relationships
- Referencing Tables
- `ON DELETE`
- `ON UPDATE`
- `CASCADE`
- `SET NULL`
- `RESTRICT`
- `NO ACTION`

### Constraint Management

- Adding Constraints
- Removing Constraints
- Naming Constraints

---

## Class 06 — PostgreSQL Functions & Expressions

### Built-in Functions

- String Functions
- Numeric Functions
- Date & Time Functions
- Conversion Functions
- Conditional Functions

### String Functions

- `LOWER()`
- `UPPER()`
- `LENGTH()`
- `TRIM()`
- `CONCAT()`
- `SUBSTRING()`
- `REPLACE()`

### Numeric Functions

- `ROUND()`
- `CEIL()`
- `FLOOR()`
- `ABS()`
- `POWER()`

### Conditional Expressions

- `CASE`
- `COALESCE()`
- `NULLIF()`

### Date & Time

- `CURRENT_DATE`
- `CURRENT_TIME`
- `CURRENT_TIMESTAMP`
- Date Arithmetic
- Date Extraction
- `EXTRACT()`

---

## Class 07 — PostgreSQL Aggregation & GROUP BY

### Aggregate Functions

- `COUNT()`
- `SUM()`
- `AVG()`
- `MIN()`
- `MAX()`

### GROUP BY

- `GROUP BY`
- Grouping by One Column
- Grouping by Multiple Columns
- Aggregating Groups

### HAVING

- `HAVING`
- `WHERE` vs `HAVING`

### Practical Aggregation

- Counting Records
- Calculating Totals
- Calculating Averages
- Finding Minimum & Maximum Values
- Group-Based Reports

---

## Class 08 — PostgreSQL Joins

### Join Fundamentals

- What are Joins?
- Table Relationships
- Joining Multiple Tables

### Join Types

- `INNER JOIN`
- `LEFT JOIN`
- `RIGHT JOIN`
- `FULL OUTER JOIN`
- `CROSS JOIN`
- Self Join

### Join Conditions

- `ON`
- Joining with Primary Keys
- Joining with Foreign Keys
- Multiple Join Conditions

### Practical Queries

- One-to-One Relationships
- One-to-Many Relationships
- Many-to-Many Relationships
- Joining Three or More Tables

---

## Class 09 — PostgreSQL Advanced Queries

### Subqueries

- What is a Subquery?
- Subquery in `WHERE`
- Subquery in `SELECT`
- Subquery in `FROM`
- Correlated Subqueries

### Common Table Expressions

- `WITH`
- CTE
- Multiple CTEs
- Recursive CTEs

### Set Operations

- `UNION`
- `UNION ALL`
- `INTERSECT`
- `EXCEPT`

### Query Techniques

- Nested Queries
- Complex Filtering
- Combining Aggregation and Joins
- Query Composition

---

## Class 10 — PostgreSQL Views, Indexes & Sequences

### Views

- What is a View?
- Creating Views
- Querying Views
- Updating Views
- Dropping Views

### Materialized Views

- What is a Materialized View?
- Creating Materialized Views
- Refreshing Materialized Views
- Dropping Materialized Views

### Indexes

- What is an Index?
- Why Indexes Matter
- Creating Indexes
- Dropping Indexes
- Unique Indexes
- Composite Indexes
- Partial Indexes
- Expression Indexes

### Sequences

- What is a Sequence?
- Creating Sequences
- `nextval()`
- `currval()`
- Identity Columns

---

## Class 11 — PostgreSQL Transactions & Advanced Data

### Transactions

- What is a Transaction?
- `BEGIN`
- `COMMIT`
- `ROLLBACK`
- Transaction Atomicity
- Transaction Consistency
- Transaction Isolation
- Transaction Durability

### Transaction Control

- Savepoints
- `SAVEPOINT`
- `ROLLBACK TO`
- `RELEASE SAVEPOINT`

### JSON & JSONB

- JSON Data
- JSONB Data
- Creating JSON Data
- Querying JSON
- JSON Operators
- JSON Functions
- Updating JSON Data
- JSONB Indexing

### Arrays

- Creating Arrays
- Array Elements
- Array Operators
- Array Functions
- Querying Arrays

---

## Class 12 — PostgreSQL Database Design & Production Basics

### Database Design

- Database Design Fundamentals
- Entities
- Attributes
- Relationships
- Primary Keys
- Foreign Keys
- Normalization
- First Normal Form
- Second Normal Form
- Third Normal Form
- Denormalization

### Schema Design

- Schemas
- Creating Schemas
- Schema Organization
- Naming Conventions
- Database Structure

### Performance

- Query Performance
- `EXPLAIN`
- `EXPLAIN ANALYZE`
- Query Planning
- Index Optimization
- Common Query Performance Problems

### PostgreSQL Security

- Users
- Roles
- Creating Roles
- Role Permissions
- `GRANT`
- `REVOKE`
- Database Privileges
- Table Privileges
- Schema Privileges

### Backup & Maintenance

- Database Backup
- Database Restore
- `pg_dump`
- `pg_restore`
- PostgreSQL Maintenance
- `VACUUM`
- `ANALYZE`

### PostgreSQL Project Preparation

- Database Requirements
- Entity Identification
- Relationship Design
- Schema Design
- Table Creation
- Constraints
- Indexes
- Seed Data
- Complex Queries
- Database Testing
- Production-Ready Database Structure