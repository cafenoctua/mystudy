from ..backend_py import test

def test_answer():
    assert test.main() == 'test'