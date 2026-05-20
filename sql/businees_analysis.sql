-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM Superstore_sales;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM Superstore_sales;

-- Region Wise Sales
SELECT Region, SUM(Sales) AS Sales
FROM Superstore_sales
GROUP BY Region
ORDER BY Sales DESC;

-- Category Wise Sales
SELECT Category, SUM(Sales) AS Sales
FROM Superstore_sales
GROUP BY Category
ORDER BY Sales DESC;

-- Segment Wise Sales
SELECT Segment, SUM(Sales) AS Sales
FROM Superstore_sales
GROUP BY Segment
ORDER BY Sales DESC;

-- Top 10 Products by Sales
SELECT Product_Name, SUM(Sales) AS Sales
FROM Superstore_sales
GROUP BY Product_Name
ORDER BY Sales DESC
LIMIT 10;