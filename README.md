<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# MarketMoodAI

Final project for the Building AI course

## Summary

MarketMoodAI is an AI-powered financial news sentiment analysis system that classifies financial headlines as positive, negative, or neutral to estimate potential market impact. The project applies natural language processing and supervised machine learning techniques.  
Building AI course project.


## Background

Financial markets react quickly to news releases, earnings reports, geopolitical developments, and macroeconomic data. Investors must interpret large volumes of financial text daily, which creates information overload and subjective bias.

This project aims to address the following problems:

* Information overload in financial media  
* Subjective interpretation of market news  
* Difficulty in quantifying qualitative financial information  
* Limited access to AI-based analysis tools for individual investors  

My motivation is to explore how artificial intelligence can transform unstructured financial text into structured analytical signals. Sentiment analysis plays an important role in algorithmic trading, risk monitoring, and market research. This topic is both academically and practically important.


## How is it used?

The system takes financial news headlines or article text as input and classifies them into sentiment categories:

- Positive  
- Negative  
- Neutral  

The solution can be used in financial research environments, portfolio monitoring, trading strategy development, or academic experimentation.

Typical workflow:

1. Collect a labeled financial news dataset  
2. Preprocess text (cleaning, tokenization, normalization)  
3. Convert text into numerical features (TF-IDF)  
4. Train a supervised machine learning model  
5. Evaluate performance  
6. Predict sentiment for new financial headlines  

Images will make your README look nice!
Once you upload an image to your repository, you can link to it like this (replace the URL with file path, if you've uploaded an image to Github.)

![AI Sentiment](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Artificial_Intelligence_%26_AI_%26_Machine_Learning_-_30212411048.jpg/640px-Artificial_Intelligence_%26_AI_%26_Machine_Learning_-_30212411048.jpg)

If you need to resize images, you have to use an HTML tag, like this:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Artificial_Intelligence_%26_AI_%26_Machine_Learning_-_30212411048.jpg/640px-Artificial_Intelligence_%26_AI_%26_Machine_Learning_-_30212411048.jpg" width="300">

This is how you create code examples:

## Data sources and AI methods

Where does your data come from? Do you collect it yourself or do you use data collected by someone else?

The dataset will consist of publicly available financial news datasets. Possible sources include open datasets from Kaggle and publicly available financial headline collections.

If you need to use links, here's an example:
[https://www.kaggle.com](https://www.kaggle.com)

AI methods used in the project:

| Method | Description |
| ----------- | ----------- |
| Text preprocessing | Cleaning, normalization and tokenization |
| TF-IDF vectorization | Converting text into numerical features |
| Logistic Regression | Supervised classification model |
| Model evaluation | Accuracy, precision, recall metrics |


## Challenges

This project does not directly predict stock prices or guarantee investment performance. It only analyzes textual sentiment.

Limitations include:

* Financial language complexity and sarcasm  
* Dataset bias and labeling quality  
* Market reaction may not align with textual sentiment  
* Risk of overfitting with small datasets  

Ethical considerations:

* The model should not be used as sole financial advice  
* Transparency about model limitations is necessary  
* Responsible use of publicly available data  


## What next?

The project can be extended by:

* Integrating real-time news scraping  
* Connecting sentiment results with stock price movement data  
* Using advanced deep learning models (LSTM, BERT)  
* Deploying a simple web interface using Streamlit  
* Backtesting sentiment signals against historical returns  

Further development would require larger labeled datasets, more advanced NLP techniques, and deployment infrastructure.


## Acknowledgments

* Kaggle open datasets  
* Scikit-learn documentation  
* Building AI course materials  
* Open-source Python community  

All external materials used in this project comply with their respective licenses.
