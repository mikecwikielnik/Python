# CHAPTER 11 
"""Testing your code. """


def get_formatted_name(first_name, last_name):
    """Generate a neatly formatted full name. """
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# from name_function import get_formatted_name

print("Enter 'q' at any time to quit. ")

while True:
    first = input("\nPlease give me a first name: ")
    if first == "q":
        break
    last = input("Please give me a last name: ")
    if last == "q":
        break
    
formatted_name = get_formatted_name(first, last)
print(f"\n Neatly formatted name: {formatted_name}.")

# A Passing Test

from ctypes import FormatError
import unittest
from urllib import response 

# from name_function immport get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for get_formatted_name. """
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
if __name__ == '__main__':        # for some reason, this program causes problems. 
    unittest.main()
    

def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name. """
    full_name = f"{first} {middle} {last}"
    return full_name


def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name. """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {middle} {last}"
    return full_name.title()



# Adding a new test

import unittest

class NamesTestCase(unittest.TestCase):
    """Tests for get_formatted_name """
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work? """
        
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work? """
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Mozart Amadeus')
        
if __name__ == '__main__':
    unittest.main()


# 11-1, 11-2 were not done because of the errors in the terminal when running tests in the file so far. 



# Testing a class


# A class to Test


class AnonymousSurvey:
    """Collect anonymous answers to a survey question. """
    
    def __init__(self, question):
        """Store a question, and prepare to store responses. """
        self.question = question
        self.responses = []
        
    def shou_question(self):
        """Show the survey question. """
        print(self.question)
        
    def store_response(self, new_response):
        """Store a single response to the survey. """
        self.responses.append(new_response)
        
    def show_results(self):
        """Show all the responses that have been given. """
        print("Survey Results:")
        for response in self.responses:
            print(f"- {response}")
            
# from survey import AnonymousSurvey 

# Define a question, and make a survey 

question = 'What language did you first learn to speak? '
my_survey = AnonymousSurvey(question)

# Show a question, and store the responses to the question 

my_survey.shou_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
   
# Show the survey results 

print("\nThank you to everyone who took the surver! ")
my_survey.show_results()


# Testing the AnonymousSurvey Class

import unittest
# from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvery. """
    
    def test_store_single_response(self):
     """Test that a single response is stored properly. """
     question = "What language did you first learn to speak? "
     my_survey = AnonymousSurvey(question)
     my_survey.store_response('English')
     self.assertIn('English', my_survey.responses)
     
# if __name__ == '__main__':    # This program still generates errors
#     unittest.main()


import unittest
# from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
       
    def test_store_single_response(self):
        """Test that a single response is stored properly. """
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    def test_store_three_responses(self):
           """Test that three individual responses are stored properly."""
           question = "What language did you first learn to speak?"
           my_survey = AnonymousSurvey(question)    
           responses = ['English', 'Spanish', 'Mandarin']
           for response in responses:
               my_survey.store_response(response)
           for response in responses:
               self.assertIn(response, my_survey.responses)

# if __name__ == '__main__':
#     unittest.main()
    
    

