from django.shortcuts import render

def cv1_index(request):
    kontext = {
        "meno": "samo",
    }
    return render(request, "cv1/cv1_index.html", kontext)

def obchod(request):
    kontext = [
        {"nazov": "kava", "cena": 8.99},
        {"nazov": "muka", "cena": 2.59},
        {"nazov": "pero", "cena": 1.09},
        {"nazov": "zavlazovac", "cena": 35.99},
    ]

    max = request.GET.get("max", "")

    if max != "":
        max = float(max)
        nove = []
        for k in kontext:
            if k["cena"] <= max:
                nove.append(k)
        kontext = nove
    return render(request, "cv1/obchod.html", {"kontext": kontext})

def cv1_body(request):
    ans = None
    if request.method == "POST":
            body = float(request.POST["body"])
            max = float(request.POST["max"])

            perc = (body / max) * 100
            if perc >= 90:
                    zn = 1
            elif perc >= 75:
                zn = 2
            elif perc >= 50:
                zn = 3
            elif perc >= 30:
                zn = 4
            else:
                zn = 5

            ans = f"{body} z {max} bodov = {round(perc, 2)}% -> {zn}"
    return render(request, "cv1/cv1_body.html", {"ans": ans})