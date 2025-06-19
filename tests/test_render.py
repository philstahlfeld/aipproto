import aipproto


def test_render():
    namespace = aipproto.Namespace("foo.bar.com")
    foo = namespace.resource("Foo")
    bar = foo.nest("BarBaz")

    content = aipproto.generate_file_content(
        package="bar.foo.v1",
        service_name="TestService",
        resource_types=[foo, bar],
    )
    print("Proto file:\n" + content)
