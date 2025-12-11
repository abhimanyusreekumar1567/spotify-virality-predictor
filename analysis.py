import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_and_clean(filename):
    df = pd.read_csv(filename)
    df.drop_duplicates(inplace=True)
    df = df[df['Streams_Millions'] > 0]
    return df

def analyze_correlations(df):
    numeric_df = df.select_dtypes(include=[np.number])
    matrix = numeric_df.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Feature Correlation Matrix')
    plt.tight_layout()
    plt.show()

def analyze_genre_performance(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Genre', y='Streams_Millions', data=df, palette='viridis')
    plt.title('Stream Distribution by Genre')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def analyze_virality_factors(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Danceability', y='Streams_Millions', hue='Genre', size='Energy', sizes=(20, 200), alpha=0.7, data=df)
    plt.title('Impact of Danceability & Energy on Streams')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        print("Loading Data from CSV...")
        df = load_and_clean('music_data.csv')
        
        print("Dataset Stats:")
        print(df.describe())
        print("-" * 30)
        
        print("Top 5 Artists by Streams:")
        top_artists = df.groupby('Artist_Name')['Streams_Millions'].sum().sort_values(ascending=False).head(5)
        print(top_artists)
        
        print("Generating Correlation Heatmap...")
        analyze_correlations(df)
        
        print("Generating Genre Analysis...")
        analyze_genre_performance(df)
        
        print("Generating Virality Scatter Plot...")
        analyze_virality_factors(df)
        
    except FileNotFoundError:
        print("Error: 'music_data.csv' not found. Run make_data.py first.")