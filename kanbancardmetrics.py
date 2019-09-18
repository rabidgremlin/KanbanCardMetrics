import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel

# This is some ugly ugly code

HOLIDAYS = [pd.Timestamp('2016-12-26'), pd.Timestamp('2016-12-27'), pd.Timestamp('2016-12-28'), pd.Timestamp('2016-12-29'), pd.Timestamp('2016-12-30'),
            pd.Timestamp('2017-01-02'), pd.Timestamp('2017-01-03'), pd.Timestamp('2017-01-04'), pd.Timestamp('2017-01-05'), pd.Timestamp('2017-01-06'),
            pd.Timestamp('2017-01-31'), pd.Timestamp('2017-02-06')]

def calc_days_to_complete(df):
    # from http://stackoverflow.com/a/22819128
    A = [d.date() for d in df['Started']]
    B = [d.date() for d in df['Finished']]

    print(B)

    df['DaysToComplete'] = np.busday_count(A, B) + 1 #, )holidays=HOLIDAYS) + 1

    # TODO check for negative days to ID bad data
    #print(df)

    return df 

def generate_cards_complete_by_day_graph(df):       

    df4 = df[['Finished','ID']]    

    df4 = df4.set_index('Finished')
    df4 = df4[['ID']]   

    df4 = df4.groupby(df4.index).count()
    df4.columns = ['Cards Completed']
    #df4['7 Day Average'] = pd.rolling_mean(df4['Cards Completed'], 7)

    df4['7 Day Average'] = df4['Cards Completed'].rolling(window=7,center=False).mean()
    df4['30 Day Average'] = df4['Cards Completed'].rolling(window=30,center=False).mean()

    print(df4)

    p = df4.plot()
    p.set(xlabel="Date", ylabel="Cards", title='Cards completed by day')    
    fig = p.get_figure()        
    fig.tight_layout()
    fig.savefig("cardsbyday.pdf")

def generate_avg_days_to_complete_over_time_graph(df):

    df5 = df[['Finished','DaysToComplete']] 
    df5 = df5.set_index('Finished')
    df5 = df5.sort_index()

    df5['Avg Days To Complete'] = df5.expanding(min_periods=1).mean()

    df5 = df5[['Avg Days To Complete']]

    print(df5)  

    p = df5.plot()
    p.set(xlabel="Date", ylabel="Days", title='Average Days to Complete a Card over time')    
    fig = p.get_figure()        
    fig.tight_layout()
    fig.savefig("avgdaystocompleteovertime.pdf")
    

def dump_stats(df):
    print('---------------------------------')
    print('Number of cards completed: %d' % len(df))
    print('Avg days to complete     : %f (working days)' % np.mean(df['DaysToComplete']))
    print()

    print('---------------------------------')
    print('Average Days to Complete by Type')
    df1 = df[['Type', 'DaysToComplete']]
    df1.columns = ['Type', 'Avg Days To Complete']
    print(df1.groupby('Type').mean())
    print()

    print('---------------------------------')
    print('Cards complete by day')
    generate_cards_complete_by_day_graph(df)
    print()

    print('---------------------------------')
    print('Avg days to complete over time')
    generate_avg_days_to_complete_over_time_graph(df)
    print()
    

    



    #print(df4)
    print()



def main():
    df = pd.read_excel("carddata.xlsx", sheetname=0)

# TODO validate dataframe & cols   

    df = calc_days_to_complete(df)

    dump_stats(df)

if __name__ == '__main__':
    main()

