from django import forms
from .models import emp

class Feedbackform(forms.Form):
    name=forms.CharField(label="enter your name" ,max_length=20)
    email=forms.EmailField(label="enter your Email" ,max_length=50)
    feedback=forms.CharField(label="provide your feedback" ,widget=forms.Textarea)


    def __init__(self, *args, **kwargs):
          super(Feedbackform, self).__init__(*args, **kwargs)
          for visible in self.visible_fields():
              visible.field.widget.attrs['class'] = 'form-control'    

class Empform(forms.Form):
     class Meta:
          model=emp
          fields=['name','emp_id','phone','address']
