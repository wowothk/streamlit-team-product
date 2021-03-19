import streamlit as st
import pandas as pd

EMPLOYEE = ["Frey", "Martin", "Fiki", "Arief"]

def _form():
    planning = st.text_input("Planning")
    task_score = st.text_input("Task Score")
    startdate = st.date_input("Start Date")
    enddate = st.date_input("End Date")
    return planning, startdate, enddate

def _submit_form(employee, planning, startdate, enddate):
    filename = "planning_"+employee+".csv"
    df = pd.read_csv(filename)
    input_df = pd.DataFrame([{"planning": planning, 
                            "start_date": startdate, 
                            "end_date": enddate}])
    df = df.append(input_df).reset_index(drop=True)
    df.to_csv(filename, index=False)

def _standard_form(employee):
    planning, startdate, enddate = _form()
    submit = st.button("Submit")
    if submit:
        try:
            _submit_form(employee, planning, startdate, enddate)
            st.success("Success")
        except:
            st.error("Failed")

def planning():
    employee = st.selectbox("Pilih Nama", EMPLOYEE)
    if employee == "Frey":
        _standard_form(employee)
    elif employee == "Martin":
        _standard_form(employee)
    elif employee == "Fiki":
        _standard_form(employee)
    elif employee == "Arief":
        _standard_form(employee)
