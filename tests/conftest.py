import pytest


collect_ignore_glob = ["*/factories.py"]


class BS4Matchers:

    @staticmethod
    def button(tag):
        return (
            tag.name == "button"
            or tag.has_attr("class") and "btn" in tag["class"]
        )


@pytest.fixture
def bs4_matchers():
    return BS4Matchers
