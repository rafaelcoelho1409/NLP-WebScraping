# Processamento de Linguagem Natural (NLP Básico) & Web Scraping

## Objetivo
Obter os termos mais citados em uma página HTML usando Web Scraping e NLP para processamento de texto.  
O projeto consiste em coletar textos de sites em português, usar NLP para tratamento dos dados de texto e coletar os termos que são mais citados dentro do texto obtido.  
O projeto possui dois arquivos principais:
- nlp.py: A aplicação construída é voltada para funcionar com o Streamlit
- nlp.ipynb: Uma versão mais genérica do projeto dentro de um Jupyter Notebook

## Recursos utilizados
- Visual Studio Code
- python3.9
- virtualenv
- pip3: gerenciador de pacotes python3.x

## Pacotes do Python
- selenium (Selenium Webdriver)
- webdriver_manager (Webdriver Manager)
- nltk (NLTK: Natural Language Toolkit)
- pandas
- plotly
- streamlit

## Screenshots do projeto construído
<img src="screenshot01.png" />
<img src="screenshot02.png" />

## Para executar esse repositório localmente em sua máquina
- baixe esse repositório em sua máquina:
> git clone https://github.com/rafaelcoelho1409/NLP-WebScraping.git
- instale os pacotes necessários que estão no arquivo requirements.txt:
> pip3 install -r requirements.txt
- escolha seu interpretador python (python3, python3.x)  
- execute os seguintes comandos (para Linux):
> cd NLP-WebScraping  
> streamlit run nlp.py
- Com esses comandos, a página será aberta automaticamente. Caso não abra, vá até seu navegador e digite:
> http://localhost:8501  