import pandas as pd
import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts, st_echarts

EMP = ["Frey", "Martin", "Fiki", "Arief"]
df = pd.read_csv("progress01.csv")

def _set_completion(df):
    df.loc[df["status"] == "Done", "Completion"] = 100
    df.loc[(df["status"] == "Break")|(df["status"] == "To Do"), "Completion"] = 0
    df.loc[df["status"] == "On Progress", "Completion"] = 50
    return df

def _task_completion(df, task):
    df = df[df["task"] == task]
    completion = df["Completion"].iloc[-1]
    return completion

def _planning_completion(df, planning):
    df = df[df["planning"] == planning]
    done_date = df["datetime_report"].iloc[-1]
    compl = []
    for i in df["task"].unique():
        compl.append(_task_completion(df, i))

    completion = sum(compl)/df["task_score"].iloc[-1]
    timedelta = done_date - df["end_date"].iloc[-1]
    if completion == 100:
        if timedelta.days > 0:
            status_completion = "Overdue"
        elif timedelta.days < 0:
            status_completion = "In Time"
        else:
            status_completion = "On Time"
    else:
        status_completion = "On Progress"

    ret = {
        "name": df["nama"].iloc[-1], 
        "planning": planning, 
        "completion": completion, 
        "status_completion": status_completion, 
        "report_date": done_date
    }
    return ret

def planning_summary(df):
    plans = df["planning"].unique()
    summary = []
    for i in plans:
        summary.append(_planning_completion(df, i))
    
    ret = pd.DataFrame(summary)
    return ret

def bar_status_completion(planning_summary):
    df = planning_summary[planning_summary["status_completion"] != "On Progress"]
    counting = df["status_completion"].value_counts()
    xaxis = counting.index.tolist()
    yaxis = counting.tolist()
    st_echarts({
        "title": {
            "text": "Planning Completion"
        },
        # "legend": {
        #     "data": ['completion']
        # },
        "xAxis": {
            "type": "category",
            "data": xaxis
        },
        "yAxis": { "type": "value" },
        "series": [
            {"data": yaxis, "type": "bar" }
        ],
    })

def _open_csv(name):
    df = pd.read_csv("progress01.csv")
    ndf = df[df["nama"] == name]
    return ndf

def report():
    emp = st.selectbox("Select", EMP)
    df = _set_completion(_open_csv(emp))
    df["datetime_report"] = pd.to_datetime(df["datetime_report"])
    df["start_date"] = pd.to_datetime(df["start_date"])
    df["end_date"] = pd.to_datetime(df["end_date"])
    df["datetime_report"] = pd.to_datetime(df["end_date"])
    if emp == "Frey":
        plan_sum = planning_summary(df)
        bar_status_completion(plan_sum)
    elif emp == "Martin":
        plan_sum = planning_summary(df)
        bar_status_completion(plan_sum)
    elif emp == "Fiki":
        # plan_sum = planning_summary(df)
        # bar_status_completion(plan_sum)
        pass
    elif emp == "Arief":
        # plan_sum = planning_summary(df)
        # bar_status_completion(plan_sum)
        pass