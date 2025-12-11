import pandas as pd
import numpy as np
import random

def generate_csv():
    rows = 2000
    genres = ['Pop', 'Hip-Hop', 'Rock', 'Electronic', 'Jazz', 'Classical', 'Indie']
    artists = ['Artist_' + str(i) for i in range(1, 51)]
    
    data = {
        'Track_ID': range(1001, 1001 + rows),
        'Genre': [random.choice(genres) for _ in range(rows)],
        'Artist_Name': [random.choice(artists) for _ in range(rows)],
        'Duration_Min': [round(random.uniform(2.0, 5.0), 2) for _ in range(rows)],
        'Danceability': [round(random.uniform(0.1, 1.0), 2) for _ in range(rows)],
        'Energy': [round(random.uniform(0.1, 1.0), 2) for _ in range(rows)],
        'Acousticness': [round(random.uniform(0.0, 0.9), 2) for _ in range(rows)],
        'Streams_Millions': []
    }

    for i in range(rows):
        base_streams = random.uniform(1, 50)
        if data['Genre'][i] in ['Pop', 'Hip-Hop'] and data['Danceability'][i] > 0.7:
            base_streams *= random.uniform(2, 5)
        if data['Energy'][i] > 0.8:
            base_streams *= 1.2
        data['Streams_Millions'].append(round(base_streams, 2))

    df = pd.DataFrame(data)
    df.to_csv('music_data.csv', index=False)
    print("Success: 'music_data.csv' has been created.")

if __name__ == "__main__":
    generate_csv()