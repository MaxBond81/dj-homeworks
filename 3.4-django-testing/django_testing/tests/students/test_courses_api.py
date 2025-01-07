import pytest
from rest_framework.reverse import reverse

from students.models import Student, Course
from rest_framework.test import APIClient
from model_bakery import baker

BASE_URL = "/api/v1/courses"


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_course(client, course_factory):
    # Arrange
    course_list = course_factory(_quantity=1)
    course_id = course_list[0].id
    # Act
    response = client.get(f'{BASE_URL}/{course_id}/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == course_list[0].name


@pytest.mark.django_db
def test_course_list(client, course_factory):
    # Arrange
    course_list = course_factory(_quantity=3)
    course_id_set = {course.id for course in course_list}
    # Act
    response = client.get(f'{BASE_URL}/')
    # Assert
    assert response.status_code == 200
    data = response.json()
    data_id_set = {course['id'] for course in data}
    assert data_id_set == course_id_set


@pytest.mark.django_db
def test_course_filter_id(client, course_factory):
    # Arrange
    course_list = course_factory(_quantity=3)
    # Act
    response = client.get(f'{BASE_URL}/?id={course_list[1].id}')
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == course_list[1].id


@pytest.mark.django_db
def test_course_filter_name(client, course_factory):
    # Arrange
    course_list = course_factory(_quantity=3)
    # Act
    response = client.get(f'{BASE_URL}/?name={course_list[1].name}')
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course_list[1].name


@pytest.mark.django_db
def test_course_create(client):
    # Arrange
    count = Course.objects.count()
    # Act
    response = client.post(f'{BASE_URL}/', data={'name': "Математика"})

    # Assert
    assert response.status_code == 201
    course = Course.objects.get(name="Математика")
    data = response.json()
    assert Course.objects.count() == count + 1
    assert data['name'] == course.name


@pytest.mark.django_db
def test_course_update(client, course_factory):
    # Arrange
    course_list = course_factory(_quantity=1)
    course_id = course_list[0].id
    # Act
    response = client.patch(f'{BASE_URL}/{course_id}/', data={'name': "Математика"})

    # Assert
    assert response.status_code == 200
    course = Course.objects.get(id=course_id)
    data = response.json()
    assert data['name'] == course.name


@pytest.mark.django_db
def test_course_delete(client, course_factory):
    # Arrange
    course_list = course_factory(_quantity=3)
    course_id = course_list[0].id
    count = Course.objects.count()
    # Act
    response = client.delete(f'{BASE_URL}/{course_id}/')
    # Assert
    assert response.status_code == 204
    assert Course.objects.count() == count - 1


@pytest.mark.parametrize("count_students, code_status",
                         [(19, 201),(20, 201),(21, 400)])
@pytest.mark.django_db
def test_course_validate(client, student_factory,
                         count_students, code_status):
    # Arrange
    student_list = student_factory(_quantity=count_students)

    # Act
    response = client.post(f'{BASE_URL}/', data={"name": "course_1",
                                                 "students": [s.id for s in student_list]})

    # Assert
    assert response.status_code == code_status

