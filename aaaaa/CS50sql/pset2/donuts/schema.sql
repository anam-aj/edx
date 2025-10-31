CREATE TABLE ingredients (
    id INTEGER,
    name TEXT NOT NULL UNIQUE,
    rate NUMERIC NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE donuts (
    id INTEGER,
    name TEXT NOT NULL UNIQUE,
    gluten_free TEXT NOT NULL CHECK(gluten_free IN ('yes', 'no')),
    rate NUMERIC NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE orders (
    id INTEGER,
    customer_id INTEGER NOT NULL,
    order_date_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    FOREIGN KEY(customer_id) REFERENCES customers(id)
);

CREATE TABLE order_items (
    order_id INTEGER,
    donut_id INTEGER,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(donut_id) REFERENCES donuts(id)
);

CREATE TABLE customers (
    id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    PRIMARY KEY(id)
);
