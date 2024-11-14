--create database schema
CREATE schema SALES_DB;

--create customers table
CREATE TABLE sales_db.CUSTOMERS (
  customer_id SERIAL PRIMARY KEY, 
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NULL,
  phone VARCHAR(20) NULL,
  address VARCHAR(100) NULL,
  city VARCHAR(100) NULL, 
  state VARCHAR(50) NULL,
  postal_code VARCHAR(20) NULL
);


--create products table
CREATE TABLE sales_db.PRODUCTS(
  product_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  description TEXT NULL,
  price DECIMAL(10,2) NOT NULL,
  stock_quantity INT NOT NULL
);


--orders table
CREATE TABLE sales_db.ORDERS (
  order_id SERIAL PRIMARY KEY,
  order_date Timestamp NOT NULL
  product_id INT,
  customer_id INT,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  total_price DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (product_id) REFERENCES sales_db.PRODUCTS(product_id),
  FOREIGN KEY (customer_id) REFERENCES sales_db.CUSTOMERS(customer_id) 
);

