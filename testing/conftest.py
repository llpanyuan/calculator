import pytest


def pytest_collection_modifyitems(session, config, items:list):

    # print(items)
    # print(type(items))
    # items.reverse()

    for item in items:
        print(item.nodeid)

        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)

        if 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)