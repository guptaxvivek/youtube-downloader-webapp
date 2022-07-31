from pytube import YouTube
import streamlit as st
from io import BytesIO
import time

st.title("Youtube Downloader")

link = st.text_input("Enter Youtube URL")

buffer_mp4, buffer_mp3 = BytesIO(), BytesIO()


def down_mp4():
    global buffer_mp4
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().stream_to_buffer(
        buffer_mp4)
    buffer_mp4.seek(0)


def down_mp3():
    global buffer_mp3
    yt.streams.filter(only_audio=True).order_by('abr').desc().first().stream_to_buffer(buffer_mp3)
    buffer_mp3.seek(0)


if link:
    yt = YouTube(link)
    st.image(yt.thumbnail_url, width=300)
    st.header(yt.title)

    st.subheader(f"Length: {yt.length} seconds")

    with st.spinner('Please Wait...'):
        down_mp4()
        down_mp3()
        time.sleep(5)

    col1, col2 = st.columns(2)

    with col1:
        mp4_bt = st.download_button("Download mp4", buffer_mp4, f'{yt.title}.mp4')

    with col2:
        mp3_bt = st.download_button("Download mp3", buffer_mp3, f'{yt.title}.mp3')
