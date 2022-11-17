import pandas as pd
import os

#création du data frame
final_df = pd.DataFrame()

#lecture des différents fichiers et concatenation des données
for csv in os.listdir('bdd'):
    tamp_df = pd.read_csv('bdd/' + csv,index_col=0).reset_index(drop= True)

    final_df = pd.concat([final_df, tamp_df], ignore_index = True)

#normalisation
final_df[final_df.columns[0:-1:3]] = final_df[final_df.columns[0:-1:3]].sub(final_df['0_x'], axis=0) # axe x
final_df[final_df.columns[1:-1:3]] = final_df[final_df.columns[1:-1:3]].sub(final_df['0_y'], axis=0) # axe y
final_df[final_df.columns[2:-1:3]] = final_df[final_df.columns[2:-1:3]].sub(final_df['0_z'], axis=0) # axe z

#shuffle
final_df = final_df.sample(frac=1).reset_index(drop=True)
final_df.to_csv('bdd/final.csv')