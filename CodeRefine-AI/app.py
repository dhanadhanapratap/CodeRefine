import streamlit as st
from streamlit_ace import st_ace
import plotly.express as px

from ai_engine import *
from github_analyzer import *
from visualizer import *

st.set_page_config(page_title="CodeRefine AI Pro",layout="wide")

# Modern Developer Theme
st.markdown("""
<style>

.main {
background-color:#0F172A;
color:white;
}

.sidebar .sidebar-content {
background:#020617;
}

h1,h2,h3{
color:#6366F1;
}

</style>
""",unsafe_allow_html=True)

st.title("🚀 CodeRefine AI Pro")
st.caption("AI Powered Developer Intelligence Platform")

# Sidebar
menu = st.sidebar.radio("Developer Tools",[
"Code Analyzer",
"Code Converter",
"Security Scanner",
"GitHub Analyzer",
"Architecture Visualizer",
"Bug Heatmap",
"AI Chat"
])

# Code Editor
code = st_ace(
value="print('Hello CodeRefine AI')",
language="python",
theme="monokai",
height=300
)

language = st.selectbox(
"Programming Language",
["Python","JavaScript","Java","C++","Go","Rust"]
)

# -------------------------
# CODE ANALYZER
# -------------------------

if menu=="Code Analyzer":

    col1,col2,col3 = st.columns(3)

    with col1:
        if st.button("Review Code"):
            st.write(review_code(code,language))

    with col2:
        if st.button("Debug Code"):
            st.write(debug_code(code))

    with col3:
        if st.button("Auto Fix"):
            st.write(auto_fix(code))

    st.divider()

    if st.button("Complexity Analysis"):

        result = complexity_analysis(code)

        st.write(result)

        metrics = {
        "Metric":["Time","Space"],
        "Value":[3,2]
        }

        fig = px.bar(metrics,x="Metric",y="Value")

        st.plotly_chart(fig)

# -------------------------
# CODE CONVERTER
# -------------------------

elif menu=="Code Converter":

    target = st.selectbox(
    "Convert To",
    ["Python","JavaScript","Java","C++","Go","Rust"]
    )

    if st.button("Convert Code"):

        st.write(convert_code(code,target))

# -------------------------
# SECURITY
# -------------------------

elif menu=="Security Scanner":

    if st.button("Scan Security"):

        st.write(security_scan(code))

# -------------------------
# GITHUB ANALYZER
# -------------------------

elif menu=="GitHub Analyzer":

    repo = st.text_input("GitHub Repo URL")

    if st.button("Analyze Repo"):

        data = analyze_repo(repo)

        st.write(data)

        chart = px.bar(
        x=["Stars","Forks","Issues"],
        y=[data["Stars"],data["Forks"],data["Open Issues"]]
        )

        st.plotly_chart(chart)

# -------------------------
# ARCHITECTURE VISUALIZER
# -------------------------

elif menu=="Architecture Visualizer":

    st.subheader("Project Architecture")

    graph = generate_architecture()

    st.graphviz_chart(graph)

# -------------------------
# BUG HEATMAP
# -------------------------

elif menu=="Bug Heatmap":

    heat = bug_heatmap(code)

    fig = px.imshow([heat],color_continuous_scale="reds")

    st.plotly_chart(fig)

# -------------------------
# AI CHAT
# -------------------------

elif menu=="AI Chat":

    question = st.text_input("Ask AI about code")

    if st.button("Ask"):

        st.write(ask_ai(question))