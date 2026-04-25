from django import forms


class ArticleForm(forms.Form):
  title = forms.CharField()
  content = forms.CharField()


from django import forms

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    """def cleaned_title(self):
        cleaned_data = self.cleaned_data # dictionary
        print("cleaned_data", cleaned_data)
        title = cleaned_data.get('title')
        if title.lower().strip() == "the office":
            raise forms.ValidationError('This title is taken')
        print("title", title)
        return title """

        
        

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "the office":
           self.add_error('title', 'This is title is taken')
            #raise forms.ValidationError('This title is taken')
        if "office" in content or "office" in title.lower():
           self.add_error('content', "office is not allowed")
           raise forms.ValidationError("office is not alloewed..")
        return cleaned_data