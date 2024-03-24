# GeekBrains_Data_collection_and_markup_2024
Курс "Сбор и разметка данных" от GeekBrains образца 2024 года

## Урок 1. Основы клиент-серверного взаимодействия. Парсинг API
1. Ознакомиться с некоторые интересными API. https://docs.ozon.ru/api/seller/ https://developers.google.com/youtube/v3/getting-started https://spoonacular.com/food-api

[Решение задачи 1 для Озон (скриншот)](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№1/Изучение%20API%20Озон.JPG)

[Решение задачи 1 для YouTube (скриншот)](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№1/Изучение%20API%20Youtube_.JPG)

[Решение задачи 1 для Spoonacular (скриншот)](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№1/Изучение%20API%20spoonacular_.JPG)

2. Потренируйтесь делать запросы к API. Выберите публичный API, который вас интересует, и потренируйтесь делать API-запросы с помощью Postman. Поэкспериментируйте с различными типами запросов и попробуйте получить различные типы данных.

[Решение задачи 2 - запрос по автору через API сервиса Open Library](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№1/Публичный%20API%20Open%20Library%20Поиск%20по%20автору.JPG)

[Решение задачи 2 - запрос по названию книги через API сервиса Open Library](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№1/Публичный%20API%20Open%20Library%20Поиск%20по%20книге.JPG)

3. Сценарий Foursquare
4. Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
5. Используйте API Foursquare для поиска заведений в указанной категории.
6. Получите название заведения, его адрес и рейтинг для каждого из них.
7. Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.

[Решение задач 3 - 7](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№1/homework_seminar_1_05-03-2024_.ipynb)

## Урок 2. Парсинг HTML. BeautifulSoup
1. Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех книгах на сайте во всех категориях: название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

[Решение задачи 1 - код в файле .ipynb](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№2/homework_seminar_2_08-03-2024.ipynb)

2. Затем сохранить эту информацию в JSON-файле.

[Решение задачи 2 - ссылка на JSON-файл](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№2/books_from_books.toscrape.com.json)
   
## Урок 3. Системы управления базами данных MongoDB и Кликхаус в Python
1. Установите MongoDB на локальной машине, а также зарегистрируйтесь в онлайн-сервисе. https://www.mongodb.com/ https://www.mongodb.com/products/compass

[Решение задачи 1 - установленная локальная MongoDB с загруженными данными - скриншот](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№3/MongoDB%20с%20загруженными%20данными.JPG)

[Решение задачи 1 - регистрация в облачном сервисе MongoDB - скриншот](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№3/Регистрация%20в%20облачном%20сервисе%20MongoDB.JPG)

3. Загрузите данные который вы получили на предыдущем уроке путем скрейпинга сайта с помощью Buautiful Soup в MongoDB и создайте базу данных и коллекции для их хранения.
4. Поэкспериментируйте с различными методами запросов.

[Решение задач 3 - 4 - код в файле .ipynb](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№3/homework_seminar_3_12-03-2024.ipynb)   

5. Зарегистрируйтесь в ClickHouse.
6. Загрузите данные в ClickHouse и создайте таблицу для их хранения.

[Решение задач 5 - 6 - скриншот](https://github.com/AndreyOmi/GeekBrains_Data_collection_and_markup_2024/blob/main/Seminar_№3/Попытка%20работы%20с%20ClickHouse2.JPG)

Вывод о решении задач 5 - 6: загеристрироваться в ClickHouse получилось, но сервис не выдает API keys для доступа к облачному хранилищу из-за политики ограничений для России, поэтому загрузить данные в облачное хранилище невозможно.
