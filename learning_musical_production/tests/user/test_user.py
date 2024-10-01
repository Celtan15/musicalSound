import pytest
from base_app.models import User, Modules

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
    )  # type: ignore

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

@pytest.mark.django_db
def test_module_creation():
    # Crear un módulo
    module = Modules.objects.create(
        name="Producción Musical",
        status =True,
        progression = '3.5',
        quantity_microModules = '2'
    )

    # Verificar que el módulo se ha creado correctamente
    assert module.name == "Producción Musical"
    assert module.status == True

    # Verificar que el módulo está en la base de datos
    module_in_db = Modules.objects.get(id=module.id)
    assert module_in_db is not None
    assert module_in_db.name == "Producción Musical"
    assert module_in_db.status == True

    print("La prueba test_module_creation ha pasado exitosamente.")


'''
@pytest.mark.django_db
def test_remove_user():
    user=User.objects.create_user(
        username='Alejo',
        email='aaa@email.com',
        psdw='8080',
    )
'''