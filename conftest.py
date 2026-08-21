from pathlib import Path

import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from utilities.file_reader import CONFIG


@pytest.fixture
def home_page(page) -> HomePage:
    return HomePage(page, CONFIG["base_url"])


def pytest_addoption(parser):
    parser.addoption("--enable-tracing", action="store_true", help="Enable Playwright tracing")


@pytest.fixture(autouse=True)
def trace_test(context, request):
    tracing_enabled = request.config.getoption("--enable-tracing")

    if tracing_enabled:
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield

    if tracing_enabled:
        trace_dir = Path("traces")
        trace_dir.mkdir(exist_ok=True)
        context.tracing.stop(path=str(trace_dir / f"{request.node.name}.zip"))


@pytest.fixture
def cart_page(page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def landing_page(page) -> LandingPage:
    return LandingPage(page)
