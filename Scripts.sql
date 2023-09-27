SELECT * FROM merged_data md limit 4;

-----.
----Calculate total sales amount per customer
   SELECT
    customer_id,
    name AS customer_name,
    CAST(SUM(quantity * price) AS DECIMAL(10, 3)) AS total_sales_amount
FROM merged_data
     
GROUP BY
    customer_id, name
ORDER BY
    customer_id;
   
  ==========================
  --Determine the average order quantity per product.
  ==========================
  SELECT
    product_id,
    AVG(quantity) AS average_order_quantity
FROM
    merged_data  
GROUP BY
    product_id
ORDER BY
    product_id;
================================
---All Top Selling Products:
SELECT
    product_id,
    SUM(quantity) AS total_quantity_sold
FROM
    merged_data  
GROUP BY
    product_id
ORDER BY
    total_quantity_sold DESC;
	
---------------Top Selling Customers
	
	SELECT
    customer_id,
    SUM(quantity) AS total_quantity_purchased
FROM
    merged_data  
GROUP BY
    customer_id
ORDER BY
    total_quantity_purchased DESC;
---------
SELECT
    SUBSTR(order_date, 1, 1 ) AS month,
    SUM(quantity * price) AS total_sales
FROM
    merged_data  
WHERE
    order_date IS NOT NULL
GROUP BY
    month
ORDER BY
    month;
---monthly Sales
SELECT
    CASE
        WHEN order_date IS NOT NULL THEN
            CASE
                WHEN SUBSTR(order_date, 1, 1) = '1' THEN 'January'
                WHEN SUBSTR(order_date, 1, 1) = '2' THEN 'February'
                WHEN SUBSTR(order_date, 1, 1) = '3' THEN 'March'
                WHEN SUBSTR(order_date, 1, 1) = '4' THEN 'April'
                WHEN SUBSTR(order_date, 1, 1) = '5' THEN 'May'
                WHEN SUBSTR(order_date, 1, 1) = '6' THEN 'June'
                WHEN SUBSTR(order_date, 1, 1) = '7' THEN 'July'
                WHEN SUBSTR(order_date, 1, 1) = '8' THEN 'August'
                WHEN SUBSTR(order_date, 1, 1) = '9' THEN 'September'
                WHEN SUBSTR(order_date, 1, 1) = '10' THEN 'October'
                WHEN SUBSTR(order_date, 1, 1) = '11' THEN 'November'
                WHEN SUBSTR(order_date, 1, 1) = '12' THEN 'December'
                ELSE 'Invalid Month'
            END
        ELSE 'Invalid Date'
    END AS month,
    SUM(quantity * price) AS total_sales
FROM
    merged_data  
WHERE
    order_date IS NOT NULL
GROUP BY
    month
ORDER BY
    month;





