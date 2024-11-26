import streamlit as st

st.title("Видео редактор с ИИ")
st.write(
    "Какое то оисание "
)

uploaded_file = st.file_uploader(
    "Choose a video",
    type=["mp4"]
)
if uploaded_file:
    print(uploaded_file)
    video_bytes = uploaded_file.read()
    st.video(video_bytes, start_time=1.1, end_time=24.31999969482422)