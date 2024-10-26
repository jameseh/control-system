import unittest

from src.backend.dataclasses.parameter import Parameter

import dataclasses


class TestParameter(unittest.TestCase):
    """
    Test Parameter class.

    Tests:
        initial value
        set value
        immutable attributes

    Attributes:
        param (Parameter): Parameter object.

    Methods:
        test_initial_value: Test initial value.
        test_set_value: Test set value.
        test_immutable_attributes: Test immutable attributes.
    """

    def setUp(self):
        """
        Set up test environment.
        """

        self.param = Parameter(
                key="test_key",
                default_value=10,
                description="Test parameter"
        )

    def test_initial_value(self):
        """
        Test initial value.
        """

        self.assertEqual(self.param.value, 10)

    def test_set_value(self):
        """
        Test set value.
        """

        self.param.value = 20
        self.assertEqual(self.param.value, 20)

    def test_immutable_attributes(self):
        """
        Test immutable attributes.
        """

        with self.assertRaises(dataclasses.FrozenInstanceError):
            self.param.key = "new_key"
            self.param.default_value = 30
            self.param.description = "New description"


if __name__ == "__main__":
    unittest.main()
