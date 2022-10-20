import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Yes'), 'Oui')
        self.assertEqual(english_to_french(''), None)
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Oui'), 'Yes')
        self.assertEqual(french_to_english(''), None)
        self.assertEqual(french_to_english(None), None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        
unittest.main()