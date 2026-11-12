from django.shortcuts import render

def o_mne(request):
    kontext = {
        "meno": "samo smrecek",
    }
    return render(request, "domace/o_mne.html", kontext)

def du2_(request):
    kontext = {
        "meno": "samo",
        "trieda": "3.at",
        "vek": 18,
        "predmety": ["programovanie", "prax", "iot"],
    }
    return render(request, "domace/du2_.html", kontext)