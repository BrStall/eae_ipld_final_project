# The libraries you have to use
import pandas as pd
import matplotlib.pyplot as plt

# Some extra libraries to build the webapp
import streamlit as st

# ----- Page configs -----
st.set_page_config(
    page_title="<Your Name> Portfolio",
    page_icon="📊",
)

# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.write("Interactive Project to load a dataset with information about Netflix Movies and Series, extract some insights using Pandas and displaying them with Matplotlib.")
    st.write("Data extracted from: https://www.kaggle.com/datasets/shivamb/netflix-shows (with some cleaning and modifications)")

# ----- Title of the page -----
st.title("🎬 Netflix Data Analysis")
st.divider()

# ----- Loading the dataset -----

@st.cache_data
def load_data():
    data_path = "data/netflix_titles.csv"
    try:
        movies_df = pd.read_csv(data_path, index_col="show_id")  # Assuming 'show_id' is the index column
        return movies_df
    except Exception as e:
        st.error(f"Error loading the dataset: {e}")
        return None

movies_df = load_data()

# Check if the DataFrame is loaded successfully
if movies_df is not None:
    # Displaying the dataset in an expandable table
    with st.expander("Check the complete dataset:"):
        st.dataframe(movies_df)

    # ----- Extracting some basic information from the dataset -----

    # TODO: Ex 2.2: What is the min and max release years?

    # Substitua NaN por um valor padrão ou use uma estratégia apropriada, como a média dos anos de lançamento
    movies_df['release_year'].fillna(0, inplace=True)  # Substitua 0 pelo valor padrão desejado

    min_year = movies_df['release_year'].min()
    max_year = movies_df['release_year'].max()

    print(f"Min year: {min_year}, Max year: {max_year}")

    # Restante do código...
else:
    st.subheader("Error loading the dataset. Please check the data file path.")

# TODO: Ex 2.3: How many director names are missing values (NaN)?

num_missing_directors = movies_df['director'].isnull().sum()  # TODO

print(f"Number of missing directors: {num_missing_directors}")

# TODO: Ex 2.4: How many different countries are there in the data?

df = movies_df.fillna('Unknown')

countries_list = df["country"].unique().tolist()

countries_str = ', '.join(countries_list)

split_list = countries_str.split(', ')

unique_countries_list = []

for country in split_list:
    if country not in unique_countries_list and country != ("") and ',' not in country:
        unique_countries_list.append(country)

n_countries = len(unique_countries_list) 

# TODO: Ex 2.5: How many characters long are on average the title names?

avg_title_length = df['title'].apply(lambda x: len(x)).mean()  # TODO

print(f"The average title length is {avg_title_length:.2f} characters")

# ----- Displaying the extracted information metrics -----

st.write("##")
st.header("Basic Information")

cols1 = st.columns(5)
cols1[0].metric("Min Release Year", min_year)
cols1[1].metric("Max Release Year", max_year)
cols1[2].metric("Missing Dir. Names", num_missing_directors)
cols1[3].metric("Countries", n_countries)
cols1[4].metric("Avg Title Length", str(round(avg_title_length, 2)) if avg_title_length is not None else None)


# ----- Pie Chart: Top year producer countries -----

st.write("##")
st.header("Top Year Producer Countries")

cols2 = st.columns(2)
year = cols2[0].number_input("Select a year:", min_year, max_year, 2005)

# TODO: Ex 2.6: For a given year, get the Pandas Series of how many movies and series 
# combined were made by every country, limit it to the top 10 countries.

df_copy = df.copy()

df_copy['country2'] = df_copy['country'].str.split(', ')
df_copy = df_copy.explode('country2')

top_10_countries = df_copy.groupby(['country2', 'type']).size().sort_values(ascending=False).head(10)

print(top_10_countries)

# print(top_10_countries)
if top_10_countries is not None:
    fig = plt.figure(figsize=(8, 8))
    plt.pie(top_10_countries, labels=top_10_countries.index, autopct="%.2f%%")
    plt.title(f"Top 10 Countries in {year}")

    st.pyplot(fig)

else:
    st.subheader("⚠️ You still need to develop the Ex 2.6.")


# ----- Line Chart: Avg duration of movies by year -----

st.write("##")
st.header("Avg Duration of Movies by Year")

# TODO: Ex 2.7: Make a line chart of the average duration of movies (not TV shows) in minutes for every year across all the years. 

for idx, row in df.iterrows():
    if row['type'] == 'Movie' and pd.notna(row['duration']):
        df.at[idx, 'duration_minutes'] = int(row['duration'].split(' ')[0])

movies_avg_duration_per_year = df[df['type'] == 'Movie'].groupby('release_year')['duration_minutes'].mean()

if movies_avg_duration_per_year is not None:
    fig = plt.figure(figsize=(9, 6))
    plt.plot(movies_avg_duration_per_year)

    # plt.plot(...# TODO: generate the line plot using plt.plot() and the information from movies_avg_duration_per_year (the vertical axes with the minutes value) and its index (the horizontal axes with the years)

    plt.title("Average Duration of Movies Across Years")

    st.pyplot(fig)

else:
    st.subheader("⚠️ You still need to develop the Ex 2.7.")
