from django import forms
from django.utils.html import format_html

class AdminImageWidget(forms.ClearableFileInput):
    template_name = "django/forms/widgets/clearable_file_input.html"

    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, "url"):
            file_url = value.url
            if str(value).lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                # always show as 500x500 in the admin form
                output.append(
                    format_html(
                        '<img src="{0}" style="width:500px; height:500px; object-fit:contain; '
                        'border:1px solid #ccc; border-radius:8px; margin-bottom:5px;" />',
                        file_url,
                    )
                )
            else:
                output.append(
                    format_html('<span style="color:#888;">File uploaded: {}</span><br/>', value.name)
                )
        output.append(super().render(name, value, attrs, renderer))
        return format_html("".join(output))
