import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am happy")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("I am angry")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_sadness(self):
        result = emotion_detector("I am sad")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = emotion_detector("I am scared")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()