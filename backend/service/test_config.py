import unittest
from config import Config

class TestConfig(unittest.TestCase):
    """ Enhetstester for Config-klassen. """

    def test_config_loading(self):
        """ Tester at konfigurasjonsverdiene blir lastet som forventet. """
        config = Config()
        self.assertIsNotNone(config.openai_api_key)
        self.assertIsNotNone(config.database_url)
        self.assertIn("SERVER=", config.database_url)

if __name__ == '__main__':
    unittest.main()
