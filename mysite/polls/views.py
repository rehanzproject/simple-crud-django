from django.shortcuts import render , redirect

# Create your views here.
from polls.models import Tabel

def tampil(request):
    tampilin = Tabel.objects.all()
    ctx = {
        'tampilin':tampilin,
    }
    return render(request, "index.html" , ctx)

def addTabel(request):
    id = request.POST['txtId']
    namaa = request.POST['txtNama']
    kelass = request.POST['txtKelas']
    matkull = request.POST['txtMtkul']

    addData = Tabel.objects.create(id=id, nama=namaa, kelas=kelass, matkul=matkull)
    return redirect('/')

def deleteTbl(request, id):
    hapus = Tabel.objects.get(id=id)
    hapus.delete()

    return redirect('/')

def editTbl(request, id):
    cek = Tabel.objects.get(id=id)
    ctx = {
        "cek":cek,
    }
    return render(request, 'editabel.html', ctx)

def editTabel(request ):
    id = request.POST['txtId']
    namaa = request.POST['txtNama']
    kelass = request.POST['txtKelas']
    matkull = request.POST['txtMtkul']
    

    Tabell = Tabel.objects.get(id=id)
    Tabell.nama = namaa
    Tabell.kelas = kelass
    Tabell.matkul = matkull
    Tabell.save()

    return redirect('/')
