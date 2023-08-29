from django.forms import ModelForm, ValidationError
from catalog.models import Product


class ProductForm(ModelForm):

    forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

    class Meta:
        model = Product
        exclude = ('creation_date', 'change_date')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name').lower()
        for word in self.forbidden_words:
            if word in cleaned_data:
                raise ValidationError('Название содержит запрещенные слова!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description').lower()
        for word in self.forbidden_words:
            if word in cleaned_data:
                raise ValidationError('Описание содержит запрещенные слова!')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'