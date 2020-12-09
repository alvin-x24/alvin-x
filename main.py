import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date

api_key = "b261be96999d6be5a652dbac646e746f"
position = [300, 430, 555, 690, 825]

us_cities = ["New York", "Chicago", "Los Angeles", "Boston", "Miami"]
uk_cities = ["London", "Manchester", "Birmingham", "Edinburgh", "Glasgow"]
italy_cities = ["Venice", "Florence", "Milan", "Turin", "Bologna"]

country_list = [us_cities, uk_cities, italy_cities]

for country in country_list:
    image = Image.open("post.png")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("Inter.ttf", size=50)
    content = "Latest Weather Forecast"
    color = "rgb(255, 255, 255)"
    (x, y) = (46, 77)
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype("Inter.ttf", size=30)
    today = date.today()
    content = date.today().strftime("%A - %B %d, %Y")
    color = "rgb(255, 255, 255)"
    (x, y) = (46, 145)
    draw.text((x, y), content, color, font=font)

    index = 0

    for city in country:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)

        font = ImageFont.truetype("Inter.ttf", size=50)
        color = "rgb(0, 0, 0)"
        (x, y) = (135, position[index])
        draw.text((x, y), city, color, font=font)

        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(data["main"]["temp"]) + "\u00b0"
        color = "rgb(255, 255, 255)"
        (x, y) = (600, position[index])
        draw.text((x, y), content, color, font=font)

        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(data["main"]["humidity"]) + "%"
        color = "rgb(255, 255, 255)"
        (x, y) = (810, position[index])
        draw.text((x, y), content, color, font=font)

        index += 1

    # added section to name the images specifically

    if country == us_cities:
        country_imgName = "US-cities.png"
    elif country == uk_cities:
        country_imgName = "UK-cities.png"
    elif country == italy_cities:
        country_imgName = "Italy-cities.png"

    image.save("{}.png".format(country_imgName))
