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

def pozdrav(request):
    meno = request.GET.get("meno", "") #.get najde a vrati hodnotu prvku indexom meno, ako ho nenajde tak vlozi prazny
    return render(request, "ulohy/pozdrav.html", {"meno": meno})

def sucet(request):
    ans = None
    if request.method == "POST":
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        ans = int(num1) + int(num2)
    return render(request, "ulohy/sucet.html", {"ans": ans})

def kalkulacka(request):
    ans = None
    if request.method == "POST":
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        znak = request.POST["znak"]
        if znak == "+":
            ans = int(num1) + int(num2)
        elif znak == "-":
            ans = int(num1) - int(num2)
        elif znak == "*":
            ans = int(num1) * int(num2)
        
    return render(request, "ulohy/kalkulacka.html", {"ans": ans})

def obdlznik(request): 
    obsah = None 
    obvod = None
    if request.method == "POST":
        num1 = float(request.POST["num1"])
        num2 = float(request.POST["num2"])

        obsah = round(num1 * num2, 2)
        obvod = round(2*(num1 + num2), 2)

    return render(request, "ulohy/obdlznik.html", {"obsah": obsah, "obvod": obvod})
