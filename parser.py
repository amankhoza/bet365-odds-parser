import os
import sys
import json
from bs4 import BeautifulSoup


def contents(element):
    return list(map(lambda x: x.next, element))


filepath = sys.argv[1]

soup = BeautifulSoup(open(filepath), 'lxml')

store = []

for section in soup.find_all('div', {'class': 'liveAlertKey'}):
    section_em = section.h1.em
    section_name = section_em.next.strip()
    competition = ''
    if section_em.find('button'):
        market = section_name
    else:
        competition = section_name
        market = 'Full Time Result'
    for div in section.find_all('div'):
        if div.has_attr('class') and ('podHeaderRow' in div['class']):
            date = div.find('div', {'class': 'wideLeftColumn'}).next
            odds_types = contents(div.find_all('em'))
        if div.has_attr('data-fixtureid'):
            inplay = False
            start_time = ''
            game_clock = div.find('span', {'class': 'ippg-Market_GameClock'})
            if game_clock:
                game_clock = game_clock.next
                inplay = True
            else:
                inplay = False
                start_time = div.find('div', {'class': 'ippg-Market_GameStartTime'}).next
            teams = contents(div.find_all('span', {'class': 'ippg-Market_Truncator'}))
            home_team = teams[0]
            away_team = teams[1]
            match_name = home_team + ' v ' + away_team
            odds = contents(div.find_all('span', {'class': 'ippg-Market_Odds'}))
            if not odds:
                continue
            odds_object = {}
            for i in range(0, len(odds_types)):
                odds_object[odds_types[i]] = odds[i]
            store.append({'competition': competition, 'date': date, 'inplay': inplay, 'start_time': start_time,
                          'game_clock': game_clock, 'name': match_name, 'teams': teams, 'home': home_team,
                          'away': away_team, market: odds_object})

out_filepath = os.path.splitext(filepath)[0] + '.json'
with open(out_filepath, 'w') as out_file:
    json.dump(store, out_file)
