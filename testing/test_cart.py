import pytest


@pytest.fixture(scope='module', autouse=True)
def login():
    print("登录操作")
    username = 'Chris'
    yield username
    print("清空登录操作")


class TestCart:
    def test_cart1(self, login):
        print(f"test_cart1需要登录，登录名为：{login}")

    def test_cart2(self):
        print(f"test_cart2需要登录，登录名为：")

    def test_cart3(self):
        print("test_cart3 不需要登录")

    def test_cart4(self):
        print("test_cart4 不需要登录")


if __name__ == '__main__':
    pytest.main()
