from django import forms
from .models import WeightRecord

class WeightRecordForm(forms.ModelForm):
    class Meta:
        model = WeightRecord
        fields = ['date', 'max_weight', 'min_weight']
        labels = {
            'date': 'Tanggal(Format MM/DD/YYYY) :', 
            }

    def clean(self):
        cleaned_data = super().clean()
        max_weight = cleaned_data.get("max_weight")
        min_weight = cleaned_data.get("min_weight")
        date = cleaned_data.get("date")
        

        if date:
            existing_record = WeightRecord.objects.filter(date=date).exclude(pk=self.instance.pk if self.instance else None)
            if existing_record.exists():
                raise forms.ValidationError("Tanggal yang dimasukkan sudah ada dalam data. Silahkan gunakan fungsi update pada tanggal tersebut.")
        

        if max_weight is not None and min_weight is not None and max_weight < min_weight:
            raise forms.ValidationError("Max weight harus lebih besar dari min weight")
