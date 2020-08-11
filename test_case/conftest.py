import pytest


@pytest.fixture()
def actionForClass():
    print("测试类执行测试开始".center(30, '*'))
    yield
    print("测试类执行测试结束".center(30, '*'))


@pytest.fixture(scope="session")
def login():
    print("所有测试文件执行测试开始".center(30, '*'))
    yield
    print("所有测试文件执行测试结束".center(30, '*'))



