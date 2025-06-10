from smartdotenv import env
import os

def test_env():
    os.environ["TEST_BOOL"] = "true"
    os.environ["TEST_LIST"] = "a,b,c"
    os.environ["TEST_INT"] = "42"
    os.environ["TEST_FLOAT"] = "3.14"
    os.environ["TEST_STR"] = "hello"
    os.environ["TEST_JSON"] = '{"a": 1, "b": [1, 2, 3]}'

    assert env("TEST_BOOL") is True
    assert env("TEST_LIST") == ["a", "b", "c"]
    assert env("TEST_INT") == 42
    assert env("TEST_FLOAT") == 3.14
    assert env("TEST_STR") == "hello"
    assert env("TEST_JSON") == {"a": 1, "b": [1, 2, 3]}
    assert env("NON_EXISTENT", "default") == "default"
