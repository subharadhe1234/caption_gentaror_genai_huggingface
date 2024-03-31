import requests
import  streamlit as st
API_URL_Symantic = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}
API_URL_caption = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
def semantic_generatio(file):
    response = requests.post(API_URL_Symantic, headers=headers, data=file)
    return response.json()[0]['generated_text']
def captinon_genarator(payload):
    response = requests.post(API_URL_caption, headers=headers, json=payload)
    return response.json()[0]['generated_text']


st.title("Image Captioning")
file=st.file_uploader('uploade the image',type=['jpg','jpeg','png'])

if file:
    col1,col2=st.columns(2)
    with col1:
        st.image(file,use_column_width=True)
    with col2:

        with st.spinner("Generating semantics..."):
            semantic=semantic_generatio(file)
            # st.subheader("Semantics")
            # st.write(semantic)

        with st.spinner("Generating Caption..."):

            prompt_dic={
                'inputs':f"Question:Convert the following image semantics"
                f"'{semantic}' to an linkedin caption"
                f"make sure you add hash tags and emojis."
                f"Answer:"
            }
            caption_raw=captinon_genarator(prompt_dic)
            st.subheader('Captions')
            # caption = caption_raw.split("Answer: ")[1]
            # st.write(caption)
            st.write(caption_raw)




# output = query("cat_style.jpg")
# print(output)
