#!/usr/bin/env python2

from urllib import urlopen
from bs4 import BeautifulSoup

SYNOPSIS = False
BASE_URL = 'http://www.tvrage.com'
BASE_SEARCH_URL = 'http://www.tvrage.com/search.php?search='
EPISODES_URL = '/episode_list/all'


def parse_series(series_div):
    '''
    Parse a bs tag containing a div to get series' title, last episode name and
    air date, episode list url, genre and status.

    Example div
    <div class=" clearfix" id="show_search">
        <dl>
            <dt>
                <h2>
                <a href="/Smash">Smash</a> #first a is title
                <img src="http://images.tvrage.com/flags/us.gif"/>
                </h2>
            </dt>
            <dd class="img">
                <a href="/Smash">
                    <img src="http://images.tvrage.com/shows/29/thumb125-28337.jpg" width="75"/>
                </a>
            </dd>
            <dd> #second dd is last episode air date
                <strong>Latest Episode:</strong>
                May/14/2012 
                <a href="/Smash/episodes/1065174545">Bombshell</a> #third a is name
            </dd>
            <dd> #third dd is genre and status
                <strong>Genre:</strong>
                Music |
                <strong>Status:</strong>
                Returning Series 
            </dd>
       </dl>
    </div>
    '''

    #print series.prettify()
    title = series_div.find_all('a')[0].string
    episodes_url = BASE_URL + series_div.find_all('a')[0]['href'] + EPISODES_URL
    if len(series_div.find_all('a')) == 3:
        last_air_date = series_div.find_all('dd')[1].contents[2]
        last_episode = series_div.find_all('a')[2].string
    else:
        last_air_date = u'unknown'
        last_episode = u'unknown'

    return title, episodes_url, last_air_date, last_episode

def get_synopsis(episode_url):
    html = urlopen(episode_url).read()
    soup = BeautifulSoup(html)
    synopsis = soup.find_all('div', 'show_synopsis')[0].contents[0]
    return synopsis.lstrip()

def parse_episode(episode_tr):
    '''
    Parse a bs tag containing a tr to get an episode's title, air date, season,
    episode number, and synopsis.

    Example tr
    <tr bgcolor="#FFFFFF" id="brow">
        <td align="center" width="45">
            1
        </td>
        <td align="center" width="40">
            <a href="/Supernatural/episodes/166205" title="Supernatural season 1 episode 1">
                1x01
            </a>
        </td>
        <td align="center" width="80">
            13/Sep/2005
        </td>
        <td style="padding-left: 6px;">
            <a href="/Supernatural/episodes/166205/?trailer=1#trailer">
                <img border="0" height="13" src="/_layout_v3/misc/film.gif" title="View Trailer"/>
            </a>
            <a href="/Supernatural/episodes/166205">
                Pilot
            </a>
        </td>
        <td align="center">
            <a href="/Supernatural/episodes/166205/gallery">
                0
            </a>
        </td>
        <td align="center">
            9.5
        </td>
    </tr>
    '''
    anchors = episode_tr.find_all('a')
    td = episode_tr.find_all('td')
    number = anchors[0].string
    name = td[3].find_all('a')[-1].string
    season = number.split('x')[0]
    air_date = td[2].string
    episode_url = BASE_URL + anchors[-2]['href']
    synopsis = ''
    
    if SYNOPSIS:
        synopsis = get_synopsis(episode_url)
 
    if len(season) != 1:
        return None
    else:
        return number, name, season, air_date, synopsis

def search_series(series_name):
    series_name = series_name.replace(' ','+')
    url = BASE_SEARCH_URL + series_name

    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    series_list = soup.find_all(id='show_search')

    results = []
    for item in series_list:
        results.append(parse_series(item))
    return results

def get_episodes(series_tuple):
    url = series_tuple[1]

    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    episodes_table = soup.find_all(id='brow')

    episode_list = []
    for item in episodes_table:
        episode = parse_episode(item)
        if episode != None:
            episode_list.append(episode)
    return episode_list

def main():
    #results = search_series('Flash')
    #episode_list = get_episodes(results[0])
    #for episode in episode_list:
    #    print (episode)
    #    
    print ( '1. Search for series \n2. Check for series updates \n3. ' )
    decision = raw_input('#: ')
    if decision == '1':
        series = raw_input('Series:')
        results = search_series(series)
        for show in results:
            show = show.encode("utf-8")
            print ( '{0}: {1},{2}'.format(show[0], show[3], show[2] ))
    #elif decision ==2:
        
        
    
if __name__ == '__main__':
    main()
