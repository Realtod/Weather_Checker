# Weather_Checker

# Flask Weather Checker

## Описание проекта
Этот проект представляет собой веб-сервис на основе Flask, который позволяет пользователю вводить координаты двух городов и проверять неблагоприятные погодные условия на основе температуры, влажности, скорости ветра и вероятности дождя. Сервис использует **AccuWeather API** для получения данных о погоде.

---

## **Требования**
- Python 3.8 или выше
- Flask
- requests
- Действительный API-ключ для AccuWeather

---

## **Установка**

1. **Склонируйте репозиторий**:
   ```
   git clone https://github.com/your_username/weather_checker.git
   cd weather_checker
   ```

	2.	Создайте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # Для Linux/macOS
venv\Scripts\activate     # Для Windows
```
3.	Установите зависимости:
```
pip install -r requirements.txt
```

4.	Добавьте API-ключ AccuWeather:
   ```
	•	Откройте файл main.py.
	•	Найдите строку:
```
API_KEY = 'ваш_API_ключ'
```

	•	Замените 'ваш_API_ключ' на ваш действительный API-ключ.
```
Запуск сервера

	1.	Запустите Flask-сервер:

```python main.py```


	2.	Сервер будет доступен по адресу:

```http://127.0.0.1:5000/```

Проверка работоспособности

1. Главная страница

	•	Перейдите на:

```http://127.0.0.1:5000/```


•	Должно появиться сообщение:

```Flask работает!!!!!!!!!!!!```

2. Проверка маршрута /check_bad_weather

	1.	Перейдите на страницу:

```http://127.0.0.1:5000/check_bad_weather```


	2.	Введите координаты:
	•	Начальные координаты (широта, долгота): 55.7558,37.6173
	•	Конечные координаты (широта, долгота): 59.9311,30.3609
	3.	Нажмите кнопку отправки.
	4.	Ожидаемый результат:
В случае неблагоприятной погоды JSON-ответ будет выглядеть так:
```
{
  "Погода в 1-ом городке": "Погода неблагоприятна",
  "Погода во 2-ом городе": "Погода благоприятна"
}
```
Критерии неблагоприятной погоды

Погода считается неблагоприятной, если:
	•	Температура ниже -10°C или выше 35°C.
	•	Скорость ветра выше 45 км/ч.
	•	Влажность превышает 70%.
	•	Вероятность дождя превышает 70%.

Пример использования API

	1.	Получение LocationKey по координатам:

```GET /locations/v1/cities/geoposition/search?apikey=API_KEY&q=55.7558,37.6173```


	2.	Получение прогноза погоды на 1 час:

```GET /forecasts/v1/hourly/1hour/LOCATION_KEY?apikey=API_KEY&details=true```

Структура проекта

weather_checker/
│
├── templates/
│   └── get_route_points.html      # HTML-шаблон формы ввода
├── main.py                        # Основной файл приложения Flask
└── README.md                      # Документация проекта

Дополнительно

	•	Для работы проекта необходимо активное интернет-соединение.
	•	Проверьте лимиты использования API на AccuWeather Developer Portal.

Автор

Разработчик: Realtod
