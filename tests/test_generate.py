import pathlib
import aipproto
import pytest

_GOLDEN_FILES_DIR = pathlib.Path(__file__).parent / "testdata"


def test_generate_file_content(update_goldens):
    namespace = aipproto.Namespace("foo.bar.com")
    foo = namespace.resource("Foo")
    bar = foo.nest("BarBaz")

    content = aipproto.generate_file_content(
        package="bar.foo.v1",
        service_name="TestService",
        resource_types=[foo, bar],
    )

    golden_file_path = _GOLDEN_FILES_DIR / "golden.proto"
    if update_goldens:
        golden_file_path.write_text(content)
        print(f"Updated golden file: {golden_file_path}")
    else:
        assert (
            content == golden_file_path.read_text()
        ), f"Generated content doesn't match golden. Run with --update-goldens to update the golden file."


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
