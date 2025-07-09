import pathlib
import aipproto

_GOLDEN_FILES_DIR = pathlib.Path(__file__).parent / "testdata" / "v1"


def test_generate_file_content(update_goldens):
    namespace = aipproto.Namespace("foo.bar.com")
    foo = namespace.resource("Foo",
        config=aipproto.ResourceConfig(
            custom_methods=[
                aipproto.CustomMethod(name="Archive"),
                aipproto.CustomMethod(name="Sort", collection_based=True),
            ]
        ),
    )
    bar = foo.nest(
        "BarBaz",
        config=aipproto.ResourceConfig(
            custom_methods=[
                aipproto.CustomMethod(name="Archive"),
                aipproto.CustomMethod(name="Sort", collection_based=True),
            ]
        ),
    )

    content = aipproto.generate_file_content(
        package="tests.testdata.v1",
        service_name="TestService",
        resource_types=[foo, bar],
        java_outer_classname="GoldenProto",
    )

    golden_file_path = _GOLDEN_FILES_DIR / "golden.proto"
    if update_goldens:
        golden_file_path.write_text(content)
        print(f"Updated golden file: {golden_file_path}")
    else:
        assert (
            content == golden_file_path.read_text()
        ), f"Generated content doesn't match golden. Run with --update-goldens to update the golden file."
