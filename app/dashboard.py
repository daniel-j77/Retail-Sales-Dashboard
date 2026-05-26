import streamlit as st
import pandas as pd

df=pd.read_csv(
"../data/sales_clean.csv"
)

df["Date"]=pd.to_datetime(
df["Date"]
)

st.title(
"Retail Sales Dashboard"
)

city=st.selectbox(
"City",
["All"]+
list(df.City.unique())
)

if city!="All":
    df=df[df.City==city]

st.metric(
"Total Sales",
f"₹{df['Sales'].sum():,}"
)

st.line_chart(
df.groupby(
df["Date"].dt.month
)["Sales"].sum()
)

st.bar_chart(
df.groupby(
"Product"
)["Sales"].sum()
)

st.dataframe(df)