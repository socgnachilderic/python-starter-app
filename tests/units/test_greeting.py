from app.greeting import greeting


def test_greeting() -> None:
    assert greeting("hello world") == "Hello world"
