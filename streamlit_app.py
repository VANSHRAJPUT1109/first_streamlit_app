import streamlit

streamlit.title('🥭Mommies Healthy Recepies')

streamlit.header('🥣 🥗 Healthy Breakfast Menu🐔 🥑')

streamlit.text('🥣Omega 3 & Blueberry Oatmeal🍞')

streamlit.text('🥗Kale, Spinach & Rocket Soothie🐔')

streamlit.text('🐔Chicken Sausage🥑')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
