import requests
import datetime
import api_config #file made by me, to store api key
import json
def try_another_city():
    choice = input(str("Do you want to search for weather of another city?(Yes/no)")).lower()
    if(choice=='yes' or choice == 'y'):
        return True
    else:
        print("Exiting...")
        return False


api_key = api_config.api #api key is hidden for security purposes
flag=True
while(flag == True):
    city = input('Enter city: ')
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city,api_key)
    try :
        response = requests.get(api_url)
        #print(response.status_code)
        #print(type(response.status_code))
        if response.status_code == 200 :
            print('Connection Successful............')
            content = response.json()
            date = datetime.datetime.now()
            location = city
            temp = round(content['main']['temp']-273.15,2)
            weather= content['weather'][0]['description']
            humidity = content['main']['humidity']
            wind_speed = content['wind']['speed']
            print(' date: {}\n location: {}\n temperature: {}\n weather: {}\n humidity: {}\n wind_speed: {}'.format(date,location,temp,weather,humidity,wind_speed))
            try :
                f = open("result.txt", "a+")
                f.write('date: {}\nlocation: {}\ntemperature: {}\nweather: {}\nhumidity: {}\nwind_speed: {}\n'.format(date,location,temp,weather,humidity,wind_speed))
                print('result.txt file contains the output\n')
                f.close()
                flag = try_another_city()
            except Exception as file_error :
                print("FILE ERROR: {}".format(file_error))
        else:
            print("Status Code: {}, {}".format(response.status_code,response.reason))

    except Exception as error:
        print("ERROR1:{}".format(error))

