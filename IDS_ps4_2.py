from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    ''' 
    plot_weather_data is passed a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make another data visualization
    focused on the MTA and weather data we used in Project 3.
    
    Make a type of visualization different than what you did in the previous exercise.
    Try to use the data in a different way (e.g., if you made a lineplot concerning 
    ridership and time of day in exercise #1, maybe look at weather and try to make a 
    histogram in this exercise). Or try to use multiple encodings in your graph if 
    you didn't in the previous exercise.
    
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time-of-day or day-of-week
     * How ridership varies by subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out the link 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    to see all the columns and data points included in the turnstile_weather 
    dataframe.
     
   However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    pandas.options.mode.chained_assignment = None
    
    #print turnstile_weather['Hour']
    #print turnstile_weather['ENTRIESn_hourly']
    #plot = ggplot(turnstile_weather, aes(x='Hour',y='ENTRIESn_hourly')) + geom_point(color='red') + scale_x_continuous(limits=(0,23)) + scale_y_continuous(limits=(0,50000))
    #plot = ggplot(turnstile_weather, aes(x='Hour',y='ENTRIESn_hourly')) + geom_histogram(binwidth=1)
    
    Rain = turnstile_weather[turnstile_weather['rain']==1]  
    NoRain = turnstile_weather[turnstile_weather['rain']==0]
    #turnstile_weather['ENTRIESn_hourly'].hist(bins=5) # your code here to plot a historgram for hourly entries when it is raining
    #turnstile_weather['...'] # your code here to plot a historgram for hourly entries when it is not raining
    #Rain['ENTRIESn_hourly'].hist(bins=25,range=(0,6000),alpha=.5, label = "Rain", color=['green'])
    #NoRain['ENTRIESn_hourly'].hist(bins=30,range=(0,6000),alpha=.5, label = "No Rain", color=['blue'])   
    
    plot = ggplot(turnstile_weather, aes(x='Hour',y='ENTRIESn_hourly',color='rain')) + geom_point(alpha=0.1) + xlab('HOUR ') + ylab('SUBWAY PEOPLE IN') + scale_x_continuous(limits=(0,23)) + scale_y_continuous(limits=(0,50000))
    
    #plot = ggplot(Rain, aes(x='Hour',y='ENTRIESn_hourly')) + geom_point(alpha=0.1) + xlab('HOUR ') + ylab('SUBWAY PEOPLE IN') + scale_x_continuous(limits=(0,23)) + scale_y_continuous(limits=(0,50000))
    
    return plot

