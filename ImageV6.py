import cv2
from keras.backend import argmax
from matplotlib.backend_bases import MouseEvent 
import numpy as np
from keras import models
import mediapipe as mp
import subprocess
import webbrowser

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

#fonction d'interprétation des résultats
def display_prediction(prediction):
    n = prediction
    mouv=""
    if ((n==0).any()):
        mouv='Ok'
    elif((n==1).any()):
        mouv='Loser'
    elif((n==2).any()):
        mouv='Poing'
    elif((n==3).any()):
        mouv='Pouce'
    elif((n==4).any()):
        mouv='Index'
    elif((n==5).any()):
        mouv='Peace'
    elif((n==6).any()):
        mouv='Hello'
    elif((n==7).any()):
        mouv='Call'
    elif((n==8).any()):
        mouv='Jul'
    elif((n==9).any()):
         mouv="Rock'n Roll" 
    else:
        mouv='RAS_NADA'
    return mouv 

def action(mouv,key):
    if mouv=="Jul" and key==ord('a') :
        audio_file = "ressources/jul.mp3"
        return_code = subprocess.call(["afplay", audio_file])

    if mouv=="Rock'n Roll" and key==ord('a') :
        audio_file = "ressources/yeah.mp3"
        return_code = subprocess.call(["afplay", audio_file])
        
    if mouv=="Hello" and key==ord('a') :
        #  affichage de l'image correspondant au mvnt
        img = cv2.imread('ressources/hello.jpeg',1) 
        cv2.imshow('hello',img)
        cv2.waitKey(0)
        cv2.destroyWindow('hello')
        
    if mouv=="Index" and key==ord('a') :
        # ouverture de la page internet
        webbrowser.open("http://google.co.uk")
        
#Load the saved model
model = models.load_model(filepath = "Model/model_final.h5")

# lance la capture de vidéo de la webcam
cap= cv2.VideoCapture(0)
 
#initialisation de la détection avec médiapipe
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
    #début du traitement de l'image
    while True:
        succes, frame= cap.read()
        
        #vérification qu'il y a une image 
        if not succes:
            print("pas d'image")
            continue

        #détection des mains sur frame
        results = hands.process(frame)
        
        #traitement des landmarks et coordonnées
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                #affiche les landmarks
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                land_index = 0
                
                #répartition des coordonnées des landmarks dans des listes (x,y et z)
                list = []
                for landmark in hand_landmarks.landmark:
                   list.append(landmark.x)
                   list.append(landmark.y)
                   list.append(landmark.z)
                   land_index +=1
                   
                #noramalisation des coordonnées par rapport au point 0
                array = np.array(list)
                array [::3] = array[::3] -array [0]
                array [1::3] = array[1::3] -array [1]
                array [2::3] = array[2::3] -array [2]
                
                #resize la matrice dans le meme format que le model
                res = array.reshape((1,63))
                
                #prédiction du mouvement grace au model entrainé
                prediction = model.predict(res)
                
                #interprétation du mouvement avec la fonction
                mouv=display_prediction(np.argmax(prediction[0]))
                cv2.putText(frame,f"{mouv}",(50,150),cv2.FONT_HERSHEY_COMPLEX,4,(10,255,255),3,cv2.LINE_AA)
                action(mouv,key)   
                
                 
        key=cv2.waitKey(1)   
        
        #affichage de l'image
        cv2.imshow('Camera',frame)
        #arret du programme si appui sur q 
        if key==ord('q'):
            break  
cap.release()
cv2.destroyAllWindows()
