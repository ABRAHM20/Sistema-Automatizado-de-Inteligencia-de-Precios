import requests
import json
from bs4 import BeautifulSoup


#VAMOS A WEB_SCRAPEAR EL IPHONE 16 
def scrap_plazavea_limpio():
    url = "https://www.plazavea.com.pe/api/catalog_system/pub/products/search?fq=productId:101493922"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    if(response.status_code in [200,206]):
        response_json=response.json()
        for i in response_json:
            nombre=i["items"][0]["name"]
            precio=i["items"][0]["sellers"][0]["commertialOffer"]["Price"]
            return nombre,precio



def scrap_falabella():
    url="https://www.falabella.com.pe/falabella-pe/product/prod18120095/iPhone-16-128GB/20687062?kid=shopp4fc&gclsrc=aw.ds&gad_source=1&gad_campaignid=17889613129&gbraid=0AAAAADs9MO2Zve7qZSi6Y10QuplJJsZHX&gclid=CjwKCAiA2PrMBhA4EiwAwpHyC3bUYZPhvX4a2CLGb3qVObN68G_PbTdLu4tm33oNJ_qkYErRweoRQBoCc3kQAvD_BwE"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    }

    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,"html.parser")
    encontrar_script=soup.find("script",id="__NEXT_DATA__")
    #pasarlo a dict
    datos_json=json.loads(encontrar_script.string)
    nombre=datos_json["props"]["pageProps"]["productData"]["name"]
    precio=datos_json["props"]["pageProps"]["productData"]["variants"][0]["prices"][0]["price"][0]
    return precio



'''
    r=requests.get(url, headers=headers)
    soup=BeautifulSoup(r.text, "html.parser")
    if(r.status_code in [206,200]):
        #Esto retorna un Json
        script_oculto=soup.find("script",id="__NEXT_DATA__")
        if(script_oculto):
            #Convertimos a diccionario
            dict=json.loads(script_oculto.string)
            with open("ver_json.json","w",encoding="utf-8") as f:
                json.dump(dict,f,indent=4,ensure_ascii=False)

        else:
            print("No se encontro la etiqueta NEXTDATA")
    else:
        print(f"Hubo un error {r.status_code}")'''

     
def enviar():
    url="http://127.0.0.1:8000/create"

    nombre_s, precio_s=scrap_plazavea_limpio()

    precio_fala=scrap_falabella()

    #Hay que preparar el JSON

    payload={
        "nombre":nombre_s,
        "precios_web1": float(str(precio_s).replace(",", "")),
        "precios_web2": float(str(precio_fala).replace(",", ""))
    }

    reponse=requests.post(url,json=payload)

    if(reponse.status_code in[200,206]):
        print("Se logro")
    else:
        print(f"no se logro {reponse.status_code}")


#enviar()




        





