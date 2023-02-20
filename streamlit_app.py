import streamlit
streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import snowflake.connector

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("pick some fruits :",list (my_fruit_list.index),['Avocado','starwberries'])

streamlit.header("Fruityvice Fruit Advice!")
streamlit.header("Fruityvice Fruit Advice!")

