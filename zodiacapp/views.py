from django.shortcuts import render
from django.http import HttpResponse

zodiac = {
    "aries":       "Aries... próximamente",
    "tauro":       "Tauro... próximamente",
    "geminis":     "Géminis... próximamente",
    "cancer":      "Cáncer... próximamente",
    "leo":         "Leo... próximamente",
    "virgo":       "Virgo... próximamente",
    "libra":       "Libra... próximamente",
    "escorpio":    "Escorpio... próximamente",
    "sagitario":   "Sagitario... próximamente",
    "capricornio": "Capricornio... próximamente",
    "acuario":     "Acuario... próximamente",
    "piscis":      "Piscis... próximamente",
    "ofiuco":      "Ofiuco... próximamente",

}

# Create your views here.
def index(request):
    # Aquí voy a generar la lógica de todos los signos
    list_items = ''

    """for signo in zodiac.keys():
        list_items += f"<h1>Signo: {signo} </h1><br>"
        list_items += f"<p>{zodiac[signo]}</p>"
        """

    #return HttpResponse(list_items)
    return render(request, 'zodiacapp/index.html', {
        "mensaje": "Hola desde view",
        'mensaje2': 'Este es otro mensaje',
    })

