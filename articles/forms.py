from django import forms # type: ignore

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

        def clean(self):
            data = self.cleaned_data
            title = data.get('title')
            
            qs = Article.objects.filter(title__icontains=title)
            if qs.exists():
                self.add_error("title", f"\"{title}\" is already in use. Please pick a different title")


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data    # dictionary
    #     title = cleaned_data['title']
    #     return title
    
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     return cleaned_data
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        if title.lower().strip() == 'the office':
            self.add_error('title', 'This title is taken')
            # raise ValidationError('This title is taken.')
            return cleaned_data
