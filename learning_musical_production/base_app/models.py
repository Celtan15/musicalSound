from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class Micro_module(models.Model):
    name=models.CharField(max_length=40)
    content=models.TextField()
    status=models.BooleanField()
    progression=models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    def __str__(self):
        if (self.status==False):
            return 'El micro módulo se llama %s , actualmente posee un progreso de %s y se encuentra bloqueado' %(self.name,
            self.progression)

        else:
            return 'El micro módulo se llama %s , actualmente posee un progreso de %s y se encuentra desbloqueado' %(self.name,
            self.progression)

class Top_panel(Micro_module):
    images=models.ImageField(upload_to='micro_module/top_panel')

class Options_panel(Micro_module):
    images=models.ImageField(upload_to='micro_module/options_panel')

class Side_panel(Micro_module):
    images=models.ImageField(upload_to='micro_module/side_panel')

class Workstation(Micro_module):
    images=models.ImageField(upload_to='micro_module/workstation')

class Evaluations (models.Model):
    name=models.CharField(max_length=50)
    answer=models.CharField(max_length=5, blank=True)
    questions=models.CharField(max_length=5, blank=True)
    qualification=models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    approval_date=models.DateField(auto_now_add=True)
    number_attempts=models.IntegerField()

    def __str__(self):
        return 'El modulo se llama %s , posee las siguientes preguntas %s y evalua los conocimientos en interfaz de FL' %(self.name,
        self.questions)

class Modules(models.Model):
    name=models.CharField(max_length=50)
    status=models.BooleanField()
    progression=models.DecimalField(max_digits=5, decimal_places=2)
    quantity_microModules=models.IntegerField()
    micro_modules=models.ForeignKey(Micro_module, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if (self.status==False):
            return 'El modulo se llama %s , se encuentra bloqueado y posee %s micromódulos, llamados %s' %(self.name, 
            self.quantity_microModules, self.micro_modules)
        else:
            return 'El modulo se llama %s , se encuentra desbloqueado y posee %s micromódulos, llamados %s' %(self.name, 
            self.quantity_microModules, self.micro_modules)

class Interface_evaluation(Evaluations):
    
    class Meta:
        verbose_name='interface_module_evaluation'    
    
class Mixture_evaluation(Evaluations):
    
    class Meta:
        verbose_name='mixture_module_evaluation'    

class Mastering_evaluation(Evaluations):
    
    class Meta:
        verbose_name='mastering_module_evaluation'    

class Interface_module(Modules):

    images=models.ImageField(upload_to='interface_module')
    class Meta:
        verbose_name='interface_module'

class Mixture_module(Modules):

    class Meta:
        verbose_name='mixture_module'

class Mastering_module(Modules):

    class Meta:
        verbose_name='mastering_module'

class CustomUserManager(UserManager):
    def create_user(self, username, email=None, psdw=None, **extra_fields):
        return self.create_user(username, email, psdw, **extra_fields)

    def create_superuser(self, username, email=None, psdw=None, **extra_fields):
        return self.create_user(username, email, psdw, **extra_fields)

# La base de datos genera automáticamente el id, se puede sobreescribir de ser necesario, revisar si
# se necesita sobreescribir para cada clase de este modelo
class User(AbstractBaseUser):
    id=models.CharField(primary_key=True,max_length=50)
    name=models.CharField(max_length=50)
    username=models.CharField(unique=True,max_length=50)
    email=models.EmailField()
    psdw=models.CharField("Password", max_length=16)
    country=models.CharField(max_length=30)
    date_birth=models.DateField(null=True)
    phone=models.CharField(max_length=20, blank=True)
    progression=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    interface=models.ForeignKey(Interface_module, null=True, blank=True, on_delete=models.CASCADE)
    mixture=models.ForeignKey(Mixture_module, null=True, blank=True, on_delete=models.CASCADE)
    mastering=models.ForeignKey(Mastering_module, null=True, blank=True, on_delete=models.CASCADE)
    objects=UserManager()

    class Meta:
        verbose_name='user_interface_module'
        verbose_name_plural='users_interface'

    def __str__(self):
        return 'El usuario se llama %s , su nickname es %s , su correo es %s, reside en %s' %(self.name, self.username, self.email, self.country)
'''
    def create_user(self, id, name, username, email, psdw, country, date_birth, phone, progression):
        self.id=id
        self.name=name
        self.username=username
        self.email=email
        self.country=country
        self.date_birth=date_birth
        self.phone=phone
        self.progression=progression
'''
class Login(models.Model):
    email=models.EmailField()
    pdw=models.CharField("Password", max_length=16)
    user_logged=models.OneToOneField(User, on_delete=models.CASCADE)