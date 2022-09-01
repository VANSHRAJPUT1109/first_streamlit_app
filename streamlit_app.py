import streamlit

streamlit.title('🥭Mommies Healthy Recepies')

streamlit.header('🥣 🥗 Healthy Breakfast Menu🐔 🥑')

streamlit.text('🥣Omega 3 & Blueberry Oatmeal🍞')

streamlit.text('🥗Kale, Spinach & Rocket Soothie🐔')

streamlit.text('🐔Chicken Sausage🥑')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
 
fruits_to_show = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruits_to_show)
                      

