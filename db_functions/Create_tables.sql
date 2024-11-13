--create database schema
CREATE schema SALES_DB;

--create customers table
CREATE TABLE CUSTOMERS (
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
CREATE TABLE PRODUCTS(
  product_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  description TEXT NULL,
  price DECIMAL(10,2) NOT NULL,
  stock_quantity INT NOT NULL
);


--sales order table
CREATE TABLE SALES_ORDERS(
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date Timestamp NOT NULL,
  status VARCHAR(20) NOT NULL, 
  total_amount DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(customer_id)
);

--order details table
CREATE TABLE ORDER_DETAILS (
  order_detail_id INT PRIMARY KEY,
  order_id INT,
  product_id INT,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  total_price DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES SALES_ORDERS(order_id), 
  FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id) 
);

CREATE TABLE PAYMENTS(
  payment_id SERIAL PRIMARY KEY,
  order_id INT,
  payment_date Timestamp NOT NULL,
  payment_amount DECIMAL(10,2) NOT NULL,
  payment_method VARCHAR(20) NOT NULL,
  payment_status VARCHAR(20) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES SALES_ORDERS(order_id)
);

