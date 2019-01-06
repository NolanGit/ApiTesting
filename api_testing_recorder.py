# -*- coding:utf-8 -*-
import os
import sys
import time
import peewee
import requests
import platform
import configparser


cf = configparser.ConfigParser()
cf.read('C:/Users/shr12/Documents/Github/ApiTesting/ApiTesting.config')
key = (cf.get('config', 'KEY'))


database = peewee.MySQLDatabase(
    'mydb', user='root', password='root', host='localhost', port=3306)


class API_DB(peewee.Model):
    name = peewee.CharField()
    birthday = peewee.CharField()
    is_relative = peewee.BooleanField()


class Meta:
    database = database


class DataBase(object):
    def __init__(self):
        pass

    def save(self, api, result):
        API_DB.create_table()
        p = API_DB(API = api, result = result)
        p.save()

class API_Testing(object):
    def test_api(self,url,payload,target_result):
        r = requests.get(url, params=payload)
        result=r.json()

payload = {'location': 'beijing', 'key': key}
url='https://free-api.heweather.com/s6/weather/forecast'
r = requests.get(url, params=payload)
print(r.text)
target_result="{'HeWeather6': [{'basic': {'cid': 'CN101010100', 'location': '北京', 'parent_city': '北京', 'admin_area': '北京', 'cnty': '中国', 'lat': '39.90498734', 'lon': '116.4052887', 'tz': '+8.00'}, 'update': {'loc': '2019-01-06 19:56', 'utc': '2019-01-06 11:56'}, 'status': 'ok', 'daily_forecast': [{'cond_code_d': '101', 'cond_code_n': '100', 'cond_txt_d': '多云', 'cond_txt_n': '晴', 'date': '2019-01-06', 'hum': '18', 'mr': '07:33', 'ms': '17:17', 'pcpn': '0.0', 'pop': '0', 'pres': '1033', 'sr': '07:36', 'ss': '17:05', 'tmp_max': '0', 'tmp_min': '-7', 'uv_index': '4', 'vis': '10', 'wind_deg': '356', 'wind_dir': '北风', 'wind_sc': '3-4', 'wind_spd': '24'}, {'cond_code_d': '101', 'cond_code_n': '101', 'cond_txt_d': '多云', 'cond_txt_n': '多云', 'date': '2019-01-07', 'hum': '31', 'mr': '08:19', 'ms': '18:10', 'pcpn': '0.0', 'pop': '0', 'pres': '1034', 'sr': '07:35', 'ss': '17:06', 'tmp_max': '2', 'tmp_min': '-7', 'uv_index': '2', 'vis': '20', 'wind_deg': '0', 'wind_dir': '北风', 'wind_sc': '3-4', 'wind_spd': '22'}, {'cond_code_d': '100', 'cond_code_n': '101', 'cond_txt_d': '晴', 'cond_txt_n': '多云', 'date': '2019-01-08', 'hum': '24', 'mr': '09:00', 'ms': '19:06', 'pcpn': '0.0', 'pop': '0', 'pres': '1042', 'sr': '07:35', 'ss': '17:07', 'tmp_max': '1', 'tmp_min': '-8', 'uv_index': '3', 'vis': '20', 'wind_deg': '243', 'wind_dir': '西南风', 'wind_sc': '1-2', 'wind_spd': '8'}]}]}"
