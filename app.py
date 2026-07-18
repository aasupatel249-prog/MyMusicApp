import streamlit as st

st.title("🎵 My Permanent Music Player")

# Spotify link input
link = st.text_input("Paste Spotify Playlist Link Here")

if link:
    # Link ko embed player format mein badalne ka logic
    if "spotify.com/playlist/" in link:
        playlist_id = link.split("/")[-1].split("?")[0]
        embed_link = f"https://open.spotify.com/embed/playlist/{playlist_id}?utm_source=generator"
        
        # Embed player dikhane ke liye
        st.components.v1.iframe(embed_link, height=400)
    else:
        st.warning("Please enter a valid Spotify Playlist link.")
