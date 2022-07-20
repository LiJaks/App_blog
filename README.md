# Запуск приложения
   Старт работы приложения осуществляется с помощью команды **python manage.py runserver**
   
   Создание миграций командой **python manage.py makemigrations**
   
   Применение миграций **python manage.py migrate**

## Структура и возможности приложения
   **_app_blog - пакет с файлами блога. Создание, загрузка, показ и детальное отображение записи блога, а также тесты приложения._**
  
   **_app_users - пакет с файлами приложения взаимодействующие с пользователями. Регистрация, редактировние, отображение профиля, залогинивание, а также тесты прилоежения._**
   
   **_djtesting - пакет с основными данными всего проекта._**
   
   **_files_for_tests - папка хранения файлов, используемых для тестирования приложений._**
   
   **_media - папка загрузки файлов и изображения от пользователей._**
   
   **_db.sqlite - файл запуска приложения._**
  
В приложении осуществляет регистрацию пользователя с загрузкой изображения для его профиля, а также редактирование профиля. Авторизированные пользователи могут создавать, редактировать и удалять свои записи для блога. Записи доступны к прочтению для любого пользователя. Реализованы тесты, покрывающие основные аспекты работы приложения.
