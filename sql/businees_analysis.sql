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

--- Totals sales by Region 
Select region ,
sum(sales) as total_sales from superstore_sales
group by region
order by total_sales desc;

----category wise profit 
select categoty,
sum(profit) as total_profit from superstore_sales
group by category 
order by total_profit desc ;

--- Top 10 customers 
select [customer name],
sum(sales) as customer_sales
from superstore_sales
group by [customer name]
order by customer_sales desc
limit 10;


--- Monthly sales trend 
select 
    year[Order Date] as Order_year ,
    MOnth[Order Date] as Order_month,
    sum(sales) as Monthly_sales
        from superstore_sales
    group by ([order Date],
    Month[Order Month])
    group by 
    order_year ,
    order_month;








