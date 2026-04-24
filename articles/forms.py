from django import forms


class ArticleForm(forms.Form):
  title = forms.CharField()
  content = forms.CharField()


from django import forms

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def cleaned_data(self):
        title = self.cleaned_data.get('title')

        if title.lower().strip() == "the office":
            raise forms.ValidationError("This title is taken")

        return title

    def clean(self):
        cleaned_data = self.cleaned_title()
        print('all data', cleaned_data)
        return cleaned_data