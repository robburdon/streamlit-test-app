import streamlit as st
import numpy as np
import pandas as pd
import json
import requests

#secrets
API_TOKEN = ""
with open('api_token.txt') as reader:
    API_TOKEN = reader.readline().replace('\n', '')




#huggingface stuff
API_URL = "https://api-inference.huggingface.co/models/gpt2"
#API_URL = "https://api-inference.huggingface.co/models/iarfmoose/t5-base-question-generator"
#API_URL = "https://api-inference.huggingface.co/models/abbas/gpt2-horror-stories"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data, parameters = )
    return json.loads(response.content.decode("utf-8"))

#data = query("Can you please let us know more details about your ")
#get the string out of the returned json
#returned_string = data[0]["generated_text"]



#chatting shit for model prompts

context2 = """The most merciful thing in the world is the inability of the human mind to correlate all its contents. We live on a placid island of ignorance in the midst of black seas of infinity, and it was not meant that we should voyage far. The sciences, have hitherto harmed us little; but some day the piecing together of dissociated knowledge will open up such terrifying vistas of reality, and of our frightful position therein, that we shall either go mad from the revelation or flee from the deadly light into the peace and safety of a new dark age.
"""

context = "some day the piecing together of dissociated knowledge will open up such terrifying vistas of reality, and of our frightful position therein, that we shall either go mad from the revelation or flee from the deadly light into the peace and safety of a new dark age."



#app
st.title('What have I done')

user_input = st.text_area('GPT2 but it is haunted.')

if st.button('Shoot'):
    prompt = user_input
    data = query(prompt)
    returned_string = data #[0]["generated_text"]
    st.write(returned_string)


#st.write("And this is where the spiders are:")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [50.07, 14.4],
    columns=['lat', 'lon'])

#st.map(map_data)
