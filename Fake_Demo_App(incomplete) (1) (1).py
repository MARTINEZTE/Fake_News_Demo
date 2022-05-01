#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
from tkinter import *

class MyApp(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.master.title("News Buster")
        
        
        ww = 770
        wh = 570
        wx = (self.master.winfo_screenwidth() - ww) / 2
        wy = (self.master.winfo_screenheight() - wh) / 2
        
        self.master.geometry("%dx%d+%d+%d" % (ww, wh, wx, wy))
        
        self.dx = 15
        self.dy = 15
        
        self.a_label = tk.Label(master, text = "Welcome to News Buster", fg = 'Black', font = ("Times New Roman",20))
        self.a_label.grid(column = 50, row = 0, padx = self.dx,pady = self.dy)
        
        self.a_label = tk.Label(master, text ="Enter news article here", fg = 'Black', font = ("Times New Roman",12))
        self.a_label.grid(column = 0, row = 2, padx = self.dx, pady = self.dy)
        
        self.a_label = tk.Label(master, text ="Context", fg = 'Black', font = ("Times New Roman",12))
        self.a_label.grid(column = 0, row = 4, padx = self.dx, pady = self.dy)
        
        self.a_label = tk.Label(master, text ="Party", fg = 'Black', font = ("Times New Roman",12))
        self.a_label.grid(column = 0, row = 6, padx = self.dx, pady = self.dy)
        
        self.a_label = tk.Label(master, text ="Speaker", fg = 'Black', font = ("Times New Roman",12))
        self.a_label.grid(column = 0, row = 8, padx = self.dx, pady = self.dy)
        
        self.a_label = tk.Label(master, text ="Subject", fg = 'Black', font = ("Times New Roman",12))
        self.a_label.grid(column = 0, row = 10, padx = self.dx, pady = self.dy)
        
        self.an_entry = tk.Entry(master,width = 40 )
        self.an_entry.grid(column = 0, row = 3, padx = self.dx, pady = self.dy)
        
        self.an_entry = tk.Entry(master,width = 40)
        self.an_entry.grid(column = 0, row = 5, padx = self.dx, pady = self.dy)
        
        self.an_entry = tk.Entry(master,width = 40)
        self.an_entry.grid(column = 0, row = 7, padx = self.dx, pady = self.dy)
        
        self.an_entry = tk.Entry(master,width = 40)
        self.an_entry.grid(column = 0, row = 9, padx = self.dx, pady = self.dy)
        
        self.an_entry = tk.Entry(master,width = 40)
        self.an_entry.grid(column = 0, row = 11, padx = self.dx, pady = self.dy)
        
window = Tk()
btn=Button(window, text = "Next", fg = 'black')
btn.place(x=620, y=500)

if __name__ == '__main__':
    MyApp().mainloop()

window.mainloop()
    


# In[2]:


import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
from tkinter import *

class MyApp(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.master.title("News Buster")
        
        
        ww = 770
        wh = 570
        wx = (self.master.winfo_screenwidth() - ww) / 2
        wy = (self.master.winfo_screenheight() - wh) / 2
        
        self.master.geometry("%dx%d+%d+%d" % (ww, wh, wx, wy))
        
        self.dx = 15
        self.dy = 15
        
        self.a_label = tk.Label(master, text = "Results of News Article", fg = 'Black', font = ("Times New Roman",20))
        self.a_label.grid(column = 50, row = 0, padx = self.dx,pady = self.dy)
        
        self.a_label = tk.Label(master, text ="True or False: ", fg = 'Black', font = ("Times New Roman",12))
        self.a_label.grid(column = 0, row = 2, padx = self.dx, pady = self.dy)
        
        self.a_label = tk.Label(master, text ="Part that is false:", fg = 'Black', font = ("Times New Roman",12))
        self.a_label.grid(column = 0, row = 4, padx = self.dx, pady = self.dy)
        
        self.a_label = tk.Label(master, text ="Percentage of false information", fg = 'Black', font = ("Times New Roman",12))
        self.a_label.grid(column = 0, row = 6, padx = self.dx, pady = self.dy)
        
        self.an_entry = tk.Entry(master,width = 40 )
        self.an_entry.grid(column = 0, row = 3, padx = self.dx, pady = self.dy)
        
        self.an_entry = tk.Entry(master,width = 40)
        self.an_entry.grid(column = 0, row = 5, padx = self.dx, pady = self.dy)
        
        self.an_entry = tk.Entry(master,width = 40)
        self.an_entry.grid(column = 0, row = 7, padx = self.dx, pady = self.dy)
        
if __name__ == '__main__':
    MyApp().mainloop()


# In[3]:


import pandas as pd
import numpy as np
import seaborn as sb
import itertools
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, accuracy_score, confusion_matrix
from sklearn.linear_model import LinearRegression, PassiveAggressiveClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer

import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
from sklearn.pipeline import Pipeline
from nltk.stem import SnowballStemmer
from nltk.stem.porter import PorterStemmer

data = pd.read_csv('dataset_modified.csv')
data = data[data['Context'].notnull()]
#Setting up binary 
falsev = (data['Label']=="pants-fire") |(data['Label']=="FALSE") | (data['Label']=="barely-true") | (data['Label']=="half-true")
data.loc[falsev, 'Label'] = 1

truev = (data['Label']=="TRUE") | (data['Label']=="mostly-true")
data.loc[truev, 'Label'] = 0

cv = CountVectorizer()
cv.fit(data['Statement'])
for idx, i in enumerate(data['Statement']):
    newtext = cv.transform([i])
    data['Statement'][idx] = newtext
    
    
#Put Parties into numbers
partydem = (data['Party'] == "democrat")
data.loc[partydem, 'Party'] = 0

partyrep = (data['Party'] == "republican")
data.loc[partyrep, 'Party'] = 1

partyn = (data['Party'] == "none")
data.loc[partyn, 'Party'] = 2

partyother = (data['Party'] == "independent")|(data['Party'] == "organization") | (data['Party'] == "columnist") | (data['Party'] == "newsmaker") | (data['Party'] == "activist") | (data['Party'] == "journalist") | (data['Party'] == "talk-show-host") | (data['Party'] == "state-official") | (data['Party'] == "business-leader") | (data['Party'] == "labor-leader") | (data['Party'] == "government-body") | (data['Party'] == "education-official") | (data['Party'] == "county-commissioner") | (data['Party'] == "libertarian") | (data['Party'] == "democratic-farmer-labor") | (data['Party'] == "green") | (data['Party'] == "liberal-party-canada") | (data['Party'] == "tea-party-member") | (data['Party'] == "ocean-state-tea-party-action") | (data['Party'] == "Moderate") | (data['Party'] == "constitution-party")
data.loc[partyother, 'Party'] = 3


# In[4]:


#Hot encoding speakers to prep

#Democrat President
speakerPresD = (data['Speaker'] == "barack-obama") | (data['Speaker'] == "bill-clinton") | (data['Speaker']=="jimmy-carter")
data.loc[speakerPresD, 'Speaker'] = 0

#Republic President
speakerPresR = (data['Speaker'] == "donald-trump") | (data['Speaker'] == "george-w-bush") 
data.loc[speakerPresR, 'Speaker'] = 1

#Democrat Vice-Pres Speakers
speakerVPD = (data['Speaker'] == "joe-biden") | (data['Speaker'] == "al-gore")
data.loc[speakerVPD, 'Speaker'] = 2

#Republican Vice-Pres Speakers
speakerVPR = (data['Speaker'] == "mike-pence") | (data['Speaker']=="dick-cheney")
data.loc[speakerVPR, 'Speaker'] = 3

#Democrat Speaker of the House
speakerSoHD = (data['Speaker'] == "nancy-pelosi")
data.loc[speakerSoHD, 'Speaker'] = 4

#Republican Speaker of the House
speakerSoHR = (data['Speaker'] == "john-boehner") | (data['Speaker']=="newt-gingrich")
data.loc[speakerSoHR, 'Speaker'] = 5

#Republican Secretaries
speakerSecrtR = (data['Speaker'] == "bill-bennett") | (data['Speaker'] == "ed-gillespie") | (data['Speaker']=="dana-perino")
data.loc[speakerSecrtR, 'Speaker'] = 6

#Democrat Secretaries
speakerSecrtD = (data['Speaker'] == "hillary-clinton") | (data['Speaker'] == "robert-reich") | (data['Speaker']=="gina-raimondo")
data.loc[speakerSecrtD, 'Speaker'] = 7

#Heads of Agencies
speakerHead = (data['Speaker']=="michael-morell")| (data['Speaker']=="bryan-fischer") | (data['Speaker']=="dan-coats")
data.loc[speakerHead, 'Speaker'] = 8

#Democrat Senators
speakerSD = (data['Speaker'] == "sherrod-brown") | (data['Speaker'] == "leonidas-raptakis") | (data['Speaker'] == "bill-nelson") | (data['Speaker']=="chris-cummiskey") | (data['Speaker']=="gina-hinojosa") | (data['Speaker']=="mark-begich") | (data['Speaker']=="barbara-boxer")
data.loc[speakerSD, 'Speaker'] = 9

#Republican Senators
speakerSR = (data['Speaker'] == "rand-paul") | (data['Speaker'] == "kelly-ayotte") | (data['Speaker'] == "james-inhofe") | (data['Speaker'] == "rob-portman") | (data['Speaker'] == "mitt-romney") | (data['Speaker'] == "don-gaetz") | (data['Speaker'] == "marco-rubio") | (data['Speaker'] == "jim-demint") | (data['Speaker']=="jon-kyl") | (data['Speaker']=="joseph-kyrillos") | (data['Speaker']=="randy-forbes") | (data['Speaker']=="john-cornyn") | (data['Speaker']=="lois-kolkhorst")|(data['Speaker']=="howard-marklein")|(data['Speaker']=="ted-cruz")|(data['Speaker']=="john-mccain")|(data['Speaker']=="tom-cotton")|(data['Speaker']=="bill-cassidy")|(data['Speaker']=="ron-johnson")
data.loc[speakerSR, 'Speaker'] = 10
 
#Other Representatives
speakerOtR = (data['Speaker'] == "ron-paul") | (data['Speaker']=="tom-tancredo") | (data['Speaker']=="sam-adams")
data.loc[speakerOtR, 'Speaker'] = 11

#Democrat Representatives
speakerDR = (data['Speaker'] == "charlie-crist") | (data['Speaker'] == "diana-degette") | (data['Speaker'] == "sheryl-cole") | (data['Speaker'] == "nan-rich") | (data['Speaker'] == "mark-pocan") | (data['Speaker'] == "mike-tate") | (data['Speaker']=="katherine-cloonen")
data.loc[speakerDR, 'Speaker'] = 12

#Republican Representatives
speakerRR = (data['Speaker'] == "cw-bill-young") | (data['Speaker'] == "keith-faber") | (data['Speaker'] == "john-duncan") | (data['Speaker'] == "vicky-hartzler") | (data['Speaker'] == "gus-bilirakis") | (data['Speaker'] == "eric-cantor") | (data['Speaker'] == "allen-west") | (data['Speaker']=="scott-desjarlais") | (data['Speaker']=="talmadge-heflin") | (data['Speaker']=="will-weatherford") | (data['Speaker']=="karen-handel") | (data['Speaker']=="joe-straus") | (data['Speaker']=="dennis-hastert") | (data['Speaker']=="josh-mandel")
data.loc[speakerRR, 'Speaker'] = 13

#Republican Governers
speakerGovR = (data['Speaker'] == "jeb-bush") | (data['Speaker'] == "rick-perry") | (data['Speaker'] == "rick-scott") | (data['Speaker'] == "greg-abbott") | (data['Speaker'] == "nathan-deal") | (data['Speaker'] == "scott-walker") | (data['Speaker']=="george-allen") | (data['Speaker']=="tim-pawlenty") | (data['Speaker']=="chris-christie") | (data['Speaker']=="matt-bevin")
data.loc[speakerGovR, 'Speaker'] = 14

# Democrat Governers
speakerGovD = (data['Speaker'] == "roy-barnes") | (data['Speaker'] == "ted-strickland") 
data.loc[speakerGovD, 'Speaker'] = 15

#Republican Lieutenant Governors
speakerLtGovR = (data['Speaker'] == "michael-steele") | (data['Speaker'] == "david-dewhurst")
data.loc[speakerLtGovR, 'Speaker'] = 16

#Republican Mayors
speakerMR = (data['Speaker'] == "allan-fung") 
data.loc[speakerMR, 'Speaker'] = 17

#Democrat Mayors
speakerMD = (data['Speaker'] == "eric-johnson") | (data['Speaker'] == "shirley-franklin") | (data['Speaker']=="jim-kenney")
data.loc[speakerMD, 'Speaker'] =18

#Political Candidates
speakerCA = (data['Speaker']=="jamie-radtke")
data.loc[speakerCA, 'Speaker']=19

#Police
speakerPo = (data['Speaker'] == "grady-judd") | (data['Speaker'] == "broward-county-police-benevolent-association")  
data.loc[speakerPo, 'Speaker'] = 20

#Groups
speakerGroups = (data['Speaker'] == "protect-families-first") |(data['Speaker'] == "nathan-deal-and-roy-barnes") | (data['Speaker'] == "georgia-politicians") | (data['Speaker'] == "miami-seaport-alliance") | (data['Speaker'] == "house-republicans") | (data['Speaker'] == "drug-free-america") | (data['Speaker'] == "national-republican-congressional-committee") | (data['Speaker'] == "oregon-healthy-kids") | (data['Speaker'] == "council-national-interest") | (data['Speaker'] == "club-growth") | (data['Speaker'] == "dustin-inman-society") | (data['Speaker'] == "florida-wildlife-federation") | (data['Speaker'] == "texas-department-transportation") | (data['Speaker'] == "progress-texas") | (data['Speaker'] == "next-generation-climate-action-committee") | (data['Speaker'] == "americans-tax-reform") | (data['Speaker'] == "arizona-house-democrats") | (data['Speaker'] == "american-petroleum-institute") | (data['Speaker'] == "national-republican-senatorial-committee") | (data['Speaker']=="tennessee-democratic-party") | (data['Speaker']=="occupy-democrats")| (data['Speaker']=="republican-national-committee-republican")| (data['Speaker']=="republican-party-virginia")|(data['Speaker']=="lone-star-project")|(data['Speaker']=="oregon-catalyst")|(data['Speaker']=="commonwealth-institute")|(data['Speaker']=="our-oregon")|(data['Speaker']=="afl-cio")|(data['Speaker']=="oregon-education-association") | (data['Speaker']=="conservative-voters-texas-pac")|(data['Speaker']=="dekalb-county")|(data['Speaker']=="hillsborough-area-rapid-transit-hart")|(data['Speaker']=="americans-united-change")|(data['Speaker']=="republican-party-florida")|(data['Speaker']=="national-rifle-association")|(data['Speaker']=="americans-prosperity")|(data['Speaker']=="restore-our-future")|(data['Speaker']=="crossroads-gps")|(data['Speaker']=="us-chamber-commerce")|(data['Speaker']=="freedom-partners")|(data['Speaker']=="american-action-network")|(data['Speaker']=="its-still-bad-idea")|(data['Speaker']=="patriot-majority-usa")|(data['Speaker']=="priorities-usa-action")|(data['Speaker']=="60-plus-association")
data.loc[speakerGroups, 'Speaker'] = 21

#Laywers/Judges
speakerDA = (data['Speaker'] == "jana-duty") | (data['Speaker'] == "jonathan-turley") | (data['Speaker'] == "pam-bondi") | (data['Speaker'] == "joshua-marquis") | (data['Speaker'] == "pete-gallego") | (data['Speaker']=="ari-melber") | (data['Speaker']=="ralph-reed") | (data['Speaker']=="jb-van-hollen") | (data['Speaker']=="jeanine-pirro")
data.loc[speakerDA, 'Speaker'] = 22

#Activist 
speakerA = (data['Speaker'] == "desmond-meade") | (data['Speaker'] == "michael-moore") | (data['Speaker'] == "marjorie-dannenfelser") | (data['Speaker'] == "hemant-mehta") | (data['Speaker'] == "scot-ross") | (data['Speaker']=="ed-garvey") | (data['Speaker']=="al-sharpton") | (data['Speaker']=="deirdre-imus")
data.loc[speakerA, 'Speaker'] = 23

#Talk Hosts
speakerTH = (data['Speaker'] == "glenn-beck") | (data['Speaker'] == "lars-larson") | (data['Speaker'] == "rick-santorum") | (data['Speaker'] == "bill-maher") | (data['Speaker'] == "michelle-malkin") | (data['Speaker']=="al-roker") | (data['Speaker']=="neil-cavuto") | (data['Speaker']=="tucker-carlson") | (data['Speaker']=="brian-kilmeade") | (data['Speaker']=="steve-doocy") | (data['Speaker']=="chris-wallace") | (data['Speaker']=="sean-hannity") | (data['Speaker']=="chris-matthews") | (data['Speaker']=="lou-dobbs") | (data['Speaker']=="harris-faulkner")  | (data['Speaker']=="jon-stewart") | (data['Speaker']=="trevor-noah") | (data['Speaker']=="ed-schultz") | (data['Speaker']=="kimberly-guilfoyle") | (data['Speaker']=="bob-beckel") | (data['Speaker']=="eric-bolling") | (data['Speaker']=="lawrence-odonnell") | (data['Speaker']=="bill-oreilly") | (data['Speaker']=="laura-ingraham") | (data['Speaker']=="ann-coulter") | (data['Speaker']=="john-oliver") | (data['Speaker']=="joe-scarborough") | (data['Speaker']=="rachel-maddow") | (data['Speaker']=="jose-diaz-balart") | (data['Speaker']=="jay-leno") | (data['Speaker']=="charlie-sykes")
data.loc[speakerTH, 'Speaker'] = 24

#Journalists
speakerJ = (data['Speaker'] == "paul-krugman") | (data['Speaker'] == "gretchen-carlson") | (data['Speaker'] == "kai-ryssdal") | (data['Speaker'] == "hunter-schwarz") | (data['Speaker'] == "george-will") | (data['Speaker'] == "charles-krauthammer") | (data['Speaker'] == "judson-phillips") | (data['Speaker'] == "joel-keehn") | (data['Speaker'] == "chuck-donovan") | (data['Speaker'] == "scott-keyes") | (data['Speaker']=="michael-rosen") | (data['Speaker']=="brit-hume") | (data['Speaker']=="andrew-napolitano") | (data['Speaker']=="nicholas-kristof") | (data['Speaker']=="juan-williams") | (data['Speaker']=="megyn-kelly") | (data['Speaker']=="katrina-vanden-heuvel") | (data['Speaker']=="peggy-noonan") | (data['Speaker']=="pierre-thomas") | (data['Speaker']=="david-madland") | (data['Speaker']=="jake-tapper") | (data['Speaker']=="glenn-greenwald") | (data['Speaker']=="marc-thiessen") | (data['Speaker']=="jess-mcintosh") | (data['Speaker']=="andrea-mitchell") | (data['Speaker']=="dana-milbank") | (data['Speaker']=="chuck-todd") | (data['Speaker']=="rich-lowry") | (data['Speaker']=="mark-shields") | (data['Speaker']=="jorge-ramos")
data.loc[speakerJ, 'Speaker'] = 25

#Business Leaders
speakerBus=(data['Speaker'] == "arianna-huffington") | (data['Speaker'] == "warren-buffett") | (data['Speaker'] == "charles-koch") | (data['Speaker'] == "john-robitaille") | (data['Speaker'] == "herman-cain") | (data['Speaker'] == "eric-hovde") | (data['Speaker']=="carly-fiorina") 
data.loc[speakerBus, 'Speaker'] = 26

#Experts
speakerE = (data['Speaker'] == "ezekiel-emanuel") | (data['Speaker'] == "hugh-fitzsimons") | (data['Speaker']=="steven-schale") | (data['Speaker']=="james-capretta") | (data['Speaker']=="michael-eric-dyson") | (data['Speaker']=="james-carville") | (data['Speaker']=="donna-brazile")
data.loc[speakerE, 'Speaker'] = 27

#Anonomyus Speakers/People
speakerAnon = (data['Speaker'] == "chain-email") | (data['Speaker'] == "billboard") | (data['Speaker'] == "billboard-spaghetti-junction") | (data['Speaker'] == "menendez-facts") | (data['Speaker'] == "rick-scotts-starbucks-heckler") | (data['Speaker']=="john-charles") | (data['Speaker']=="cq-press-city-crime-rankings-2010-2011") | (data['Speaker']=="wayne-rogers") | (data['Speaker']=="anonymous-activist") | (data['Speaker']=="vance-smith")
data.loc[speakerAnon, 'Speaker'] = 28

#Social Media Posts
speakerSocial = (data['Speaker'] == "tweets") | (data['Speaker'] == "blog-posting") | (data['Speaker'] == "viral-media-reports") | (data['Speaker'] == "liberal-blogger") | (data['Speaker'] == "liberal-bloggers") | (data['Speaker'] == "viral-image") | (data['Speaker'] == "facebook-posts") | (data['Speaker'] == "forbes-blog") | (data['Speaker']=="jon-obrien")
data.loc[speakerSocial, 'Speaker'] = 29

#Movie
speakerMo = (data['Speaker'] == "mr-conservative")
data.loc[speakerMo, 'Speaker'] = 30

#Radio Hosts
speakerRH = (data['Speaker'] == "chuck-baldwin") | (data['Speaker'] == "erick-erickson") | (data['Speaker']=="gavin-mcinnes") | (data['Speaker']=="thom-hartmann") | (data['Speaker']=="rush-limbaugh") | (data['Speaker']=="bob-kincaid") | (data['Speaker']=="dean-obeidallah")
data.loc[speakerRH, 'Speaker'] = 31

#Website
speakerWeb = (data['Speaker'] == "emilys-list") | (data['Speaker']=="burnt-orange-report")
data.loc[speakerWeb, 'Speaker'] = 32


# In[5]:


#news articles
ContextArt=(data['Context']==' as quoted in Austin American-Statesman news article.')|(data['Context']=='a newspaper article')|(data['Context']=='a newspaper article.')|(data['Context']=='a newspaper column')|(data['Context']=='a newspaper column.')|(data['Context']=='a newspaper commentary')|(data['Context']=='a newspaper editorial')|(data['Context']=='a newspaper interview')|(data['Context']=='a newspaper interview.')|(data['Context']=='a newspaper Op/Ed')|(data['Context']=='a newspaper op-ed')|(data['Context']=='a newspaper opinion piece')|(data['Context']=='a newspaper Q&A')|(data['Context']=='a newspaper story')|(data['Context']=='')|(data['Context']=='')
data.loc[ContextArt, 'Context'] = 0

#meetings
contextMeet = (data['Context'] == ' a meeting of Florida Republicans') | (data['Context'] == ' a meeting with business leaders in Portsmouth, N.H.')|(data['Context']==' an editorial board meeting')|(data['Context']=='')
data.loc[contextMeet, 'Context'] = 1

#news shows
contextShow = (data['Context'] == ' "This Week with Christiane Amanpour"')|(data['Context']==" CNN's 'The Situation Room'")|(data['Context']==" CNN's State of the Union with John King")|(data['Context']==" the 'Rachel Maddow Show'")|(data['Context']==" This Week with George Stephanopoulos")|(data['Context']=='a "60 Minutes" interview')|(data['Context']=='a "Face the Nation" interview')|(data['Context']=='a "Face the Nation"Â interview')|(data['Context']=='a "Good Morning America" town hall')|(data['Context']=='a '"Gretchen's Take"' on The Real Story')|(data['Context']=='a "Marketplace" segment')|(data['Context']=='a "Meet the Press" interview')|(data['Context']=='a "Meet the Press" pundit panel')|(data['Context']=='a "Real Time with Bill Maher" episode')|(data['Context']=='a "Today Show" interview')|(data['Context']=='')
data.loc[contextShow, 'Context'] = 2

#news release
contextNewsR = (data['Context'] == ' a news release') | (data['Context'] == ' A news release') | (data['Context'] == "a news release.") | (data['Context'] == "a news release about Florida's tourism statistics") | (data['Context'] == "a news release about tax reform") | (data['Context'] == "a news release announcing her candidacy") | (data['Context'] == "") | (data['Context'] == "") | (data['Context'] == "") | (data['Context'] == "") | (data['Context'] == "")
data.loc [contextNewsR, 'Context'] = 3

#Speeches
contextSpeech = (data['Context'] == ' a speech')|(data['Context']=='')
data.loc[contextSpeech, 'Context'] = 4

#Web
contextWeb = (data['Context']==' a Webcast')|(data['Context']=='a "Ballot Boxing" candidate forum')|(data['Context']=='')|(data['Context']=='')
data.loc[contextWeb, 'Context'] = 5

#Social Media
contextSocial = (data['Context']==' social media and in print')|(data['Context']=='a "BloggingBlackMiami" blog post')|(data['Context']=='')
data.loc[contextSocial, 'Context'] = 6

#Conferences
contextConference = (data['Context']==' a White House news conference')|(data['Context']==' Conference call with reporters')|(data['Context']=='a conference call')|(data['Context']=='a conference call.')|(data['Context']=='a conference.')|(data['Context']=='')|(data['Context']=='')|(data['Context']=='')|(data['Context']=='')
data.loc[contextConference, 'Context']=7

#Apperances
contextApper=(data['Context']==' an appearance at Franklin Pierce University in Rindge, N.H.')|(data['Context']==' an appearance on CNN "State of the Union"')|(data['Context']=='')
data.loc[contextApper, 'Context']=8

#Email
contextE=(data['Context']==' an email')|(data['Context']==' e-mail and blog postings')|(data['Context']=='a chain e-mail')|(data['Context']=='a chain e-mail sent to many people.')|(data['Context']=='a chain e-mail based on an article written by Dick Morris')|(data['Context']=='a chain email forwarded by readers')|(data['Context']=='a chain email forwarded by an Austin American-Statesman reader.')|(data['Context']=='a chain email forwarded by a reader.')|(data['Context']=='')|(data['Context']=='')|(data['Context']=='')
data.loc[contextE, 'Context']=9

#Interview
contextInterview=(data['Context']==' an interview on CNN')|(data['Context']=='a "Florida Face to Face" interview')|(data['Context']=='a "Fox and Friends" interview')|(data['Context']=='a "Fox News Sunday" interview')|(data['Context']=='')
data.loc[contextInterview,'Context']=10

#Campaigns
contextCamp=(data['Context']==' announcing his campaign for secretary of state')|(data['Context']==' political campaign')|(data['Context']=='')
data.loc[contextCamp, 'Context']=11

#Debates
contextDe=(data['Context']==' in the 2016 vice presidential debate')|(data['Context']==' in the Fox News Google debate in Orlando')|(data['Context']=='')
data.loc[contextDe, 'Context']=12

#Newspapers
contextNP=(data['Context']==" Washington Report newsletter to constituents.")|(data['Context']=='a "Miami Herald" newspaper ad')|(data['Context']=='a "myth and fact" news release')|(data['Context']=='a "New York Times" column')|(data['Context']=='a "New York Times" op-ed')|(data['Context']=='a "Sun-Sentinel" editorial')|(data['Context']=='a "Tampa Bay Times" editorial board interview')|(data['Context']=='a "Tampa Bay Times" op-ed')|(data['Context']=='a "Tampa Tribune" blog')|(data['Context']=='a "Wall Street Journal" op-ed')|(data['Context']=='a "Wall Street Journal"Â op-ed')|(data['Context']=='a "Washington Post" article')|(data['Context']=='a "Washington Post" column')|(data['Context']=='a newspaper ad')|(data['Context']=='a newspaper ad.')|(data['Context']=='a newspaper advertisement')|(data['Context']=='')|(data['Context']=='')|(data['Context']=='')|(data['Context']=='')|(data['Context']=='')|(data['Context']=='')
data.loc[contextNP, 'Context']=13

#Books
contextB=(data['Context']=="")|(data['Context']=="")|(data['Context']=="")
data.loc[contextB, 'Context']=14

#Remarks
contextR=(data['Context']==" remarks at a General Assembly session")|(data['Context']==" remarks at the Republican National Convention in Tampa")|(data['Context']=="")
data.loc[contextR, 'Context']=15

#Bills/Laws/Vetos
contextV=(data['Context']=="2013-14 veto message")|(data['Context']=="")|(data['Context']=="")
data.loc[contextB, 'Context']=15


# In[8]:


subjectlist = set()
for i in data['Subject']:
    subjectlist.update(i.split(','))
    
subjectlist = list(subjectlist)
subjectlist.sort()

for idx, i in enumerate(data['Subject']):
    subjects = []
    for j in subjectlist:
        if j in i:
            subjects.append('1')
        else:
            subjects.append('0')
    num = "".join(subjects)
    data['Subject'][idx] = int(num,2)


# In[18]:


from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import learning_curve,  GridSearchCV
from sklearn.metrics import precision_recall_curve, average_precision_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.datasets import make_moons
from sklearn.calibration import CalibratedClassifierCV


# In[19]:


train, temp = train_test_split(data,test_size=0.5,random_state=1)
valid, test = train_test_split(temp, test_size=0.4, random_state=1)
print('Training:', train.shape)
print('Validation:', valid.shape)
print('Test:', test.shape)


# In[23]:


X_train = train[['Statement', 'Subject', 'Speaker', 'Party',
       'Barely True Counts', 'False Counts', 'Half True Counts',
       'Mostly True Counts', 'Pants on Fire', 'Context']]
y_train = train['Label']
X_test = test[['Statement', 'Subject', 'Speaker', 'Party',
       'Barely True Counts', 'False Counts', 'Half True Counts',
       'Mostly True Counts', 'Pants on Fire', 'Context']]
y_test = test['Label']


# In[20]:


X, y = make_moons()
calibrated_forest = CalibratedClassifierCV(
    base_estimator=RandomForestClassifier(n_estimators=10))
param_grid = {
    'base_estimator__max_depth': [2, 4, 6, 8]}
search = GridSearchCV(calibrated_forest, param_grid, cv=5)
search.fit(X, y)
GridSearchCV(cv=5,
             estimator=CalibratedClassifierCV(...),
             param_grid={'base_estimator__max_depth': [2, 4, 6, 8]})


# In[25]:


# Random Forest
random_forest = RandomForestClassifier(criterion = "gini", 
                                       min_samples_leaf = 1, 
                                       min_samples_split = 10,   
                                       n_estimators=100, 
                                       max_features='auto', 
                                       oob_score=True, 
                                       random_state=1, 
                                       n_jobs=-1)

random_forest.fit(X_train, y_train)
Y_prediction = random_forest.predict(X_test)

random_forest.score(Y_prediction, y_test)

print("oob score:", round(random_forest.oob_score_, 4)*100, "%")


# In[ ]:




