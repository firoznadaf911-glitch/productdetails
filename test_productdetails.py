import unittest
from io import StringIO
from unittest.mock import patch
from productdetails import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        """Set up a standard Product instance before each test."""
        self.product = Product(
            product_id=101,
            name="Wireless Mouse",
            category="Electronics",
            price=29.99,
            stock=45,
        )

    def test_product_initialization(self):
        """Verify that attributes are properly assigned on initialization."""
        self.assertEqual(self.product.product_id, 101)
        self.assertEqual(self.product.name, "Wireless Mouse")
        self.assertEqual(self.product.category, "Electronics")
        self.assertAlmostEqual(self.product.price, 29.99)
        self.assertEqual(self.product.stock, 45)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_details_output(self, mock_stdout):
        """Verify that display_details prints the exact expected format."""
        self.product.display_details()

        expected_output = (
            "--- Product Details ---\n"
            "ID       : 101\n"
            "Name     : Wireless Mouse\n"
            "Category : Electronics\n"
            "Price    : $29.99\n"
            "In Stock : 45 units\n"
            "-----------------------\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_price_formatting_whole_number(self, mock_stdout):
        """Verify that whole number prices are formatted to two decimal places."""
        whole_price_product = Product(102, "USB Cable", "Accessories", 10, 100)
        whole_price_product.display_details()

        self.assertIn("Price    : $10.00", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_zero_stock_display(self, mock_stdout):
        """Verify behavior when stock is zero."""
        out_of_stock_product = Product(103, "Webcam", "Electronics", 59.5, 0)
        out_of_stock_product.display_details()

        self.assertIn("In Stock : 0 units", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()