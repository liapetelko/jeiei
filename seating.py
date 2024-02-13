import streamlit as st
import pandas as pd
import base64


file_ = open("C:\steil\pzurim\gifwidefade2.5.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

colT1,colT2 = st.columns([1,13])
with colT2:
    st.markdown(
    "<h1 style='text-align: center;'>מקומות ישיבה / Seating Assignments</h1>", 
    unsafe_allow_html=True
)

st.markdown(
    "<div style='display: flex; justify-content: center;'>"
    f"<img src='data:image/gif;base64,{data_url}'>"
    "</div>", 
    unsafe_allow_html=True
)


st.header("Mixed Pairs / זוגות מעורבים")
st.subheader("10/11/2023")
st.subheader("Session: 2/2 - מושב: 2/2")
st.text("Link to the current results / קישור לתוצאות הנוכחיות")
st.markdown("https://www.bridge.co.il/viewer/total.php?event=22645")

seatings1_list = []
with open ('C:\steil\CSV\Book2.csv','r') as seatings1:
    seatings1 = seatings1.readlines()
    for seat in seatings1:
        fields = seat.strip().split(',')
        place = {}
        place["EW Seat"] = fields[3]
        place["NS Seat"] = fields[2]
        place["מספרי חבר / Number"]=fields[1]
        place["שמות / Names"]=fields[0]
        #place["Hall"]=fields[4]
        
        seatings1_list.append(place)

st.text("")
col_INP1, col_INP2 = st.columns([1,1])
with col_INP1:
    name1 = st.text_input("Search By Name / חיפוש לפי שם")
name1_list= []
for i in seatings1_list:
    if (name1 in i["שמות / Names"]):
        name1_list.append(i)

with col_INP2:
    number1 = st.text_input("Search By Number / חיפוש לפי מספר חבר")
number1_list= []
for j in seatings1_list:
    if (number1 in j["מספרי חבר / Number"]):
        number1_list.append(j)


if (name1!="" and len(name1_list)!=0):
    st.text("Results:")
    st.table(name1_list)
elif (number1!="" and len(number1_list)!=0):
    st.text("Results:")
    st.table(number1_list)
elif not (name1=="" and number1==""):
    st.warning("Try Searching again, either by name, number or have a search in the full list below. If you believe it's a mistake, please contact the organizators.")


st.header("Full List / רשימה מלאה") 
st.table(seatings1_list)




