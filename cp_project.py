import pandas as pd
import google.generativeai as genai
# pd.read_csv('data.csv')
GOOGLE_API_KEY="AIzaSyDjzoVQZvqPHgv9mD9dyRXUcQoMXQ1yAmo"

genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 1.0,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_NONE"
    },
]
model=genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config,safety_settings=safety_settings)
chat=model.start_chat(history=[])
# print((chat.send_message("hello")).text)
data=pd.read_csv('data.csv')
def responce(item):
      for i in data.iloc[:,0]:
          if i==item:
              break
      # return("hello")
      return((chat.send_message(f"give a detailed explanation about { item} based on {data.iloc[i,1]}as which warehuse its stored in  ,{data.iloc[i,4]} as custumer rating out of 5,{data.iloc[i,5]} as cost per product, {data.iloc[i,7]} as importance of product, {data.iloc[i,9]} as discount on porduct,,  {data.iloc[i,5]} as weight in grams add extra detail condencing it to 50 words report and report is necessery no matter the circumstance")).text)
# ,temp

# def responce(item):
#     return responce_root(item)


