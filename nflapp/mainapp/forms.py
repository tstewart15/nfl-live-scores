from django import forms
from mainapp import WEEK_TYPE_MAP, FIRST_YEAR, LAST_YEAR, WEEKS_FOR_WEEK_TYPE


class WeekForm(forms.Form):

    def __init__(self, *args, **kwargs):
        year_val = kwargs.pop('year_val')
        week_type_val = kwargs.pop('week_type_val')
        super(WeekForm, self).__init__(*args, **kwargs)
        # print WEEKS_FOR_WEEK_TYPE
        self.fields['week'].choices = \
            WEEKS_FOR_WEEK_TYPE[week_type_val][str(year_val)]

    year = forms.ChoiceField(
        choices=[(x, x) for x in range(FIRST_YEAR, LAST_YEAR+1)],
        widget=forms.Select(
            attrs={
                'class': 'dropdown',
                'id': 'yearSelector'
            }
        ),
        label=''
    )

    week_type = forms.ChoiceField(
        choices=[(key, WEEK_TYPE_MAP[key]) for key in WEEK_TYPE_MAP],
        widget=forms.Select(
            attrs={
                'class': 'dropdown',
                'id': 'weekTypeSelector'
            }
        ),
        label=''
    )

    week = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'dropdown',
                'id': 'weekSelector'
            }
        ),
        label=''
    )
