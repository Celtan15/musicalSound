import pytest
from base_app.models import User

@pytest.mark.django_db
def test_user_creation():
    user=User.objects.create_user(
        username='Alejo',
        email='aaa@email.com',
        psdw='8080',
    )

    assert user.username == 'Alejo'

@pytest.mark.django_db
def test_superuser_creation():
    user=User.objects.create_superuser(
        username='Alejo',
        email='aaa@email.com',
        psdw='8080',
        is_superuser=True,
    )

    assert user.is_superuser == True

@pytest.mark.django_db
def test_staff_user_creation():
    user=User.objects.create_user(
        username='Alejo',
        email='aaa@email.com',
        psdw='8080',
        is_staff=True,
    )

    assert user.is_staff == True

@pytest.mark.django_db
def test_user_creation_fail():
   with pytest.raises(Exception):
    User.objects.create_user(
            psdw='999',
            is_staff=False,
    )   # type: ignore
'''
@pytest.mark.django_db
def test_remove_user():
    user=User.objects.create_user(
        username='Alejo',
        email='aaa@email.com',
        psdw='8080',
    )
'''