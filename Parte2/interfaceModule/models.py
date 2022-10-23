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
    email=models.EmailField()
    psdw=models.CharField(PasswordInput, max_length=15)
    country=models.CharField(max_length=30)
    dateBirt=models.DateField()
    phone=models.CharField(max_length=20)

class  InterfaceEvaluation(models.Model):
    name=models.CharField(max_length=50)
    answer=models.CharField(max_length=5)
    question=models.CharField(max_length=5)
    qualification=models.DecimalField(max_digits=5, decimal_places=3)

class InterfaceModule(models.Model):
    name=models.CharField(max_length=50)
    quantityMicroModules=IntegerField()
    moduleLocked=BooleanField()
    state=BooleanField()
    progression=DecimalField()

class User(Person):
    totalProgresion=DecimalField()

class Admin(Person):
    addedUsers=IntegerField