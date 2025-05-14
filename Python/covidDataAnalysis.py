import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv("owid-covid-data.csv")

# Check structure
print(df.columns)
print(df.head())

# Check missing values
print(df.isnull().sum())

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter for specific countries
countries = ['USA', 'Kenya', 'India']
df_filtered = df[df['location'].isin(countries)]

# Drop rows with missing key metrics
df_filtered = df_filtered.dropna(subset=['total_cases', 'total_deaths'])

# Fill other missing values
df_filtered.fillna(0, inplace=True)

#Total case over time
plt.figure(figsize=(10,6))
for country in countries:
    subset = df_filtered[df_filtered['location'] == country]
    plt.plot(subset['date'], subset['total_cases'], label=country)

plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.savefig("total_cases_over_time.png")
plt.show()

# Plot vaccination trends
plt.figure(figsize=(10,6))
for country in countries:
    subset = df_filtered[df_filtered['location'] == country]
    plt.plot(subset['date'], subset['total_vaccinations'], label=country)

plt.title("COVID-19 Vaccination Progress Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.savefig("vaccination_progress_over_time.png")
plt.show()

#Total deaths over time
plt.figure(figsize=(10,6))
for country in countries:
    subset = df_filtered[df_filtered['location'] == country]
    plt.plot(subset['date'], subset['total_deaths'], label=country)

plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.tight_layout()
plt.savefig("total_deaths_over_time.png")
plt.show()


#Daily new cases
Kenya_data = df_filtered[df_filtered['location'] == 'Kenya']

plt.figure(figsize=(10,6))
plt.bar(Kenya_data['date'], Kenya_data['new_cases'], color='red')
plt.title("Daily New COVID-19 Cases in Kenya")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.tight_layout()
plt.savefig("daily_new_cases_Kenya.png")
plt.show()


#Death rate trend
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']

plt.figure(figsize=(10,6))
for country in countries:
    subset = df_filtered[df_filtered['location'] == country]
    plt.plot(subset['date'], subset['death_rate'], label=country)

plt.title("COVID-19 Death Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Death Rate")
plt.legend()
plt.tight_layout()
plt.savefig("death_rate_trend.png")
plt.show()

import plotly.express as px

latest = df[df['date'] == df['date'].max()]
fig = px.choropleth(latest,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    color_continuous_scale="Reds",
                    title="Total COVID-19 Cases by Country")
fig.write_html("global_cases_choropleth.html")
fig.show()