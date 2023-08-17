import requests
import time
from bs4 import BeautifulSoup
import json

from datetime import date, datetime
from datetime import datetime, date

from db.database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db import models

from dictionary import odd_types
from converter import get_types

db = SessionLocal() 

db.query(models.Prediction).delete()
db.commit()

today = str(date.today())

base_url = "https://www.vseprosport.by"

url = "https://www.vseprosport.by/news/football/all"

response = requests.get(url).text

soup = BeautifulSoup(response, 'lxml')

links_to_single = soup.find_all('a', class_="forecast")

links = []

for link in links_to_single:
    link = link.get('href')
    link = base_url + link
    links.append(link)

with open('json/vse.json', 'w', encoding='utf-8') as f:
    json.dump(links, f, indent=4, ensure_ascii=False)


with open('json/vse.json', 'r', encoding='utf-8') as f:
    links = json.load(f)

data = {}
events = []



for link in links:
    url  = requests.get(link).text

    soup = BeautifulSoup(url, 'lxml')

    teams_info = []

    title = soup.find('h1', class_='title').text
    country = soup.find('span', class_='fs-12').text
    league = soup.find('div', class_='tournamentplace').text
    matchtime = soup.find('div', class_='matchtime').text
    matchdate = soup.find('div', class_='matchdate').text
    teams_links = soup.find_all('a', class_='team-img')

    teams_hrefs = [team_link.get('href') for team_link in teams_links]

    teams_names_en = []
    for team_href in teams_hrefs:
        team_name = team_href.split('/')
        # print(team_name)
        teams_names_en.append(team_name[2])

    teams_imgs_src = []
    for team_img in teams_links:
        img = team_img.find('img', class_='img-fluid')['src']
        teams_imgs_src.append(img)

    teams_names = [team_name.find('span').text for team_name in teams_links]

    author = soup.find('div', class_='author-info').find('span', class_='name').text

    review_teams = soup.find('div', class_='review-teams')

    anons = [content.text for content in review_teams.find_all('div', class_='default-content')]

    stat_titles = soup.find_all('div', class_='statistic-title')

    prediction_section = soup.find('section', class_="prediction-section")

    prediction_content = prediction_section.find_all('p')
    predictions = [p.text for p in prediction_content 
                   if 'Наш прогноз' in p.text 
                   or 'Прогноз' in p.text 
                   or 'Наша ставка' in p.text
                   or 'Выбираем ставку' in p.text
                   ]


    def get_type(predictions, func):
        prediction_type = {}
        _odds = func
        for prediction in predictions:
            for odd_type in _odds:
                if odd_type in prediction:
                    # prediction_type = {
                    #             "type": odd_type
                    #         }
                    for team_name in teams_names:
                        if f'«{team_name}»' in prediction\
                        \
                        or f'{team_name}а' in prediction\
                        or f'{team_name[:-1]}а' in prediction\
                        \
                        or f'{team_name}у' in prediction\
                        or f'{team_name[:-1]}у' in prediction\
                        \
                        or f'{team_name}и' in prediction\
                        or f'{team_name[:-1]}и' in prediction\
                        \
                        or f'{team_name[:-1]}ы' in prediction\
                        or f'{team_name}ы' in prediction:
                            prediction_type = {
                                "team": team_name,
                                "type": odd_type
                            }
        print(prediction_type)
        return prediction_type
   
    odd_type = get_type(predictions, get_types(odd_types))


    try: 
        data = {
            'title': title,
            'country': country,
            'league': league,
            'matchtime': matchtime,
            'matchdate': matchdate,
            'teams_hrefs': teams_hrefs,
            'teams_imgs_src': teams_imgs_src,
            'teams_names_en': teams_names_en,
            'teams_names': teams_names,
            'author': author,
            'anons': anons,
            'predictions': odd_type,
            # 'predictions': predictions
        }
    except:
        continue

    events.append(data)


with open('json/predictions.json', 'w', encoding='utf-8') as f:
    json.dump(events, f, indent=4, ensure_ascii=False)

with open('json/predictions.json', 'r', encoding='utf-8') as f:
    events = json.load(f)

for event in events:

    game = models.Prediction()

    game.title = event['title']
    game.country = event['country']
    game.league = event['league']
    game.matchtime = event['matchtime']
    game.matchdate = event['matchdate']
    game.home_team_link = event['teams_hrefs'][0]
    game.away_team_link = event['teams_hrefs'][1]
    game.home_team_img = event['teams_imgs_src'][0]
    game.away_team_img = event['teams_imgs_src'][1]
    game.home_team_name_en = event['teams_names_en'][0]
    game.away_team_name_en = event['teams_names_en'][1]
    game.home_team_name = event['teams_names'][0]
    game.away_team_name = event['teams_names'][1]
    game.author = event['author']
    game.home_team_anons = event['anons'][0]
    game.away_team_anons = event['anons'][1]
    game.predictions = event['predictions']
 

    db.add(game)
    db.commit()