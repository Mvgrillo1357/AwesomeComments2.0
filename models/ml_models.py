### Building csv for Training ###
import pandas as pd
df=pd.read_csv('AwesomeComments2.0/models/cyberbullying_tweets_full.csv')
#to save the dataframe, df to 123.pkl
df.to_pickle('/models/cyberbullying_tweets_full.csv/df.pkl')    
#to load 123.pkl back to the dataframe df
tweet_df = pd.read_pickle('/Drive Path/df.pkl') 
print(tweet_df.head(20))