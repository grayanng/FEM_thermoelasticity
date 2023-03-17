import streamlit as st


"""
# Ниже показано, как можно просто преобразовать его в веб-приложение с помощью Streamlit:

```python
import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
st.write("# Real Time Sentiment Analysis")

user_input = st.text_input("Please rate our services >>: ")
nltk.download("vader_lexicon")
s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)

if score == 0:
    st.write(" ")
elif score["neg"] != 0:
    st.write("# Negative")
elif score["pos"] != 0:
    st.write("# Positive")
```
Здесь вам следует знать, что всякий раз, когда вы используете эту структуру в Python для создания веб-приложения, 
вы не можете запустить свой код без использования команды: streamlit run filename.py. 
"""
