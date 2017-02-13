[1mdiff --git a/browse/forms.py b/browse/forms.py[m
[1mindex 2cb65e2..ed445db 100644[m
[1m--- a/browse/forms.py[m
[1m+++ b/browse/forms.py[m
[36m@@ -26,6 +26,7 @@[m [mclass teamNumForm(forms.ModelForm):[m
             #'shirtImg': 'put a direct link to an image of your shirt here',[m
             "wanted": "put a list of team numbers, formatted like so: 100,200,300"[m
         }[m
[32m+[m[41m    [m
        [m
 class messageForm(forms.ModelForm):[m
     class Meta:[m
