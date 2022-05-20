# Natural Language Processing (NLP) & Web Scraping

## Purpose
Obtain the most mentioned terms in an HTML page using Web Scraping and NLP.  
The project consists in collecting texts from Portuguese websites, use NLP for text processing and collecting the most mentioned terms into the obtained text.  
This project have two main files:
- nlp.py: This application is builded with Streamlit
- nlp.ipynb: A generic version of this project into a Jupyter Notebook

## Resources
- Visual Studio Code
- python3.9
- virtualenv
- pip3: python3.x packages manager

## Python packages
- selenium (Selenium Webdriver)
- webdriver_manager (Webdriver Manager)
- nltk (NLTK: Natural Language Toolkit)
- pandas
- plotly
- streamlit

## Screenshots
<img src="screenshot01.png" />
<img src="screenshot02.png" />

## Running this repo in your local machine
- clone this repo:  
> git clone https://github.com/rafaelcoelho1409/NLP-WebScraping.git
- install required packages that are in 'requirements.txt' file:
> pip3 install -r requirements.txt
- choose your Python interpreter (python3.x)  
- run the following commands (for Linux):
> cd NLP-WebScraping  
> streamlit run nlp.py
- With these commands, a web page will be opened automatically. In the case it doesn't open, go to the browser and type:
> http://localhost:8501  
