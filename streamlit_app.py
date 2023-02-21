import streamlit

import snowflake.connector

import pandas
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row=my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.header("The fruit load  list contains")
streamlit.dataframe(my_data_row)
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("pick some fruits :",list (my_fruit_list.index),['Avocado','starwberries'])

streamlit.header("Fruityvice Fruit Advice!")
streamlit.header("Fruityvice Fruit Advice!")

