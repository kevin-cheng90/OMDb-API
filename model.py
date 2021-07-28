# model.py
import urllib.request
import urllib.parse
import json
import os.path as op
import csv
# ENTER OMDb API KEY HERE
API_KEY = ''


class Connect():
    def __init__(self):
        self.season_url = ''
        self.episode_url = ''
        self.seasons = 0
        self.episodes = []
        self.series_name = ''
        self.saved_info = []

    def take_input(self, series_name: str):
        # Takes an series name as an input and creates an API
        # url for that series name
        series_name = series_name.replace(' ', '+')
        self.series_name = series_name
        self.season_url = ('http://www.omdbapi.com/?type=series&t=' +
                           series_name + '&episodes&apikey=3f536bb9')

    def get_total_seasons(self):
        # Gets the total number of seasons for get_episodes to
        # know how many seasons to loop through
        response = urllib.request.urlopen(self.season_url)
        data = response.read()
        text = data.decode(encoding='utf-8')
        obj1 = json.loads(text)
        self.seasons = obj1['totalSeasons']

    def get_episodes(self):
        # Uses self.seasons to loop through every season and gather
        # information from each one
        for i in range(int(self.seasons)):
            self.episode_url = ('http://omdbapi.com/?type=series&t=' +
                                self.series_name + '&Season=' +
                                str(i+1) + '&apikey=' + API_KEY)
            response = urllib.request.urlopen(self.episode_url)
            data = response.read()
            text = data.decode(encoding='utf-8')
            obj1 = json.loads(text)
            self.episodes.append(obj1)

    def return_episodes(self):
        # Returns the episodes gathered
        return self.episodes

    def gather_info(self, saved_ep: [str]):
        # Gathers the plot of the saved episodes
        for x in saved_ep:
            stripped_x = x.replace(' ', '')
            split_str = stripped_x.split(':--:')
            season_ep = split_str[1].split('|')
            season_number = season_ep[0].replace('Season', '')
            episode_number = season_ep[1].replace('Episode', '')
            # This is the url that contains the plot of the episode
            plot_url = ('http://www.omdbapi.com/?type=series&t=' +
                        self.series_name + '&Season=' + season_number +
                        '&Episode=' + episode_number + '&apikey=' +
                        API_KEY)
            response = urllib.request.urlopen(plot_url)
            data = response.read()
            text = data.decode(encoding='utf-8')
            obj = json.loads(text)
            self.saved_info.append(obj)

    def return_saved_info(self):
        # Returns self.saved_info, containing information about episode plots
        return self.saved_info

    def handle_saved(self, filename: str):
        # Saves the Title, Season, Episode, and Plot to a csv file
        with open(filename, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(['Title', 'Season', 'Episode', 'Plot'])
            for x in self.saved_info:
                filewriter.writerow([x['Title'], x['Season'], x['Episode'],
                                    x['Plot']])
