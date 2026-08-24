from django.shortcuts import render, redirect


def giriş_request(request):
    return render(request, "account/giriş.html")


def kayıt_request(request):
    return render(request, "account/kayıt.html")


def çıkış_request(request):
    return redirect("home")
