import time
import httpx
import json
from threading import Thread


def downloader_first():
    url = 'https://jsonplaceholder.typicode.com/users'
    reader = httpx.get(url).json()
    with open('first.json', 'w') as file:
        json.dump(reader, file, indent=2)


def downloader_second():
    url = 'https://jsonplaceholder.typicode.com/albums'
    reader = httpx.get(url).json()
    with open('second.json', 'w') as file:
        json.dump(reader, file, indent=2)


def downloader_third():
    url = 'https://jsonplaceholder.typicode.com/photos'
    reader = httpx.get(url).json()
    with open('third.json', 'w') as file:
        json.dump(reader, file, indent=2)


def downloader_fourth():
    url = 'https://jsonplaceholder.typicode.com/todos'
    reader = httpx.get(url).json()
    with open('fourth.json', 'w') as file:
        json.dump(reader, file, indent=2)


def downloader_fifth():
    url = 'https://jsonplaceholder.typicode.com/users'
    reader = httpx.get(url).json()
    with open('fifth.json', 'w') as file:
        json.dump(reader, file, indent=2)


start = time.time()
first_wave = Thread(target=downloader_first(), daemon=True)
second_wave = Thread(target=downloader_second(), daemon=True)
third_wave = Thread(target=downloader_third(), daemon=True)
fourth_wave = Thread(target=downloader_fourth(), daemon=True)
fifth_wave = Thread(target=downloader_fifth(), daemon=True)

end = time.time()
print(int(end - start), '- seconds')
