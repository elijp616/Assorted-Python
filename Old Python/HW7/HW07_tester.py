# std library
from unittest.mock import patch
import unittest
from pathlib import Path
import importlib
import json
import time
import re
import urllib.parse
import urllib.request
import urllib.error
import ssl


# 3rd party
import requests

"""
HW07 Student Tester - Fall 2018
"""

__author__ = "Jack Wolfard"
__version__ = 1.0

# checks if the passed in url matches any of the urls in cached_responses
# first preprocesses the url to sort out the query strings to make for easier
# regex matching


def find(url):
    parsed_url = urllib.parse.urlparse(url)
    url = urllib.parse.urlunparse(parsed_url[:3] + ("", "", ""))
    if parsed_url.query:
        url += "?{}".format("&".join(sorted(parsed_url.query.split("&"))))
    for response in cached_responses:
        if response.match(url):
            return response


# a limited representation of a mocked requests.get response

class CachedResponse():
    def __init__(self, url_regex, json_text, status_code):
        self.url_regex = url_regex
        self.json_data = json.loads(json_text)
        self.status_code = status_code
        self.text = json_text

    def json(self):
        return self.json_data

    def match(self, string):
        return self.url_regex.fullmatch(string)

# if you're reading this, you're probably curious as to how this works, so I'll
# do my best to explain.

# below is a cached_responses list which contains an object which will be used
# in the place of a typical returned reponse from requests.get

# I used data from the different apis at the time of writing this tester in
# order to get real  json data, but the cached_responses will never change as
# long as the person requesting data has their url match one of the urls in the
# list through regex matching.


cached_responses = [
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/name\/[tT][aA][iI][wW][aA][nN](\?fullText=true)?\/?"), '[{"name":"Taiwan","topLevelDomain":[".tw"],"alpha2Code":"TW","alpha3Code":"TWN","callingCodes":["886"],"capital":"Taipei","altSpellings":["TW","Táiwān","Republic of China","中華民國","Zhōnghuá Mínguó"],"region":"Asia","subregion":"Eastern Asia","population":23503349,"latlng":[23.5,121.0],"demonym":"Taiwanese","area":36193.0,"gini":null,"timezones":["UTC + 08: 00"],"borders":[],"nativeName":"臺灣","numericCode":"158","currencies":[{"code":"TWD","name":"New Taiwan dollar","symbol":"$"}],"languages":[{"iso639_1":"zh","iso639_2":"zho","name":"Chinese","nativeName":"中文 (Zhōngwén)"}],"translations":{"de":"Taiwan","es":"Taiwán","fr":"Taïwan","ja":"台湾（中華民国）","it":"Taiwan","br":"Taiwan","pt":"Taiwan","nl":"Taiwan","hr":"Tajvan","fa":"تایوان"},"flag":"https: // restcountries.eu / data / twn.svg","regionalBlocs":[],"cioc":"TPE"}]',
                   200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/name\/[lL][aA][oO][sS](\?fullText=true)?\/?"), '''[{"name":"Lao People's Democratic Republic","topLevelDomain":[".la"],"alpha2Code":"LA","alpha3Code":"LAO","callingCodes":["856"],"capital":"Vientiane","altSpellings":["LA","Lao","Laos","Lao People's Democratic Republic","Sathalanalat Paxathipatai Paxaxon Lao"],"region":"Asia","subregion":"South-Eastern Asia","population":6492400,"latlng":[18.0,105.0],"demonym":"Laotian","area":236800.0,"gini":36.7,"timezones":["UTC+07:00"],"borders":["MMR","KHM","CHN","THA","VNM"],"nativeName":"ສປປລາວ","numericCode":"418","currencies":[{"code":"LAK","name":"Lao kip","symbol":"₭"}],"languages":[{"iso639_1":"lo","iso639_2":"lao","name":"Lao","nativeName":"ພາສາລາວ"}],"translations":{"de":"Laos","es":"Laos","fr":"Laos","ja":"ラオス人民民主共和国","it":"Laos","br":"Laos","pt":"Laos","nl":"Laos","hr":"Laos","fa":"لائوس"},"flag":"https://restcountries.eu/data/lao.svg","regionalBlocs":[{"acronym":"ASEAN","name":"Association of Southeast Asian Nations","otherAcronyms":[],"otherNames":[]}],"cioc":"LAO"}]''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/name\/[tT][aA][lL]'[dD][oO][rR][eE][iI](\?fullText=true)?\/?"), '''{"status":404,"message":"Not Found"}''', 404),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[jJ][pP][nN]\/?"), '''{"name":"Japan","topLevelDomain":[".jp"],"alpha2Code":"JP","alpha3Code":"JPN","callingCodes":["81"],"capital":"Tokyo","altSpellings":["JP","Nippon","Nihon"],"region":"Asia","subregion":"Eastern Asia","population":126960000,"latlng":[36.0,138.0],"demonym":"Japanese","area":377930.0,"gini":38.1,"timezones":["UTC+09:00"],"borders":[],"nativeName":"日本","numericCode":"392","currencies":[{"code":"JPY","name":"Japanese yen","symbol":"¥"}],"languages":[{"iso639_1":"ja","iso639_2":"jpn","name":"Japanese","nativeName":"日本語 (にほんご)"}],"translations":{"de":"Japan","es":"Japón","fr":"Japon","ja":"日本","it":"Giappone","br":"Japão","pt":"Japão","nl":"Japan","hr":"Japan","fa":"ژاپن"},"flag":"https://restcountries.eu/data/jpn.svg","regionalBlocs":[],"cioc":"JPN"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[iI][tT][aA]\/?"), '''{"name":"Italy","topLevelDomain":[".it"],"alpha2Code":"IT","alpha3Code":"ITA","callingCodes":["39"],"capital":"Rome","altSpellings":["IT","Italian Republic","Repubblica italiana"],"region":"Europe","subregion":"Southern Europe","population":60665551,"latlng":[42.83333333,12.83333333],"demonym":"Italian","area":301336.0,"gini":36.0,"timezones":["UTC+01:00"],"borders":["AUT","FRA","SMR","SVN","CHE","VAT"],"nativeName":"Italia","numericCode":"380","currencies":[{"code":"EUR","name":"Euro","symbol":"€"}],"languages":[{"iso639_1":"it","iso639_2":"ita","name":"Italian","nativeName":"Italiano"}],"translations":{"de":"Italien","es":"Italia","fr":"Italie","ja":"イタリア","it":"Italia","br":"Itália","pt":"Itália","nl":"Italië","hr":"Italija","fa":"ایتالیا"},"flag":"https://restcountries.eu/data/ita.svg","regionalBlocs":[{"acronym":"EU","name":"European Union","otherAcronyms":[],"otherNames":[]}],"cioc":"ITA"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[aA][aA][aA]\/?"), '''{"status":404,"message":"Not Found"}''', 404),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[uU][sS][aA]\/?"), '''{"name":"United States of America","topLevelDomain":[".us"],"alpha2Code":"US","alpha3Code":"USA","callingCodes":["1"],"capital":"Washington, D.C.","altSpellings":["US","USA","United States of America"],"region":"Americas","subregion":"Northern America","population":323947000,"latlng":[38.0,-97.0],"demonym":"American","area":9629091.0,"gini":48.0,"timezones":["UTC-12:00","UTC-11:00","UTC-10:00","UTC-09:00","UTC-08:00","UTC-07:00","UTC-06:00","UTC-05:00","UTC-04:00","UTC+10:00","UTC+12:00"],"borders":["CAN","MEX"],"nativeName":"United States","numericCode":"840","currencies":[{"code":"USD","name":"United States dollar","symbol":"$"}],"languages":[{"iso639_1":"en","iso639_2":"eng","name":"English","nativeName":"English"}],"translations":{"de":"Vereinigte Staaten von Amerika","es":"Estados Unidos","fr":"États-Unis","ja":"アメリカ合衆国","it":"Stati Uniti D'America","br":"Estados Unidos","pt":"Estados Unidos","nl":"Verenigde Staten","hr":"Sjedinjene Američke Države","fa":"ایالات متحده آمریکا"},"flag":"https://restcountries.eu/data/usa.svg","regionalBlocs":[{"acronym":"NAFTA","name":"North American Free Trade Agreement","otherAcronyms":[],"otherNames":["Tratado de Libre Comercio de América del Norte","Accord de Libre-échange Nord-Américain"]}],"cioc":"USA"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[cC][aA][nN]\/?"), '''{"name":"Canada","topLevelDomain":[".ca"],"alpha2Code":"CA","alpha3Code":"CAN","callingCodes":["1"],"capital":"Ottawa","altSpellings":["CA"],"region":"Americas","subregion":"Northern America","population":36155487,"latlng":[60.0,-95.0],"demonym":"Canadian","area":9984670.0,"gini":32.6,"timezones":["UTC-08:00","UTC-07:00","UTC-06:00","UTC-05:00","UTC-04:00","UTC-03:30"],"borders":["USA"],"nativeName":"Canada","numericCode":"124","currencies":[{"code":"CAD","name":"Canadian dollar","symbol":"$"}],"languages":[{"iso639_1":"en","iso639_2":"eng","name":"English","nativeName":"English"},{"iso639_1":"fr","iso639_2":"fra","name":"French","nativeName":"français"}],"translations":{"de":"Kanada","es":"Canadá","fr":"Canada","ja":"カナダ","it":"Canada","br":"Canadá","pt":"Canadá","nl":"Canada","hr":"Kanada","fa":"کانادا"},"flag":"https://restcountries.eu/data/can.svg","regionalBlocs":[{"acronym":"NAFTA","name":"North American Free Trade Agreement","otherAcronyms":[],"otherNames":["Tratado de Libre Comercio de América del Norte","Accord de Libre-échange Nord-Américain"]}],"cioc":"CAN"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[mM][eE][xX]\/?"), '''{"name":"Mexico","topLevelDomain":[".mx"],"alpha2Code":"MX","alpha3Code":"MEX","callingCodes":["52"],"capital":"Mexico City","altSpellings":["MX","Mexicanos","United Mexican States","Estados Unidos Mexicanos"],"region":"Americas","subregion":"Central America","population":122273473,"latlng":[23.0,-102.0],"demonym":"Mexican","area":1964375.0,"gini":47.0,"timezones":["UTC-08:00","UTC-07:00","UTC-06:00"],"borders":["BLZ","GTM","USA"],"nativeName":"México","numericCode":"484","currencies":[{"code":"MXN","name":"Mexican peso","symbol":"$"}],"languages":[{"iso639_1":"es","iso639_2":"spa","name":"Spanish","nativeName":"Español"}],"translations":{"de":"Mexiko","es":"México","fr":"Mexique","ja":"メキシコ","it":"Messico","br":"México","pt":"México","nl":"Mexico","hr":"Meksiko","fa":"مکزیک"},"flag":"https://restcountries.eu/data/mex.svg","regionalBlocs":[{"acronym":"PA","name":"Pacific Alliance","otherAcronyms":[],"otherNames":["Alianza del Pacífico"]},{"acronym":"NAFTA","name":"North American Free Trade Agreement","otherAcronyms":[],"otherNames":["Tratado de Libre Comercio de América del Norte","Accord de Libre-échange Nord-Américain"]}],"cioc":"MEX"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[mM][nN][gG]\/?"), '''{"name":"Mongolia","topLevelDomain":[".mn"],"alpha2Code":"MN","alpha3Code":"MNG","callingCodes":["976"],"capital":"Ulan Bator","altSpellings":["MN"],"region":"Asia","subregion":"Eastern Asia","population":3093100,"latlng":[46.0,105.0],"demonym":"Mongolian","area":1564110.0,"gini":36.5,"timezones":["UTC+07:00","UTC+08:00"],"borders":["CHN","RUS"],"nativeName":"Монгол улс","numericCode":"496","currencies":[{"code":"MNT","name":"Mongolian tögrög","symbol":"₮"}],"languages":[{"iso639_1":"mn","iso639_2":"mon","name":"Mongolian","nativeName":"Монгол хэл"}],"translations":{"de":"Mongolei","es":"Mongolia","fr":"Mongolie","ja":"モンゴル","it":"Mongolia","br":"Mongólia","pt":"Mongólia","nl":"Mongolië","hr":"Mongolija","fa":"مغولستان"},"flag":"https://restcountries.eu/data/mng.svg","regionalBlocs":[],"cioc":"MGL"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[cC][hH][nN]\/?"), '''{"name":"China","topLevelDomain":[".cn"],"alpha2Code":"CN","alpha3Code":"CHN","callingCodes":["86"],"capital":"Beijing","altSpellings":["CN","Zhōngguó","Zhongguo","Zhonghua","People's Republic of China","中华人民共和国","Zhōnghuá Rénmín Gònghéguó"],"region":"Asia","subregion":"Eastern Asia","population":1377422166,"latlng":[35.0,105.0],"demonym":"Chinese","area":9640011.0,"gini":47.0,"timezones":["UTC+08:00"],"borders":["AFG","BTN","MMR","HKG","IND","KAZ","PRK","KGZ","LAO","MAC","MNG","PAK","RUS","TJK","VNM"],"nativeName":"中国","numericCode":"156","currencies":[{"code":"CNY","name":"Chinese yuan","symbol":"¥"}],"languages":[{"iso639_1":"zh","iso639_2":"zho","name":"Chinese","nativeName":"中文 (Zhōngwén)"}],"translations":{"de":"China","es":"China","fr":"Chine","ja":"中国","it":"Cina","br":"China","pt":"China","nl":"China","hr":"Kina","fa":"چین"},"flag":"https://restcountries.eu/data/chn.svg","regionalBlocs":[],"cioc":"CHN"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[rR][uU][sS]\/?"), '''{"name":"Russian Federation","topLevelDomain":[".ru"],"alpha2Code":"RU","alpha3Code":"RUS","callingCodes":["7"],"capital":"Moscow","altSpellings":["RU","Rossiya","Russian Federation","Российская Федерация","Rossiyskaya Federatsiya"],"region":"Europe","subregion":"Eastern Europe","population":146599183,"latlng":[60.0,100.0],"demonym":"Russian","area":1.7124442E7,"gini":40.1,"timezones":["UTC+03:00","UTC+04:00","UTC+06:00","UTC+07:00","UTC+08:00","UTC+09:00","UTC+10:00","UTC+11:00","UTC+12:00"],"borders":["AZE","BLR","CHN","EST","FIN","GEO","KAZ","PRK","LVA","LTU","MNG","NOR","POL","UKR"],"nativeName":"Россия","numericCode":"643","currencies":[{"code":"RUB","name":"Russian ruble","symbol":"₽"}],"languages":[{"iso639_1":"ru","iso639_2":"rus","name":"Russian","nativeName":"Русский"}],"translations":{"de":"Russland","es":"Rusia","fr":"Russie","ja":"ロシア連邦","it":"Russia","br":"Rússia","pt":"Rússia","nl":"Rusland","hr":"Rusija","fa":"روسیه"},"flag":"https://restcountries.eu/data/rus.svg","regionalBlocs":[{"acronym":"EEU","name":"Eurasian Economic Union","otherAcronyms":["EAEU"],"otherNames":[]}],"cioc":"RUS"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[cC][oO][lL]\/?"), '''{"name":"Colombia","topLevelDomain":[".co"],"alpha2Code":"CO","alpha3Code":"COL","callingCodes":["57"],"capital":"Bogotá","altSpellings":["CO","Republic of Colombia","República de Colombia"],"region":"Americas","subregion":"South America","population":48759958,"latlng":[4.0,-72.0],"demonym":"Colombian","area":1141748.0,"gini":55.9,"timezones":["UTC-05:00"],"borders":["BRA","ECU","PAN","PER","VEN"],"nativeName":"Colombia","numericCode":"170","currencies":[{"code":"COP","name":"Colombian peso","symbol":"$"}],"languages":[{"iso639_1":"es","iso639_2":"spa","name":"Spanish","nativeName":"Español"}],"translations":{"de":"Kolumbien","es":"Colombia","fr":"Colombie","ja":"コロンビア","it":"Colombia","br":"Colômbia","pt":"Colômbia","nl":"Colombia","hr":"Kolumbija","fa":"کلمبیا"},"flag":"https://restcountries.eu/data/col.svg","regionalBlocs":[{"acronym":"PA","name":"Pacific Alliance","otherAcronyms":[],"otherNames":["Alianza del Pacífico"]},{"acronym":"USAN","name":"Union of South American Nations","otherAcronyms":["UNASUR","UNASUL","UZAN"],"otherNames":["Unión de Naciones Suramericanas","União de Nações Sul-Americanas","Unie van Zuid-Amerikaanse Naties","South American Union"]}],"cioc":"COL"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[bB][rR][aA]\/?"), '''{"name":"Brazil","topLevelDomain":[".br"],"alpha2Code":"BR","alpha3Code":"BRA","callingCodes":["55"],"capital":"Brasília","altSpellings":["BR","Brasil","Federative Republic of Brazil","República Federativa do Brasil"],"region":"Americas","subregion":"South America","population":206135893,"latlng":[-10.0,-55.0],"demonym":"Brazilian","area":8515767.0,"gini":54.7,"timezones":["UTC-05:00","UTC-04:00","UTC-03:00","UTC-02:00"],"borders":["ARG","BOL","COL","GUF","GUY","PRY","PER","SUR","URY","VEN"],"nativeName":"Brasil","numericCode":"076","currencies":[{"code":"BRL","name":"Brazilian real","symbol":"R$"}],"languages":[{"iso639_1":"pt","iso639_2":"por","name":"Portuguese","nativeName":"Português"}],"translations":{"de":"Brasilien","es":"Brasil","fr":"Brésil","ja":"ブラジル","it":"Brasile","br":"Brasil","pt":"Brasil","nl":"Brazilië","hr":"Brazil","fa":"برزیل"},"flag":"https://restcountries.eu/data/bra.svg","regionalBlocs":[{"acronym":"USAN","name":"Union of South American Nations","otherAcronyms":["UNASUR","UNASUL","UZAN"],"otherNames":["Unión de Naciones Suramericanas","União de Nações Sul-Americanas","Unie van Zuid-Amerikaanse Naties","South American Union"]}],"cioc":"BRA"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[eE][cC][uU]\/?"), '''{"name":"Ecuador","topLevelDomain":[".ec"],"alpha2Code":"EC","alpha3Code":"ECU","callingCodes":["593"],"capital":"Quito","altSpellings":["EC","Republic of Ecuador","República del Ecuador"],"region":"Americas","subregion":"South America","population":16545799,"latlng":[-2.0,-77.5],"demonym":"Ecuadorean","area":276841.0,"gini":49.3,"timezones":["UTC-06:00","UTC-05:00"],"borders":["COL","PER"],"nativeName":"Ecuador","numericCode":"218","currencies":[{"code":"USD","name":"United States dollar","symbol":"$"}],"languages":[{"iso639_1":"es","iso639_2":"spa","name":"Spanish","nativeName":"Español"}],"translations":{"de":"Ecuador","es":"Ecuador","fr":"Équateur","ja":"エクアドル","it":"Ecuador","br":"Equador","pt":"Equador","nl":"Ecuador","hr":"Ekvador","fa":"اکوادور"},"flag":"https://restcountries.eu/data/ecu.svg","regionalBlocs":[{"acronym":"USAN","name":"Union of South American Nations","otherAcronyms":["UNASUR","UNASUL","UZAN"],"otherNames":["Unión de Naciones Suramericanas","União de Nações Sul-Americanas","Unie van Zuid-Amerikaanse Naties","South American Union"]}],"cioc":"ECU"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[pP][aA][nN]\/?"), '''{"name":"Panama","topLevelDomain":[".pa"],"alpha2Code":"PA","alpha3Code":"PAN","callingCodes":["507"],"capital":"Panama City","altSpellings":["PA","Republic of Panama","República de Panamá"],"region":"Americas","subregion":"Central America","population":3814672,"latlng":[9.0,-80.0],"demonym":"Panamanian","area":75417.0,"gini":51.9,"timezones":["UTC-05:00"],"borders":["COL","CRI"],"nativeName":"Panamá","numericCode":"591","currencies":[{"code":"PAB","name":"Panamanian balboa","symbol":"B/."},{"code":"USD","name":"United States dollar","symbol":"$"}],"languages":[{"iso639_1":"es","iso639_2":"spa","name":"Spanish","nativeName":"Español"}],"translations":{"de":"Panama","es":"Panamá","fr":"Panama","ja":"パナマ","it":"Panama","br":"Panamá","pt":"Panamá","nl":"Panama","hr":"Panama","fa":"پاناما"},"flag":"https://restcountries.eu/data/pan.svg","regionalBlocs":[{"acronym":"CAIS","name":"Central American Integration System","otherAcronyms":["SICA"],"otherNames":["Sistema de la Integración Centroamericana,"]}],"cioc":"PAN"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[pP][eE][rR]\/?"), '''{"name":"Peru","topLevelDomain":[".pe"],"alpha2Code":"PE","alpha3Code":"PER","callingCodes":["51"],"capital":"Lima","altSpellings":["PE","Republic of Peru"," República del Perú"],"region":"Americas","subregion":"South America","population":31488700,"latlng":[-10.0,-76.0],"demonym":"Peruvian","area":1285216.0,"gini":48.1,"timezones":["UTC-05:00"],"borders":["BOL","BRA","CHL","COL","ECU"],"nativeName":"Perú","numericCode":"604","currencies":[{"code":"PEN","name":"Peruvian sol","symbol":"S/."}],"languages":[{"iso639_1":"es","iso639_2":"spa","name":"Spanish","nativeName":"Español"}],"translations":{"de":"Peru","es":"Perú","fr":"Pérou","ja":"ペルー","it":"Perù","br":"Peru","pt":"Peru","nl":"Peru","hr":"Peru","fa":"پرو"},"flag":"https://restcountries.eu/data/per.svg","regionalBlocs":[{"acronym":"PA","name":"Pacific Alliance","otherAcronyms":[],"otherNames":["Alianza del Pacífico"]},{"acronym":"USAN","name":"Union of South American Nations","otherAcronyms":["UNASUR","UNASUL","UZAN"],"otherNames":["Unión de Naciones Suramericanas","União de Nações Sul-Americanas","Unie van Zuid-Amerikaanse Naties","South American Union"]}],"cioc":"PER"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[vV][eE][nN]\/?"), '''{"name":"Venezuela (Bolivarian Republic of)","topLevelDomain":[".ve"],"alpha2Code":"VE","alpha3Code":"VEN","callingCodes":["58"],"capital":"Caracas","altSpellings":["VE","Bolivarian Republic of Venezuela","República Bolivariana de Venezuela"],"region":"Americas","subregion":"South America","population":31028700,"latlng":[8.0,-66.0],"demonym":"Venezuelan","area":916445.0,"gini":44.8,"timezones":["UTC-04:00"],"borders":["BRA","COL","GUY"],"nativeName":"Venezuela","numericCode":"862","currencies":[{"code":"VEF","name":"Venezuelan bolívar","symbol":"Bs F"}],"languages":[{"iso639_1":"es","iso639_2":"spa","name":"Spanish","nativeName":"Español"}],"translations":{"de":"Venezuela","es":"Venezuela","fr":"Venezuela","ja":"ベネズエラ・ボリバル共和国","it":"Venezuela","br":"Venezuela","pt":"Venezuela","nl":"Venezuela","hr":"Venezuela","fa":"ونزوئلا"},"flag":"https://restcountries.eu/data/ven.svg","regionalBlocs":[{"acronym":"USAN","name":"Union of South American Nations","otherAcronyms":["UNASUR","UNASUL","UZAN"],"otherNames":["Unión de Naciones Suramericanas","União de Nações Sul-Americanas","Unie van Zuid-Amerikaanse Naties","South American Union"]}],"cioc":"VEN"}''', 200),
    CachedResponse(re.compile("https?:\/\/(www\.)?restcountries\.eu\/rest\/v2\/alpha\/[mM][aA][rR]\/?"), '''{"name":"Morocco","topLevelDomain":[".ma"],"alpha2Code":"MA","alpha3Code":"MAR","callingCodes":["212"],"capital":"Rabat","altSpellings":["MA","Kingdom of Morocco","Al-Mamlakah al-Maġribiyah"],"region":"Africa","subregion":"Northern Africa","population":33337529,"latlng":[32.0,-5.0],"demonym":"Moroccan","area":446550.0,"gini":40.9,"timezones":["UTC"],"borders":["DZA","ESH","ESP"],"nativeName":"المغرب","numericCode":"504","currencies":[{"code":"MAD","name":"Moroccan dirham","symbol":"د.م."}],"languages":[{"iso639_1":"ar","iso639_2":"ara","name":"Arabic","nativeName":"العربية"}],"translations":{"de":"Marokko","es":"Marruecos","fr":"Maroc","ja":"モロッコ","it":"Marocco","br":"Marrocos","pt":"Marrocos","nl":"Marokko","hr":"Maroko","fa":"مراکش"},"flag":"https://restcountries.eu/data/mar.svg","regionalBlocs":[{"acronym":"AU","name":"African Union","otherAcronyms":[],"otherNames":["الاتحاد الأفريقي","Union africaine","União Africana","Unión Africana","Umoja wa Afrika"]},{"acronym":"AL","name":"Arab League","otherAcronyms":[],"otherNames":["جامعة الدول العربية","Jāmiʻat ad-Duwal al-ʻArabīyah","League of Arab States"]}],"cioc":"MAR"}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&id=4180386"),
                   '''{"coord":{"lon":-83.38,"lat":33.96},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":281.35,"pressure":1021,"humidity":87,"temp_min":280.15,"temp_max":283.15},"visibility":16093,"wind":{"speed":1.76,"deg":28.0002},"clouds":{"all":1},"dt":1540367760,"sys":{"type":1,"id":746,"message":0.0045,"country":"US","sunrise":1540381576,"sunset":1540421310},"id":4180386,"name":"Athens","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&id=4179574"),
                   '''{"coord":{"lon":-84.29,"lat":34.08},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":281.35,"pressure":1021,"humidity":93,"temp_min":280.15,"temp_max":284.15},"visibility":16093,"wind":{"speed":1.56,"deg":11.5002},"clouds":{"all":1},"dt":1540368900,"sys":{"type":1,"id":790,"message":0.0043,"country":"US","sunrise":1540381803,"sunset":1540421519},"id":4179574,"name":"Alpharetta","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&id=4179074"),
                   '''{"coord":{"lon":-84.68,"lat":34.07},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":280.7,"pressure":1021,"humidity":81,"temp_min":277.15,"temp_max":284.15},"visibility":16093,"wind":{"speed":3.1,"deg":340},"clouds":{"all":1},"dt":1540368900,"sys":{"type":1,"id":749,"message":0.0304,"country":"US","sunrise":1540381896,"sunset":1540421613},"id":4179074,"name":"Acworth","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&id=22727337282"), '''{"cod":"404","message":"city not found"}''', 404),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&id=5809844"),
                   '''{"coord":{"lon":-122.33,"lat":47.61},"weather":[{"id":701,"main":"Mist","description":"mist","icon":"50n"}],"base":"stations","main":{"temp":283.91,"pressure":1018,"humidity":81,"temp_min":281.15,"temp_max":285.15},"visibility":16093,"wind":{"speed":3.6,"deg":140},"clouds":{"all":75},"dt":1540367880,"sys":{"type":1,"id":2949,"message":0.0042,"country":"US","sunrise":1540392124,"sunset":1540429442},"id":5809844,"name":"Seattle","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&id=5641727"),
                   '''{"coord":{"lon":-111.04,"lat":45.68},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":280.96,"pressure":1016,"humidity":86,"temp_min":276.15,"temp_max":285.15},"visibility":16093,"wind":{"speed":0.91,"deg":168.5},"clouds":{"all":1},"dt":1540368900,"sys":{"type":1,"id":1719,"message":0.0122,"country":"US","sunrise":1540389209,"sunset":1540426940},"id":5641727,"name":"Bozeman","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&id=4391354"),
                   '''{"coord":{"lon":-91.96,"lat":37.33},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":279.18,"pressure":1026,"humidity":75,"temp_min":278.15,"temp_max":280.15},"visibility":16093,"wind":{"speed":1.5,"deg":100},"clouds":{"all":1},"dt":1540367760,"sys":{"type":1,"id":1641,"message":0.004,"country":"US","sunrise":1540383888,"sunset":1540423113},"id":4391354,"name":"Houston","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&lat=\-10\.0&lon=\-55\.0"),
                   '''{"coord":{"lon":-55,"lat":-10},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02n"}],"base":"stations","main":{"temp":293.767,"pressure":995.88,"humidity":98,"temp_min":293.767,"temp_max":293.767,"sea_level":1023.52,"grnd_level":995.88},"wind":{"speed":0.91,"deg":42.5002},"clouds":{"all":8},"dt":1540370674,"sys":{"message":0.0035,"country":"BR","sunrise":1540372328,"sunset":1540416971},"id":3469034,"name":"Federative Republic of Brazil","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&lat=\-2\.0&lon=\-77\.5"),
                   '''{"coord":{"lon":-77.5,"lat":-2},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"base":"stations","main":{"temp":295.467,"pressure":975.37,"humidity":98,"temp_min":295.467,"temp_max":295.467,"sea_level":1021.82,"grnd_level":975.37},"wind":{"speed":0.96,"deg":324},"clouds":{"all":32},"dt":1540370709,"sys":{"message":0.0031,"country":"EC","sunrise":1540378141,"sunset":1540421951},"id":3658394,"name":"Republic of Ecuador","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&lat=9\.0&lon=\-80\.0"),
                   '''{"coord":{"lon":-80,"lat":9},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"base":"stations","main":{"temp":298.15,"pressure":1011,"humidity":94,"temp_min":298.15,"temp_max":298.15},"visibility":10000,"wind":{"speed":2.1,"deg":270},"clouds":{"all":40},"dt":1540368000,"sys":{"type":1,"id":4230,"message":0.0089,"country":"PA","sunrise":1540379301,"sunset":1540421983},"id":3703430,"name":"Republic of Panama","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&lat=60\.0&lon=\-95\.0"),
                   '''{"coord":{"lon":-95,"lat":60},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"base":"stations","main":{"temp":271.242,"pressure":1035.6,"humidity":94,"temp_min":271.242,"temp_max":271.242,"sea_level":1037.55,"grnd_level":1035.6},"wind":{"speed":5.56,"deg":116.5},"clouds":{"all":92},"dt":1540371505,"sys":{"message":0.0041,"country":"CA","sunrise":1540387384,"sunset":1540421044},"id":5887448,"name":"Arviat","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&lat=23\.0&lon=\-102\.0"),
                   '''{"coord":{"lon":-102,"lat":23},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"base":"stations","main":{"temp":285.942,"pressure":802.55,"humidity":99,"temp_min":285.942,"temp_max":285.942,"sea_level":1028.35,"grnd_level":802.55},"wind":{"speed":3.86,"deg":170.5},"rain":{"3h":0.2075},"clouds":{"all":68},"dt":1540371533,"sys":{"message":0.0036,"country":"MX","sunrise":1540385343,"sunset":1540426489},"id":3996063,"name":"Mexico","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&id=5160041"),
                   '''{"coord":{"lon":-82.12,"lat":41.24},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"base":"stations","main":{"temp":277.86,"pressure":1026,"humidity":56,"temp_min":273.15,"temp_max":281.15},"visibility":16093,"wind":{"speed":3.6,"deg":360},"clouds":{"all":40},"dt":1540371360,"sys":{"type":1,"id":2182,"message":0.0045,"country":"US","sunrise":1540381847,"sunset":1540420426},"id":5160041,"name":"Lagrange","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&id=733840"),
                   '''{"coord":{"lon":24.88,"lat":41.14},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":289.15,"pressure":1006,"humidity":72,"temp_min":289.15,"temp_max":289.15},"visibility":10000,"wind":{"speed":3.6,"deg":230},"clouds":{"all":0},"dt":1540369200,"sys":{"type":1,"id":5684,"message":0.0038,"country":"GR","sunrise":1540356138,"sunset":1540394780},"id":733840,"name":"Xanthi","cod":200}''', 200),
    CachedResponse(re.compile("https?:\/\/api\.openweathermap\.org\/data\/2\.5\/weather\?[aA][pP][pP][iI][dD]=[a-zA-Z0-9]+&id=29329748293"), '''{"cod":"404","message":"city not found"}''', 404),
]

# effectively this a mocked out version of the request.get function
# returns a response either from request.get or CachedResponse depending on
# if the url passed in had a match in cached_responses


class RequestGetMocker():
    def __init__(self, url, params=None):
        if params:
            self.url = "{}?{}".format(url, '&'.join(['{}={}'.format(key, params[key]) for key in params]))
        else:
            self.url = url
        response = find(self.url)
        if response is None:
            response = requests.request("GET", url)
        self._response = response
        self.text = self._response.text
        self.status_code = self._response.status_code

    def json(self):
        return self._response.json()

# inside this class are all the tests which will be run against the student's
# hw assignment


class TestMyClass(unittest.TestCase):

    error_messages = {}
    maxDiff = None

    @classmethod
    def set_hw(cls, hw):
        cls.hw = hw

    def test_author(self):
        self.error_messages["author"] = "Missing or empty __author__ global variable."
        self.assertTrue(self.hw.__author__, msg=self.error_messages["author"])
        del self.error_messages["author"]

    def test_collab(self):
        self.error_messages["collab"] = "Missing or empty __collab__ global variable."
        self.assertTrue(self.hw.__collab__, msg=self.error_messages["collab"])
        del self.error_messages["collab"]

    # patch is used here as a function decorator in order to replace all
    # instances of requests.get inside this function with our mocked
    # representation RequestGetMocker
    # now when the hw calls requests.get, RequestGetMocker will be used instead

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_currencyConverter_1(self, patch):
        params = "taiwan", 88.88, 31
        ans = "In taiwan, $88.88 USD is worth $2755.28 TWD."
        func = "currencyConverter"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.currencyConverter(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_currencyConverter_2(self, patch):
        params = "LaOs", 730, 8541.65
        ans = "In LaOs, $730 USD is worth ₭6235404.5 LAK."
        func = "currencyConverter"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.currencyConverter(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_currencyConverter_3(self, patch):
        params = "Tal'Dorei", 42, 9001
        ans = "Tal'Dorei is not a valid country."
        func = "currencyConverter"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.currencyConverter(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    def test_translator_1(self):
        params = [],
        ans = {}
        func = "translator"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.translator(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_translator_2(self, patch):
        params = ["JPN", "ita", "aaa"],
        ans = {'Japan': '日本', 'Italy': 'Italia'}
        func = "translator"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.translator(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_nearby_locations_1(self, patch):
        params = ["mng", "usa"],
        ans = [(60.0, -95.0), (23.0, -102.0)]
        func = "nearbyLocations"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.nearbyLocations(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_nearby_locations_2(self, patch):
        params = ["col", "MAR", "jpn"],
        ans = [(-10.0, -55.0), (-2.0, -77.5), (9.0, -80.0),
               (-10.0, -76.0), (8.0, -66.0)]
        func = "nearbyLocations"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.nearbyLocations(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_humidity_check_1(self, patch):
        params = [4180386, 4179574, 4179074], 85,
        ans = ['Acworth']
        func = "humidityCheck"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.humidityCheck(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_humidity_check_2(self, patch):
        params = [22727337282, 5809844, 5641727, 4391354], 90,
        ans = "22727337282 is not a valid ID"
        func = "humidityCheck"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.humidityCheck(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_location_temps_1(self, patch):
        params = [(-10.0, -55.0), (-2.0, -77.5), (9.0, -80.0)],
        ans = [('Federative Republic of Brazil', 293.767),
               ('Republic of Ecuador', 295.467),
               ('Republic of Panama', 298.15)]
        func = "locationTemps"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.locationTemps(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_location_temps_2(self, patch):
        params = [(60.0, -95.0), (23.0, -102.0)],
        ans = [('Arviat', 271.242), ('Mexico', 285.942)]
        func = "locationTemps"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.locationTemps(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_types_of_weather_1(self, patch):
        params = [4180386, 4179574, 4179074, 5160041, 733840],
        ans = {'Clear': ['Athens', 'Alpharetta', 'Acworth', 'Xanthi'],
               'Clouds': ['Lagrange']}
        func = "typesOfWeather"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.typesOfWeather(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    @patch("requests.get", side_effect=RequestGetMocker)
    def test_types_of_weather_2(self, patch):
        params = [29329748293, 4180386, 4179574],
        ans = "29329748293 is not a valid ID"
        func = "typesOfWeather"
        curr_time = time.time()
        self.error_messages[curr_time] = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.typesOfWeather(*params),
                         msg=self.error_messages[curr_time])
        del self.error_messages[curr_time]

    def test_zeta_error_messages(self):
        """function to compile all errors into one place."""
        errors = [self.error_messages[key] for key in self.error_messages]
        errors_msg = "\n".join(errors)
        self.assertEqual(
            {},
            self.error_messages,
            msg=f'\n\nMissed Tests:\n{errors_msg}'
        )

# imports the student's hw and runs it through the unittests


def run(student_file):
    hw = importlib.import_module(student_file.with_suffix("").name)
    TestMyClass.set_hw(hw)

    print("starting tester")
    with Path("out.txt").open(mode="w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner, exit=False)
    print("sucessfully ran, check out.txt")


# when a python script is run directly (not through import), then it's __name__
# is main and as such should do something. for us, that's testing the hw by
# calling run


if __name__ == "__main__":
    student_file = Path("HW07.py")
    if student_file.exists is False:
        print("Cannot find student's homework file. Make sure it's in the same"
              " folder and is named {}.".format(student_file.name))
    else:
        run(student_file)
