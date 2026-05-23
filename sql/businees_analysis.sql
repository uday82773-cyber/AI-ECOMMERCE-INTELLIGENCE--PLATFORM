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

----Monthly Sales Trend

SELECT 
YEAR([Order_Date]) as Order_year,
MONTH([Order_Date]) as Order_month,
SUM(Sales) as Monthly_sales
FROM Superstore_sales,
 GROUP BY 
 YEAR([Order_Date]),MONTH([Order_DATE])
ORDER BY 
Order_Year,Order_Month;

---Most profitable Category
SELECT 
Category,sum(Profit) as Total_Profit
FROM Superstore_sales
GROUP BY Category 
ORDER BY Total_Profit DESC;

--Loss Making Products 
SELECT
[Product_Name],
SUM(Profit) as Total_Profit
FROM Superstore_sales
GROUP BY [Product_Name]
having sum(Profit) < 0 ORDER BY Total_Profit;

----Top customers
SELECT
[Customer_Name],sum(Sales) as Total_Sales
from Superstore_sales
group by [Customer_Name]
ORDER by Total_Sales DESC
LIMIT 10;

---Average Shipping Delay 
SELECT
AVG[Shipping_days] as Avg_shipping_days
from Superstore_sales











