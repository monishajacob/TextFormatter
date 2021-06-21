import unittest
import json
from main import app


class TestJsonInput(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_valid_input(self):
        payload = {"string_to_cut": "iamyourlyftdriver"}
        response = self.client.post('/test', data=json.dumps(payload))
        response_data = response.get_json(force=True)
        self.assertEqual(response_data["return_string"], "muydv")

    def test_multiple_key(self):
        payload = {"string_to_cut": "i", "testing": "fake"}
        response = self.client.post('/test', data=json.dumps(payload))
        self.assertIn(b"Only 1 Key \'string_to_cut\' should be present.", response.data)

    def test_invalid_value(self):
        payload = {"string_to_cut": "i"}
        response = self.client.post('/test', data=json.dumps(payload))
        self.assertIn(b'The value has Insufficient Length', response.data)

    def test_invalid_key(self):
        payload = {"string_t0_cut": "test"}
        response = self.client.post('/test', data=json.dumps(payload))
        self.assertIn(b"Make sure the key is \'string_to_cut\'", response.data)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
