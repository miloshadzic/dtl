from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(max_length=50, label='Book Title'
                            help_text='Search book titles.')
