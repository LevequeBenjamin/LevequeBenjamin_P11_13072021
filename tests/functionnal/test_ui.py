"""This module contains a functional test."""

# selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import Driver, BaseFixture


class TestUi(BaseFixture, Driver):
    """Docstrings."""

    def setup_method(self):
        """Docstrings."""
        self.places = "12"

    @staticmethod
    def test_login_ui(driver, database):
        """Docstrings."""
        # the user enters his email and clicks on the "enter" button.
        # it is redirected to the welcome page with the message "Welcome, test1@test.com".

        database.load()

        email_input = driver.find_element_by_name("email")
        email_input.send_keys(database.CLUBS[0]['email'])
        email_input.submit()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Welcome')]"))
        )

        assert f"Welcome, {database.CLUBS[0]['email']}" in driver.page_source

    @staticmethod
    def test_show_summary_ui(driver, database):
        """Docstrings."""
        # The number of places available is displayed and there are 20.
        # The competitions are displayed and and the number is correct.
        # The user clicks on the "booking" link of the "Competition Test 1".
        # And it is redirected to the "booking" page.

        assert f"Points available: {database.CLUBS[0]['points']}" in driver.page_source

        competition_list = driver.find_element_by_class_name("competitions_container")
        competitions = competition_list.find_elements_by_tag_name("li")

        assert len(competitions) == len(database.COMPETITIONS)

        for competition in database.COMPETITIONS:
            assert competition["name"] in driver.page_source

        competitions[0].find_element_by_tag_name("a").click()

    def test_booking_ui(self, driver, database):
        """Docstrings."""
        # The name of the competition and the number of places available is displayed.
        # The user can take between 1 and his number of tickets.
        # He takes 12 tickets.
        # It is redirected to the "welcome" page with the message "booking complete!".

        title = driver.find_element_by_tag_name("h2")

        assert database.COMPETITIONS[0]['name'] in title.text
        assert str(database.COMPETITIONS[0]['numberOfPlaces']) in driver.page_source

        places_input = driver.find_element_by_name("places")

        assert places_input.get_attribute("min") == "1"
        assert places_input.get_attribute("max") == database.CLUBS[0]['points']

        places_input.send_keys(self.places)

        submit_button = driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()

        assert "booking complete!" in driver.page_source

    def test_values_update_ui(self, driver, database):
        """Docstrings."""
        # The 12 tickets have been removed from his account.
        # The 12 places are well removed from the available places of the competition.

        assert f"Points available: {int(database.CLUBS[0]['points']) - int(self.places)}" in driver.page_source

        competition_list = driver.find_element_by_class_name("competitions_container")
        competitions = competition_list.find_elements_by_tag_name("li")

        assert f"Number of Places: {str(database.COMPETITIONS[0]['numberOfPlaces'] - int(self.places))}" in \
               competitions[0].text

    @staticmethod
    def test_logout_ui(driver, database):
        """Docstrings."""
        # The user clicks on the logout button.
        # It is redirected to the "index" page.
        logout_input = driver.find_element_by_class_name("logout")
        logout_input.click()

        assert "GUDLFT Registration" in driver.page_source

    @staticmethod
    def test_club_list_ui(driver, database):
        """Docstrings."""
        # The user clicks on the link "View all registered clubs and respective point count".
        # All clubs are well displayed and the number is correct.
        a_input = driver.find_element_by_tag_name("a")
        a_input.click()

        clubs_list = driver.find_element_by_class_name("clubs_container")
        clubs = clubs_list.find_elements_by_tag_name("li")

        assert len(clubs) == len(database.CLUBS)

        for club in database.CLUBS:
            assert club["name"] in driver.page_source
