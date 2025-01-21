import pandas as pd
import streamlit as st
import json

def main():
    st.title("Attendance JSON Viewer")

    # File uploader for JSON file
    uploaded_file = st.file_uploader("Upload the attendance.json file", type=["json"])

    if uploaded_file is not None:
        try:
            # Load JSON data
            json_data = json.load(uploaded_file)
            
            # Check JSON structure
            if isinstance(json_data, list):  # JSON file contains a list of records
                df = pd.DataFrame(json_data)
            elif isinstance(json_data, dict):  # JSON file contains a dictionary
                df = pd.json_normalize(json_data)
            else:
                st.error("Unsupported JSON structure. Please upload a valid JSON file.")
                return

            # Display the DataFrame
            st.write("Attendance Data:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error processing the JSON file: {e}")

if __name__ == "__main__":
    main()
