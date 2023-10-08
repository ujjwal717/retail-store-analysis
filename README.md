# retail-sales-analysis
It is a retail store analysis. It provides insight and detailed analysis of the retail sales including various categories and detailed patterns that can affect the retail sales. The dataset is cleaned in which I removed missing values, modified the dataset by adding columns such as total amount etc according the requirement, preprocessed and transformed the data mainly using SQL and little bit of Excel. The dataset is taken from kaggle, analysis is done using SQL, Python, Pandas and visualization is done using Python, Bokeh and Plotly

The various imports in the project including modules etc are :- 
1) import psycopg2
2) import pandas as pd
3) from math import pi
4) from bokeh.palettes import Dark2
5) from bokeh.plotting import figure, output_file, save, show
6) from bokeh.transform import cumsum
7) from bokeh.models import ColumnDataSource
8) from bokeh.palettes import Bright6
9) from bokeh.transform import factor_cmap
10) import webbrowser
11) from bokeh.models import HoverTool
12) import plotly.express as px

Now Let's discuss what I found from the analysis of the retail sales dataset and what insight I have drawn from it. I will be discussing it according to the each visualization and what it tries to convey us.

**Note :- The images are captured using the snipping tool and this is why we cannot see the precised data/value in the images below but the project has support for hover tool which simply means that you can see the exact data/value of all the parts of all the visualization by hovering your cursor over the figure.**

1)**Retail Sales Percentage according to Categories**

![categories percentage](https://github.com/ujjwal717/retail-sales-analysis/assets/93403224/97bd0d58-062b-4fe9-8ff0-54b20fdeb687)

In the above visualization, we can see the percentage of retail sales division according to the categories. The clothing category has a sales percentage of 35%, It is 34% for Electronics and 30% for Beauty.

**Insight :-**

A) We found that the sales percentage of clothing is maximum while it is least for beauty.

B) The reason might be the size constraint that is present in the online shopping, it means generally while shopping clothes on E-Commerce platform, we cannot be sure about the size of the clothes and also every brand generally has a little difference in size in the same size convention say 2XL.

C) So, the customers might prefer to shop in retail stores to check the size of the clothes and they buy it which adds to the sales value of the clothing category.

D) The Beauty category has the least sales percentage which can be because customers generally know which beauty products they want along with the brand name and the name of the exact product and because the E-Commerce platform generally has more discount than retail stores as online shopping removes the middle men, customers might be preferring online stores for beauty products.


2)**Average of total Amount Spent by the Customers in different Categories**

![average total amount in different categories](https://github.com/ujjwal717/retail-sales-analysis/assets/93403224/097169b3-d086-4a3c-8436-b7e6092e9171)

In the above visualization, we see the average of the total amount spent by the customers across various categories.

**Insight :-**

A) Here we can see that the average of total amount is very close among different categories. Also, we should note that we are not considering the count of the product sold and the amount of each product(one category can have various product and one of them can be very affordable while one can be expensive). So, this might be one of the reason why the average of total amount spent is close.


3)**Retail Sales Insight divided according to Months and Days**

![sales according to months and days](https://github.com/ujjwal717/retail-sales-analysis/assets/93403224/5c82933e-5cbf-41a1-815a-099c117e5b43)

In the above visualization, we can see the sales insight of the retail store divided across months and days to have a detailed understanding about the sales.

**Insight :-**

A) **Insight 1 :-** We can see that the sales have skyrocketed in the month of may and there can be multiple reasons for that, Let's discuss them one by one :-

**Reason 1 :-**  In India, the financial year ends in March and generally companies provide yearly bonus to their employees in the month of May or June(Sometime bonus is given even in july and actually depends from company to company). And employees can be those one of the customer categories that might be purchasing products from the retail stores during that period of time in the year.

**Reason 2 :-** Another reason can be the fact that there is absence of great dicsount on the online stores during that period of time in the year and that is more evident than the reason 1. In India, the massive online sales are during the festive seasons and generally online discounts are not that great during the months such as May, June, July. Due to this, the customers might prefer taking products from a retail store since there is no major difference in the price and they will get the product same day(Online sales generally do not deliver product within same day in a lot of citites) and can even check the product before purchasing it.

B) **Insight 2 :-** We can see a significant dip in the retail sales during some months such as Januray, March, June, October(after mid), November. Let's discuss the reason according to months.

**Reason 1 :- January and March :-** In India, there are two big festivals that are celebrated across the country, one is **Dhanteras**(in January) and second **Holi**(in March). Now during these months, there are discounts on the online platforms and customers actually pre-plan purchasing products for the festivals from the online stores and this is why, we see drop in the sales of retail stores.

**Reason 2 :- June :-** This time of year, online stores include sales such as "Monsoon Sales" and again customer prefer saving money from these discounts. Another reason which can be a bigger reason for the dip of retail sales in this month can be the fact that In India, there is summer vacation from schools during the month of June and families which are indeed the customers, plan to go on a vacation during this month and due to this, they avoid spending money on products and save it for their trip/vacation which seems to be one of the reasons for the dip in the retail sales.

**Reason 3 :- October (after 14/15 October) :-** This time of year, the leading E-Commerce platform in India namely "Flipkart" and "Amazon India" have their biggest discounts/offers of the year. For Amazon, it is generally named as "Great Indian Festival" and for Flipkart, it is named as "Big Billion Days". Both of these discount goes on for few days(they might increase the days of the discounts as well) and include massive amount of discounts and exciting deals. And these sales generally begin from the later part of the october(the beginning date may also vary) and during this time, the retail sales dips. Customer plans for these discount days from 1-2 months before and stop purchasing prodcucts that are not needed immediately as they wait for these deals, this is the reason why we see a dip in the retail sales in the month of **September** as well.

**Reason 4 :- November :-** In India, November month generally has one of the biggest festival and that is **Diwali**. The diwali festival is celebrated according to the Hindu calendar due to which, it's date changes slightly every year and is generally after the first week of November. The online stores are again ready to give heavy discount during the month of November and we can see the sales of retail stores dips after the 8th/9th November due to the online sales. It is very evident dip in the retail sales which can be seen easily from the sales and is very exact.

4)**Quantity of Products Purchased each Month and DAY with comparison according to Gender**


![quantity purchased according to gender](https://github.com/ujjwal717/retail-sales-analysis/assets/93403224/8cf43f9c-c243-4b40-b6fd-27346ab8c5cc)


**Insight :-** We can see that for a few months female customers purchase more while in some months male customer are more dominant in purchasing various products from the retail stores.


5)**Overall Products purchased in different Categories according to Gender**


![overall products purcahsed in different categories according to gender](https://github.com/ujjwal717/retail-sales-analysis/assets/93403224/7dd927b8-b278-43d6-abd8-5181a8767f13)

I wanted to check which of the gender purchased more products from the retail stores as it was not clear from the previous visualization, and this visualization clears the confusion.

**Insight :-** We can clearly see and is evident as well that females purchased more products from the retail stores as compared to males in the categories such as "Beauty" and "Electronics" while males purchase more "clothing" products than females from the retail stores.

Now to get a detailed insight, we can hover across the various parts of the visualization and see the actual difference between the quantity of products purchased by males and females.

Clothing :- Male - 453, Female - 441

Electronics :- Male - 410, Female - 439

Beauty :- Male - 353, Female - 418

Now with the exact amount, we can say that females prefer retail store more as compared to males as even in the category(Clothing) where males have purchased more, the difference is not that significant but in cases where the females are dominant in terms of purchasing products such as Beauty, the difference is significant, also as Electronics products are generally expensive, we can consider that difference as big as well.


6)**Retail Sales of the Year distributed across Months and Categories**


![sales of year across months and categories](https://github.com/ujjwal717/retail-sales-analysis/assets/93403224/1695e2dc-62ae-4499-8964-7c953ae67c09)



In this visualization, we have divided the sales according to the categories and the scatterplots shows the sales of the products of each category throughout the year. It gives us a detailed explanation/analysis of how each category performed each month of the year. Also, like each and every other visualization, this visualization also includes the hovering features which allows you to see the sales of each and every day of the year for every category to see the insight. It also inludes date/month ranges that is present in various other visualizations as well by which you can select the part of the year such as "6 Months", "3 Months", "1 Month" or even custom month/date range for which the scrolling tool is given.

**Insight :-** We can see that products of the Beauty Category has performed better if we consider only one factor and that is "maximum sale per day". But if we consider, which category/categories have sold more than 10 products on mutiple occassions than those categories will be "Electronics" and "Clothing as they have sold 10 products in a day around 6 times a year.

There is also difference in the months of the maximum sale achieved by a category and that is May for "Electronics", July for "Beauty" and September for "Clothing".

A detailed performance of each product category can be seen from the above visualization by hovering to the month/day part of the visualization.


7)**Total Quantity of Products Purchased by Customers according to their Age**


![total quantity purchased according to customer age](https://github.com/ujjwal717/retail-sales-analysis/assets/93403224/e9d63b6f-a79a-4cec-a566-83b09b27e1b0)


In the above visualization, we can see that the quantity of products sold are divided according to the age of the customers. It will allow us to understand more about the age group of the customers who prefer retail store and which age group of customers don't prefer retail stores.


**Insight :-** We can clearly see that younger people are not that interested in purchasing from the retail stores and it is very obvious that there will be exception and this data might also include that exception which can be one of the reason why according to this visualization, certain young customers are also purchasing from the retail stores. But the difference is clear because the product quantity of older customers is way more than that of younger customers. Also, this visualization also has support for hovering to see the exact age and the quantity of the products purchased.

**Reason :-** The reason seems obvious that older customer generally do not trust online stores, E-Commerce platform etc and we have also seen few frauds that happened by the seller end from various E-Commerce platforms which might be the reason that older customers might be reluctant to use such online platforms, obviously there will be exception in this case as well. But the younger customers are more aware in terms of facilities provided by such online stores such as replacement policies and "make video while unboxing a product to keep evidence" which might be the reasons that younger customer do not prefer retail stores that much.


**Now the Various Steps that a Retail Store can take to improve their Sales :-**

1) They can try to decrease their profit margin and provide discount to compete with online stores.

2) They can provide facilities such as One day Delivery and free installation of the Electronic products such as LED TVs, Air Conditioners etc which can be a major benefit to the customers as installation charges are generally high.

3) Retail stores can also provide plans for additional warranty without any additional cost for which the online store charge the customers.


