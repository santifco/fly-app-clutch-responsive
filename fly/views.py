from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello, Fly!")

def linktree(request):

    return render (request,'app_1/linktree.html')

def linktree_basketball_menu(request):

    return render (request,'app_1/linktree_basketball_menu.html')

def linktree_basketball_pedidos(request):

    return render (request,'app_1/linktree_basketball_pedidos.html')

def linktree_soccer(request):

    return render (request,'app_1/linktree_soccer.html')

def linktree_tenis(request):

    return render (request,'app_1/linktree_tenis.html')

def linktree_urban(request):

    return render (request,'app_1/linktree_urban.html')

def linktree_urban_women(request):

    return render (request,'app_1/linktree_urban_women.html')

def linktree_genero(request):

    return render (request,'app_1/linktree_genero.html')

def linktree_volley(request):

    return render (request,'app_1/linktree_volley.html')


from unittest import result
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
import json
import requests
from bs4 import BeautifulSoup
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
import pandas as pd
import re
from django.contrib.admin.widgets import AdminDateWidget
from .forms import CalulatorForm2
from datetime import datetime,timedelta


def base(request):
    return render(request,'app_1/base.html')

def calculator(request):

    if request.method == 'POST': 

        value = request.POST["value"]

        print(value)

        # url = "https://www.cronista.com/MercadosOnline/dolar.html"
        # html_page = requests.get(url)
        # soup = BeautifulSoup(html_page.content, 'html.parser')
        # Dolar_Solidario = soup.find_all(class_="sell-value")[2].text.replace("$","").replace(",",".")
        # Dolar_Blue = soup.find_all(class_="sell-value")[1].text.replace("$","").replace(",",".")
        
        # url = "https://www.cronista.com/MercadosOnline/moneda.html?id=ARSTAR"
        # html_page = requests.get(url)
        # soup = BeautifulSoup(html_page.content, 'html.parser')
        # Dolar_Tarjeta = soup.find_all(class_="sell-value")[0].text.replace("$","").replace(",",".")

        
        import json
        import requests
        
        # defining key/request url
        key = "https://api.binance.com/api/v3/ticker/price?symbol=USDTARS"
        
        # requesting data from url
        data = requests.get(key)  
        data = data.json()
        # print(f"{data['symbol']} price is {data['price']}")

        dolar_blue = float(data['price'])

        
        ganancia = 20000
        #ganancia=7000
        envio_aereo = 20000
        #envio_aereo = 18766
        precio_compra_us = float(value)
        tiempo_demora = "20-25 días"

        compra_final_us = 0.07*(precio_compra_us) + precio_compra_us 

        compra_final_pesos =  round(float(compra_final_us) * float(dolar_blue),0) + envio_aereo
        
        precio_venta =  round(compra_final_pesos + float(ganancia),0)

        ctx = {"precio_venta" : precio_venta ,"precio_compra":compra_final_pesos,"value":value,"tiempo_demora":tiempo_demora}

        # print(dolar_blue)
        # print("Dolar Solidario = " + str(Dolar_Solidario))
        # print("Dolar_Blue = " + str(Dolar_Blue))                                               
        # print("Dolar_Tarjeta = " + str(Dolar_Tarjeta))                                               

        return render (request,'app_1/calculator.html',ctx)

    return render (request,'app_1/calculator.html')

def seguimiento(request):

    if request.method == 'POST': 

        value = request.POST["value"]

        print(value)

        url = "https://docs.google.com/spreadsheets/d/145NJRd5LARs6hu0wnoVBhVg1Kraujfps/edit?usp=sharing&ouid=110020071842220435368&rtpof=true&sd=true"
        url_for_pandas = url.replace("/edit?usp=sharing", "/export?format=xlsx")
        df = pd.read_excel(url_for_pandas)
        df['id'] = df['id'].astype(str)
        df = df[df["id"]==value]
        print(df)

        print(len(df))

        tracking_number = df.iloc[0,df.columns.get_loc("tracking_number")]
        if str( tracking_number ) == "NaN":
                tracking_number = 0 
                print(tracking_number)

        if len(df) == 0:

            value = 0
            fecha_llegada_deposito=0
            fecha_compra=0
            fecha_arribo=0
            fecha_vuelo=0
            fecha_llegada_estimada=0

        else:

            try:
                fecha_llegada_deposito = df.iloc[0,df.columns.get_loc("FECHA DE LLEGADA")].date()
            except:
                fecha_llegada_deposito=0
            
            if str( fecha_llegada_deposito ) == "NaT":
                fecha_llegada_deposito = 0 
                print(fecha_llegada_deposito)
            try:
                fecha_compra = df.iloc[0,df.columns.get_loc("FECHA COMPRA")].date()
            except:
                fecha_compra=0
            print(fecha_compra)
            if str( fecha_compra ) == "NaT":
                fecha_compra = 0 
                print(fecha_compra)
            try:
                fecha_vuelo = df.iloc[0,df.columns.get_loc("FECHA VUELO")].date()
            except:
                fecha_vuelo = 0 
            print("Fecha_vuelo =" + str(fecha_vuelo))
            if str( fecha_vuelo ) == "NaT":
                fecha_vuelo = 0 
                print(fecha_vuelo)
            try:
                fecha_arribo = df.iloc[0,df.columns.get_loc("FECHA ARRIBO")].date()
            except:
                fecha_arribo = 0 
            if str( fecha_arribo ) == "NaT":
                fecha_arribo = 0 
                print(fecha_arribo) 
            if fecha_vuelo != 0:
                fecha_llegada_estimada = fecha_vuelo + timedelta(days=7)
            else:
                try:
                    fecha_llegada_estimada = (df.iloc[0,df.columns.get_loc("FECHA COMPRA")] +  timedelta(days=25)).date()
                except:
                    fecha_llegada_estimada=0

            print("Fecha Compra" + str(fecha_compra))
            print("Fecha Llegada deposito" + str(fecha_llegada_deposito))
            print("Fecha Llegada Estimada " + str(fecha_llegada_estimada))
            print("Fecha Vuelo " + str(fecha_vuelo))
            print("Fecha Arribo" + str(fecha_arribo))

    
        ctx = {"tracking" : value, "fecha_llegada_deposito":fecha_llegada_deposito,"fecha_compra":fecha_compra,"fecha_vuelo":fecha_vuelo,"fecha_arribo":fecha_arribo,"fecha_llegada_estimada":fecha_llegada_estimada,"tracking_number":tracking_number}                                            

        return render (request,'app_1/seguimiento.html',ctx)

    return render (request,'app_1/seguimiento.html')


def calculator_mayorista(request):

    if request.method == 'POST': 

        value = request.POST["value"]

        print(value)

        url = "https://www.cronista.com/MercadosOnline/dolar.html"
        html_page = requests.get(url)
        soup = BeautifulSoup(html_page.content, 'html.parser')
        Dolar_Solidario = soup.find_all(class_="sell-value")[2].text.replace("$","").replace(",",".")
        Dolar_Blue = soup.find_all(class_="sell-value")[1].text.replace("$","").replace(",",".")
        
        # f = open(r'C:\Users\santi\Jupyter Notebook Codes\Django\firstproject\firstapp\json_data\dolar_data.json')
        # data = json.load(f)
        # dolar = data["value"]
        
        #ganancia = 14000
        ganancia=6000
        envio_aereo = 14000
        #envio_aereo = 28*1.35*float(Dolar_Blue)
        print("Envio Aereo = "+str(envio_aereo))
        precio_compra_us = float(value)
        tiempo_demora = "20-25 días"


        compra_final_us = 0.07*(precio_compra_us) + precio_compra_us 

        compra_final_pesos =  round(float(compra_final_us) * float(Dolar_Blue),0) + envio_aereo

        precio_venta =  round(compra_final_pesos + float(ganancia),0)

        ctx = {"precio_venta" : precio_venta ,"precio_compra":compra_final_pesos,"value":value,"dolar_blue":Dolar_Blue,"tiempo_demora":tiempo_demora}

        print(Dolar_Solidario)
        print(Dolar_Blue)                                               

        return render (request,'app_1/calculator.html',ctx)

    return render (request,'app_1/calculator.html')