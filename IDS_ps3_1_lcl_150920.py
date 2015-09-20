import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):

    Rain = turnstile_weather[turnstile_weather['rain']==1]  
    NoRain = turnstile_weather[turnstile_weather['rain']==0]

    names = []

    for i in range(0,24):
        names.append("Hour " + str(i))

    
    rain_data_to_plot = []
    for i in range(0,24):
        Hour_i_data = Rain[Rain['Hour']==i]
        rain_data_to_plot.append(Hour_i_data['ENTRIESn_hourly'])

    norain_data_to_plot = []
    for i in range(0,24):
        Hour_i_data = NoRain[NoRain['Hour']==i]
        norain_data_to_plot.append(Hour_i_data['ENTRIESn_hourly'])

    fig = plt.figure()
    ax = plt.subplot()
    ax.set_ylim(0, 4e3)
    bp = ax.boxplot(rain_data_to_plot,showmeans=True)
    xtickNames = plt.setp(ax, xticklabels=np.repeat(names, 1))
    plt.setp(xtickNames, rotation=90, fontsize=10)
    ax.yaxis.grid(True, linestyle='-', which='major', color='black',
              alpha=.75)
    
    plt.ylabel('Frequency')
    plt.xlabel('Hour')
    plt.title('Boxplots of ENTRIESn_hourly for Rain condition. Zoom for clarity.')
    plt.legend()
        
    return plt

filename = "turnstile_data_master_with_weather.csv"
df_1 = pandas.DataFrame.from_csv(filename)

entries_histogram(df_1)
