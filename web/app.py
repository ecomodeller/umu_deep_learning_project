import streamlit as st
import numpy as np
import pandas as pd


def app2():

     st.sidebar.subheader("Settings")

     if st.checkbox("Show code"):
          st.code("""
          def foo(x):
               return x**2
          """)

     "# End of the world app"

     if st.checkbox('Show list'):
          """
          * Foo
          * Bar
          * Baz
          """
     st.radio("Regulariation",["None","L1","L2"])

def app1():

     st.sidebar.subheader("Settings")

     slope = st.sidebar.slider('slope',min_value=-10.0,max_value=10.0,step=0.25,value=0.0)

     "# Hello world app"

     x = np.linspace(0,10)
     y = slope*x

     if st.checkbox('Show list'):
          """
          * Foo
          * Bar
          * Baz
          """

     chart_data = pd.DataFrame(y,
          columns=['y'])
     st.line_chart(chart_data)

qp = st.experimental_get_query_params()




app_mode = st.sidebar.selectbox("Select app:", options=["First","Second"])



if app_mode == "First":
     app1()
else:
     app2()

