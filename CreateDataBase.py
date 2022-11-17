import csv
import pandas as pd
import numpy as np
import cv2
import mediapipe as mp

#intitialisation des variables
video = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
df = pd.DataFrame()
count = 0
imagecount = 1500
columns = []

#création du tableau pour stockage des coords des landmarks
for i in range (21):
    columns.append(f"{i}_x")
    columns.append(f"{i}_y")
    columns.append(f"{i}_z")
columns.append("label")
print (columns)
df = pd.DataFrame(columns=columns)

#détection des mains avec médiapipe
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
    while True and count < imagecount:
        key=cv2.waitKey(1)
        succes , frame = video.read()
        
        #vérification de la capture vidéo
        if not succes:
            print ('echec capture')
            continue
        
        #affichage de la cam et des landmarks
        cv2.imshow('cam', frame)
        results = hands.process(frame)
          
        #sauvegarde des coordonnées des landmarks dans le tableau
        if key==ord('s') and results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                land_index = 0
                for landmark in hand_landmarks.landmark:
                    df.loc[count,f"{land_index}_x"] = landmark.x  
                    df.loc[count,f"{land_index}_y"] = landmark.y  
                    df.loc[count,f"{land_index}_z"] = landmark.z  
                    land_index +=1
            count += 1
            print (count)
            
        #quitter
        if key == ord('q'):
            break
        
#enregistrer la DataFrame
df = df.assign(label=8) 
df.to_csv('bdd/data_jul2.csv')

video.release()
cv2.destroyAllWindows()