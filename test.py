from datetime import datetime,date

today = date.today()
num_of_day = today.strftime("%d")

num_of_day =28

the_date = today.strftime("%Y-%m-")

api ={"forecast":
        {"forecastday": 
            [{"date":"2023-07-28",
                "day":
                {"maxtemp_c":33.4,
                "mintemp_c":26.9,
                "avgtemp_c":29.9,
                "maxwind_kph":16.6,
                "totalprecip_mm":0.0,
                "totalsnow_cm":0.0,
                "daily_chance_of_rain":0,
                "daily_chance_of_snow":0,
                "condition":{}},
                
                "astro":{},
                
                "hour":[{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}}]},
                
            {"date":"2023-07-29",
            "day":  
                {"maxtemp_c":33.2, 
                "mintemp_c":26.8,
                "avgtemp_c":28.9,
                "maxwind_kph":19.4,
                "totalprecip_mm":0.0,
                "totalsnow_cm":0.0,
                "daily_chance_of_rain":0,
                "daily_chance_of_snow":0,
                "condition":{}},
                
                "astro":{},
                "hour":[{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}}]},
                
            {"date":"2023-07-30",
            "day":
                {"maxtemp_c":32.7,
                "mintemp_c":26.3,
                "avgtemp_c":28.7,
                "maxwind_kph":22.0,
                "totalprecip_mm":0.0,
                "totalsnow_cm":0.0,
                "daily_chance_of_rain":0,
                "daily_chance_of_snow":0,
                "condition":{}},
                
                "astro":{},
                
                "hour":[{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}},{"condition":{}}]}]}
                
}

for i in range(3):
    if(api["forecast"]["forecastday"][0]["date"] == the_date+str(int(num_of_day)+i)):
        print("yes")
    else:
        x =the_date+str(int(num_of_day)+i)
        print(api["forecast"]["forecastday"][0]["date"].x)

