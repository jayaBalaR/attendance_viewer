import sqlite3
import pandas as pd
import streamlit as st

# Streamlit app
def main():
    st.title("Attendance Database Viewer")

    # Connect to SQLite database
    db_path = 'attendance.db'  # Update with the correct path to your SQLite database
    conn = sqlite3.connect(db_path)

    # Query options
    st.sidebar.header("Query Options")
    table_name = st.sidebar.text_input("Enter Table Name", value="attendance")

    # Query the database
    try:
        if st.sidebar.button("Show Data"):
            query = f"SELECT * FROM {table_name}"
            data = pd.read_sql_query(query, conn)
            st.write(f"Data from the `{table_name}` table:")
            st.dataframe(data)  # Display the data as a table
    except Exception as e:
        st.error(f"Error querying the database: {e}")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
