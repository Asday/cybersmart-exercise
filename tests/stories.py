import django.urls

from bs4 import BeautifulSoup
import pytest

from .locations.factories import Location
from .tasks.factories import Task
from .weather_reports.factories import WeatherReport


@pytest.mark.django_db
def homepage_to_add_tasks_form(client, bs4_matchers):
    # GIVEN I am on the TODO list application
    tasks_response = client.get(django.urls.reverse("website:tasks"))
    assert tasks_response.status_code == 200
    tasks = BeautifulSoup(str(tasks_response.content), features="html5lib")

    # WHEN I click on the add tasks button
    add_task_button = tasks.find(
        lambda t: bs4_matchers.button(t) and "add task" in t.text.lower(),
    )
    assert add_task_button is not None
    assert add_task_button.has_attr("href")

    # THEN I should be presented with an add tasks form
    add_task_response = client.get(add_task_button["href"])
    assert add_task_response.status_code == 200
    add_task = BeautifulSoup(
        str(add_task_response.content),
        features="html5lib",
    )

    assert add_task.find("form") is not None


@pytest.mark.django_db
def homepage_to_edit_tasks_form(client):
    task = Task.create()

    # GIVEN I am on the TODO list application
    tasks_response = client.get(django.urls.reverse("website:tasks"))
    assert tasks_response.status_code == 200
    tasks = BeautifulSoup(str(tasks_response.content), features="html5lib")

    # WHEN I click on an specific task
    task_url = (
        tasks
        .find(lambda t: (
            t.has_attr("class")
            and "card-header" in t["class"]
            and task.name.lower() in t.text.lower()
        ))
        .find_parent(lambda t: (
            t.name.strip("\\n") == "a"
            and t.has_attr("href")
        ))
    )
    assert task_url is not None
    task_detail_response = client.get(task_url["href"])
    assert task_detail_response.status_code == 200
    task_detail = BeautifulSoup(
        str(task_detail_response.content),
        features="html5lib",
    )
    # AND click edit this task
    task_edit_url = (
        task_detail
        .find(lambda t: (
            t.name.strip("\\n") == "a"
            and t.has_attr("href")
            and "edit this task" in t.text.lower()
        ))
    )
    assert task_edit_url is not None
    edit_task_response = client.get(task_edit_url["href"])
    assert edit_task_response.status_code == 200
    edit_task = BeautifulSoup(
        str(edit_task_response.content),
        features="html5lib",
    )

    # THEN I should be presented with an edit tasks form
    assert edit_task.find("form") is not None


@pytest.mark.django_db
def add_edit_tasks_location_dropdown(client):
    location_count = 3
    for _ in range(location_count):
        location = Location.create()

    task = Task.create(location=location)

    # GIVEN I am on the add or edit tasks form
    add_task_response = client.get(django.urls.reverse("website:task_create"))
    edit_task_response = client.get(django.urls.reverse(
        "website:task_update",
        kwargs={"pk": task.pk},
    ))
    assert add_task_response.status_code == 200
    assert edit_task_response.status_code == 200
    add_task = BeautifulSoup(
        str(add_task_response.content),
        features="html5lib",
    )
    edit_task = BeautifulSoup(
        str(edit_task_response.content),
        features="html5lib",
    )

    # WHEN I click on the location drop-down list
    # THEN I should be presented with a list of possible locations
    def location_options(soup):
        return (
            soup
            .find(lambda t: (
                t.name.strip("\\n") == "label"
                and "location" in t.text.lower()
            ))
            .find_next_sibling("select")
            .find_all("option")
        )

    assert len(location_options(add_task)) == location_count + 1
    assert len(location_options(edit_task)) == location_count + 1


@pytest.mark.skip
def weather_reports_dictate_add_edit_task_form_background():
    # TODO:  PhantomJS with Selenium to test the JS behaves.

    # GIVEN I select a location from the drop-down list
    # WHEN I view the add/edit tasks form
    # THEN I should see the background colour changing
    assert False


@pytest.mark.skip
def temperature_shows_in_add_edit_tasks():
    # TODO:  PhantomJS with Selenium to test the JS behaves.

    # GIVEN I select a location from the drop-down list
    # WHEN I view the add/edit tasks form
    # THEN I should see the current temperature
    assert False


@pytest.mark.django_db
def weather_reports_dictate_task_background(client):
    weathers_to_classes = {
        "Clear": "bg-danger",
        "Clouds": "bg-primary",
        "Rain": "bg-info",
    }
    locations = {
        weather: Location.create()
        for weather in weathers_to_classes
    }
    tasks = {
        weather: Task.create(location=location)
        for weather, location in locations.items()
    }
    tasks_by_name = {
        task.name: {"task": task, "weather": weather}
        for weather, task in tasks.items()
    }
    del tasks  # Would be overwritten later.

    for weather, location in locations.items():
        WeatherReport.create(location=location, name=weather)

    # GIVEN I am on the TODO list application
    tasks_response = client.get(django.urls.reverse("website:tasks"))
    assert tasks_response.status_code == 200
    tasks = BeautifulSoup(str(tasks_response.content), features="html5lib")

    # WHEN I view all of my tasks
    # THEN I should see the tasks displayed with respective colours to
    # their local weather
    #
    # Blue for “cold” or “rain”, Yellow-Orange for “warm” or “cloudy”
    # and Red for “hot” or “sunny” (the product owner did not specify
    # the exact parameters for temperature and colour).
    cards = tasks.find_all(lambda t: (
        t.has_attr("class")
        and "card" in t["class"]
    ))

    for card in cards:
        task = tasks_by_name[
            card
            .find(lambda t: t.has_attr("class") and "card-header" in t["class"])
            .text
        ]
        clean_classes = [
            class_.strip("\\n") for class_ in card["class"]
            if class_.strip("\\n")
        ]

        assert weathers_to_classes[task['weather']] in clean_classes
