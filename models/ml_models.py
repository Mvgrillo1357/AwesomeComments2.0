### Building csv for Training ###
import pandas as pd
df=pd.read_csv("E:/summer22/individual_project/AwesomeComments2.0/models/cyberbullying_tweets_full.csv")
#print(df.head()) good this is the correct pathing
import pickle
#to save the dataframe, df to df.pkl
df.to_pickle("E:/summer22/individual_project/AwesomeComments2.0/models/df.pkl")    
#to load 123.pkl back to the dataframe tweet_df
tweet_df = pd.read_pickle("E:/summer22/individual_project/AwesomeComments2.0/models/df.pkl") 
print(tweet_df.head(20))