from django.db import models


class Tickets(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    compra = models.DecimalField(null=False,max_digits=5, decimal_places=2)
    valor_accion = models.IntegerField()
    fecha = models.DateTimeField()
    activa = models.BinaryField(default=True,null=False)

class Acciones(models.Model):
    # id = define here to change from int autoincrement to other type of format
    id_ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=200,null=False,default="Sin nombre")
    celular = models.CharField(max_length=15,null=False,default="Sin celular")
    correo = models.CharField(max_length=100,null=False,default="Sin correo")