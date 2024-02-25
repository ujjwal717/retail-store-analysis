import pingouin
import psycopg2
import pandas as pd
import plotly.express as px

db_link = psycopg2.connect("dbname = Sales user=postgres password = 5580 host = localhost port = 5432")

df = pd.read_sql('select * from sales_data', db_link)


def category_percentage():
    df_beauty = pd.read_sql(
        """SELECT COUNT(product_category) AS "Order Count", 
        COUNT(product_category)*100/1000 AS Percentage, 
        product_category as "Product Category" FROM sales_data GROUP BY product_category HAVING product_category = 'Beauty' 
        ORDER BY product_category""",
        db_link,
    )
    df_electronic = pd.read_sql(
        """SELECT COUNT(product_category)AS "Order Count",
        COUNT(product_category)*100/1000 AS Percentage, 
        product_category as "Product Category" FROM sales_data GROUP BY product_category HAVING product_category = 'Electronics' 
        ORDER BY product_category""",
        db_link,
    )
    df_clothes = pd.read_sql(
        """SELECT COUNT(product_category) AS "Order Count",
        COUNT(product_category)*100/1000 AS Percentage, 
        product_category as "Product Category" FROM sales_data GROUP BY product_category HAVING product_category = 'Clothing' 
        ORDER BY product_category""",
        db_link,
    )
    df_categories = pd.concat([df_beauty, df_electronic, df_clothes])
    df_categories = df_categories.reset_index(drop=True)

    fig_category_percentage = px.pie(df_categories, values ='percentage', names='Product Category', title='SALES PERCENTAGE BY CATEGORIES',
                 width=1000, height=700)
    fig_category_percentage.show()


def avg_amount():
    df_avg_beauty = pd.read_sql(
        """SELECT product_category AS "Product Category", 
        avg(total_amount) AS "Average Amount" FROM sales_data GROUP BY product_category 
        HAVING product_category = 'Beauty' """,
        db_link,
    )
    df_avg_electronics = pd.read_sql(
        """SELECT product_category AS "Product Category", 
        avg(total_amount) AS "Average Amount" FROM sales_data 
        GROUP BY product_category HAVING product_category = 'Electronics' """,
        db_link,
    )
    df_avg_clothes = pd.read_sql(
        """SELECT product_category AS "Product Category", 
        avg(total_amount) AS "Average Amount" FROM sales_data 
        GROUP BY product_category HAVING product_category = 'Clothing' """,
        db_link,
    )
    df_avg_final = pd.concat([df_avg_beauty, df_avg_electronics, df_avg_clothes])

    fig_avg_amount = px.bar(df_avg_final, x="Product Category", y="Average Amount",
                            title="AVERAGE OF TOTAL AMOUNT SPENT BY THE CUSTOMERS IN DIFFERENT CATEGORIES",
                            color="Product Category", height=700,width=900)
    fig_avg_amount.show()





def monthly_sales():
    df_sales = pd.read_sql(
        """SELECT DISTINCT date, 
        COUNT(transaction_id) OVER(PARTITION BY date) AS "Sales Per Day" 
        FROM sales_data ORDER BY date""",
        db_link,
    )

    fig_monthly_sales = px.line(
        df_sales,
        x="date",
        y="Sales Per Day",
        hover_data={"date": "|%B %d, %Y"},
        title="RETAIL SALES INSIGHT DIVIDED ACCORDING TO MONTHS AND DAYS",
        range_x=["2023-01-01", "2023-12-31"],
    )

    fig_monthly_sales.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1 Month", step="month", stepmode="backward"),
                    dict(count=3, label="3 Months", step="month", stepmode="backward"),
                    dict(count=6, label="6 Months", step="month", stepmode="backward"),
                    dict(count=1, label="1 Year", step="year", stepmode="todate"),
                ]
            )
        ),
    )

    fig_monthly_sales.show()


def gender_quantity():
    df_male_quantity = pd.read_sql(
        """SELECT customer_id, 
        gender, date, sum(quantity) OVER(PARTITION BY date ) AS "Purchase Quantity" 
        FROM sales_data WHERE gender = 'Male' ORDER BY date""",
        db_link,
    )
    df_female_quantity = pd.read_sql(
        """SELECT customer_id, 
        gender, date, sum(quantity) OVER(PARTITION BY date ) AS "Purchase Quantity"  
        FROM sales_data WHERE gender = 'Female' ORDER BY date""",
        db_link,
    )
    df_gender_quantity = pd.concat([df_male_quantity, df_female_quantity])

    fig_1 = px.line(
        df_gender_quantity,
        hover_data={"date": "|%B %d, %Y"},
        x="date",
        y="Purchase Quantity",
        color="gender",
        title="QUANTITY OF PRODUCTS PURCHASED EACH MONTH AND DAY WITH COMPARISON ACCORDING TO GENDER",
    )

    fig_1.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1 Month", step="month", stepmode="backward"),
                    dict(count=3, label="3 Months", step="month", stepmode="backward"),
                    dict(count=6, label="6 Months", step="month", stepmode="backward"),
                    dict(count=1, label="1 Year", step="year", stepmode="todate"),
                ]
            )
        ),
    )

    fig_1.show()


def gender_product_category():
    df_male_electronics = pd.read_sql(
        """SELECT SUM(quantity) AS "Quantity Ordered", 
        product_category as "Product Category",gender FROM sales_data WHERE gender = 'Male' 
        AND product_category = 'Electronics' GROUP BY product_category,gender """,
        db_link,
    )
    df_male_beauty = pd.read_sql(
        """SELECT SUM(quantity) AS "Quantity Ordered", 
        product_category as "Product Category",gender 
        FROM sales_data 
        WHERE gender = 'Male' AND product_category = 'Beauty' 
        GROUP BY product_category,gender""",
        db_link,
    )
    df_male_clothes = pd.read_sql(
        """SELECT SUM(quantity) AS "Quantity Ordered", 
        product_category as "Product Category",gender 
        FROM sales_data 
        WHERE gender = 'Male' AND product_category = 'Clothing' 
        GROUP BY product_category,gender""",
        db_link,
    )

    df_female_electronics = pd.read_sql(
        """SELECT SUM(quantity) AS "Quantity Ordered", 
        product_category as "Product Category" ,gender 
        FROM sales_data 
        WHERE gender = 'Female' AND product_category = 'Electronics' 
        GROUP BY product_category,gender """,
        db_link,
    )
    df_female_beauty = pd.read_sql(
        """SELECT SUM(quantity) AS "Quantity Ordered", 
        product_category as "Product Category",gender 
        FROM sales_data 
        WHERE gender = 'Female' AND product_category = 'Beauty' 
        GROUP BY product_category,gender""",
        db_link,
    )
    df_female_clothes = pd.read_sql(
        """SELECT SUM(quantity) AS "Quantity Ordered", 
        product_category as "Product Category",gender 
        FROM sales_data WHERE gender = 'Female' AND product_category = 'Clothing' 
        GROUP BY product_category,gender""",
        db_link,
    )

    df_products_category = pd.concat(
        [
            df_male_electronics,
            df_male_clothes,
            df_male_beauty,
            df_female_electronics,
            df_female_beauty,
            df_female_clothes,
        ]
    )

    fig_gender_product_category = px.histogram(
        df_products_category,
        x="Product Category",
        y="Quantity Ordered",
        color="gender",
        barmode="group",
        height=700,
        width=1000,
        title="OVERALL PRODUCTS PURCHASED IN DIFFERENT CATEGORIES ACCORDING TO GENDER",
    )

    fig_gender_product_category.show()


def year_sales_categories():
    df_year_electronics = pd.read_sql(
        """SELECT DISTINCT product_category as "Product Category", 
        date , sum(quantity) OVER (partition BY date) AS sales 
        FROM sales_data 
        WHERE product_category = 'Electronics' 
        ORDER BY date """,
        db_link,
    )
    df_year_beauty = pd.read_sql(
        """ SELECT DISTINCT product_category as "Product Category", 
        date , sum(quantity) OVER (partition BY date) AS sales 
        FROM sales_data 
        WHERE product_category = 'Beauty' 
        ORDER BY date """,
        db_link,
    )
    df_year_clothes = pd.read_sql(
        """SELECT DISTINCT product_category as "Product Category",
        date, sum(quantity) OVER (partition BY date) AS sales 
        FROM sales_data 
        WHERE product_category = 'Clothing' 
        ORDER BY date """,
        db_link,
    )
    df_year_categories = pd.concat(
        [df_year_electronics, df_year_beauty, df_year_clothes]
    )

    fig_year_sales_categories = px.scatter(
        df_year_categories,
        title="RETAIL SALES OF THE YEAR DISTRIBUTED ACROSS MONTHS AND CATEGORIES",
        x="date",
        y="sales",
        color="sales",
        facet_col="Product Category",
        hover_data={"date": "|%B %d, %Y"},
        width=1500,
        height=800,
    )

    fig_year_sales_categories.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1 Month", step="month", stepmode="backward"),
                    dict(count=3, label="3 Months", step="month", stepmode="backward"),
                    dict(count=6, label="6 Months", step="month", stepmode="backward"),
                    dict(count=1, label="1 Year", step="year", stepmode="backward"),
                ]
            )
        ),
    )

    fig_year_sales_categories.show()


def age_quantity():
    df_age_quantity = pd.read_sql(
        """SELECT distinct age, SUM(quantity) OVER(PARTITION BY age) AS "Total Quantity" 
        FROM sales_data""",
        db_link,
    )

    fig_year_sales_categories = px.bar(
        df_age_quantity,
        x="age",
        y="Total Quantity" ,
        color="Total Quantity" ,
        title="TOTAL QUANTITY OF PRODUCTS PURCHASED BY CUSTOMERS ACCORDING TO THEIR AGE ",
    )

    fig_year_sales_categories.show()


category_percentage()
avg_amount()
monthly_sales()
gender_quantity()
gender_product_category()
year_sales_categories()
age_quantity()


db_link.close()
