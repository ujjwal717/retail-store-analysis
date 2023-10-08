# retail-sales-analysis
It is a retail sales analysis. It provides insight and detailed analysis of the retail sales including various categories and detailed patterns that can affect the retail sales. The dataset is cleaned in which I removed missing values, modified the dataset by adding columns such as total amount etc according the requirement, preprocessed and transformed the data mainly using SQL and little bit of Excel. 

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

Now Let's discuss what I found from the analysis of the retail sales dataset and what insight I hace drawn from it. I will be discussing it according to the each visual and what it tries to convey us.

**Note :- The images are captured using the snipping tool and this is why we cannot see the precised data/value in the images below but the project has support for hover tool which simply means that you can see the exact data/value of all the parts of all the visualization by hovering your cursor over the figure.**

1)**Retail Sales Percentage according to Categories**

![categories percentage](https://github.com/ujjwal717/retail-sales-analysis/assets/93403224/97bd0d58-062b-4fe9-8ff0-54b20fdeb687)

In the above visualization, we can see the percentage of retail sales division according to the categories. The clothing category has a sales percentage of 35%, It is 34% for Electronics and 30% for Beauty.

**Insight :-**

A) We found that the sales percentage of clothing is maximum while it is least for beauty.

B) The reason might be the size constraint that is present in the online shopping, it means generally while shopping clothes on E-Commerce platform, we cannot be sure about the size of the clothes and also every brand generally has a little difference in size in the same size convention say 2XL.

C) So, the customers might prefer to shop in retail stores to check the size of the clothes and they buy it which adds to the sales value of the clothing category.

D) The Beauty category has the least sales percentage which can be because customers generally know which beauty products they want along with the branch name and the name of the exact product and because the E-Commerce platform generally has more discount than retail stores as online shopping removes the middle men, customers might be preferring online stores for beauty products.


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

**Reason 1 :-**  In India, the financial year ends in March and generally companies provide yearly bonus to their employees in the month of May or June(Sometime bonus is given even in july and actually depends from company to company). And employees can be those one of the customer categories that might be purchasing products from the retail sales during that period of time in the year.

**Reason 2 :-** Another reason can be the fact that there is absence of great dicsount on the online stores during that period of time in the year and that is more evident than the reason 1. In India, the massive online sales are during the festive seasons and generally online sales are not that great during the months such as May, June, July. Due to this, the customers might prefer taking products from a retail store since there is no major difference in the price and they will get the product same day(Online sales generally do not deliver product within same day in a lot of citites) and can even check the product before purchasing it.

B) **Insight 2 :-** We can see a significant dip in the retail sales during some months such as Januray, March, June, October(after mid), November. Let's discuss the reason according to months.

**Reason 1 :- January and March :-** In India, there are two big festivals that are celebrated across the country, one is **Dhanteras**(in January) and second **Holi**(in March). Now during these months, there are discounts on the online sales and customers actually pre-plan purchasing products for the festivals from the online stores and this is why, we see drop in the sales of retail stores.

**Reason 2 :- June :-** This time of year, online stores include sales such as "Monsoon Sales" and again customer prefer saving money from these discounts. Another reason which can be a bigger reason for the dip of retail sales in this month can be the fact that In India, there is summer vacation from schools during the month of June and families which are indeed the customers plan to go on a vacation during this month and due to this, they avoid spending money on products and save it for their trip/vacation which seems to be one of the reasons for the dip in the retail sales.


