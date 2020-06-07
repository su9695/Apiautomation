import pytest
import allure
import os


@allure.feature('这是一个测试')
def test_al():
    print('hello world')
    assert 1 > 2


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', '../reports'])
