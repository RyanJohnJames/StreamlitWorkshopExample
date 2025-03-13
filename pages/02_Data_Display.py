import streamlit as st
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data display", page_icon="📊", layout="centered")

st.title("Data display example")

st.warning("NOTE: Most data here is generated using the random library to generate dummy values!")

st.header("st.json()")
with st.echo():
    st.json({"config": {"timeout": 30, "retries" : 3 }})

st.divider()


st.header("st.dataframe()")

with st.echo():
    # creating a data frame and storing it in a var
    df = pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
            "stars": [random.randint(0, 1000) for _ in range(3)],
            "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
        }
    )
    st.dataframe(
    df, # Var for the data
    column_config={  # Simple config, replacing the key of each vaule to the title (e.g. "name" is changed to "App Name")
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn( # converts the values and translate it into a line cart
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
    )

st.divider()

st.header("st.table()")

with st.echo():
    # Generatiing random values for the data.
    df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)
    st.table(df)


st.divider()

st.header("st.line_chart()")

with st.echo():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"]) 
    st.line_chart(chart_data)

st.divider()

st.header("st.area_chart()")

with st.echo():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)


st.divider()

st.header("st.bar_chart()")

with st.echo():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)

st.write("Yes, I am reusing the same dataset.")

st.divider()

st.header("st.pyplot()")

with st.echo():
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig)


st.divider()

st.header("st.map()")

with st.echo():
    df = pd.DataFrame(
        {
            
            "lat": np.random.normal(38.897957, 0.01, 1000),  
            "lon": np.random.normal(-77.036560, 0.01, 1000)
        }
    )
    st.map(df)

st.write("That's all, feel free to check the offical documation to see more ways to display data!")
st.subheader("[Data Element](https://docs.streamlit.io/develop/api-reference/data)")
