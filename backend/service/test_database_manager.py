import unittest
from unittest.mock import patch, MagicMock
from database_manager import DatabaseManager
from config import Config

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.config = Config()
        self.db_manager = DatabaseManager(self.config)

    @patch('pyodbc.connect')
    def test_connect(self, mock_connect):
        mock_connect.return_value = MagicMock()
        self.db_manager.connect()
        mock_connect.assert_called_with(self.config.database_url)

    def test_disconnect(self):
        with patch.object(self.db_manager, 'connection', create=True) as mock_connection:
            mock_connection.close = MagicMock()
            self.db_manager.disconnect()
            mock_connection.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
