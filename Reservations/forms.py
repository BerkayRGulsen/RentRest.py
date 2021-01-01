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






