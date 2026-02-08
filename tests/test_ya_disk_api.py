import requests
import unittest

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
TOKEN = "введите ваш токен" # токен с полигона Яндекс https://yandex.ru/dev/disk/poligon
headers = {'Authorization': f'OAuth {TOKEN}'}
folder_name = "test_folder" # название тестовой папки

class TestYaDiskAPI(unittest.TestCase):

    def test_create_folder(self):
        """Создание папки"""
        response = requests.put(BASE_URL, headers=headers, params={'path': folder_name})
        self.assertEqual(response.status_code, 201, f"Ошибка при создании, ожидался код 201, получен {response.status_code}")

    def test_create_folder_exist(self):
        """Создание папки с уже существующим именем"""
        response = requests.put(BASE_URL, headers=headers, params={'path': folder_name})
        self.assertEqual(response.status_code, 409,
                         f"При проверке, ожидался код 409, получен {response.status_code}")


    def test_create_folder_invalid_path(self):
        response = requests.put(BASE_URL, headers=headers, params={'path': 'disk://///'})
        self.assertEqual(response.status_code, 404,
                         f"Ожидался код 404, получен {response.status_code}")


    @classmethod
    def tearDownClass(cls):
        """
        После ВСЕХ тестов. Пытаемся удалить тестовую папку, если она есть
        """
        try:
            requests.delete(BASE_URL, headers=headers, params={'path': folder_name, 'permanently': 'true'})
            print(f"Тестовая папка {folder_name} удалена")
        except Exception as err:
            print(f"Ошибка при удалении: {err}")