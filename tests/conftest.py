import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--update-goldens",
        action="store_true",
        default=False,
        help="Update golden files",
    )


@pytest.fixture(scope="session")
def update_goldens(request):
    """Fixture to check if --update-goldens was passed."""
    return request.config.getoption("--update-goldens")
