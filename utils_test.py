import unittest
import utils

class TestGenerateOutput(unittest.TestCase):
    def test_generate_output_positive(self):
        results = [
            {'twitter':[
                {'username': '@GuyEndoreKaiser', 'tweet': 'If you live to be 100, you should make up some fake reason why, just to mess with people... like claim you ate a pinecone every single day.'},
                {'username': '@mikeleffingwell', 'tweet': "STOP TELLING ME YOUR NEWBORN'S WEIGHT AND LENGTH I DON'T KNOW WHAT TO DO WITH THAT INFORMATION."}
            ]},
            {'facebook': [
                {'name': 'Some Friend', 'status': "Here's some photos of my holiday. Look how much more fun I'm having than you are!"},
                {'name': 'Drama Pig', 'status': 'I am in a hospital. I will not tell you anything about why I am here.'}
            ]},
            {'instagram': [
                {'username': 'hipster1', 'picture': 'food'},
                {'username': 'hipster2', 'picture': 'coffee'},
                {'username': 'hipster3', 'picture': 'coffee'},
                {'username': 'hipster4', 'picture': 'food'},
                {'username': 'hipster5', 'picture': 'this one is of a cat'}
            ]}
        ]

        expected_output = {
            'twitter': 2,  # 2 tweets
            'facebook': 2,  # 2 facebook statuses
            'instagram': 5  # 5 instagram posts
        }
        expected_errors = []

        output, errors = utils.generate_output(results)
        self.assertEqual(output, expected_output)
        self.assertEqual(errors, expected_errors)

    def test_generate_output_negative(self):
        results = [
            {'twitter':None},
            {'facebook': [
                {'name': 'Some Friend', 'status': "Here's some photos of my holiday. Look how much more fun I'm having than you are!"},
                {'name': 'Drama Pig', 'status': 'I am in a hospital. I will not tell you anything about why I am here.'}
            ]},
            {'instagram': [
                {'username': 'hipster1', 'picture': 'food'},
                {'username': 'hipster2', 'picture': 'coffee'},
                {'username': 'hipster3', 'picture': 'coffee'},
                {'username': 'hipster4', 'picture': 'food'},
                {'username': 'hipster5', 'picture': 'this one is of a cat'}
            ]}
        ]

        expected_output = {
            'facebook': 2,  # 2 facebook statuses
            'instagram': 5  # 5 instagram posts
        }
        expected_errors = ["twitter returned an error"]

        output, errors = utils.generate_output(results)
        self.assertEqual(output, expected_output)
        self.assertEqual(errors, expected_errors)

if __name__ == '__main__':
    unittest.main()


