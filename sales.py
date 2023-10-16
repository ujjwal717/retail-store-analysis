import psycopg2
import pandas as pd
from math import pi
from bokeh.palettes import Dark2
from bokeh.plotting import figure, output_file, save, show
from bokeh.transform import cumsum
from bokeh.models import ColumnDataSource
from bokeh.palettes import Bright6
from bokeh.transform import factor_cmap
import webbrowser
from bokeh.models import HoverTool
import plotly.express as px

db_link = psycopg2.connect("dbname=<your database name> user=<your database username> password = <your database password> host = <your host> port = <your port number>")


def category_percentage():
    df_beauty = pd.read_sql('''SELECT COUNT(product_category) AS order_count, COUNT(product_category)*100/1000 AS percentage, product_category FROM sales_data GROUP BY product_category HAVING product_category = 'Beauty' ORDER BY product_category''', db_link)
    df_electronic = pd.read_sql('''SELECT COUNT(product_category)AS order_count,COUNT(product_category)*100/1000 AS percentage, product_category FROM sales_data GROUP BY product_category HAVING product_category = 'Electronics' ORDER BY product_category''', db_link)
    df_clothes = pd.read_sql('''SELECT COUNT(product_category) AS order_count,COUNT(product_category)*100/1000 AS percentage, product_category FROM sales_data GROUP BY product_category HAVING product_category = 'Clothing' ORDER BY product_category''', db_link)
    df_categories = pd.concat([df_beauty,df_electronic,df_clothes])
    df_categories = df_categories.reset_index(drop=True)

    x = {
        'Beauty': df_categories['percentage'],
        'Electronics': df_categories['percentage'],
        'Clothing': df_categories['percentage']
    }

    df_categories['angle'] = df_categories['percentage'] / df_categories['percentage'].sum() * 2 * pi
    df_categories['color'] = Dark2[len(df_categories['percentage'])]

    p_percentage = figure(height=350, title="RETAIL SALES PERCENTAGE ACCORDING TO CATEGORIES", toolbar_location=None,
               tools="hover", tooltips="@product_category: @percentage", x_range=(-0.5, 1.0))

    p_percentage.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='product_category', source=df_categories)

    p_percentage.axis.axis_label = None
    p_percentage.axis.visible = False
    p_percentage.grid.grid_line_color = None

    output_file("p_percentage.html")
    save(p_percentage)
    webbrowser.open("p_percentage.html")


def avg_amount():
    df_avg_beauty = pd.read_sql('''SELECT product_category, avg(total_amount) AS average_amount FROM sales_data GROUP BY product_category HAVING product_category = 'Beauty' ''', db_link)
    df_avg_electronics = pd.read_sql('''SELECT product_category, avg(total_amount) AS average_amount FROM sales_data GROUP BY product_category HAVING product_category = 'Electronics' ''', db_link)
    df_avg_clothes = pd.read_sql('''SELECT product_category, avg(total_amount) AS average_amount FROM sales_data GROUP BY product_category HAVING product_category = 'Clothing' ''', db_link)
    df_avg_final = pd.concat([df_avg_beauty, df_avg_electronics, df_avg_clothes])
    

    category = df_avg_final['product_category']
    average_amount = df_avg_final['average_amount']

    TOOLTIPS = HoverTool(tooltips=[
        ("Products Category", "@category"),
        ("Average of total amount", "@average_amount")
    ])

    source = ColumnDataSource(data=dict(category=category, average_amount=average_amount))
    p_avg_amount = figure(x_range= category, height=500, toolbar_location=None, tools = [TOOLTIPS], title="AVERAGE OF TOTAL AMOUNT SPENT BY CUSTOMERS IN DIFFERENT CATEGORIES")
    p_avg_amount.vbar(x= 'category' , top='average_amount', width=0.4, source=source, legend_field="category",line_color='white', fill_color=factor_cmap('category', palette=Bright6, factors=category))
    p_avg_amount.xgrid.grid_line_color = None
    p_avg_amount.y_range.start = 0
    p_avg_amount.y_range.end = 600
    p_avg_amount.legend.orientation = "horizontal"
    p_avg_amount.legend.location = "top_center"

    output_file("p_avg_amount.html")
    save(p_avg_amount)
    webbrowser.open("p_avg_amount.html")


def monthly_sales():
    df_sales = pd.read_sql('''SELECT DISTINCT date, COUNT(transaction_id) OVER(PARTITION BY date) AS sales_per_day FROM sales_data ORDER BY date''', db_link)

    fig_0 = px.line(df_sales, x="date", y="sales_per_day",
                  hover_data={"date": "|%B %d, %Y"},
                  title='REATIL SALES INSIGHT DIVIDED ACCORDING TO MONTHS AND DAYS',  range_x=['2023-01-01', '2023-12-31'])

    fig_0.update_xaxes( dtick="M1",tickformat="%b\n%Y",rangeslider_visible=True,rangeselector=dict(buttons=list([
            dict(count=1, label="1 Month", step="month", stepmode="backward"),
            dict(count=3, label="3 Months", step="month", stepmode="backward"),
            dict(count=6, label="6 Months", step="month", stepmode="backward"),
            dict(count=1, label="1 Year", step="year", stepmode='todate' )
        ])))

    fig_0.show()


def gender_quantity():
    df_male_quantity = pd.read_sql('''SELECT customer_id, gender, date, sum(quantity) OVER(PARTITION BY date ) AS purchase_quantity FROM sales_data WHERE gender = 'Male' ORDER BY date''', db_link)
    df_female_quantity = pd.read_sql('''SELECT customer_id, gender, date, sum(quantity) OVER(PARTITION BY date ) AS purchase_quantity FROM sales_data WHERE gender = 'Female' ORDER BY date''', db_link)
    df_gender_quantity = pd.concat([df_male_quantity, df_female_quantity])
    

    fig_1 = px.line(df_gender_quantity,hover_data={"date": "|%B %d, %Y"}, x="date", y="purchase_quantity", color='gender', title = 'QUANTITY OF PRODUCTS PURCHASED EACH MONTH AND DAY WITH COMPARISON ACCORDING TO GENDER')

    fig_1.update_xaxes(dtick="M1", tickformat="%b\n%Y", rangeslider_visible=True, rangeselector=dict(buttons=list([
        dict(count=1, label="1 Month", step="month", stepmode="backward"),
        dict(count=3, label="3 Months", step="month", stepmode="backward"),
        dict(count=6, label="6 Months", step="month", stepmode="backward"),
        dict(count=1, label="1 Year", step="year", stepmode='todate')
    ])))

    fig_1.show()


def gender_product_category():
    df_male_electronics = pd.read_sql('''SELECT SUM(quantity) AS quantity_ordered, product_category,gender FROM sales_data WHERE gender = 'Male' AND product_category = 'Electronics' GROUP BY product_category,gender ''',db_link)
    df_male_beauty = pd.read_sql('''SELECT SUM(quantity) AS quantity_ordered, product_category,gender FROM sales_data WHERE gender = 'Male' AND product_category = 'Beauty' GROUP BY product_category,gender''', db_link)
    df_male_clothes = pd.read_sql('''SELECT SUM(quantity) AS quantity_ordered, product_category,gender FROM sales_data WHERE gender = 'Male' AND product_category = 'Clothing' GROUP BY product_category,gender''', db_link)

    df_female_electronics = pd.read_sql('''SELECT SUM(quantity) AS quantity_ordered, product_category,gender FROM sales_data WHERE gender = 'Female' AND product_category = 'Electronics' GROUP BY product_category,gender''', db_link)
    df_female_beauty = pd.read_sql('''SELECT SUM(quantity) AS quantity_ordered, product_category,gender FROM sales_data WHERE gender = 'Female' AND product_category = 'Beauty' GROUP BY product_category,gender''', db_link)
    df_female_clothes = pd.read_sql('''SELECT SUM(quantity) AS quantity_ordered, product_category,gender FROM sales_data WHERE gender = 'Female' AND product_category = 'Clothing' GROUP BY product_category,gender''', db_link)

    df_products_category = pd.concat([df_male_electronics, df_male_clothes, df_male_beauty, df_female_electronics, df_female_beauty, df_female_clothes])

    fig_2 = px.histogram(df_products_category, x="product_category", y="quantity_ordered",  color='gender', barmode='group',height=700, width=1000, title = 'OVERALL PRODUCTS PURCHASED IN DIFFERENT CATEGORIES ACCORDING TO GENDER')

    fig_2.show()


def year_sales_categories():
    df_year_electronics = pd.read_sql('''SELECT DISTINCT product_category, date , sum(quantity) OVER (partition BY date) AS sales FROM sales_data WHERE product_category = 'Electronics' ORDER BY date ''', db_link)
    df_year_beauty = pd.read_sql(''' SELECT DISTINCT product_category, date , sum(quantity) OVER (partition BY date) AS sales  FROM sales_data WHERE product_category = 'Beauty' ORDER BY date ''',db_link)
    df_year_clothes = pd.read_sql('''SELECT DISTINCT product_category,date, sum(quantity) OVER (partition BY date) AS sales  FROM sales_data WHERE product_category = 'Clothing' ORDER BY date ''',db_link)
    df_year_categories = pd.concat([df_year_electronics,df_year_beauty,df_year_clothes])
    

    fig_3 = px.scatter(df_year_categories, title="RETAIL SALES OF THE YEAR DISTRIBUTED ACROSS MONTHS AND CATEGORIES", x="date", y="sales", color="sales", facet_col="product_category",hover_data={"date": "|%B %d, %Y"},width = 1500, height = 800)

    fig_3.update_xaxes(dtick="M1", tickformat="%b\n%Y", rangeslider_visible=True, rangeselector=dict(buttons=list([
        dict(count=1, label="1 Month", step="month", stepmode="backward"),
        dict(count=3, label="3 Months", step="month", stepmode="backward"),
        dict(count=6, label="6 Months", step="month", stepmode="backward"),
        dict(count=1, label="1 Year", step="year", stepmode='backward')
    ])))

    fig_3.show()

def age_quantity():
    df_age_quantity = pd.read_sql('''SELECT distinct age, SUM(quantity) OVER(PARTITION BY age) AS total_quantity FROM sales_data''',db_link)

    fig_4 = px.bar(df_age_quantity, x='age', y='total_quantity', color = 'total_quantity', title = 'TOTAL QUANTITY OF PRODUCTS PURCHASED BY CUSTOMERS ACCORDING TO THEIR AGE ')

    fig_4.show()


category_percentage()
avg_amount()
monthly_sales()
gender_quantity()
gender_product_category()
year_sales_categories()
age_quantity()


db_link.close()

