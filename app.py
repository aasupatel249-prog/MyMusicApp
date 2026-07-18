import streamlit as st

st.title("🎵 My Permanent Music Player")
link = st.text_input("Paste Spotify Link Here")
if st.button("Load Playlist"):
    st.write(f"Loading music from: {link}")
