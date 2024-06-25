# Arabic Fake News Detection System

## Project Description

This project aims to address the rapid spread of misinformation on digital platforms, specifically within the Arabic-speaking community. We have developed an Arabic Fake News Detection (AFND) system utilizing advanced natural language processing (NLP) and machine learning techniques. Our system leverages Long Short-Term Memory (LSTM) neural networks to detect and classify fake news in Arabic. The research utilizes the Arabic Fake News Dataset (AFND) and the Gaza Dataset, demonstrating that our LSTM model outperforms traditional machine learning approaches such as Naive Bayes and Support Vector Machines (SVM).

### System Functionalities

The AFND system allows users to input news articles and perform the following tasks:

1. **Data Collection and Preprocessing:**
   - Collect and preprocess Arabic news articles from various sources.
   - Remove Arabic stopwords using the NLTK library.
   - Encode target labels and tokenize the text data for model input.

2. **Model Training and Evaluation:**
   - Train an LSTM model with an embedding layer, two LSTM layers, and a dense output layer with softmax activation.
   - Compare the performance of the LSTM model with baseline models (Naive Bayes and SVM) using metrics like accuracy, precision, recall, and F1-score.

3. **Real-time Fake News Detection:**
   - Provide a user-friendly web interface for users to input news articles and receive real-time predictions on their credibility.

### User Interface

The application will be built using HTML, CSS, and JavaScript, ensuring a responsive and intuitive interface. Users will be able to easily navigate through different functionalities and input required data efficiently.

## Datasets:

- [Classified Arabic News](https://www.kaggle.com/datasets/tariqodeh/classified-arabic-news)
  
## Gallery

### Initial Photo
![Initial Photo](Demo/Demo%20Results/IMG_7829.PNG)

## How to Run

- Clone the repository to your local machine.
- Open the `index.html` file in a web browser.

## Languages And Tools:

<img align="left" alt="HTML" width="50px" src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" /> <img align="left" alt="CSS" width="50px" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg" /> <img align="left" alt="JavaScript" width="50px" src="https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png" /> 

