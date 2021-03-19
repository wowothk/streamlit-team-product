import streamlit as st
import pandas as pd

# FILE = pd.read_csv("progress.csv")
EMPLOYEE = ["Frey", "Martin", "Fiki", "Arief"]

def _form(listplanning):
    plan = st.selectbox("Planning", listplanning)
    datetime = st.date_input("Datetime Report")
    task = st.text_input("Task")
    status = st.selectbox("Status", ["To Do", "On Progress", "Done", "Break"])
    kendala = st.text_area("kendala")
    keterangan = st.text_area("keterangan")

    return {
        "planning": plan,
        "datetime_report": datetime,
        "task": task,
        "status": status,
        "kendala": kendala,
        "keterangan": keterangan
    }

def _submit_progress(nama):
    filename = "planning_"+nama+".csv"
    file_planning = pd.read_csv(filename)
    list_plan = file_planning["planning"].tolist()
    data = _form(list_plan)
    selected_plan = file_planning.loc[file_planning["planning"] == data["planning"]]
    start_date = selected_plan["start_date"][0]
    end_date = selected_plan["end_date"][0]
    df = pd.read_csv("progress.csv")
    input_df = pd.DataFrame([{
        "nama": nama,
        "planning": data["planning"],
        "start_date": start_date,
        "end_date": end_date,
        "datetime_report": data["datetime_report"],
        "task": data["task"],
        "status": data["status"],
        "kendala": data["kendala"],
        "keterangan": data["keterangan"]
    }])
    df = df.append(input_df).reset_index(drop=True)
    submit = st.button("Submit")
    if submit:
        try:
            df.to_csv("progress.csv", index=False)
            st.success("Success")
        except:
            st.error("Failed")

def progress():
    nama = st.selectbox("Name", EMPLOYEE)
    if nama == "Frey":
        _submit_progress(nama)
    elif nama == "Martin":
        _submit_progress(nama)
    elif nama == "Fiki":
        _submit_progress(nama)
    elif nama == "Arief":
        _submit_progress(nama)
