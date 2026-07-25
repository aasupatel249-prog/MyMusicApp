import os
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

CSV_FILE = my_final_playlist_no_api.csv

def load_songs_from_csv(playlist_name=None):
    df = pd.read_csv(CSV_FILE)
    all_playlists = df['Playlist name'].unique().tolist()
    if playlist_name:
        filtered = df[df['Playlist name'] == playlist_name]
        songs = filtered.to_dict('records')
    else:
        songs = df.to_dict('records')
    return songs, all_playlists

@app.route('/')
def index():
    _, all_playlists = load_songs_from_csv()
    return render_template('index.html', playlists=all_playlists)

@app.route('/playlist/<playlist_name>')
def get_playlist(playlist_name):
    songs, _ = load_songs_from_csv(playlist_name)
    return jsonify(songs)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
