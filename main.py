import streamlit as sl
import time as ts
from datetime import time

# Remove The Streamlit Hambuger Menu and the streamlit footer
sl.markdown("""
<style>
.css-14xtw13.e8zbici0
{
    visibility: hidden;
}
.css-cio0dv.egzxvld1
{
    visibility: hidden;
}
</style>    
""", unsafe_allow_html= True)


# Single File Uploader
sl.title("Upload Single Video File!")
sl.markdown("---")
video = sl.file_uploader("Please upload a video", type="mp4")
if video is not None:
    sl.video(video)


# Multiple Files Uploader
sl.title("Upload Multiple Images Files!")
sl.markdown("---")
images = sl.file_uploader("Please Upload multiple images", type=["jpg", "png"], accept_multiple_files= True)
if images is not None:
    for image in images:
        sl.image(image)



# Slider
val = sl.slider("This is a Slider", min_value=50, max_value=150, value=70, step=5)


# Text Input
value = sl.text_input("Enter your Course Title", max_chars=60)
print(value)

# Text Area
valore = sl.text_area("Enter the course description", max_chars=150)
print(valore)

# Date Input
data = sl.date_input("Enter your registration Date")
print(data)

# Time Input
timer = sl.time_input("Set Timer")

# Progress bar
bar = sl.progress(0)
for i in range(10):
    bar.progress((i+1)*10)
    #Remove the comment for give the functionality to this progress
    # ts.sleep(1)
   


# A Progress Bar Binded to the Time Input

# Function that convert datetime to Seconds
def converter(value):
    m,s,ms = value.split(":")
    tot_s = ((int(m)*60) + int(s) + (int(ms)/1000))
    return tot_s

# Time Input
timer2 = sl.time_input("Timer Binded to the Progress Bar", value=time(0,0,0))

if str(timer2) == "00:00:00":
    sl.write("Please set timer!")
else:
   
    #estraiamo i secondi selezionati nel input timer2
    sec = converter(str(timer2))

    #inizializiamo la progress bar al valore 0
    bar = sl.progress(0)

    # diamo ala progress bar uno step in modo che possiamo dire a che percentuale siamo nel timer: 
    # esempio: su 100 secondi, lo step è di 1secondo , quindi 1% corrisponde ad un secondo 
    # esempio2: su 500 secondi, lo step è di 5 secondi, quindi 1% corrisponde a 5 secondi 
    step = sec/100

    # Creiamo un widget vuoto in cui fare il display della percentuale di "progresso"
    progress_status = sl.empty()
    
    # Logica Progress bar    
    for i in range(100):
        bar.progress((i+1))
        progress_status.write(str(i+1)+ " %")
        ts.sleep(step)