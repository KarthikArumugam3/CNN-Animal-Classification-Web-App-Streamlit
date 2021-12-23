import streamlit as st
import tensorflow as tf


@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('my_cnn_model.hdf5')
  return model

with st.spinner('Model is being loaded..'):
  model=load_model()

st.write("""
         # Dog vs Cat Classification
         """
         )

file = st.file_uploader("Please upload the image", type=["jpg", "png"])
import cv2
from PIL import Image, ImageOps
import numpy as np
st.set_option('deprecation.showfileUploaderEncoding', False)
def import_and_predict(image_data, model):
    
        size = (64,64)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction
        
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    #score = tf.nn.softmax(predictions[0])
    #st.write(predictions)
    #st.write(score)
    if predictions[0][0] > 0.5:
      st.write(f"This image most likely belongs to Dog class with a {predictions[0][0] * 100} percent confidence.")

    else:
      st.write(f"This image most likely belongs to Cat class with a {predictions[0][0] * 100} percent confidence.")