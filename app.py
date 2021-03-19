import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_echarts, st_pyecharts
from lib.progress_report.pr import progress
from lib.planning.pl import planning
from lib.productivity.report import report

def main():
    st.sidebar.title("Kalkula")
    action = st.sidebar.selectbox("Navigation", ["Productivity", "Planning", "Progress Report", "Chart"])
    if action == "Productivity":
        st.title("Productivity")
        report()
    elif action == "Planning":
        st.title("Planning")
        planning()
    elif action == "Progress Report":
        st.title("Progress Report")
        progress()
    elif action == "Chart":
        st.title("Sample Chart")
        b = (
            Bar()
            .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
            .add_yaxis(
                "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2]
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
                )
            )
        )
        st_pyecharts(b)
        st_echarts({"xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": { "type": "value" },
        "series": [
            {"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "bar" }
        ],})

if __name__ == "__main__":
    main()