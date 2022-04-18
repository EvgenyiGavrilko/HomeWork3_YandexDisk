import requests

class YaUploader:
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def get_upload_link(self, file_path):
        params = {'path': file_path, 'overwrite': 'true'}
        headers = {'Content-Type': 'application/json', 'Authorization': self.token}
        response = requests.get(self.url, params=params, headers=headers)
        print(response.json())
        return response.json()

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(file_path).get('href')
        if not href:
            print('Файл не загружен')
            return False
        with open(file_path, 'rb') as f:
            response = requests.put(href, files={'file': f})
            if response.status_code == 201:
                print('Файл загружен')
                return True

if __name__ == '__main__':
    #Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
