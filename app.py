import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
import os

from ydata_profiling import ProfileReport

from pycaret.classification import setup, compare_models,pull, save_model

rare_threshold = 1     # minimum number of samples per category


def clean_df(df):
    #for classification model
    df = df.dropna(subset=[target])
    #   Convert numeric columns stored as object
    for col in df.select_dtypes(include=['object']):
        df[col] = pd.to_numeric(df[col], errors='ignore')
    #   Convert remaining object columns to categorical
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].astype('category')
    #   Drop categorical columns with <2 unique values
    for col in df.select_dtypes(include=['category']):
        if df[col].nunique() < 2:
            df = df.drop(columns=[col])
    #   Fill numeric missing values with mean
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    return df

with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("AutoStreamML")
    choice = st.radio("Navigation",["Upload", "Profiling","ML","Download"])
    st.info("This application allows you to build automated ML pipeline using StreamLit, Pandas profiling and pycaret")


if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col = None)

if choice ==  "Upload":
    st.title("Upload your Data for Modelling!")
    file =st.file_uploader("Upload your dataset here")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("sourcedata.csv", index=None)
        st.dataframe(df)

if choice == "Profiling":
    st.title("Automated exploratory Data analisys")
    profile_report = ProfileReport(df, explorative=True)
    html(profile_report.to_html(), height=1000, scrolling=True)

if choice == "ML":
    st.title("Machine Learning go for experimental model")
    target = st.selectbox("Select your Target",df.columns)
    if st.button("Train experimental model"):
        df=clean_df(df)
        setup(df, target = target , verbose=False, html=False)
        setup_df = pull()
        st.info("This is the ML Experiment settings")
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.info("This is the ML Model")
        st.dataframe(compare_df)
        best_model
        save_model(best_model, 'best_model')

if choice == "Download":
    with open("best_model.pkl", 'rb') as f:
            st.download_button("Download the Model",f,"trained_model.pkl")
