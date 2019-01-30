temp = int(input ("What is the temperature today (in Farenheight)"))
wind = input ("Is it windy today (yes/no)?")
rain = input ("Is it raining today (yes/no)?")


def check_wind_and_rain ():
    #check to see if it is windy
    if wind == "yes":
        #assign a true value if it is windy
        is_wind = True
    else:
        #assign a false value if it is not windy
        is_wind = False
    #check to see if it is raining
    if rain == "yes":
        #assign a true value if it is raining
        is_raining = True
    else:
        #assign a true value if it is not raining
        is_raining = False
    return is_wind, is_raining


def what_to_wear (temp, rain, wind):
    is_wind, is_raining = check_wind_and_rain()
    message = ""
    if temp < 30:
        message = "Brrr its cold, make sure to wear a jacket, sweater, hat, and gloves!"
        if is_raining or is_wind == True:
            message = "Wear the heaviest clothes you have. A jacket, sweater, hat, and gloves is a must!"
    if temp <=45 and temp>=30:
        message = "Its a little chilly. You should be fine with a heavy sweater or a light jacket"
        if is_raining or is_wind == True:
            message = "wear a wind breaker with a heavy sweater"
    if temp <=60 and temp>45:
        message = "Wear a light sweater or maybe a jacket"
        if is_wind == True:
            message = "Wear a heavy sweater, but you should be fine without a jacket"
        if is_raining == True:
            message = "Wear a rain jacket, but you probably dont need a sweater"
    if temp <=70 and temp>60:
        message = "A t-shirt and jeans is perfect for this weather"
        if is_wind == True:
            message = "Wear a light sweater with a t-shirt and jeans"
        if is_raining == True:
            message = "Wear a light raincoat with a t-shrit and jeans"
    if temp > 70:
        message = "Wear shorts and a t-shirt"
        if is_raining == True:
            message = "Its too hot for a jacket or sweater, so just bring an umbrella and wear shorts with a t-shirt"
    return message

print (what_to_wear(temp,rain,wind))
