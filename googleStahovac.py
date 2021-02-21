import requests
# import os
from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# import webbrowser
query_list = input("Zadej token: ").split(",")
print(query_list)
celkovy_list_obrazku = []
for query in query_list:
  list_our_query = []
  youtube_search =f"""https://www.google.cz/search?q={query}&authuser=0&hl=en&sxsrf=ALeKk018wPckjR7oGWn3A-_3W9BpGD4Siw:1603054706175&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi-jsSShL_sAhWKDxQKHSLiCJMQ_AUoAXoECA4QAw&biw=1366&bih=600"""
#   print(youtube_search)
  r = requests.get(youtube_search)
  html = r.text
  print(html)
  soup = BeautifulSoup(html, 'html.parser')
  for i in soup.find_all("img"):
    if ".gif" not in i["src"]:
      print(i["src"])
      list_our_query.append(i["src"])
  celkovy_list_obrazku.append(list_our_query)
#   # upravene = [z.split("&")[0] for z in celkovy_list_zprav if not z.startswith("https://accounts.google.com") if len(z.split("&")[0]) < 250 and len(z.split("&")[0]) > 60 ]






# ------------------------------------------------------------------
import requests
import time
import os
start_measure = time.time()
# Function for downloading
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3] #a way how to name the picture
    img_name = '{}.jpg'.format(img_name)
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print('{} was downloaded...'.format(img_name))
threads = [] #prepare a list for future threads
for name,img_url_list in zip(query_list,celkovy_list_obrazku):
  path = f"/content/{name}"
  try:
    os.mkdir(path)
    os.chdir(path)
  except FileExistsError:
    print("Jiz vytvorena")
  for url in img_url_list:
        download_image(url)
  stop_measure = time.time()
  print('Finished in {} seconds'.format(stop_measure-start_measure))



