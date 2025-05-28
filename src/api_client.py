import requests

def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    #mport ipdb; ipdb.set_trace()
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
    }

def get_country_code(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    #import ipdb; ipdb.set_trace()
    return {
        "countryCode": data["countryCode"]
    }

def get_geo_localitation(ip):
    valid_ip = check_ip(ip)
    if valid_ip:
        url = f"https://freeipapi.com/api/json/{ip}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    
        return {
            "latitude": data["latitude"]
        } 
    else:
        raise NameError("Ip invalida")

def check_ip(ip):
    #Recibir la ip
    #Contar los caracteres pensando en IPv4 
    octetos = ip.split(".")
    list_length = len(octetos)
            
    if list_length == 4: 
        for octeto in octetos:
            octeto = int(octeto)
            if octeto >= 0 and octeto <= 254:
                continue
            else:
                return False
        return True
    else:
        return False
    #Si cumple continua el proceso
    #Sino manda un error

'''
if __name__ == "__main__":
    print(get_location("8.8.8.8"))
    print(get_country_code("8.8.8.8"))
    print(check_ip("8.8.8.8"))
    print(get_geo_localitation("8.8.8.8"))
'''
