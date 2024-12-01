

def query_data(user_group):
    """
    Retrieve data from the health_info table based on the user's group.
    """
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        if user_group == 'H':
            query = """
            SELECT id, first_name, last_name, gender, age, weight, height, health_history
            FROM health_info
            """
        elif user_group == 'R':
            query = """
            SELECT id, gender, age, weight, height, health_history
            FROM health_info
            """
        else:
            print("Invalid user group.")
            return []

        cursor.execute(query)
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

def update_data(user_group, record_id, updates):
    """
    Update specific fields in the health_info table. Only allowed for Group H.
    """
    if user_group != 'H':
        print("Permission denied: Only Group H users can update data.")
        return False

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        set_clause = ", ".join([f"{column} = %s" for column in updates.keys()])
        values = list(updates.values()) + [record_id]
        query = f"UPDATE health_info SET {set_clause} WHERE id = %s"

        cursor.execute(query, values)
        conn.commit()
        print("Record updated successfully.")
        return True
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False
    finally:
        cursor.close()
        conn.close()

def delete_data(record_id):
    """
    Delete a specific record from the health_info table by its ID.
    """
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "DELETE FROM health_info WHERE id = %s"
        cursor.execute(query, (record_id,))
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False
    finally:
        cursor.close()
        conn.close()
