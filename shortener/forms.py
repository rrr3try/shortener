from django import forms


class URLForm(forms.Form):
    bootstrap_styles = {"class": "form-control text-center", "placeholder": "URL"}
    url_form_widget = forms.widgets.URLInput(attrs=bootstrap_styles)

    url = forms.URLField(label='', widget=url_form_widget)
