# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listings
from listings.forms import BandForm, ContactUsForm
from django.core.mail import send_mail

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nou adorons le chocolat</p>')

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def band_detail(request, id):  # notez le paramètre id supplémentaire
   return render(request,
          'listings/band_detail.html',
         {'id': id}) # nous passons l'id au modèle


def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def hello(request):
    bands = Listings.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Les titres des annonces sont :<p>
        <ul>
            <li>{bands[0].title}</li>
            <li>{bands[1].title}</li>
            <li>{bands[2].title}</li>
            <li>{bands[3].title}</li>
        </ul>
""")


def hello(request):
    bands = Band.objects.all()   
    return render(request, 'listings/hello.html',
        {'bands': bands})
        

def contact(request):
    form = ContactUsForm()  # ajout d’un nouveau formulaire ici
    return render(request,
          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit

  # ajoutez ces instructions d'impression afin que nous puissions jeter un coup d'oeil à « request.method » et à « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)


 # ...nous pouvons supprimer les déclarations de journalisation qui étaient ici...

    if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
        'listings/contact.html',
        {'form': form})

    form = ContactUsForm()




def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
     # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
            'listings/contact.html',
            {'form': form})


def band_create(request):
    form = BandForm()
    return render(request, 'listings/band_create.html', {'form':form})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})


def band_update(request, id):
            band = Band.objects.get(id=id)
            form = BandForm(instance=band)  # on pré-remplir le formulaire avec un groupe existant
            return render(request, 'listings/band_update.html', {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,'listings/band_update.html', {'form': form})
  

def band_delete(request, id):
    band = Band.objects.get(id=id)
    return render(request,
           'listings/band_delete.html',
           {'band': band})