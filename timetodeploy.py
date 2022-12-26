import pandas as pd
import keras
import os
import numpy as np
import tensorflow as tf
import streamlit as st
import helper
from collections import Counter
os.system('cls')

tab1, tab2, tab3,tab4, tab5 = st.tabs(['Premier League','La Liga','Serie A','Bundesliga','Ligue 1'])

with tab1:
       epldftrain = pd.read_csv('EPLDataset.csv').drop(columns=['Unnamed: 0','HomeTeam','AwayTeam'])
       epldf = pd.read_csv('EPLData.csv').drop(columns='Unnamed: 0')
       eplteam = pd.read_csv('EPLTeam.csv')

       eplteam = eplteam['HomeTeam'].drop_duplicates().sort_values(ascending=True).reset_index().drop(columns='index')
       eplname_team = []
       for i in eplteam['HomeTeam']:
              eplname_team.append(i)
       col1,col2 = st.columns(2)
       with col1:
              eplhometim = st.selectbox('Home Team',eplname_team)
       with col2:
              eplawaytim = st.selectbox('Away Team',eplname_team)

       eplhomeform = helper.HomeForm(epldf, eplhometim)
       eplawayform = helper.AwayForm(epldf, eplawaytim)
       eplhomegoal = helper.HomeGoal(epldf, eplhometim)
       eplawaygoal = helper.AwayGoal(epldf, eplawaytim)
       eplh2h = helper.H2H(epldf, eplhometim, eplawaytim)

       col3,col4,col5 = st.columns(3)
       col6,col7= st.columns(2)

       eplbethome = col3.number_input('Bet for Home Team Win: ',min_value=0.1,key=1)
       eplbetdraw = col4.number_input('Bet for Draw: ',min_value=0.1,key=2)
       eplbetaway = col5.number_input('Bet for Away Team Win: ',min_value=0.1,key=3)
       eplbetover1 = col6.number_input('First Bet for Over: ',min_value=0.1,key=4)
       eplbetunder1 = col7.number_input('First Bet for Under: ',min_value=0.1,key=5)

       eplbetover2 = col6.number_input('Second Bet for Over: ',min_value=0.1,key=9)
       eplbetunder2 = col7.number_input('Second Bet for Under: ',min_value=0.1,key=10)

       eplbetover3 = col6.number_input('Third Bet for Over: ',min_value=0.1,key=14)
       eplbetunder3 = col7.number_input('Third Bet for Under: ',min_value=0.1,key=15)

       eplbetover = (eplbetover1+eplbetover2+eplbetover3)/3
       eplbetunder = (eplbetunder1+eplbetunder2+eplbetunder3)/3
       eplhdstd = eplbetdraw/eplbethome
       epladstd = eplbetdraw/eplbetaway

       eplpred = [eplbetover,eplbetunder,eplhdstd,epladstd]
       epldata1 = pd.DataFrame([eplpred])
       epldata1['HG'],epldata1['AG'] = eplhomegoal,eplawaygoal
       eplhf = pd.DataFrame(eplhomeform).astype('int')
       eplaf = pd.DataFrame(eplawayform).astype('int')
       eplhtoh = pd.DataFrame(eplh2h).astype('int')

       eplpreddata = pd.concat([epldata1,eplhf,eplaf,eplhtoh],axis=1)
       eplpreddata = np.array(eplpreddata)

       eplmodel = keras.models.load_model('EPLModel.h5')

       if st.button('Prediction',key=100):
              with st.spinner('Gathering Data.....'):
                     eplmodel.fit(epldftrain.iloc[:,5:],(epldftrain.iloc[:,:3],epldftrain.iloc[:,3:5]),epochs=10)
              st.snow()
              eply = eplmodel.predict(eplpreddata)
              eply1 = np.round(eply[0],decimals=2)
              eply2 = np.round(eply[1],decimals=2)
              eplrp=[]
              for i in eply1:
                     eplrp.append(i)
              eplsp=[]
              for i in eply2:
                     eplsp.append(i)
              st.success(f'Result Prediction: ')
              st.write(f'Home Win Percentage {eplrp[0][0]*100:.2f}%------Draw Percentage {eplrp[0][1]*100:.2f}%------Away Win Percentage {eplrp[0][2]*100:.2f}')
              st.success(f'Score Prediction: ')
              st.write(f'Over 2 Prediction {eplsp[0][0]*100:.2f}%------Under 2 Prediction {eplsp[0][1]*100:.2f}%')

with tab2:
       laligadftrain = pd.read_csv('LaligaDataset.csv').drop(columns=['Unnamed: 0','HomeTeam','AwayTeam'])
       laligadf = pd.read_csv('LaligaData.csv').drop(columns='Unnamed: 0')
       laligateam = pd.read_csv('LaligaTeam.csv')

       laligateam = laligateam['HomeTeam'].drop_duplicates().sort_values(ascending=True).reset_index().drop(columns='index')
       laliganame_team = []
       for i in laligateam['HomeTeam']:
              laliganame_team.append(i)
       laligacol8 , laligacol9 = st.columns(2)
       with laligacol8:
              laligahometim = st.selectbox('Home Team' , laliganame_team)
       with laligacol9:
              laligaawaytim = st.selectbox('Away Team' , laliganame_team)

       laligahomeform = helper.HomeForm(laligadf, laligahometim)
       laligaawayform = helper.AwayForm(laligadf, laligaawaytim)
       laligahomegoal = helper.HomeGoal(laligadf, laligahometim)
       laligaawaygoal = helper.AwayGoal(laligadf, laligaawaytim)
       laligah2h = helper.H2H(laligadf, laligahometim, laligaawaytim)

       laligacol10 , laligacol11 , laligacol12 = st.columns(3)
       laligacol13 , laligacol14 = st.columns(2)
     
       laligabethome = laligacol10.number_input('Bet for Home Team Win: ',min_value=0.1,key=16)
       laligabetdraw = laligacol11.number_input('Bet for Draw: ',min_value=0.1,key=17)
       laligabetaway = laligacol12.number_input('Bet for Away Team Win: ',min_value=0.1,key=18)
       laligabetover1 = laligacol13.number_input('First Bet for Over: ',min_value=0.1,key=19)
       laligabetunder1 = laligacol14.number_input('First Bet for Under: ',min_value=0.1,key=20)

       laligabetover2 = laligacol13.number_input('Second Bet for Over: ',min_value=0.1,key=24)
       laligabetunder2 = laligacol14.number_input('Second Bet for Under: ',min_value=0.1,key=25)

       laligabetover3 = laligacol13.number_input('Third Bet for Over: ',min_value=0.1,key=29)
       laligabetunder3 = laligacol14.number_input('Third Bet for Under: ',min_value=0.1,key=30)

       laligabetover = (laligabetover1+laligabetover2+laligabetover3)/3
       laligabetunder = (laligabetunder1+laligabetunder2+laligabetunder3)/3
       laligahdstd = laligabetdraw/laligabethome
       laligaadstd = laligabetdraw/laligabetaway

       laligapred = [laligabetover,laligabetunder,laligahdstd,laligaadstd]
       laligadata1 = pd.DataFrame([laligapred])
       laligadata1['HG'],laligadata1['AG'] = laligahomegoal,laligaawaygoal
       laligahf = pd.DataFrame(laligahomeform).astype('int')
       laligaaf = pd.DataFrame(laligaawayform).astype('int')
       laligahtoh = pd.DataFrame(laligah2h).astype('int')

       laligapreddata = pd.concat([laligadata1,laligahf,laligaaf,laligahtoh],axis=1)
       laligapreddata = np.array(laligapreddata)

       laligamodel = keras.models.load_model('LaLigaModel.h5')

       if st.button('Prediction',key=200):
              with st.spinner('Gathering Data.....'):
                     laligamodel.fit(laligadftrain.iloc[:,5:],(laligadftrain.iloc[:,:3],laligadftrain.iloc[:,3:5]),epochs=10)
              st.snow()
              laligay = laligamodel.predict(laligapreddata)
              laligay1 = np.round(laligay[0],decimals=2)
              laligay2 = np.round(laligay[1],decimals=2)
              laligarp=[]
              for i in laligay1:
                     laligarp.append(i)
              laligasp=[]
              for i in laligay2:
                     laligasp.append(i)
              st.success(f'Result Prediction: ')
              st.write(f'Home Win Percentage {laligarp[0][0]*100:.2f}%------Draw Percentage {laligarp[0][1]*100:.2f}%------Away Win Percentage {laligarp[0][2]*100:.2f}')
              st.success(f'Score Prediction: ')
              st.write(f'Over 2 Prediction {laligasp[0][0]*100:.2f}%------Under 2 Prediction {laligasp[0][1]*100:.2f}%')

with tab3:
       seriadftrain = pd.read_csv('SeriADataset.csv').drop(columns=['Unnamed: 0','HomeTeam','AwayTeam'])
       seriadf = pd.read_csv('SeriAData.csv').drop(columns='Unnamed: 0')
       seriateam = pd.read_csv('SeriATeam.csv')

       seriateam = seriateam['HomeTeam'].drop_duplicates().sort_values(ascending=True).reset_index().drop(columns='index')
       serianame_team = []
       for i in seriateam['HomeTeam']:
              serianame_team.append(i)
       seriacol1,seriacol2 = st.columns(2)
       with seriacol1:
              seriahometim = st.selectbox('Home Team',serianame_team)
       with seriacol2:
              seriaawaytim = st.selectbox('Away Team',serianame_team)

       seriahomeform = helper.HomeForm(seriadf, seriahometim)
       seriaawayform = helper.AwayForm(seriadf, seriaawaytim)
       seriahomegoal = helper.HomeGoal(seriadf, seriahometim)
       seriaawaygoal = helper.AwayGoal(seriadf, seriaawaytim)
       seriah2h = helper.H2H(seriadf, seriahometim, seriaawaytim)

       seriacol3,seriacol4,seriacol5 = st.columns(3)
       seriacol6,seriacol7= st.columns(2)

       seriabethome = seriacol3.number_input('Bet for Home Team Win: ',min_value=0.1,key=31)
       seriabetdraw = seriacol4.number_input('Bet for Draw: ',min_value=0.1,key=32)
       seriabetaway = seriacol5.number_input('Bet for Away Team Win: ',min_value=0.1,key=33)
       seriabetover1 = seriacol6.number_input('First Bet for Over: ',min_value=0.1,key=34)
       seriabetunder1 = seriacol7.number_input('First Bet for Under: ',min_value=0.1,key=35)
       
       seriabetover2 = seriacol6.number_input('Second Bet for Over: ',min_value=0.1,key=39)
       seriabetunder2 = seriacol7.number_input('Second Bet for Under: ',min_value=0.1,key=40)
       
       seriabetover3 = seriacol6.number_input('Third Bet for Over: ',min_value=0.1,key=44)
       seriabetunder3 = seriacol7.number_input('Third Bet for Under: ',min_value=0.1,key=45)

       seriabetover = (seriabetover1+seriabetover2+seriabetover3)/3
       seriabetunder = (seriabetunder1+seriabetunder2+seriabetunder3)/3
       seriahdstd = seriabetdraw/seriabethome
       seriaadstd = seriabetdraw/seriabetaway

       seriapred = [seriabetover,seriabetunder,seriahdstd,seriaadstd]
       seriadata1 = pd.DataFrame([seriapred])
       seriadata1['HG'],seriadata1['AG'] = seriahomegoal,seriaawaygoal
       seriahf = pd.DataFrame(seriahomeform).astype('int')
       seriaaf = pd.DataFrame(seriaawayform).astype('int')
       seriahtoh = pd.DataFrame(seriah2h).astype('int')

       seriapreddata = pd.concat([seriadata1,seriahf,seriaaf,seriahtoh],axis=1)
       seriapreddata = np.array(seriapreddata)

       seriamodel = keras.models.load_model('SeriAModel.h5')

       if st.button('Prediction',key=300):
              with st.spinner('Gathering Data.....'):
                     seriamodel.fit(seriadftrain.iloc[:,5:],(seriadftrain.iloc[:,:3],seriadftrain.iloc[:,3:5]),epochs=10)
              st.snow()
              seriay = seriamodel.predict(seriapreddata)
              seriay1 = np.round(seriay[0],decimals=2)
              seriay2 = np.round(seriay[1],decimals=2)
              seriarp=[]
              for i in seriay1:
                     seriarp.append(i)
              seriasp=[]
              for i in seriay2:
                     seriasp.append(i)
              st.success(f'Result Prediction: ')
              st.write(f'Home Win Percentage {seriarp[0][0]*100:.2f}%------Draw Percentage {seriarp[0][1]*100:.2f}%------Away Win Percentage {seriarp[0][2]*100:.2f}')
              st.success(f'Score Prediction: ')
              st.write(f'Over 2 Prediction {seriasp[0][0]*100:.2f}%------Under 2 Prediction {seriasp[0][1]*100:.2f}%')

with tab4:
       bldftrain = pd.read_csv('BundesligaDataset.csv').drop(columns=['Unnamed: 0','HomeTeam','AwayTeam'])
       bldf = pd.read_csv('BundesligaData.csv').drop(columns='Unnamed: 0')
       blteam = pd.read_csv('BundesligaTeam.csv')

       blteam = blteam['HomeTeam'].drop_duplicates().sort_values(ascending=True).reset_index().drop(columns='index')
       blname_team = []
       for i in blteam['HomeTeam']:
              blname_team.append(i)
       blcol1,blcol2 = st.columns(2)
       with blcol1:
              blhometim = st.selectbox('Home Team',blname_team)
       with blcol2:
              blawaytim = st.selectbox('Away Team',blname_team)

       blhomeform = helper.HomeForm(bldf, blhometim)
       blawayform = helper.AwayForm(bldf, blawaytim)
       blhomegoal = helper.HomeGoal(bldf, blhometim)
       blawaygoal = helper.AwayGoal(bldf, blawaytim)
       blh2h = helper.H2H(bldf, blhometim, blawaytim)

       blcol3,blcol4,blcol5 = st.columns(3)
       blcol6,blcol7= st.columns(2)

       blbethome = blcol3.number_input('Bet for Home Team Win: ',min_value=0.1,key=46)
       blbetdraw = blcol4.number_input('Bet for Draw: ',min_value=0.1,key=47)
       blbetaway = blcol5.number_input('Bet for Away Team Win: ',min_value=0.1,key=48)
       blbetover1 = blcol6.number_input('First Bet for Over: ',min_value=0.1,key=49)
       blbetunder1 = blcol7.number_input('First Bet for Under: ',min_value=0.1,key=50)

       blbetover2 = blcol6.number_input('Second Bet for Over: ',min_value=0.1,key=54)
       blbetunder2 = blcol7.number_input('Second Bet for Under: ',min_value=0.1,key=55)

       blbetover3 = blcol6.number_input('Third Bet for Over: ',min_value=0.1,key=59)
       blbetunder3 = blcol7.number_input('Third Bet for Under: ',min_value=0.1,key=60)

       blbetover = (blbetover1+blbetover2+blbetover3)/3
       blbetunder = (blbetunder1+blbetunder2+blbetunder3)/3
       blhdstd = blbetdraw/blbethome
       bladstd = blbetdraw/blbetaway

       blpred = [blbetover,blbetunder,blhdstd,bladstd]
       bldata1 = pd.DataFrame([blpred])
       bldata1['HG'],bldata1['AG'] = blhomegoal,blawaygoal
       blhf = pd.DataFrame(blhomeform).astype('int')
       blaf = pd.DataFrame(blawayform).astype('int')
       blhtoh = pd.DataFrame(blh2h).astype('int')

       blpreddata = pd.concat([bldata1,blhf,blaf,blhtoh],axis=1)
       blpreddata = np.array(blpreddata)

       blmodel = keras.models.load_model('BundesligaModel.h5')

       if st.button('Prediction',key=400):
              with st.spinner('Gathering Data.....'):
                     blmodel.fit(bldftrain.iloc[:,5:],(bldftrain.iloc[:,:3],bldftrain.iloc[:,3:5]),epochs=10)
              st.snow()
              bly = blmodel.predict(blpreddata)
              bly1 = np.round(bly[0],decimals=2)
              bly2 = np.round(bly[1],decimals=2)
              blrp=[]
              for i in bly1:
                     blrp.append(i)
              blsp=[]
              for i in bly2:
                     blsp.append(i)
              st.success(f'Result Prediction: ')
              st.write(f'Home Win Percentage {blrp[0][0]*100:.2f}%------Draw Percentage {blrp[0][1]*100:.2f}%------Away Win Percentage {blrp[0][2]*100:.2f}')
              st.success(f'Score Prediction: ')
              st.write(f'Over 2 Prediction {blsp[0][0]*100:.2f}%------Under 2 Prediction {blsp[0][1]*100:.2f}%')

with tab5:
       l1dftrain = pd.read_csv('Ligue1Dataset.csv').drop(columns=['Unnamed: 0','HomeTeam','AwayTeam'])
       l1df = pd.read_csv('Ligue1Data.csv').drop(columns='Unnamed: 0')
       l1team = pd.read_csv('Ligue1Team.csv')

       l1team = l1team['HomeTeam'].drop_duplicates().sort_values(ascending=True).reset_index().drop(columns='index')
       l1name_team = []
       for i in l1team['HomeTeam']:
              l1name_team.append(i)
       l1col1,l1col2 = st.columns(2)
       with l1col1:
              l1hometim = st.selectbox('Home Team',l1name_team)
       with l1col2:
              l1awaytim = st.selectbox('Away Team',l1name_team)

       l1homeform = helper.HomeForm(l1df, l1hometim)
       l1awayform = helper.AwayForm(l1df, l1awaytim)
       l1homegoal = helper.HomeGoal(l1df, l1hometim)
       l1awaygoal = helper.AwayGoal(l1df, l1awaytim)
       l1h2h = helper.H2H(l1df, l1hometim, l1awaytim)

       l1col3,l1col4,l1col5 = st.columns(3)
       l1col6,l1col7= st.columns(2)

       l1bethome = l1col3.number_input('Bet for Home Team Win: ',min_value=0.1,key=61)
       l1betdraw = l1col4.number_input('Bet for Draw: ',min_value=0.1,key=62)
       l1betaway = l1col5.number_input('Bet for Away Team Win: ',min_value=0.1,key=63)
       l1betover1 = l1col6.number_input('First Bet for Over: ',min_value=0.1,key=64)
       l1betunder1 = l1col7.number_input('First Bet for Under: ',min_value=0.1,key=65)

       l1betover2 = l1col6.number_input('Second Bet for Over: ',min_value=0.1,key=69)
       l1betunder2 = l1col7.number_input('Second Bet for Under: ',min_value=0.1,key=70)

       l1betover3 = l1col6.number_input('Third Bet for Over: ',min_value=0.1,key=74)
       l1betunder3 = l1col7.number_input('Third Bet for Under: ',min_value=0.1,key=75)

       l1betover = (l1betover1+l1betover2+l1betover3)/3
       l1betunder = (l1betunder1+l1betunder2+l1betunder3)/3
       l1hdstd = l1betdraw/l1bethome
       l1adstd = l1betdraw/l1betaway

       l1pred = [l1betover,l1betunder,l1hdstd,l1adstd]
       l1data1 = pd.DataFrame([l1pred])
       l1data1['HG'],l1data1['AG'] = l1homegoal,l1awaygoal
       l1hf = pd.DataFrame(l1homeform).astype('int')
       l1af = pd.DataFrame(l1awayform).astype('int')
       l1htoh = pd.DataFrame(l1h2h).astype('int')

       l1preddata = pd.concat([l1data1,l1hf,l1af,l1htoh],axis=1)
       l1preddata = np.array(l1preddata)

       l1model = keras.models.load_model('Ligue1Model.h5')

       if st.button('Prediction',key=500):
              with st.spinner('Gathering Data.....'):
                     l1model.fit(l1dftrain.iloc[:,5:],(l1dftrain.iloc[:,:3],l1dftrain.iloc[:,3:5]),epochs=10)
              st.snow()
              l1y = l1model.predict(l1preddata)
              l1y1 = np.round(l1y[0],decimals=2)
              l1y2 = np.round(l1y[1],decimals=2)
              l1rp=[]
              for i in l1y1:
                     l1rp.append(i)
              l1sp=[]
              for i in l1y2:
                     l1sp.append(i)
              st.success(f'Result Prediction: ')
              st.write(f'Home Win Percentage {l1rp[0][0]*100:.2f}%------Draw Percentage {l1rp[0][1]*100:.2f}%------Away Win Percentage {l1rp[0][2]*100:.2f}')
              st.success(f'Score Prediction: ')
              st.write(f'Over 2 Prediction {l1sp[0][0]*100:.2f}%------Under 2 Prediction {l1sp[0][1]*100:.2f}%')
