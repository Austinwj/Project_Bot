#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ananas
import json
import requests
import json
import time

KEY = "&key=0ad1aed5d18442c9a13f7caa139df5be"
APIURL_Now = "https://free-api.heweather.net/s6/weather/now?location=E2080"
APIURL_forecast = "https://free-api.heweather.net/s6/weather/forecast?location=E2080"


class ExampleBot(ananas.PineappleBot):

    # Get some current weather information data
    def now_weather(self):
        url = APIURL_Now + KEY
        now_res = requests.get(url)
        now_res_json = now_res.json()

        # Actual weather temperature
        real_tmp = now_res_json['HeWeather6'][0]['now']['tmp']
        # Somatosensory temperature
        feel_tmp = now_res_json['HeWeather6'][0]['now']['fl']

        # Get information back
        return real_tmp, feel_tmp


    def now_and_future_twodays_weather(self):
        # Weather forecast
        now_weathers = []
        # Tomorrow weather forecast
        tomorrow_weather = []
        # Acquired weather forecast
        the_day_after_tomorrow_weather = []

        url = APIURL_forecast + KEY
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
        return country, province, city_name, lat, lon, local_update_weather_time, status,         now_date, now_cond_txt_d, now_sr, now_uv_index, now_ss, now_mr, now_ms, now_cond_txt_n,         now_tmp_max, now_tmp_min, now_hum, now_wind_dir, now_wind_sc, now_wind_spd, now_pcpn, now_pop,        tomorrow_date, tomorrow_cond_txt_d, tomorrow_sr, tomorrow_uv_index, tomorrow_ss, tomorrow_mr, tomorrow_ms, tomorrow_cond_txt_n,        tomorrow_tmp_max, tomorrow_tmp_min, tomorrow_hum, tomorrow_wind_dir, tomorrow_wind_sc, tomorrow_wind_spd, tomorrow_pcpn, tomorrow_pop,        the_day_after_tomorrow_date, the_day_after_tomorrow_cond_txt_d, the_day_after_tomorrow_sr, the_day_after_tomorrow_uv_index, the_day_after_tomorrow_ss,        the_day_after_tomorrow_mr, the_day_after_tomorrow_ms, the_day_after_tomorrow_cond_txt_n, the_day_after_tomorrow_tmp_max, the_day_after_tomorrow_tmp_min,        the_day_after_tomorrow_hum, the_day_after_tomorrow_wind_dir, the_day_after_tomorrow_wind_sc, the_day_after_tomorrow_wind_spd, the_day_after_tomorrow_pcpn, the_day_after_tomorrow_pop

    def get_time(self):
        tim = time.localtime(time.time())
        tm_hour = tim[3]
        tm_min = tim[4]
        return tm_hour, tm_min

    def main(self, tm_hour, tm_min):
        # Get the return value of the now_weather() function
        real_tmp, feel_tmp = self.now_weather()

        # Get all return values of now_and_future_twodays_weather() function
        country, province, city_name, lat, lon, local_update_weather_time, status,         now_date, now_cond_txt_d, now_sr, now_uv_index, now_ss, now_mr, now_ms, now_cond_txt_n,         now_tmp_max, now_tmp_min, now_hum, now_wind_dir, now_wind_sc, now_wind_spd, now_pcpn, now_pop,        tomorrow_date, tomorrow_cond_txt_d, tomorrow_sr, tomorrow_uv_index, tomorrow_ss, tomorrow_mr, tomorrow_ms, tomorrow_cond_txt_n,        tomorrow_tmp_max, tomorrow_tmp_min, tomorrow_hum, tomorrow_wind_dir, tomorrow_wind_sc, tomorrow_wind_spd, tomorrow_pcpn, tomorrow_pop,        the_day_after_tomorrow_date, the_day_after_tomorrow_cond_txt_d, the_day_after_tomorrow_sr, the_day_after_tomorrow_uv_index, the_day_after_tomorrow_ss,        the_day_after_tomorrow_mr, the_day_after_tomorrow_ms, the_day_after_tomorrow_cond_txt_n, the_day_after_tomorrow_tmp_max, the_day_after_tomorrow_tmp_min,        the_day_after_tomorrow_hum, the_day_after_tomorrow_wind_dir, the_day_after_tomorrow_wind_sc, the_day_after_tomorrow_wind_spd, the_day_after_tomorrow_pcpn,        the_day_after_tomorrow_pop = self.now_and_future_twodays_weather()

        # Message construction
        msg = 'region：'+country+'--'+province+'--'+city_name+'\n'+'longitude：'+lon+'\n'+'latitude：'+lat+'\n'+'Current weather information update time：\n'+local_update_weather_time+'\nMessage sending time：'+str(tm_hour)+':'+str(tm_min)+'\nstatus：'+status+'\n=======================\n' +         'The following is the information for today：\n'+'date：'+now_date+'\nDaytime weather conditions：'+now_cond_txt_d+'\nsunrise：'+now_sr+'\nUV intensity：'+now_uv_index+'\nHighest temperature：'+now_tmp_max+'\nMinimum temperature：'+now_tmp_min+'\n' +         'True temperature：'+real_tmp+'\nSomatosensory temperature：'+feel_tmp+'\nRelative humidity：'+now_hum+'\nWind direction：'+now_wind_dir+'\nWind power：'+now_wind_sc+'\nWind speed：'+now_wind_spd+'\nIs it raining：'+now_pcpn+'\nRain probability (percentage)：'+now_pop+'\n' +         'sunset：'+now_ss+'\nMoon rise：'+now_mr+'\nNight weather conditions：'+now_cond_txt_n+'\nMoonlight：'+now_ms +         '\n=======================' +         '\nEvery day is beautiful, just enjoy it!'+'\n----From a Weather Bot！'

        return msg

    @ananas.hourly(minute=45)
    def toot(self):
        tm_hour, tm_min = self.get_time()
        msg = self.main(tm_hour, tm_min)
        self.mastodon.toot(msg)
        print('Tooted: %s' % msg)
# if __name__ == "__main__":
#     WeatherBot = ExampleBot(ananas.PineappleBot)
#     tm_hour, tm_min = WeatherBot.get_time()
#     msg = WeatherBot.main(tm_hour, tm_min)
#     WeatherBot.mastodon.toot(print(msg))

    
    