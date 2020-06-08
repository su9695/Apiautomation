import pytest


@pytest.fixture()
def action():
    print("测试开始".center(30,'*'))
    yield
    print("测试结束".center(30,'*'))