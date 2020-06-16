import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter, MonthLocator
from fbprophet import Prophet

plt.style.use('ggplot')

# read in birthdates data and set ds and y variables
birthdates = pd.read_csv('/Users/shioulinsam/Documents/Data/birthdates.csv')
birthdates['y'] = np.log(birthdates['births'])
birthdates['ds'] = birthdates['Date']

m = Prophet(changepoint_prior_scale=0.1)
m.fit(birthdates)
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)

# plot forecast
forecast_color = '#0072B2'
fig1 = plt.figure(facecolor='w', figsize=(9, 4))
ax = plt.subplot(111)
plt.plot(forecast['ds'], forecast['yhat'], ls='-', c=forecast_color)
#plt.plot(forecast['ds'], forecast['yhat_lower'], ls='--', c=forecast_color, alpha=0.5)
#plt.plot(forecast['ds'], forecast['yhat_upper'], ls='--', c=forecast_color, alpha=0.5)
ax.fill_between(
    forecast['ds'].values,
    forecast['yhat_lower'],
    forecast['yhat_upper'],
    facecolor=forecast_color,
    alpha=0.2)
plt.plot(m.history['ds'], m.history['y'], 'k.')
ax.grid(True, which='major', c='gray', ls='-', lw=1, alpha=0.2)
ax.set_xlim('1987', '1990')
ax.set_xlabel('Date')
ax.set_ylabel('Births')
fig1.show()
fig_string = '/Users/shioulinsam/Documents/Figures/' + 'birth' + 'forecast.png'
fig1.tight_layout()
fig1.savefig(fig_string)

# plot components(trend, holidays, weekly, yearly if available)
plot_trend = True
plot_holidays = m.holidays is not None
plot_weekly = 'weekly' in forecast
plot_yearly = 'yearly' in forecast

npanel = plot_trend + plot_holidays + plot_weekly + plot_yearly
fig2 = plt.figure(facecolor='w', figsize=(9, 2 * npanel))
panel_num = 1
ax = plt.subplot(npanel, 1, panel_num)
ax.plot(forecast['ds'], forecast['trend'], ls='-', c=forecast_color)
ax.plot(
    forecast['ds'],
    forecast['trend_lower'],
    ls='--',
    c=forecast_color,
    alpha=0.5)
ax.plot(
    forecast['ds'],
    forecast['trend_upper'],
    ls='--',
    c=forecast_color,
    alpha=0.5)
ax.fill_between(forecast['ds'].values,
                forecast['trend_lower'],
                forecast['trend_upper'],
                facecolor=forecast_color, alpha=0.2)
ax.set_xlabel('Date')
ax.set_ylabel('Trend')

if plot_holidays:
    panel_num += 1
    ax = fig2.add.subplot(npanel, 1, panel_num)
    holiday_comps = m.holiday['holidays'].unique()
    y_holiday = forecast[holiday_comps].sum(1)
    y_holiday_l = forecast[[h + '_lower' for h in holiday_comps]].sum(1)
    y_holiday_u = forecast[[h + '_upper' for h in holiday_comps]].sum(1)
    ax.plot(forecast['ds'], y_holiday, ls='-', c=forecast_color)
    ax.set_xlabel('Date')
    ax.set_yabel('Holidays')


if plot_weekly:
    panel_num += 1
    ax = plt.subplot(npanel, 1, panel_num)
    df_s = forecast.copy()
    df_s['dow'] = df_s['ds'].dt.weekday_name
    df_s = df_s.groupby('dow').first()
    #days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday']
    y_weekly = [df_s.loc[d]['weekly'] for d in days]
    y_weekly_l = [df_s.loc[d]['weekly_lower'] for d in days]
    y_weekly_u = [df_s.loc[d]['weekly_upper'] for d in days]
    ax.plot(range(len(days)), y_weekly, ls='-', c=forecast_color)
    plt.xticks(range(len(days)), days)
    # ax.set_xticklabels(days)
    ax.set_xlabel('Day of week')
    ax.set_ylabel('Weekly')

if plot_yearly:
    panel_num += 1
    ax = plt.subplot(npanel, 1, panel_num)
    df_s = forecast.copy()
    df_s['doy'] = df_s['ds'].map(lambda x: x.strftime('2000-%m-%d'))
    df_s = df_s.groupby('doy').first().sort_index()
    ax.plot(
        pd.to_datetime(
            df_s.index),
        df_s['yearly'],
        ls='-',
        c=forecast_color)
    months = MonthLocator(range(1, 13), bymonthday=1, interval=2)
    ax.xaxis.set_major_formatter(DateFormatter('%B %-d'))
    ax.xaxis.set_major_locator(months)
    ax.set_xlabel('Day of year')
    ax.set_ylabel('Yearly')


fig2.show()
fig_string = '/Users/shioulinsam/Documents/Figures/' + 'birth' + 'component.png'
fig2.tight_layout()
fig2.savefig(fig_string)
