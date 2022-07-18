from selenium import webdriver
from pyfiglet import Figlet
import requests
import socket
import folium
import time
import os

def get_ip_by_hostname():
    hostname = input(Figlet(font='slant').renderText('Enter URL :'))
    try: return socket.gethostbyname(hostname)
    except socket.gaierror as error: print(error)
    return socket.gethostname()

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]':str(response.get('query')) + "   " + str(response.get('org')),
            '[Сoordinates]': str(response.get('lat')) + "," + str(response.get('lon')),
            '[Region]':str(response.get('city')) + " (" + str(response.get('zip')) + "), " + str(response.get('regionName')) + " (" + str(response.get('region')) + "), " + str(response.get('country')) + ", " + str(response.get('timezone'))
        }
        for name,info in data.items(): print(f'{name}:{info}')
        return response.get('lat'), response.get('lon'), data['[Region]'], response.get('query'), response.get('org')
    except requests.exceptions.ConnectionError as error: print(error)

def marker(lat,lon, reg, ip, org):     #max_zoom_start:18
    marker = folium.Map(location=[lat,lon], zoom_start=13, tiles= "CartoDB dark_matter") # the value of the "tiles" parameter sets the style of the map 
    marker.circle_marker(location=[lat,lon], popup = f"{org}<br/>{reg}", radius=250, line_color='#3186cc', fill_color='#3186cc')
    marker.create_map(f'{os.getcwd()}/Desktop/map_{ip}.html')
    return f'map_{ip}.html'

def run_html_file(html_file):
    try:
        option = webdriver.ChromeOptions()
        option.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
        # provide the correct address for your files - {os.getcwd()}, I have it is: /USER/v.syroiezhin
        driver = webdriver.Chrome(executable_path=f"{os.getcwd()}/.wdm/drivers/chromedriver/mac64/103.0.5060.53/chromedriver", options=option)
        driver.get("file://" + f"{os.getcwd()}/Desktop/{html_file}")
        
    except Exception as error: print(error)
    finally: 
        time.sleep(60) # Selenium working hours
        driver.close()
        driver.quit()



if __name__ == '__main__':
    lat,lon,reg,ip,org = get_info_by_ip(get_ip_by_hostname())
    html_file = marker(lat,lon,reg,ip,org)
    run_html_file(f"{html_file}")
    
    