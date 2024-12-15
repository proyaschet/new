import unittest

from service.app import create_app


class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_redact_text_success(self):
        response = self.client.post(
            "/api/redact", json={"text": "John Doe lives at 123 Baker Street."}
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("redacted_text", data)

    def test_missing_text(self):
        response = self.client.post("/api/redact", json={})
        self.assertEqual(response.status_code, 400)
        

if __name__ == "__main__":
    unittest.main()
