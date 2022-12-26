from collections import Counter
import pandas as pd

def HomeForm(df,hometim):
       a = df[['FTR','HomeTeam','AwayTeam']]
       c=0
       WDLh = []
       while True:
              W,D,L = 0,0,0
              match = a[(((a['HomeTeam'] == hometim)|(a['AwayTeam'] == hometim)) & (a.index >= c))]
              match5 = match[:c+5].head()
              #COUNTER DRAW
              countD = Counter(match5['FTR'] =='D').elements()
              inD = list(countD).count(True)
              D=inD
              #COUNTER WIN
              con1 = match5[['FTR','HomeTeam']] == ['H',hometim]
              con2 = match5[['AwayTeam','FTR']] == [hometim,'A']
              r1 = con1['FTR'] == True
              s1 = con1['HomeTeam'] == True
              r2 = con2['FTR'] == True
              s2 = con2['AwayTeam'] == True
              countH1 = Counter((r1==True) & (s1==True)).elements()
              countH2 = Counter((s2==True) & (r2==True)).elements()
              inH1 = list(countH1).count(True)
              inH2 = list(countH2).count(True)
              W = inH1+inH2
              #COUNTER WIN
              countL = match5['FTR'].count()
              if countL < 5:
                     L = countL - (W+D)
              else:
                     L = 5 - (W+D)
              WDLh.append([W,D,L])
              if c == (0):
                     break
       return WDLh

def AwayForm(df,awaytim):
       a = df[['FTR','HomeTeam','AwayTeam']]
       c=0
       WDLh = []
       while True:
              W,D,L = 0,0,0
              match = a[(((a['HomeTeam'] == awaytim)|(a['AwayTeam'] == awaytim)) & (a.index >= c))]
              match5 = match[:c+5].head()
              #COUNTER DRAW
              countD = Counter(match5['FTR'] =='D').elements()
              inD = list(countD).count(True)
              D=inD
              #COUNTER WIN
              con1 = match5[['FTR','HomeTeam']] == ['H',awaytim]
              con2 = match5[['AwayTeam','FTR']] == [awaytim,'A']
              r1 = con1['FTR'] == True
              s1 = con1['HomeTeam'] == True
              r2 = con2['FTR'] == True
              s2 = con2['AwayTeam'] == True
              countH1 = Counter((r1==True) & (s1==True)).elements()
              countH2 = Counter((s2==True) & (r2==True)).elements()
              inH1 = list(countH1).count(True)
              inH2 = list(countH2).count(True)
              W = inH1+inH2
              #COUNTER WIN
              countL = match5['FTR'].count()
              if countL < 5:
                     L = countL - (W+D)
              else:
                     L = 5 - (W+D)
              WDLh.append([W,D,L])
              if c == (0):
                     break
       return WDLh

def H2H(df,hometim,awaytim):
       newdf = df[['FTR','HomeTeam','AwayTeam']]
       c=0
       WDL = []
       while True:
              W,D,L = 0,0,0
              kon1 = newdf[(((((newdf['HomeTeam']== hometim)|(newdf['AwayTeam']==hometim))) & (((newdf['HomeTeam']== awaytim)|(newdf['AwayTeam']== awaytim)))) & (newdf.index >= c))]
              match5 = kon1[:c+5].head()
              #COUNTER DRAW
              countD = Counter(match5['FTR'] =='D').elements()
              inD = list(countD).count(True)
              D=inD
              #COUNTER WIN
              con1 = match5[['FTR','HomeTeam']] == ['H',hometim]
              con2 = match5[['FTR','AwayTeam']] == ['A',awaytim]
              con3 = match5[['FTR','HomeTeam']] == ['H',awaytim]
              con4 = match5[['FTR','AwayTeam']] == ['A',hometim]
              r1 = con1['FTR'] == True
              s1 = con1['HomeTeam'] == True
              r2 = con2['FTR'] == True
              s2 = con2['AwayTeam'] == True
              r3 = con3['FTR'] == True
              s3 = con3['HomeTeam'] == True
              r4 = con4['FTR'] == True
              s4 = con4['AwayTeam'] == True
              countH1 = Counter((r1==True) & (s1==True)).elements()
              countH2 = Counter((s2==True) & (r2==True)).elements()
              countH3 = Counter((r3==True) & (s3==True)).elements()
              countH4 = Counter((s4==True) & (r4==True)).elements()
              inH1 = list(countH1).count(True)
              inH2 = list(countH2).count(True)
              inH3 = list(countH3).count(True)
              inH4 = list(countH4).count(True)
              W = inH1 + inH4
              L = inH2 + inH3
              WDL.append([W,D,L])              
              if c == (0):
                     break

       return WDL

def HomeGoal(df,hometim):
       a = df[['HomeTeam','AwayTeam','FTHG','FTAG']]
       c=0
       G = []
       while True:
              HG = 0
              match = a[(((a['HomeTeam'] == hometim)|(a['AwayTeam'] == hometim)) & (a.index >= c))]
              match5 = match[:c+5].head()
              con1 = match5['HomeTeam'] == hometim
              con2 = match5['AwayTeam'] == hometim
              hg=match5['FTHG'].where(con1==True).sum()
              ag=match5['FTAG'].where(con2==True).sum()
              HG = hg+ag
              G.append(int(HG))
              if c == (0):
                     break
       return G

def AwayGoal(df,awaytim):
       a = df[['HomeTeam','AwayTeam','FTHG','FTAG']]
       c=0
       G = []
       while True:
              HG = 0
              match = a[(((a['HomeTeam'] == awaytim)|(a['AwayTeam'] == awaytim)) & (a.index >= c))]
              match5 = match[:c+5].head()
              con1 = match5['HomeTeam'] == awaytim
              con2 = match5['AwayTeam'] == awaytim
              hg=match5['FTHG'].where(con1==True).sum()
              ag=match5['FTAG'].where(con2==True).sum()
              HG = hg+ag
              G.append(int(HG))
              if c == (0):
                     break
       return G