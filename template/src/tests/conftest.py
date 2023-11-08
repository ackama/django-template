import os

import pytest

# Playwright runs in an asncio event loop - django's `async_unsafe` decorator checks for
# the existence of an event loop and shouts out if finds one - this turns off the check
# during testing. Not ideal and I'd like it to only apply when playright is used.
os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


def pytest_collection_modifyitems(config, items):
    """
    Performs post-processing on found test items

    This function is called by pytest after test file discovery. We are using it to
    automatically apply a test marker of `functional` to functional tests, `system` to
    system tests. This allows us to isolate test runs for these types of tests.
    """
    functional_test_mark = pytest.mark.functional
    system_test_mark = pytest.mark.system

    for item in items:
        if "tests/functional" in str(item.fspath):
            item.add_marker(functional_test_mark)
        elif "tests/system" in str(item.fspath):
            item.add_marker(system_test_mark)


def pytest_collection_finish(session):
    """
    This function is called by pytest after collection has been performed and modified.
    We are using it to ensure that every test package has an __init__.py file - whilst
    Python 3 technically doesn't need a __init__.py in every package folder this
    sometimes makes pytest unhappy. Pytest itself does some gnarly magic behind the
    scenes which can cause odd test failures if an init file is not present.
    """
    unique_paths = {item.fspath.dirpath() for item in session.items}
    paths_missing_init = []

    for path in unique_paths:
        if not path.join("__init__.py").check():
            paths_missing_init.append(path)

    if paths_missing_init:
        missing_list = "\n".join([str(p) for p in paths_missing_init])
        raise pytest.UsageError(
            "The following test paths are missing an `__init__.py` file. "
            "Please ensure all folders containing tests also contain an `__init__.py` "
            "file."
            f"\n{missing_list}"
        )
