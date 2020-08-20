#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ananas
from ananas import html_strip_tags
from bs4 import BeautifulSoup
import json
import requests
import time
import emoji

KEY = "&key=0ad1aed5d18442c9a13f7caa139df5be"
APIURL_locid = "https://geoapi.heweather.net/v2/city/lookup?lang=en&location="
APIURL_Now = "https://free-api.heweather.net/s6/weather/now?lang=en&location="
APIURL_forecast = "https://free-api.heweather.net/s6/weather/forecast?lang=en&location="


class ExampleBot(ananas.PineappleBot):

    # Get some current weather information data
    def now_weather(self):
        url = APIURL_Now + location + KEY
        now_res = requests.get(url)
        now_res_json = now_res.json()

        # Actual weather temperature
        real_tmp = now_res_json['HeWeather6'][0]['now']['tmp']
        # Somatosensory temperature
        feel_tmp = now_res_json['HeWeather6'][0]['now']['fl']

        # Get information back
        return real_tmp, feel_tmp


    def today_weather(self):
        # Weather forecast
        now_weathers = []

        url = APIURL_forecast + location + KEY
        forecast_res = requests.get(url)
        forecast_res_json = forecast_res.json()
        # print(forecast_res_json)
        
        ############################################################
        # Public information
        ############################################################
        # Country, Province, Region, Latitude, Longitude, Local Weather Update Time, Status Information
        country = forecast_res_json['HeWeather6'][0]['basic']['cnty']
        province = forecast_res_json['HeWeather6'][0]['basic']['admin_area']
        city_name = forecast_res_json["HeWeather6"][0]["basic"]["location"]
        lat = forecast_res_json['HeWeather6'][0]['basic']['lat']
        lon = forecast_res_json['HeWeather6'][0]['basic']['lon']
        local_update_weather_time = forecast_res_json['HeWeather6'][0]['update']['loc']
        status = forecast_res_json['HeWeather6'][0]['status']
        ###########################################################

        ###########################################################
        # Get general weather information
        # daily_forecast is a list structure, which can be analyzed by taking out the elements inside separately
        daily_forecast = forecast_res_json['HeWeather6'][0]['daily_forecast']

        # Get weather information for today
        now_weathers = daily_forecast[0]
        # Get date
        now_date = now_weathers['date']
        # Get today's weather status information - daytime
        now_cond_txt_d = now_weathers['cond_txt_d']
        # Get sunrise, UV intensity, sunset, moonrise, moonset
        now_sr = now_weathers['sr']
        now_uv_index = now_weathers['uv_index']
        now_ss = now_weathers['ss']
        now_mr = now_weathers['mr']
        now_ms = now_weathers['ms']
        # Get today's weather status information - evening
        now_cond_txt_n = now_weathers['cond_txt_n']

        # Highest temperature, lowest temperature, relative humidity
        now_tmp_max = now_weathers['tmp_max']
        now_tmp_min = now_weathers['tmp_min']
        now_hum = now_weathers['hum']

        # Wind direction, wind force, wind speed, rainfall, rainfall probability
        now_wind_dir = now_weathers['wind_dir']
        now_wind_sc = now_weathers['wind_sc']
        now_wind_spd = now_weathers['wind_spd']
        now_pcpn = now_weathers['pcpn']
        now_pop = now_weathers['pop']

        # Get the data back
        return country, province, city_name, lat, lon, local_update_weather_time, status,         now_date, now_cond_txt_d, now_sr, now_uv_index, now_ss, now_mr, now_ms, now_cond_txt_n,         now_tmp_max, now_tmp_min, now_hum, now_wind_dir, now_wind_sc, now_wind_spd, now_pcpn, now_pop


    def tomorrow_weather(self):
        # Tomorrow weather forecast
        tomorrow_weather = []

        url = APIURL_forecast + location + KEY
        forecast_res = requests.get(url)
        forecast_res_json = forecast_res.json()
        # print(forecast_res_json)
        
        ############################################################
        # Public information
        ############################################################
        # Country, Province, Region, Latitude, Longitude, Local Weather Update Time, Status Information
        country = forecast_res_json['HeWeather6'][0]['basic']['cnty']
        province = forecast_res_json['HeWeather6'][0]['basic']['admin_area']
        city_name = forecast_res_json["HeWeather6"][0]["basic"]["location"]
        lat = forecast_res_json['HeWeather6'][0]['basic']['lat']
        lon = forecast_res_json['HeWeather6'][0]['basic']['lon']
        local_update_weather_time = forecast_res_json['HeWeather6'][0]['update']['loc']
        status = forecast_res_json['HeWeather6'][0]['status']
        ###########################################################

        ###########################################################
        # Get general weather information
        # daily_forecast is a list structure, which can be analyzed by taking out the elements inside separately
        daily_forecast = forecast_res_json['HeWeather6'][0]['daily_forecast']

        # Get weather forecast information for tomorrow
        tomorrow_weather = daily_forecast[1]
        # Get date
        tomorrow_date = tomorrow_weather['date']

        # Get tomorrow's weather status information - daytime
        tomorrow_cond_txt_d = tomorrow_weather['cond_txt_d']
        # Get sunrise, UV intensity, sunset, moonrise, moonset
        tomorrow_sr = tomorrow_weather['sr']
        tomorrow_uv_index = tomorrow_weather['uv_index']
        tomorrow_ss = tomorrow_weather['ss']
        tomorrow_mr = tomorrow_weather['mr']
        tomorrow_ms = tomorrow_weather['ms']
        # Get tomorrow's weather status information - evening
        tomorrow_cond_txt_n = tomorrow_weather['cond_txt_n']

        # Highest temperature, lowest temperature, relative humidity
        tomorrow_tmp_max = tomorrow_weather['tmp_max']
        tomorrow_tmp_min = tomorrow_weather['tmp_min']
        tomorrow_hum = tomorrow_weather['hum']

        # Wind direction, wind force, wind speed, rainfall, rainfall probability
        tomorrow_wind_dir = tomorrow_weather['wind_dir']
        tomorrow_wind_sc = tomorrow_weather['wind_sc']
        tomorrow_wind_spd = tomorrow_weather['wind_spd']
        tomorrow_pcpn = tomorrow_weather['pcpn']
        tomorrow_pop = tomorrow_weather['pop']

        # Get the data back
        return country, province, city_name, lat, lon, local_update_weather_time, status, tomorrow_date, tomorrow_cond_txt_d, tomorrow_sr, tomorrow_uv_index, tomorrow_ss, tomorrow_mr, tomorrow_ms, tomorrow_cond_txt_n,        tomorrow_tmp_max, tomorrow_tmp_min, tomorrow_hum, tomorrow_wind_dir, tomorrow_wind_sc, tomorrow_wind_spd, tomorrow_pcpn, tomorrow_pop


    def the_day_after_tomorrow_weather(self):
        # Acquired weather forecast
        the_day_after_tomorrow_weather = []

        url = APIURL_forecast + location + KEY
        forecast_res = requests.get(url)
        forecast_res_json = forecast_res.json()
        # print(forecast_res_json)
        
        ############################################################
        # Public information
        ############################################################
        # Country, Province, Region, Latitude, Longitude, Local Weather Update Time, Status Information
        country = forecast_res_json['HeWeather6'][0]['basic']['cnty']
        province = forecast_res_json['HeWeather6'][0]['basic']['admin_area']
        city_name = forecast_res_json["HeWeather6"][0]["basic"]["location"]
        lat = forecast_res_json['HeWeather6'][0]['basic']['lat']
        lon = forecast_res_json['HeWeather6'][0]['basic']['lon']
        local_update_weather_time = forecast_res_json['HeWeather6'][0]['update']['loc']
        status = forecast_res_json['HeWeather6'][0]['status']
        ###########################################################

        ###########################################################
        # Get general weather information
        # daily_forecast is a list structure, which can be analyzed by taking out the elements inside separately
        daily_forecast = forecast_res_json['HeWeather6'][0]['daily_forecast']

        # Get weather forecast information for the day after tomorrow
        the_day_after_tomorrow_weather = daily_forecast[2]
        # Get date
        the_day_after_tomorrow_date = the_day_after_tomorrow_weather['date']

        # Get the weather information of the day after tomorrow - daytime
        the_day_after_tomorrow_cond_txt_d = the_day_after_tomorrow_weather['cond_txt_d']
        # Get sunrise, UV intensity, sunset, moonrise, moonset
        the_day_after_tomorrow_sr = the_day_after_tomorrow_weather['sr']
        the_day_after_tomorrow_uv_index = the_day_after_tomorrow_weather['uv_index']
        the_day_after_tomorrow_ss = the_day_after_tomorrow_weather['ss']
        the_day_after_tomorrow_mr = the_day_after_tomorrow_weather['mr']
        the_day_after_tomorrow_ms = the_day_after_tomorrow_weather['ms']
        # Get the weather information of the day after tomorrow -- evening
        the_day_after_tomorrow_cond_txt_n = the_day_after_tomorrow_weather['cond_txt_n']

        # Highest temperature, lowest temperature, relative humidity
        the_day_after_tomorrow_tmp_max = the_day_after_tomorrow_weather['tmp_max']
        the_day_after_tomorrow_tmp_min = the_day_after_tomorrow_weather['tmp_min']
        the_day_after_tomorrow_hum = the_day_after_tomorrow_weather['hum']

        # Wind direction, wind force, wind speed, rainfall, rainfall probability
        the_day_after_tomorrow_wind_dir = the_day_after_tomorrow_weather['wind_dir']
        the_day_after_tomorrow_wind_sc = the_day_after_tomorrow_weather['wind_sc']
        the_day_after_tomorrow_wind_spd = the_day_after_tomorrow_weather['wind_spd']
        the_day_after_tomorrow_pcpn = the_day_after_tomorrow_weather['pcpn']
        the_day_after_tomorrow_pop = the_day_after_tomorrow_weather['pop']

        # Get the data back
        return country, province, city_name, lat, lon, local_update_weather_time, status,the_day_after_tomorrow_date, the_day_after_tomorrow_cond_txt_d, the_day_after_tomorrow_sr, the_day_after_tomorrow_uv_index, the_day_after_tomorrow_ss,        the_day_after_tomorrow_mr, the_day_after_tomorrow_ms, the_day_after_tomorrow_cond_txt_n, the_day_after_tomorrow_tmp_max, the_day_after_tomorrow_tmp_min,        the_day_after_tomorrow_hum, the_day_after_tomorrow_wind_dir, the_day_after_tomorrow_wind_sc, the_day_after_tomorrow_wind_spd, the_day_after_tomorrow_pcpn, the_day_after_tomorrow_pop
    
    def get_emoji(self, str):

        if str == "Sunny":
            eomjis = emoji.emojize(u'\u2600' + u'\uFE0F')
        elif str == "Partly Cloudy"  or str =="Few Clouds":
            eomjis = emoji.emojize(u'\u26C5' + u'\uFE0F')
        elif str == "Cloudy":
            eomjis = emoji.emojize(u'\u2601' + u'\uFE0F')
        elif str == "Shower Rain" or str =="Light to moderate rain" or str =="Light Rain" or str =="Drizzle Rain" or str =="Rain":
            eomjis = emoji.emojize(u'\U0001F326' + u'\uFE0F')
        elif str == "Thundershower" or str =="Heavy Thunderstorm" or str =="Thundershower with hail":
            eomjis = emoji.emojize(u'\u26C8' + u'\uFE0F')
        elif str == "Moderate Rain" or str =="Heavy Rain" or str =="Heavy Shower Rain" or str =="Extreme Rain" or str =="Moderate to heavy rain":
            eomjis = emoji.emojize(u'\U0001F327' + u'\uFE0F')
        elif str == "Storm" or str =="Heavy rain to storm" or str =="Storm to heavy storm" or str =="Heavy to severe storm" or str =="Heavy Storm" or str =="Severe Storm":
            eomjis = emoji.emojize(u'\U0001F32A' + u'\uFE0F')
        elif str == "Freezing Rain" or str =="Shower Snow" or str =="Snow Flurry" or str =="Light Snow" or str =="Sleet" or str =="Rain And Snow":
            eomjis = emoji.emojize(u'\U0001F328' + u'\uFE0F')
        elif str == "Moderate Snow" or str =="Heavy Snow" or str =="Snowstorm" or str =="Light to moderate snow" or str =="Moderate to heavy snow" or str =="Heavy snow to snowstorm" or str =="Snow" :
            eomjis = emoji.emojize(u'\u2744' + u'\uFE0F')       
        elif str == "Mist" or str =="Foggy" or str =="Haze" or str =="Sand" or str =="Dust" or str =="Dense fog" or str =="Strong fog" or str =="Moderate haze" or str =="Heavy haze" or str =="Severe haze" or str =="Heavy fog" or str =="Extra heavy fog":
            eomjis = emoji.emojize(u'\U0001F301' + u'\uFE0F')
        elif str == "Duststorm" or str =="Sandstorm":
            eomjis = emoji.emojize(u'\U0001F32B' + u'\uFE0F')
        elif str == "Hot":
            eomjis = emoji.emojize(u'\U0001F975' + u'\uFE0F')
        elif str == "Cold":
            eomjis = emoji.emojize(u'\U0001F976' + u'\uFE0F')
        else:
            eomjis = emoji.emojize(u'\U0001F916' + u'\uFE0F')

        return eomjis

    def rain(self, pcn):

        pcn = float(pcn)
        if pcn == 0.0:
            msg = "No"
        elif 0.0 < pcn <= 0.2:
            msg = "Very Small"
        elif 0.2 < pcn <= 1.0:
            msg = "Small"
        elif 1.0 < pcn <= 3.0:
            msg = "Moderate"
        elif 3.0 < pcn <= 6.0:
            msg = "Bit Heavy"
        elif 6.0 < pcn <= 13.0:
            msg = "Heavy"
        elif pcn > 13.0 :
            msg = "Very Heavy"
        return msg

    def rain_pop(self, pop):

        pop = int(pop)
        if pop == 0:
            msg = "No"
        elif 0 < pop <= 20:
            msg = "Unlikely"
        elif 20 < pop <= 40:
            msg = "Likely"
        elif 40 < pop <= 60:
            msg = "Bit Likely"
        elif 60 < pop <= 80:
            msg = "Very Likely"
        elif 80 < pop <= 100:
            msg = "Almost Certain"
        return msg     

    def get_time(self):
        tim = time.localtime(time.time())
        tm_hour = tim[3]
        tm_min = tim[4]
        return tm_hour, tm_min

    def today(self, tm_hour, tm_min):
        # Get the return value of the now_weather() function
        real_tmp, feel_tmp = self.now_weather()

        # Get all return values of now_and_future_twodays_weather() function
        country, province, city_name, lat, lon, local_update_weather_time, status,        now_date, now_cond_txt_d, now_sr, now_uv_index, now_ss, now_mr, now_ms, now_cond_txt_n, now_tmp_max, now_tmp_min, now_hum, now_wind_dir, now_wind_sc, now_wind_spd, now_pcpn, now_pop = self.today_weather()

        # Message construction
        msg_today = 'Region：'+country+'--'+province+'--'+city_name+'\n'+'Longitude：'+lon+'\n'+'Latitude：'+lat+'\n============\n' + 'The Forecast For Today '+'('+ now_date+'):'+'\nWeather conditions：'+ now_cond_txt_d +'┆'+ self.get_emoji(now_cond_txt_d)+'\nUV intensity：'+now_uv_index+'\nHighest temperature：'+now_tmp_max + '℃' +'\nMinimum temperature：'+now_tmp_min+ '℃' + '\nSomatosensory temperature：'+feel_tmp+ '℃' +'\nRelative humidity：'+now_hum+ '%' +'\nWind direction：'+now_wind_dir+'\nWind speed：'+now_wind_spd+ 'km/h' +'\nIs it raining：'+ self.rain(now_pcpn) +'\nRain probability：'+now_pop+ '%' +'\n============' + '\nEvery day is beautiful, just enjoy it!'+'\n----Weather Bot'+ '\t'+ emoji.emojize(u'\U0001F916' + u'\uFE0F')

        return msg_today
    
    def tomorrow(self, tm_hour, tm_min):

        # Get all return values of now_and_future_twodays_weather() function
        country, province, city_name, lat, lon, local_update_weather_time, status, tomorrow_date, tomorrow_cond_txt_d, tomorrow_sr, tomorrow_uv_index, tomorrow_ss, tomorrow_mr, tomorrow_ms, tomorrow_cond_txt_n, tomorrow_tmp_max, tomorrow_tmp_min, tomorrow_hum, tomorrow_wind_dir, tomorrow_wind_sc, tomorrow_wind_spd, tomorrow_pcpn, tomorrow_pop = self.tomorrow_weather()

        # Message construction
        msg_tomorrow = 'Region：'+country+'--'+province+'--'+city_name+'\n'+'Longitude：'+lon+'\n'+'Latitude：'+lat+'\n============\n' + 'The Forecast For Tomorrow '+'('+tomorrow_date+'):'+'\nWeather conditions：'+ tomorrow_cond_txt_d +'┆'+ self.get_emoji(tomorrow_cond_txt_d)+'\nUV intensity：'+tomorrow_uv_index+'\nHighest temperature：'+tomorrow_tmp_max+'℃' +'\nMinimum temperature：'+tomorrow_tmp_min+'℃' + '\nRelative humidity：'+tomorrow_hum+'%' +'\nWind direction：'+tomorrow_wind_dir+'\nWind speed：'+tomorrow_wind_spd+'km/h' +'\nWill it rain tomorrow：'+self.rain_pop(tomorrow_pop)+'\nRain probability：'+tomorrow_pop+'%' +'\n============' + '\nEvery day is beautiful, just enjoy it!'+'\n----Weather Bot'+ '\t' + emoji.emojize(u'\U0001F916' + u'\uFE0F')

        return msg_tomorrow

    def the_day_after_tomorrow(self, tm_hour, tm_min):

        # Get all return values of now_and_future_twodays_weather() function
        country, province, city_name, lat, lon, local_update_weather_time, status, the_day_after_tomorrow_date, the_day_after_tomorrow_cond_txt_d, the_day_after_tomorrow_sr, the_day_after_tomorrow_uv_index, the_day_after_tomorrow_ss,  the_day_after_tomorrow_mr, the_day_after_tomorrow_ms, the_day_after_tomorrow_cond_txt_n, the_day_after_tomorrow_tmp_max, the_day_after_tomorrow_tmp_min, the_day_after_tomorrow_hum, the_day_after_tomorrow_wind_dir, the_day_after_tomorrow_wind_sc, the_day_after_tomorrow_wind_spd, the_day_after_tomorrow_pcpn,        the_day_after_tomorrow_pop = self.the_day_after_tomorrow_weather()

        # Message construction
        msg_the_day_after_tomorrow = 'Region：'+country+'--'+province+'--'+city_name+'\n'+'Longitude：'+lon+'\n'+'Latitude：'+lat+'\n============\n' + 'The Forecast For Day_After_Tomorrow '+'('+the_day_after_tomorrow_date+'):'+'\nWeather conditions：'+ the_day_after_tomorrow_cond_txt_d +'┆'+ self.get_emoji(the_day_after_tomorrow_cond_txt_d)+'\nUV intensity：'+the_day_after_tomorrow_uv_index+'\nHighest temperature：'+the_day_after_tomorrow_tmp_max+'℃' +'\nMinimum temperature：'+the_day_after_tomorrow_tmp_min+'℃' +'\nRelative humidity：'+the_day_after_tomorrow_hum+'%'+'\nWind direction：'+the_day_after_tomorrow_wind_dir+'\nWind speed：'+the_day_after_tomorrow_wind_spd+'km/h' +'\nWill it rain the_day_after_tomorrow：'+self.rain_pop(the_day_after_tomorrow_pop)+'\nRain probability：'+the_day_after_tomorrow_pop+'%' +'\n============' + '\nEvery day is beautiful, just enjoy it!'+'\n----Weather Bot'+ '\t' + emoji.emojize(u'\U0001F916' + u'\uFE0F')

        return msg_the_day_after_tomorrow

    @ananas.daily(hour=6, minute=15)
    # Automatically post the Weather conditions of the specified location at fixed time, the current location is Glasgow
    def toot(self):
        global location
        location = "E2080"
        tm_hour, tm_min = self.get_time()
        msg = self.today(tm_hour, tm_min)
        self.mastodon.toot(msg)
        print('Tooted: %s' % msg)
    
    @ananas.reply
    # Address ID query and Weather condition query
    def respond_weather(self, status, user):
        try:
            # post a reply of the form "@<user account>"
            global location
            username = user["acct"]
            msg_rec = html_strip_tags(status["content"], True, chr(31))

            bs = BeautifulSoup(status["content"], "lxml")
            # strip out mentions
            for mention in status["mentions"]:
                for a in bs.find_all(href=mention["url"]):
                    a.extract()
            # put all the lines in a list
            for br in bs.find_all("br"):
                br.replace_with('\n')
            #  then replace consecutive p tags with a double newline
            Input = [Input.text for Input in bs.find_all('p')]
            Input = '\n\n'.join(Input)
            #  finally split all the lines up at the newlines we just added
            Input = [Input.strip() for line in Input.splitlines() if Input.strip()]
            
            if len(Input) == 0:

                msg_date = "The weatherbot can query the weather conditions in the next three days" +'\n========\n'+ "1.Please @ Weatherbot + 'location' + ',' + 'Today' or 'Tomorrow' or 'Day After Tomorrow' to query (e.g. London,Today)"     +'\n========\n'+ "2.If the query result is not in the desired area, please @ Weatherbot + ’location’ + ',' + 'country code' + 'Today' or 'Tomorrow' or 'Day After Tomorrow'(e.g. London,GB,Today). The country code query address: https://www.iso.org/iso-3166-country-codes.html"

                self.mastodon.toot(msg_date)
            
            else:

                # According to "," split list elements
                location_date = Input[0].split(",")
                
                # If the length of the returned list after element separation is 1, it means that there is no "," in the original list; the purpose of user input is to query the location Id

                if len(location_date) == 2:
                    location = location_date[0].capitalize()
                    print(location_date[0],location_date[1])
                    
                    tm_hour, tm_min = self.get_time()
                    if location_date[1].capitalize() == "Today":
                        msg = self.today(tm_hour, tm_min)
                        self.mastodon.toot("@{} {}".format(username, '\n'+msg))
                    elif location_date[1].capitalize() == "Tomorrow":
                        msg = self.tomorrow(tm_hour, tm_min)
                        self.mastodon.toot("@{} {}".format(username, '\n'+msg))
                    elif location_date[1].title() == "Day After Tomorrow":
                        msg = self.the_day_after_tomorrow(tm_hour, tm_min)
                        self.mastodon.toot("@{} {}".format(username, '\n'+msg))

                # Otherwise, the user's purpose is to check weather conditions
                elif len(location_date) == 3:
                    
                    url = APIURL_locid + location_date[0].capitalize() + "&range=" + location_date[1].lower() + KEY
                    locid_res = requests.get(url)
                    locid_res_json = locid_res.json()

                    location = locid_res_json["location"][0]["id"]
                    print(location_date[0],location,location_date[1],location_date[2])

                    tm_hour, tm_min = self.get_time()
                    if location_date[2].capitalize() == "Today":
                        msg = self.today(tm_hour, tm_min)
                        self.mastodon.toot("@{} {}".format(username, '\n'+msg))
                    elif location_date[2].capitalize() == "Tomorrow":
                        msg = self.tomorrow(tm_hour, tm_min)
                        self.mastodon.toot("@{} {}".format(username, '\n'+msg))
                    elif location_date[2].title() == "Day After Tomorrow":
                        msg = self.the_day_after_tomorrow(tm_hour, tm_min)
                        self.mastodon.toot("@{} {}".format(username, '\n'+msg))
        except:
            msg = "This location is not found or Your input is incorrect, please re-enter"
            self.mastodon.toot("@{} {}".format(username, '\n'+msg))

        print("Received toot from {}: {}".format(username,msg_rec.replace(chr(31), "\n")))