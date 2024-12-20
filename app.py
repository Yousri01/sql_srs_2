import io

import duckdb
import pandas as pd
import streamlit as st

csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
result = duckdb.query(answer).df()

with st.sidebar:
    option = st.selectbox(
        "select you an item sql",
        ("join", "group by", "widow function"),
    )
    st.write("You selected:", option)

st.header("enter your code")
query = st.text_area(label="votre code sql ici", key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["table", "solution"])
#
with tab2:
    st.write("table : beverages")
    st.dataframe(beverages)
    st.write("table : food_items")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(result)
##
with tab3:
    st.write(answer)
