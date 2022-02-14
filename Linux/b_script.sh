#! /usr/bin/env bash
#0 7 * * * /home/sasha/python-education/Linux/b_script.sh

echo `curl "api.openweathermap.org/data/2.5/weather?lat=49.98&lon=36.23&appid=b0a467c1d1f4ad43c81acc7718754c5a&lang=ru"` >> /home/sasha/python-education/Linux/b_weather.txt