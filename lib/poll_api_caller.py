import http.client


def get_weather_data():
    conn = http.client.HTTPConnection("api.openweathermap.org")

    headers = {
        'cache-control': "no-cache"
    }

    conn.request("GET", "data/2.5/weather?zip=08540,us&appid=<provide-app-id-here>", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


get_weather_data()
