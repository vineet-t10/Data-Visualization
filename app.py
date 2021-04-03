import streamlit as st
import numpy as np
import pandas as pd
import os
import streamlit.components.v1 as stc
from fpdf import FPDF
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.models import ColumnDataSource
from bokeh.embed import components
from bokeh.palettes import Spectral5
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression


def main():
	st.title("Student Data Analysis")
	menu = ["Home","Job Prediction with Scores","Resume Generator","Student Score Prediction"]
	choice = st.sidebar.selectbox("Menu",menu)
	

	if choice == "Home":
		st.subheader("Home")
		st.header("Job Search Engine")
		job_field=st.text_input("Enter your Job Field:")
		job_location=st.text_input("Enter Job Location")
		if st.button('Linkedin'):
			PATH="/home/kali/Desktop/Streamlit/chromedriver"
			driver=webdriver.Chrome(PATH)
			driver.get("https://in.linkedin.com/jobs/search?keywords=&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0")
			search=driver.find_element_by_name("keywords")
			search1=driver.find_element_by_name("location")
			search.send_keys(job_field)
			search1.clear();
			search1.send_keys(job_location)
			search.send_keys(Keys.RETURN)
			time.sleep(25) 
		elif st.button('Indeed'):
			PATH="/home/kali/Desktop/Streamlit/chromedriver"
			driver=webdriver.Chrome(PATH)
			driver.get("https://in.indeed.com/?sq=1")
			search=driver.find_element_by_name("q")
			search1=driver.find_element_by_name("l")
			search.send_keys(job_field)
			search1.clear();
			search1.send_keys(job_location)
			search.send_keys(Keys.RETURN)
			time.sleep(25) 
			#search
			


	if choice == "Job Prediction with Scores":
		st.subheader("Job Prediction with Scores")
		
		data_file = st.file_uploader("Upload CSV",type=['csv','xslx'])
		if st.button("Process"):
			if data_file is not None:
				
				df = pd.read_csv(data_file)
				subject_data=df["Subject"]
				marks_data=df["Marks"]
				explode=(marks_data==max(marks_data))
				fig, ax = plt.subplots()
				ax.pie(marks_data, labels=subject_data, explode=explode,shadow=True,autopct='%1.1f%%', startangle=45)
				st.title("Student Data Analysis")
				st.pyplot(fig)

	if choice == "Resume Generator":
		st.subheader("Resume Generator")
		def createfunc(fname,lname,email,address,contact,portfolio,LinkedIn,profession,field,subfield,qualification,degree,skills,age,projects,AdditionalSkills,Extracurricular,Certificates,achievement,Hobbies,tagline):
		  pdf=FPDF()
		  pdf.add_page()
		  pdf.set_draw_color(176,224,230)
		  pdf.set_font("Arial",'B',size=14)
		  name=fname+" "+lname 
		  info=email+" | "+contact
		  pdf.cell(200,20,txt=name,ln=2,align='L')

		  pdf.set_font("Arial",size=12)
		  pdf.cell(200,10,txt=info,ln=2,align='L')
		  pdf.cell(200,10,txt=address,ln=2,align='L')
		  pdf.cell(200,10,txt=portfolio,ln=2,align='L',link=portfolio)
		  pdf.cell(200,10,txt=LinkedIn,ln=2,align='L',link=LinkedIn)
		  pdf.set_line_width(3)

		  pdf.line(10,72,200,72)
		  pdf.set_line_width(0.3)
		  pdf.set_font("Arial",'B',size=14)
		  pdf.cell(190,25,txt="Objective",border='B',ln=2,align='L')
		 

		  pdf.set_font("Arial",size=12)
		  pdf.multi_cell(190,10,txt=tagline)

		  pdf.set_font("Arial",'B',size=14)
		  pdf.cell(190,10,txt="Education",border='B',ln=2,align='L')


		  pdf.set_font("Arial",size=12)
		  pdf.cell(200,10,txt=field+" - "+degree,ln=2)

		  pdf.set_font("Arial",'B',size=14)
		  pdf.cell(190,10,txt="Skills",border='B',ln=2,align='L')


		  pdf.set_font("Arial",size=12)
		  sk=len(skills)
		  for i in range(sk):
		    pdf.multi_cell(200,10,txt=chr(149)+" "+skills[i])

		  pdf.set_font("Arial",'B',size=14)
		  pdf.cell(190,10,txt="Projects",ln=2,border='B',align='L')
		  pdf.set_font("Arial",size=12)
		  pdf.multi_cell(200,10,txt=projects)

		  pdf.set_font("Arial",'B',size=14)
		  pdf.cell(190,10,txt="Additional Skills",border='B',ln=2,align='L')
		  pdf.set_font("Arial",size=12)
		  pdf.multi_cell(200,10,txt=Additionalskills)
		    
		  pdf.set_font("Arial",'B',size=14)
		  pdf.cell(190,10,txt="Extracurricular and Academic Activities",border='B',ln=2,align='L')
		  pdf.set_font("Arial",size=12)
		  pdf.multi_cell(200,10,txt=Extracurricular)
		  

		  pdf.set_font("Arial",'B',size=14)
		  pdf.cell(190,10,txt="Certifications",border='B',ln=2,align='L')
		  pdf.set_font("Arial",size=12)
		  pdf.multi_cell(200,10,txt=Certificates)
		 

		  pdf.set_font("Arial",'B',size=14)
		  pdf.cell(190,10,txt="Hobbies",border='B',ln=2,align='L')
		  pdf.set_font("Arial",size=12)
		  pdf.multi_cell(200,10,txt=Hobbies)
		  

		  pdf.set_font("Arial",size=12)
		  pdf.cell(200,20,txt="I hereby declare that all the details given are true to the best of my knowledge and belief.",ln=2,align='L')
		  pdf.cell(200,25,txt=name,ln=2,align='L')
		  
		  pdf.output("Resume.pdf",dest='F').encode('utf-8')
		  



		st.header("Create your own Resume")
		st.markdown("---")
		fname=st.text_input("First Name:")
		lname=st.text_input("Last Name:")
		email=st.text_input("Email Address:")
		address=st.text_input("Address:")
		contact=st.text_input("Contact Number:")
		portfolio=st.text_input("Portfolio Link(if available):")
		LinkedIn=st.text_input("LinkedIn link:")
		profession=st.radio("Are you a Student or an Employee?",["Student","Employee"])

		if profession=="Student":
		  field=st.selectbox("Your Field:",["Science","Commerce","Arts","Medicine"])
		  if field=="Science":
		    subfield=st.selectbox("Subfield:",["Computer Science","IT","Biology","Maths"])
		    qualification=st.selectbox("Qualification:",["Diploma","Associate","Bachelor","Master","Doctorate"])
		    if qualification=="Diploma":
		      degree=st.selectbox("Degree:",["Diploma in Science"])
		    elif qualification=="Associate":
		      degree=st.selectbox("Degree:",["IT"])
		    elif qualification=="Bachelor":
		      degree=st.selectbox("Degree:",["Bachelor of Computer Science","Bachelor of IT","Bachelor of MicroBiology","Bachelor of Maths"])
		    elif qualification=="Master":
		      degree=st.selectbox("Degree:",["Master of Computer Science","Master of IT","Master of MicroBiology","Master of Maths"])
		    else:
		      degree=st.selectbox("Degree:",["PhD","Masters(Honours)"])
		    profession=st.radio("Do you want to add another field?",["Yes","No"])
		    skills=st.multiselect("What are your skills?",["AutoCAD","Java","C","C++","Python","DBMS","Web Designing","Graphic Designing","Tekla","Catia","Drawing","Fabrication","CNC coding","CNC operation"])
		  elif field=="Commerce":
		    qualification=st.selectbox("Qualification:",["Bachelor","Master","Doctorate"])
		  elif field=="Arts":
		    qualification=st.selectbox("Qualification:",["Diploma","Bachelor","Master","Doctorate"])
		  else:
		    qualification=st.selectbox("Qualification:",["Diploma","Bachelor","Master","Doctorate"])
		  age=st.date_input("Birth Date:")
		  projects=st.text_area("Projects:")
		  Additionalskills=st.text_area("Additional Skills:")
		  Extracurricular=st.text_area("Extracurricular Activities:")
		  Certificates=st.text_area("Certifications(Provide a line about the achievement):")
		  achievement=st.text_area("Professional Achievements/Experience:")
		  Hobbies=st.text_area("Hobbies:")
		  tagline=st.text_area("Objective:")

		  
		  if st.button("Create Resume!"):
		    with st.spinner("Creating Resume..."):
		      createfunc(fname,lname,email,address,contact,portfolio,LinkedIn,profession,field,subfield,qualification,degree,skills,age,projects,Additionalskills,Extracurricular,Certificates,achievement,Hobbies,tagline)
		      time.sleep(3)
		    st.success("Resume Created!")
		    
		    
		else:
		  field=st.selectbox("Field of Profession:",["Engineering","IT","Commerce","Arts","Medicine"])
		  if field=="Engineering":
		    subfield=st.selectbox("Subfield:",["Mechanical Engineer","Automobile Engineer","Civil Engineer","Electrical Engineer"])
		    qualification=st.selectbox("Qualification:",["Diploma","Associate","Bachelor","Master","Doctorate"])
		    if qualification=="Diploma":
		      degree=st.selectbox("Degree:",["Diploma in Engineering","Diploma in Engineering(Sandwich)"])
		    elif qualification=="Associate":
		      degree=st.selectbox("Degree:",["ITI"])
		    elif qualification=="Bachelor":
		      degree=st.selectbox("Degree:",["Bachelor of Engineering","Bachelor of Technology"])
		    elif qualification=="Master":
		      degree=st.selectbox("Degree:",["Master of Engineering","Master of Technology","M.Phil","PGD"])
		    else:
		      degree=st.selectbox("Degree:",["PhD","Masters(Honours)"])
		    experience=st.slider("Experience:",0,15)
		  elif field=="IT":
		    qualification=st.selectbox("Qualification:",["Self-Learned","Diploma","Bachelor","Master","Doctorate"])
		    if qualification=="Self-Learned":
		      degree=st.selectbox("Degree:",["Bootcamp","Online Certifications","Professional Courses"])
		    elif qualification=="Diploma":
		      degree=st.selectbox("Degree:",["Diploma in Engineering","Diploma in IT"])
		    elif qualification=="Bachelor":
		      degree=st.selectbox("Degree:",["BSC in IT","BCA","BCS","Bachelor of Engineering","Bachelor of Technology"])
		    elif qualification=="Master":
		      degree=st.selectbox("Degree:",["MSC in IT","MCA","MCS","MBA in IT","Master of Engineering","Master of Technology","M.Phil","PGD"])
		    else:
		      degree=st.selectbox("Degree:",["PhD","Masters(Honours)"])
		    experience=st.slider("Experience:",0,15)
		  elif field=="Commerce":
		    qualification=st.selectbox("Qualification:",["Bachelor","Master","Doctorate"])
		    experience=st.slider("Experience:",0,15)
		  elif field=="Arts":
		    qualification=st.selectbox("Qualification:",["Diploma","Bachelor","Master","Doctorate"])
		    experience=st.slider("Experience:",0,15)
		  else:
		    qualification=st.selectbox("Qualification:",["Diploma","Bachelor","Master","Doctorate"])
		    experience=st.slider("Experience:",0,15)
		  age=st.date_input("Birth Date:")
		  Additionalskills=st.text_area("Additional Skills:")
		  Extracurricular=st.text_area("Extracurricular Activities:")
		  Hobbies=st.text_area("Hobbies:")
		  st.button("Create Resume!")
					
	if choice == "Student Score Prediction":
		st.header('Student Score Prediction with number of Hours')
		st.subheader('Present DataSet')
		data_file = st.file_uploader("Upload CSV",type=['csv','xslx'])
		if st.button("Process"):
			if data_file is not None:
				df = pd.read_csv(data_file)
				st.subheader('The Dataet is')
				st.write(df)

				#No of columns
				st.subheader('Number of Columns present in DataSet')
				df.columns


				#Page Columns
				col1, col2 = st.beta_columns(2)


				#Descriptive Statistic Analysis of Score
				col1.subheader('Descriptive Statistic Analysis of Scores')
				score_dc=df['scores'].describe()
				col1.write(score_dc)


				#Descriptive Statistic Analysis of Hours
				col2.subheader('Descriptive Statistic Analysis of Hours')
				score_dc=df['hours'].describe()
				col2.write(score_dc)


				#Distribution Plot of Scores
				fig, ax = plt.subplots(figsize=(15,10))
				st.header('Distribution Plot of Scores')
				ax=sns.distplot(df['scores'])
				st.pyplot(fig)


				#RegressionPlot
				fig1, ax1 = plt.subplots(figsize=(15,10))
				st.header('Regression Plot')
				ax1=sns.regplot(x="hours", y="scores", data=df)
				st.pyplot(fig1)


				#Regression
				X=(df['hours'].values).reshape(-1,1)
				Y=(df['scores'].values).reshape(-1,1)
				X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.30, random_state=0)

				regressor=LinearRegression()
				regressor.fit(X_train,Y_train)

				Y_pred=regressor.predict(X_test)

				st.title('Actual Score VS Predicted Score')
				st.header('Comparing Actual Values VS Predicted Values')
				df1=pd.DataFrame({'Actual Score':[Y_test], 'Predicted_Score':[Y_pred]})
				st.write(df1)

				fig3, ax3 = plt.subplots(figsize=(15,10))
				st.header('Visualizaing Actual Score VS Predicted Score')
				ax3=plt.scatter(X_train,Y_train, color='blue')
				ax4=plt.plot(X_train, regressor.predict(X_train),color='green')
				plt.xlabel('Hours')
				plt.ylabel('Scores')
				st.pyplot(fig3)


main()

