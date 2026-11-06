from django.shortcuts import render

def o_mne(request):
    kontext = {
        "meno": "samo smrecek",
    }
    return render(request, "domace/o_mne.html", kontext)