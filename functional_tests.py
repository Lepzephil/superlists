from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):      
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith goes to check out webpage.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        # She is invited to enter a to-do item straight away.

        # She types 'buy peacock feathers' (her hobby is tying fish-flying lures).
        
        # When she hits 'enter' the page updates and now the page lists 
        # 1. ' Buy peacock feathers' as an item in a to-do list.
        
        # There is still a test-box inviting her to add another iterm. She enters 'use peacock feathers to make a fly'
        # (Edith is very methodical).
        
        # The page updates again and now shows both items on her list.
        
        #Wonders whether the site will remember that. But feels better knowing that there is a unique URL. 
        
        # Satisfied, she goes back to sleep.

if  __name__  == '__main__':
    unittest.main(warnings = 'ignore')
