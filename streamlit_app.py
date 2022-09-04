import streamlit

streamlit.title('🥭Mommies Healthy Recepies')

streamlit.header('🥣 🥗 Healthy Breakfast Menu🐔 🥑')

streamlit.text('🥣Omega 3 & Blueberry Oatmeal🍞')

streamlit.text('🥗Kale, Spinach & Rocket Soothie🐔')

streamlit.text('🐔Chicken Sausage🥑')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
 
streamlit.dataframe(my_fruit_list)
                      

 #New Section to Display
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

l
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json() )

#take the json version of response  and normalize it
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

