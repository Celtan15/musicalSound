from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, User

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

class Pregunta(models.Model):

    NUM_RES_PERMITIDAS = 1

    texto = models.TextField(verbose_name='Introduce pregunta')
    max_resultado = models.DecimalField(verbose_name='Calificación máxima', default=3, decimal_places=2, max_digits=6)
    interface_evaluation = models.ForeignKey('Interface_evaluation', on_delete=models.CASCADE, related_name='preguntas')

    def __str__(self):
        return self.texto

class ElegirRespuesta(models.Model):

    MAXIMO_RESPUESTA = 4

    pregunta_elegir = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto_elegir = models.TextField(verbose_name='Introduce una opción de respuesta' )
    correcta_elegir = models.BooleanField(default=False, null=False, verbose_name='¿Esta es la opción correcta?')
    
class Concepts(Micro_module):
    images=models.ImageField(upload_to='micro_module/concepts')

class Basic_techniques(Micro_module):
    images=models.ImageField(upload_to='micro_module/basic_techniques')

class Mid_techniques(Micro_module):
    images=models.ImageField(upload_to='micro_module/mid_techniques')

class Advance_techniques(Micro_module):
    images=models.ImageField(upload_to='micro_module/advance_techniques')

class Evaluations (models.Model):
    name=models.CharField(max_length=50)
    answer=models.CharField(max_length=5, blank=True)
    questions=models.CharField(max_length=5, blank=True)
    qualification=models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    approval_date=models.DateField(auto_now_add=True)
    number_attempts=models.IntegerField()

    def __str__(self):
        return self.texto

class Evaluations (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    resultado_total = models.DecimalField(verbose_name='Resultado total', default=0, decimal_places=2, max_digits=10, null=True)

    def nuevos_intentos(self, pregunta):
        intento = RespuestaUsuario(pregunta = pregunta, evaluacion_user=self)
        intento.save()

    def nuevas_preguntas(self):
        respondidas = RespuestaUsuario.objects.filter(evaluacion_user=self).values_list('pregunta__pk', flat=True)
        preguntas_restantes = Pregunta.objects.exclude(pk__in = respondidas)
        if not preguntas_restantes.exists():
            return None
        return random.choice(preguntas_restantes)

    def validar_intento(self, pregunta_respondida, respuesta_seleccionada):
        if pregunta_respondida.pregunta_id != respuesta_seleccionada.pregunta_id:
            return

        pregunta_respondida.respuesta_seleccionada = respuesta_seleccionada
        if respuesta_seleccionada.correcta is True:
            pregunta_respondida.correcta = True
            pregunta_respondida.resultado = respuesta_seleccionada.pregunta.max_resultado
            pregunta_respondida.respuesta = respuesta_seleccionada

        else:
            pregunta_respondida.respuesta = respuesta_seleccionada

        pregunta_respondida.save()
        self.actualizar_resultado()

    def actualizar_resultado(self):
        resultado_actualizado = self.intentos.filter(correcta=True).aggregate(models.Sum('resultado'))['resultado__sum']
        self.resultado_total = resultado_actualizado
        self.save()

class RespuestaUsuario(models.Model):
    evaluacion_user = models.ForeignKey(Evaluations, on_delete=models.CASCADE, related_name='intentos')
    fecha_respuesta = models.DateTimeField(auto_now_add=True)
    pregunta= models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null=True)
    correcta= models.BooleanField(verbose_name='¿Esta es la respuesta correcta?', default=False, null=False)
    resultado = models.DecimalField(verbose_name='Resultado', default=0, decimal_places=2, max_digits=6)

class Interface_evaluation(Evaluations):

    class Meta:
        verbose_name='interface_module_evaluation'

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