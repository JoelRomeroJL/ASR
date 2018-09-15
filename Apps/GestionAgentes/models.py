from django.db import models
from .pySNMP import consultaSNMP   #se debe importar el metodo de pySNMP
# Create your models here.

#Modelo Agentes, para guardar agentes

class Agente(models.Model):
    hostname = models.CharField(max_length=50)
    vSNMP = models.CharField(max_length=50)
    puerto = models.PositiveSmallIntegerField()
    comunidad = models.CharField(max_length=50)

    def AgenteDatos(self):
        cadena = "{0} {1} {2} -> {3}"
        return cadena.format(self.hostname, self.vSNMP, self.puerto, self.comunidad)

    def consulta(self):  #Metodo para consultar en la SNMP del dispositivo, recibe la comunidad y Hostname
        resultado = consultaSNMP(self.comunidad, self.hostname, "1.3.6.1.2.1.1.1.0")
        return resultado

    def __str__(self):
        return self.AgenteDatos()
