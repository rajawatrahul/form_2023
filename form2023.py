import streamlit as st
import mysql.connector

# Database connection configuration
# mysql-connector-python==8.0.32
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Rajawatr@hul65",
    "database": "voting_form2023"
}


# Create a table for user data
def create_table():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            polling_station VARCHAR(255),
            serial_number INT,
            caste VARCHAR(255),
            profession VARCHAR(255),
            party VARCHAR(255)
        )
    """)
    conn.commit()
    conn.close()


# Insert user data into the database
def insert_data(polling_station, serial_number, caste, profession, party):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    insert_query = """
        INSERT INTO user_data (polling_station, serial_number, caste, profession, party)
        VALUES (%s, %s, %s, %s, %s)
    """
    data = (polling_station, serial_number, caste, profession, party)
    cursor.execute(insert_query, data)
    conn.commit()
    conn.close()


def main():
    st.title('Polling Data Submission')

    create_table()

    # Form input fields
    ps = st.text_input('Polling Station')
    sr = st.number_input('Serial Number', min_value=1, max_value=5000)
    cast = st.text_input('Caste')
    prof = st.text_input('Profession')
    par = st.radio('Party', ['Cong', 'Bjp', 'Bsp', 'xxx'])

    if st.button("Submit"):
        # Check if any field is empty
        if ps == '' or sr == 0 or cast == '' or prof == '' or par == '':
            st.warning("Please fill in all details before submitting.")
        else:
            # Insert data into MySQL database
            insert_data(ps, sr, cast, prof, par)
            st.success("Data submitted successfully!")


if __name__ == '__main__':
    main()
