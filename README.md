# Тестовое задание для Nova

Для запуска необходим Docker:


```bash
$ git clone https://github.com/aimerkz/nova-test.git
$ cd nova-test
$ cp env.example .env
$ docker-compose up -d
```
Перейдите по ссылке: \
[Nova-test API](http://127.0.0.1:8001/api/docs/)

```
 - GET/Upload-file - просмотр записей о загруженных файлах в Google Drive
 - POST/Upload-file - загрузка файла в Google Drive по переданным name и data в теле запроса
```
Зайти в [Google Drive](https://drive.google.com/drive/u/1/folders/1KvwiJ0j5DYv85B22kEu1CSXJIYRrhGSA) и проверить наличие файла
