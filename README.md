# retail-store-analysis
It is a retail store sales analysis. It provides insight and detailed analysis of the retail sales including various categories and detailed patterns that can affect the retail sales. The dataset is cleaned in which I removed missing values, modified the dataset by adding columns such as total amount etc according the requirement, preprocessed and transformed the data mainly using SQL and little bit of Excel. The dataset is taken from kaggle, analysis is done using SQL, Python, Pandas and visualization is done using Python, Bokeh and Plotly


Now Let's discuss what I found from the analysis of the retail sales dataset and what insight I have drawn from it. I will be discussing it according to the each visualization and what it tries to convey us.

**Note :- The images are captured using the snipping tool and this is why we cannot see the precised data/value in the images below but the project has support for hover tool which simply means that you can see the exact data/value of all the parts of all the visualization by hovering your cursor over the figure.**

1)**Retail Sales Percentage according to Categories**

![sales percentage by categories](https://github.com/ujjwal717/retail-store-analysis/assets/93403224/bfaabda0-dc8b-4118-a3ef-a36eef27639f)


Explanation :- In the above visualization, we can see the percentage of retail sales division according to the categories. The clothing category has a sales percentage of 35%, It is 34% for Electronics and 30% for Beauty.

Insight :- It can be seen that the sales percentage of clothing is maximum while it is least for beauty.

Possible Reason :- There can be multiple reasons for it, and they are :-

The reason might be the size constraint that is present in the online shopping, it means generally while shopping clothes on E-Commerce platform, we cannot be sure about the size of the clothes and every brand has a slight difference in size in the same size convention say 2XL. So, the customers might prefer to shop in retail stores to check the size of the clothes and they buy it which adds to the sales value of the clothing category.
The Beauty category has the least sales percentage which can be because customers generally know which beauty products, they want along with the brand name and the name of the exact product and because the E-Commerce platform generally has more discount than retail stores as online shopping removes the middlemen, customers might be preferring online stores for beauty products.



2)**Average of total Amount Spent by the Customers in different Categories**

![avg of total amount spent by customers in different categories](https://github.com/ujjwal717/retail-store-analysis/assets/93403224/83265eb4-bbda-4918-98eb-5b3e6278903c)


Explanation :- In the above visualization, we see the average of the total amount spent by the customers across various categories.

Insight :- It can be seen that beauty has maximum average amount spent by the customers followed by electronics and clothing.

Possible Reason :- Here, we can consider the general high cost of branded beauty products and as people prefer branded products to ensure that it does not harm their skin, the average amount spent on beauty products is more.

3)**Retail Sales Insight divided according to Months and Days**

![retail sales insight divided according to month and days](https://github.com/ujjwal717/retail-store-analysis/assets/93403224/c6d7e989-e491-421f-a42e-8edcc0dd2939)


Explanation :- Here, we have months/day on the X-Axis while sales per day on the Y-Axis and we have options for 1 month, 3 months, 6 months and 1 years which can be used to understand after quarterly sales as well.

Insight 1 :- We can see that the sales have skyrocketed in the month of may.

Possible Reason 1 :- In India, there are no major festivals that are celebrated across entire country and because of this, E-Commerce platform does not have many discounts and because of this, customers prefer purchasing from retail stores as they get product faster, can check product physically and a lot more benefits.

Insight 2 :- The sales have decreased from May end to July mid.

Possible Reason 2 :- In India, summer vacations for students basically goes from ending of may and goes till second week of July(varies from state to state) and is generally for 40-45 days. So, the families tend to spend that money for their tours and trips to other countries or visiting places in India only. This is the biggest reason all the visiting places in India are packed during these months as well. So, people save money by not purchasing products and use it to travel.

Insight 3 :- It can be seen that sales decrease during the specific days of months such as around 15th of october, second week of november , january and first two weeks of march.

Possible Reason 3 :- India is a country of festivals and these sale decrease is just because of that, let’s discuss them one by one :-

There are 2 biggest discounts in India on E-Commerce platform that goes on for few days and it is done by two biggest E-Commerce platform in India namely Flipkart and Amazon. Amazons’ discount season is knows as Amazon Great Indian Festival sale and Flipkart’s discount is knows as Big Billion Days sale and it starts few days before Diwali(name of Indian festival) and Dussehra(indian festival name) due to which retail store sales face a dip in their sales. This is the probable reason for retail store sales drop around 15th of october(around Dussehra) and during second week of november (around Diwali).

In january, there is festival named Makar Sankranti where it is special occasion to purchase new products and things at home so there is discounts on E-Commerce platform during januray as well.

Another festival and really big one is Holi that happens generally during the first 2 weeks of march and again E-Commerce platform has sales and thus, retail store sales dips.
Also, the festivals in India are according to Hindu Calendar and the dates of festivals changes slightly every year, so this is why there is a trend of sales dropping during these months.

4)**Quantity of Products Purchased each Month and DAY with comparison according to Gender**


![quantity of products purchased each month and day with comparison according to gender](https://github.com/ujjwal717/retail-store-analysis/assets/93403224/a2c2a542-d7a6-4cb3-8420-699de9ca04f8)



Explanation :- It is again a time series line chart having two lines for each gender having months and day on X-Axis and product quantity on Y-Axis.

Insight :- We can see that for a few months female customers purchase more while in some months male customer are more dominant in purchasing various products from the retail stores.


5)**Overall Products purchased in different Categories according to Gender**


![overall products purchased in different categories according to gender](https://github.com/ujjwal717/retail-store-analysis/assets/93403224/632f4142-eef5-494e-a7eb-032080796b77)


Explanation :- I wanted to check which of the gender purchased more products from the retail stores as it was not clear from the previous visualization, and this visualization clears the confusion.

Insight :- We can clearly see and is evident as well that females purchased more products from the retail stores as compared to males in the categories such as “Beauty” and “Electronics” while males purchase more “clothing” products than females from the retail stores.





6)**Retail Sales of the Year distributed across Months and Categories**


![retail sales of the year distributed across months and categories](https://github.com/ujjwal717/retail-store-analysis/assets/93403224/60efb778-9974-4a08-9bd2-b140a682e975)




Explanation :- In this visualization, we have divided the sales according to the categories and the scatterplots shows the sales of the products of each category throughout the year. It gives us a detailed explanation/analysis of how each category performed each month of the year. Also, like each and every other visualization, this visualization also includes the hovering features which allows you to see the sales of each day of the year for every category to see the insight. It also inludes date/month ranges that is present in various other visualizations as well by which you can select the part of the year such as “6 Months”, “3 Months”, “1 Month” or even custom month/date range for which the scrolling tool is given.

Insight :- We can see that products of the Beauty Category has performed better if we consider only one factor and that is “maximum sale per day”. But if we consider, which category/categories have sold more than 10 products on multiple occassions than those categories will be “Electronics” and “Clothing as they have sold 10 products in a day around 6 times a year. There is also difference in the months of the maximum sale achieved by a category and that is May for “Electronics”, July for “Beauty” and September for “Clothing”.


7)**Total Quantity of Products Purchased by Customers according to their Age**


![total quantity of products purchased by customers according to age](https://github.com/ujjwal717/retail-store-analysis/assets/93403224/1c9075a8-ac43-407e-ab65-4de78cfe2897)



Explanation :- In the above visualization, we can see that the quantity of products sold are divided according to the age of the customers. It will allow us to understand more about the age group of the customers who prefer retail store and which age group of customers don’t prefer retail stores.

Insight :- This insight however does not give any concrete information about the customer’s age that is preferring or not referring retail store but we can see that around 43-52 ages prefer retail stores more than other ages.


**Now the Various Steps that a Retail Store can take to improve their Sales :-**

1) They can try to decrease their profit margin and provide discount to compete with online stores.

2) They can provide facilities such as One day Delivery and free installation of the Electronic products such as LED TVs, Air Conditioners etc which can be a major benefit to the customers as installation charges are generally high.

3) Retail stores can also provide plans for additional warranty without any additional cost for which the online store charge the customers.


