import mysql.connector
import bcrypt

def authenticate_user(username, password):
    """
    Authenticate the user and return their group if successful.
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Homesh@99",
            database="secure_health_db"
        )
        cursor = conn.cursor()



        if result is None:
            print("User not found.")
            return None

        stored_password, user_group = result

        # Convert stored_password to bytes if it is a bytearray
        if isinstance(stored_password, bytearray):
            stored_password = bytes(stored_password)

        # Verify the password using bcrypt
        if bcrypt.checkpw(password.encode(), stored_password):
            return user_group
        else:
            print("Invalid password.")
            return None
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()
