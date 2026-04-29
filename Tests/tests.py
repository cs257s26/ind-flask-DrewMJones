from app import *
import unittest

class TestRoutes(unittest.TestCase):
    def test_start_route(self):
        """This tests the homepage routing. It sees if it has the instructions on it.
         It also checks if the other routes has not been called"""

        self.app = app.test_client() 
        response = self.app.get('/', follow_redirects=True) 

        # This tests that the deafult instruction page routes to these instructions.
        self.assertEqual(b'Hi please enter /city/city-name/prefered-search-radius/number of species members/ or /leaderboard/common name of animal/.', response.data) 

        # This demonstrates that the other routes have not been called. These words are specific to the other routing outcomes.
        self.assertNotIn(b'Leaderboard', response.data)
        self.assertNotIn(b'observations within', response.data)

    def test_leaderboard_route(self):
        """This creates a new test application and runs tests on it. It checks if the response data 
        contains information congruent to the HTTPS leaderboard request."""

        self.app = app.test_client() 
        response = self.app.get('/leaderboard/Muskrat/', follow_redirects=True) 

        # These are the equivalence cases, with the starts of the output sections and the end of the output tested.
        self.assertIn(b'Muskrat', response.data) 
        self.assertIn(b'|1|Count:102 User:tefetro', response.data)
        self.assertIn(b'|100|Count:4 User:wide_eyed_outside', response.data)  
        self.assertIn(b'      1931 Muskrat sightings', response.data)
        self.assertIn(b'              LEADERBOARD', response.data)
        
        # These only show up in the other routing senarios, such as a different animal and the species routing.
        self.assertNotIn(b'Common Loon', response.data)
        self.assertNotIn(b'observations within', response.data)
        
        # This tests if the common_name input error and subsequent error handling results in the proper output.
        response = self.app.get('/leaderboard/common_name/', follow_redirects=True) 
        self.assertEqual(b"The common_name species does not exist, please try again.", response.data)



    def test_top_species_route(self):
        """Here we test the leaderboard routing. Edge and equivelence cases are tested."""

        self.app = app.test_client() 
        response = self.app.get('/city/Minneapolis/3/3/', follow_redirects=True) 

        # Given the previous HTTPS, these results should come up. These tests encapsualte the classes of animal and one animal from each class.
        self.assertIn(b'Found 25831 observations within 3 miles of Minneapolis:', response.data) 
        self.assertIn(b'American Toad (Anaxyrus americanus): 85 observations', response.data)

        # The bird class:
        self.assertIn(b'Aves:', response.data)  
        self.assertIn(b'Canada Goose (Branta canadensis): 663 observations', response.data)

        # The insect class:
        self.assertIn(b'Insecta:', response.data)
        self.assertIn(b'Brown-belted Bumble Bee (Bombus griseocollis): 472 observations', response.data)

        # The mammal class:
        self.assertIn(b'Mammalia:', response.data)
        self.assertIn(b'Red Fox (Vulpes vulpes): 94 observations', response.data) 

        # The reptile class: 
        self.assertIn(b'Reptilia:', response.data)
        self.assertIn(b'Painted Turtle (Chrysemys picta): 111 observations', response.data)
        
        # Incorrect hings that would come up if a different animal/route was called.
        self.assertNotIn(b'Muskrat', response.data)
        self.assertNotIn(b'Leaderboard', response.data)

        # Testing for failure to find city error handeling.
        response = self.app.get('/city/Milodoe/9/9/', follow_redirects=True) 
        self.assertEqual(b"Could not geocode 'Milodoe'.", response.data)

        # Testing that a city doesn't have anyrhing with in Minnesota surrounding.
        response = self.app.get('/city/Cairo/9/9/', follow_redirects=True) 
        self.assertEqual(b"No observations found near 'Cairo'. Make sure your location is in Minnesota.", response.data)



    def test_the_unexpected(self):
        """This tests what happends when we input HTTPS that will not cause a proper routing. """

        self.app = app.test_client() 
        response = self.app.get('/Wrong/thing/inccorect/not_present/', follow_redirects=True) 

        # This tests the the output wanted when an input that does not adhere to any of the routing guidlines occurs.
        self.assertEqual(b"The URL input is incorrectly formatted, /city/city-name/prefered search radius/number of species members/ or /leaderboard/common name of animal/ is needed.", response.data)

        # This tests that the other routing situations are not called when a completely incorrect HTTP is entered.
        self.assertNotEqual(b"observations within", response.data)
        self.assertNotEqual(b"LEADERBOARD", response.data)





