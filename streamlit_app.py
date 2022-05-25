import streamlit
import pandas
import requests
streamlit.title("My First streamlit App")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Banana','Peach'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
if fruits_selected: 
  streamlit.dataframe(fruits_to_show)
else : 
  streamlit.dataframe(my_fruit_list)
  
streamlit.header("Fruitvice response")


fruitvice_response = requests.get("https://www.fruityvice.com/api/fruit/" +"kiwi")
streamlit.text(fruitvice_response.json())#just writes the data to the screen

fruitvice_normalize = pandas.json_normalize(fruitvice_response.json())
streamlit.dataframe(fruitvice_normalize)

fruit_choice = streamlit.text_input('What fruit would you like to know about','kiwi')
streamlit.write('The user entered - 'fruit_choice)
