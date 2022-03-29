from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pandas as pd
import plotly.express as px
import streamlit as st

class WebText:
    def __init__(self, driver = None):
        self.driver = driver
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--window-size=1920x1080')
        if self.driver == None:
            self.driver = webdriver.Chrome(
                options = self.options,
                desired_capabilities = DesiredCapabilities.CHROME.copy(),
                service = Service(ChromeDriverManager().install()))
    def get_url(self, url):
        self.url = url
        if not self.url.startswith('https://'):
            url = f'https://{url}'
        self.driver.get(self.url)

    def process_text(self):
        html = self.driver.find_element(By.TAG_NAME, 'html')
        #A página deve estar no idioma português
        if html.get_attribute('lang') not in ['pt', 'PT', 'pt-BR', 'pt_BR', 'pt-br', 'pt_br', 'PT-BR', 'PT_BR', 'PT-br', 'PT_br']:
            print('A página não está em português.')
        else:
            #Obtém o texto da página inteira
            text = html.text
            #Retira as quebras de linha (\n)
            text = text.replace('\\n', '')
            #Usa Regex para pegar apenas termos que possuam letras e números
            tokenizer = RegexpTokenizer('\w+')
            tokens = tokenizer.tokenize(text)
            #letras minúsculas e remoção de números
            tokens = [word.lower() for word in tokens if not word.isdigit()]
            #remoção de stopwords
            sw = stopwords.words('portuguese')
            tokens = [word for word in tokens if word not in sw]
            return tokens

    def word_count(self):
        #Exibição final dos dados obtidos
        tokens = self.process_text()
        df = pd.DataFrame(tokens).rename(columns = {0: 'termos'})
        value_counts = df.value_counts().reset_index().rename(columns = {0: 'contagem'})[:20]
        fig = px.bar(value_counts, x = 'termos', y = 'contagem', color = 'termos', title = 'Os 20 termos que mais aparecem na página')
        st.plotly_chart(fig)
        #fig.show()
    
    def page_screenshot(self):
        image = self.driver.get_screenshot_as_png()
        st.image(image, caption = 'Screenshot da página')

    def page(self):
        st.title('Termos mais citados em uma página web')
        st.write('_Autor: Rafael Silva Coelho_')
        st.write(
            """O intuito desta aplicação é usar recursos básicos de NLP (processamento de texto) e web scraping para
            obter os termos que são mais citados em uma página web qualquer que esteja no idioma português""")
        url = st.text_input("URL", value = "https://pt.wikipedia.org/wiki/Hist%C3%B3ria_da_Wikip%C3%A9dia")
        st.caption("De preferência, coloque a URL começando com https://")
        if url is not None:
            self.get_url(url)
            self.process_text()
            self.page_screenshot()
            self.word_count()

webtext = WebText()
webtext.page()
webtext.driver.quit()