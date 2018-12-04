from django import forms


class ContactForm(forms.Form):
    Ad = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    İsmaric = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    İsmaric.label='İsmarıc'

def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    self.fields['Ad'].label = "Your name:"
    self.fields['Email'].label = "Your email:"
    self.fields['İsmaric'].label = "What do you want to say?"