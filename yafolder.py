import requests


class YaFolder:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}',
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {
            "href": "string",
            "method": "string",
            'path': f'disk:/',
            "templated": True
        }
        response = requests.get(files_url, headers=headers, params=params)
        return response.json()

    def upload_folder(self, folder_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {
            "href": "string",
            "method": "string",
            'path': f'disk:/{folder_name}',
            "templated": True
        }

        response = requests.put(upload_url, headers=headers, params=params)
        response.raise_for_status()
        return response.status_code
    