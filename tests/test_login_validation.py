import pytest

from utilities.file_reader import read_csv

@pytest.mark.smoke
@pytest.mark.regression
def test_login_page_loads(home_page, login_page) -> None:
    home_page.open()
    home_page.go_to_login()
    login_page.verify_loaded()


@pytest.mark.parametrize("credentials", read_csv("test_login.csv"))
def test_login_validation(home_page, login_page, landing_page, credentials: dict) -> None:
    home_page.open()
    home_page.go_to_login()
    login_page.verify_loaded()
    login_page.login(credentials["email"], credentials["password"])
    print(f"Testing login with email: {credentials['email']} and password: {credentials['password']}");
    if credentials["type"] == "valid":
        landing_page.verify_logged_in(credentials["expected_message"])
    else:
        login_page.verify_login_error(credentials["expected_message"])



