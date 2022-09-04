import snowflake.connector
import streamlit
import pandas
import requests

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

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json() )


my_cur.execute("insert into fruit_load_list values ('from streamlit')")


#take the json version of response  and normalize it
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)



if streamlit.button('Get Fruit Load List'):
 
 my_cnx = snowflake.connector.connect(user='pc_river_user',password='Alexa@202881',account='ew01286.ap-south-1',application='snowflake')
 #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 my_data_rows = get_fruit_load_list()
 my_cnx.close()
 streamlit.dataframe(my_data_rows)           #streamlit.stop()    #dont run anything Past
                                     
#allow the end user to add fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('guava')")  #jackfruit papaya kiwi guava
    return "Thanks for adding " + new_fruit
  
add_my_fruit = streamlit.text_input('what fruit would you like add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
  
  
#streamlit.write('Thanks for adding', add_fruit_list)


add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      back_from_function = insert_row_snowflake(add_my_fruit)
      streamlit.text(back_from_function)
