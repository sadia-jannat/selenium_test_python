import pytest


@pytest.mark.login
def test_regression():
    print("regression test")

@pytest.mark.login
def test_sanity():
    print("regression test")

@pytest.mark.login
@pytest.mark.form    
def test_function():
    print("regression test")


@pytest.mark.form
def test_api():
    print("regression test")            