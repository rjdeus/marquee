import pandas as pd
import matplotlib as plt

####### Tables
        
def table(gsid):

    df = pd.read_csv('data\\' + gsid + '.csv')
    print(df)
    
    attributes = ['growthScore','financialReturnsScore','multipleScore','integratedScore']
    plt.rcParams["figure.figsize"] = [plt.rcParams["figure.figsize"][0] *2, plt.rcParams["figure.figsize"][1]]
    df.plot(x = 'date', y = attributes)
    plt.legend(bbox_to_anchor=(0.7, 0.7), loc=2,
               ncol=2, mode="expand", borderaxespad=0.)
    plt.suptitle(company_id[0] + ": Fundamental Attributes vs Time")
    plt.ylabel("Attribute Value")
    plt.xlabel("Date")
    #plt.savefig('attributetime.png')

    df.plot(x = 'date', y = 'close')
    plt.title(company_id[0] + ": Close Price vs Time")
    leg = plt.legend( loc = 'best')
    plt.ylabel("Cost ($ US)")
    plt.xlabel("Date")
    #plt.savefig('costtime.png')
    plt.show()

    '''
    plt.plot(merged['date'], merged['growthScore'])
    plt.title(company_id[0] + " growthScore over Time")
    plt.xticks([merged['date'].iloc[0],merged['date'].iloc[len(merged['date'])//2],merged['date'].iloc[-1]])
    plt.show()
    '''

table("11308")
