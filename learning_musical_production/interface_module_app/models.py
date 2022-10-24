from decimal import Decimal
import email
from enum import unique
from logging.config import IDENTIFIER
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from xml.dom.minidom import Identified
from django.db import models

from django.forms import BooleanField, DecimalField, EmailField, IntegerField, PasswordInput

# La base de datos genera automáticamente el id, se puede sobreescribir de ser necesario, revisar si
# se necesita sobreescribir para cada clase de este modelo
class Person(models.Model):
    id=models.CharField(primary_key=True,max_length=50)
    name=models.CharField(max_length=50)
    nickname=models.CharField(unique=True,max_length=50)
    email=models.EmailField()
    psdw=models.CharField(PasswordInput, max_length=15)
    country=models.CharField(max_length=30)
    date_birth=models.DateField()
    phone=models.CharField(max_length=20, blank=True)

    def __str__(self):
        return 'El usuario se llama %s , su nickname es %s , su correo es %s y reside en %s' %(self.name,
        self.nickname, self.email, self.country)

class InterfaceEvaluation(models.Model):
    name=models.CharField(max_length=50)
    answer=models.CharField(max_length=5, blank=True)
    questions=models.CharField(max_length=5, blank=True)
    qualification=models.DecimalField(max_digits=5, decimal_places=3, blank=True)
    
    def __str__(self):
        return 'El modulo se llama %s , posee las siguientes preguntas %s y evalua los conocimientos en interfaz de FL' %(self.name,
        self.questions)

class User(Person):
    total_progression=DecimalField()

class Admin(Person):
    added_users=IntegerField()
    
class InterfaceModule(models.Model):
    name=models.CharField(max_length=50)
    moduleLocked=models.BooleanField(True)
    status=models.BooleanField(blank=False)
    progression=models.DecimalField(max_digits=4, decimal_places=2)
    quantity_microModules=models.IntegerField(blank=True)

    def __str__(self):
        return 'El modulo se llama %s , se encuentra %s y posee %s micromódulos' %(self.name, self.status, 
        self.quantity_microModules)