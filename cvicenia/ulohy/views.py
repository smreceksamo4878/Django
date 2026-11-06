from django.shortcuts import render, HttpResponse

def ahoj(request):
    return HttpResponse("ahoj bruno")

def o_mne(request):
    kontext = {
        "meno": "samo",
        "vek": 18,
        "zaluby": ["oliver♥", "zas oliver"],
    }
    return render(request, "ulohy/o_mne.html", kontext)

def rozvrh(request):
    hodiny = [
        {"cislo": 1, "predmet": "PI1"},
        {"cislo": 2, "predmet": "PI1"},
        {"cislo": 3, "predmet": "MAT"},
        {"cislo": 4, "predmet": "PRX"},
        {"cislo": 5, "predmet": "PRX"},
        {"cislo": 6, "predmet": "ANJ"},
    ]
    return render(request, "ulohy/rozvrh.html", {"den": "po", "hodiny": hodiny})