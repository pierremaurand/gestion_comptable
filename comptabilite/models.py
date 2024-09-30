from django.db import models
from django.conf import settings


class Compte(models.Model):
    number = models.CharField(max_length=6, verbose_name="Numéro Compte")
    description = models.TextField(max_length=255, verbose_name="Libellé du Compte")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Auteur")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    def __str__(self) -> str:
        return f'{self.number}'
    
    class Meta:
        ordering = ["number"]
    
class Ecriture(models.Model):
    description = models.TextField(max_length=255, verbose_name="Libellé")
    date_application = models.DateField(verbose_name="Date")
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["date_application"]
    
class Mouvement(models.Model):
    DEBIT = 'DEBIT'
    CREDIT = 'CREDIT'

    TYPE_CHOICES = (
        (DEBIT, 'Débit'),
        (CREDIT, 'Crédit'),
    )
    
    mouvement = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name='Type de mouvement')
    montant = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Montant du mouvemnt")
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE, verbose_name="Compte comptable")
    ecriture = models.ForeignKey(Ecriture, on_delete=models.CASCADE, verbose_name="Numéro Ecriture")

    