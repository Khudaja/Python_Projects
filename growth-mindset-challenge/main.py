import streamlit as st
import pandas as pd
# os is used to work with folders and files
import os
#convert file into binary ,and keep them in memory for converting the files. act as a buffer.
from io import BytesIO
 
#setup our App
st.set_page_config(page_title="📀Data Sweeper", layout="wide")
st.title("📀Data Sweeper")
st.write("Transform your files between CSV and Excel formats with biult-in data cleaning and visualization.")

uploaded_file = st.file_uploader("Upload your Files(CSV or Excel):", type=["csv", "xlsx"],
accept_multiple_files = True)
# accept_multiple_files true means you can give multiple csv files in here

if uploaded_file:
    for file in uploaded_file:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file) # read the csv file df= data frame
        elif file_ext == ".xlsx":
                df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file format: {file_ext}")
            continue

#Display info about File

        st.write(f"**FileName:** {file.name}")
        st.write(f"**File Size:** {file.size/1024}")
        st.write(f"**File Type:** {file.type}")

#Shows 5rows of our Data
        
        st.write("Preview the Head of the Dataframe")
        st.dataframe(df.head()) #head() is used to show the first 5 rows of the data frame

#Option for DataCleaning        

        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean data for {file.name}"):
                col1, col2 = st.columns(2)

                with col1:
                        if st.button("Remove Duplicates from {file.name}"):
                         df.drop_duplicates(inplace=True) #drop_duplicates() is used to remove the duplicates from the data frame | alters the state of original data frame
                        st.write("Duplicate Removed!")

                with col2:
                        if st.button(f"Fill missing values for {file.name}"):
                                numeric_cols = df.select_dtypes(include=["number"]).columns
                                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())# fillna() is used to fill the missing values in the data frame
                                st.write("Missing values filled!")

#Choose Specific Column to Convert

        st.subheader("Select columns to convert")
        cloumns = st.multiselect(f"Select columns for {file.name}", df.columns, default=df.columns)
        df = df[cloumns]

#Create some Visualization

        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
                st.bar_chart(df.select_dtypes (include=["number"]).iloc[:,:2])
#convert the file from CSV to excel and vice versa
        st.subheader("Conversion Options")
        conversion_types = st.radio(f"Convert file {file.name} to:", ["CSV", "Excel"], key = {file.name})
        if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                if conversion_types == "CSV":
                        df.to_csv(buffer,  index=False)
                        file.name = file.name.replace(file_ext, ".csv")
                        mime_type = "text/csv"
                elif conversion_types == "Excel":
                        df.to_excel(buffer, index=False)
                        file.name = file.name.replace(file_ext, ".xlsx")
                        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" #mime type is used to identify the type of file
                buffer.seek(0)

#download button
                st.download_button(
                        label = f"Click here to download {file.name} as {conversion_types}",
                        data = buffer,
                        file_name = file.name,
                        mime = mime_type
                )
st.success("All files are processed.")
st.success("Thankyou for using Data Sweeper!")                