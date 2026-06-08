SELECT * FROM superstore;

SELECT region, SUM(sales)
FROM superstore
GROUP BY region;

SELECT category, AVG(sales)
FROM superstore
GROUP BY category;

SELECT *
FROM superstore
WHERE sales > 500;

SELECT *
FROM superstore
ORDER BY sales DESC;

SELECT segment, COUNT(*)
FROM superstore
GROUP BY segment;

SELECT category, MAX(profit)
FROM superstore
GROUP BY category;

SELECT region, MIN(sales)
FROM superstore
GROUP BY region;

SELECT *
FROM superstore
WHERE profit < 0;

SELECT category, SUM(quantity)
FROM superstore
GROUP BY category;