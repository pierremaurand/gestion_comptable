from django import forms
from . import models 

class CompteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields): 
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        
        
    class Meta:
        model = models.Compte
        fields = ['number', 'description']
        
class MouvementForm(forms.ModelForm):
    class Meta: 
        model = models.Mouvement
        fields = ['compte','mouvement', 'montant']

class EcritureForm(forms.ModelForm):
    class Meta: 
        model = models.Ecriture
        fields = ['date_application','description']