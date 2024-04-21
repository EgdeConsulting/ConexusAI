import unittest
from database import get_db_connection, close_db_connection

class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        """Test if the database connection is successfully established and can execute a query."""
        conn = None
        try:
            # Attempt to get a database connection
            conn = get_db_connection()
            self.assertIsNotNone(conn, "Failed to establish a database connection")

            # Create a cursor from the connection
            cursor = conn.cursor()

            # Execute a simple query to test the connection
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            self.assertTrue(result is not None, "Query returned no results")

            # Close the cursor
            cursor.close()

        except Exception as e:
            self.fail(f"Database connection test failed with an exception: {e}")
        finally:
            # Ensure the connection is closed after the test
            if conn:
                close_db_connection(conn)

if __name__ == '__main__':
    unittest.main()
