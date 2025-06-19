import aipproto


def test_render():
    namespace = aipproto.Namespace("foo.bar.com")
    foo = namespace.resource("Foo")
    bar = foo.nest("BarBaz")

    content = aipproto.generate_file_content(
        package="bar.foo.v1",
        domain="foo.bar.com",
        service_name="TestService",
        resource_types=[foo, bar],
    )
    print("Proto file:\n" + content)
