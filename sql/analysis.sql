SELECT SUM(Sales)
FROM sales;


SELECT
Product,
SUM(Sales)
FROM sales
GROUP BY Product;


SELECT
City,
SUM(Sales)
FROM sales
GROUP BY City;


SELECT
substr(Date,1,7),
SUM(Sales)
FROM sales
GROUP BY 1;