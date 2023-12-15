import streamlit as st
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

def plot_histogram(dataframe):
    ans, ax = plt.subplots()
    ax.hist(dataframe['Age'], bins='auto', edgecolor='pink')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    ax.set_title('Question 3')
    return ans



st.header('Upload the file here', divider='rainbow')

uploaded_file = st.file_uploader("Choose a file",type='csv')
if uploaded_file is not None:

    dataframe = pd.read_csv(uploaded_file)
    a=len(dataframe.columns)
    if(a==2):
            ans = plot_histogram(dataframe)
            st.pyplot(ans)

    else:
         st.warning('Upload a csv file with 2 column')

         
