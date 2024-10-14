import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# Set the page title
st.set_page_config(page_title="Multi-Page Dashboard", layout="wide")

# Define the page options for the sidebar
page = st.sidebar.selectbox("Select an option", ["Home", "Seaborn Charts", "Plotly Charts"])
st.title(f"Welcome to the {page} page!")

# Display content based on the selected page
if page == "Home":
    st.write("This is the home page. Select a page from the sidebar to view the charts.")

elif page == "Seaborn Charts":
    st.header("Seaborn Charts")

    # Load dataset
    iris = sns.load_dataset("iris")

    # Create columns for better layout
    col1, col2 = st.columns(2)

    # Content of column 1
    with col1:
        # Create a Scatter Plot
        st.subheader("Scatterplot")
        fig, ax = plt.subplots()
        sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species", ax=ax)
        st.pyplot(fig)

        # Create a Heatmap
        st.subheader("Heatmap")
        corr_matrix = iris.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    # Content of column 2
    with col2:
        # Create a Histogram
        st.subheader("Histogram")
        fig, ax = plt.subplots()
        sns.histplot(data=iris, x="sepal_length", bins=10, ax=ax)
        st.pyplot(fig)

elif page == "Plotly Charts":
    st.header("Plotly Charts")

    # Load dataset
    iris = px.data.iris()

    # Create a Scatter Plot
    st.subheader("Scatterplot")
    scatter_fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
    st.plotly_chart(scatter_fig)

    # Create a Bar Plot
    st.subheader("Bar Chart")
    bar_fig = px.bar(iris, x="species", y="sepal_width", color="species")
    st.plotly_chart(bar_fig)

    # Create a Line Plot
    st.subheader("Line Plot")
    line_fig = px.line(iris, x="sepal_length", y="sepal_width", color="species")
    st.plotly_chart(line_fig)

# Additional Metrics Section
if page != "Home":
    st.subheader("Key Metrics")
    st.metric(label="Average Sepal Length", value=round(iris['sepal_length'].mean(), 2))
    st.metric(label="Average Sepal Width", value=round(iris['sepal_width'].mean(), 2))
    st.metric(label="Species Count", value=len(iris['species'].unique()))
