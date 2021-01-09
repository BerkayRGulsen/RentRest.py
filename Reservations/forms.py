from django import forms




class FilteredListCars(forms.Form):
    branches = (
        ("Adana", "Adana"),
        ("İzmir", "İzmir"),
    )
    branch = forms.ChoiceField(choices=branches, label='Pick Up Branch')


    takeDate = forms.DateTimeField(label="Pick Up Date",
                                   widget=forms.DateTimeInput(attrs={
                                       "type": "datetime-local", "name": "tookDate", "id": "first", "min": "",
                                       "class": "form-control datepicker px-3"
                                   })
                                   )

    return_branches = (
        ("Adana", "Adana"),
        ("İzmir", "İzmir"),
    )
    return_branch = forms.ChoiceField(choices=return_branches, label='Return Branch')



    returnDate = forms.DateTimeField(label="Pick Off Date",
                                     widget=forms.DateTimeInput(attrs={
                                         "type": "datetime-local", "name": "tookDate", "id": "second",
                                         "class": "form-control datepicker px-3"
                                     })
                                     )

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("takeDate")
        end_date = cleaned_data.get("returnDate")
        if end_date < start_date:
            msg = u"End date should be greater than start date."
            self._errors["end_date"] = self.error_class([msg])



