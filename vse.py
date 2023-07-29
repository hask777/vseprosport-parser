import requests
from bs4 import BeautifulSoup
import json

base_url = "https://www.vseprosport.by"

# url = "https://www.vseprosport.by/news/all"

# response = requests.get(url).text

# soup = BeautifulSoup(response, 'lxml')

# links_to_single = soup.find_all('a', class_="forecast")

# links = []

# for link in links_to_single:
#     link = link.get('href')
#     link = base_url + link
#     links.append(link)

# with open('json/vse.json', 'w', encoding='utf-8') as f:
#     json.dump(links, f, indent=4, ensure_ascii=False)


with open('json/vse.json', 'r', encoding='utf-8') as f:
    links = json.load(f)

data = {}
result = []



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

    # for title in stat_titles:
    #     paragraphs = title.find_all('p')
    #     # for p in paragraphs:
    #     #     spans = p.find_all('span')
    #         # print(spans)
    #     try:
    #         stat_odds = [print(str(span.text)) for span in paragraphs]
    #     except:
    #         continue

    prediction_section = soup.find('section', class_="prediction-section")

    prediction_content = prediction_section.find_all('p')
    predictions = [p.text for p in prediction_content]
    print(predictions)

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
            'predictions': predictions
        }
    except:
        continue

    result.append(data)


with open('json/result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)


