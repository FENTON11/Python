import unittest
from roman_converter import roman_to_int


class TestRomanConverter(unittest.TestCase):
    def testConvertZero(self):
        result = roman_to_int("0")
        self.assertEqual(result, 0)

    def testConvertInvalidRomanNumeral(self):
        result = roman_to_int("XXXX")
        self.assertEqual(result, -1)

    def testConvertLargeRomanNumeral(self):
        result = roman_to_int("MMMMCMXCIX")
        self.assertEqual(result, 4999)

    def testConvertRomanNumeralWithLowercaseLetters(self):
        result = roman_to_int("xxiV")
        self.assertEqual(result, 24)

    def testConvertEmptyString(self):
        result = roman_to_int("")
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
