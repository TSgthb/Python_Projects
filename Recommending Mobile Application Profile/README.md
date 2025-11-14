# App Profile Recommendation for Android and iOS Devices
> _This project was created using documentation available on [Dataquest](https://www.dataquest.io/blog/data-analyst-projects-for-beginners/)._

<p align="justify">
This project aims to identify profitable app profiles for <b>Dev_It</b>, a fictitious mobile app development company that monetizes through in-app advertisements. Since revenue depends on user engagement, the goal is to analyze app store data to determine which types of apps are most likely to attract users and generate higher ad impressions.
</p>

<p align="justify">
The analysis uses sample datasets from Android's <b>Google Play Store</b> and Apple's <b>App Store</b>, focusing on free apps because they typically attract more downloads and engagement.
</p>

Jump to end for *[Analysis & Findings](https://github.com/TSgthb/Python_Projects/tree/main/Analyzing%20Walmart%20Sales%20Data#analysis--findings).*

## Project Outline
1. **Data Acquisition and Setup**  
   - Imported [Play Store](https://www.kaggle.com/lava18/google-play-store-apps) and [App Store](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps) datasets from Kaggle. 
   - Loaded data into Python DataFrames for cleaning, transforming and analysis.

2. **Data Cleaning and Preparation**  
   - Removed inaccurate and missing data (e.g., row with missing category in Play Store dataset).  
   - Eliminated duplicate entries by retaining the record with the highest number of reviews for each app.  
   - Filtered out non-English apps using ASCII-based checks.  
   - Isolated free apps for both marketplaces. Final count was:
     - **Google Play** – 8,863 apps
     - **App Store** – 3,222 apps

3. **Exploratory Analysis**  
   - Built frequency tables for app categories and genres in both stores to get a holistic view of general trend.  
   - Identified dominant categories and genres:
     - **Google Play**: Family, Tools, Entertainment, Games.
     - **App Store**: Games, Entertainment, Photo & Video.
   - Analyzed average downloads (Google Play) and ratings (App Store) by category.

4. **Advanced Insights**  
   - Investigated skewed averages caused by a few highly popular apps (e.g., Google Maps, Facebook, Bible).  
   - Determined that categories like Navigation, Social Networking, and Music have high engagement but are dominated by major players, making them less viable for new entrants.

## Analysis & Findings

1. **Dominant Categories**  
   - **Google Play**: Family (18.9%), Games (9.7%), Tools (8.4%).  
   - **App Store**: Games (58.16%), Entertainment (7.88%), Photo & Video (4.96%).

2. **High Engagement Niches**  
   - Navigation, Social Networking, and Music categories show high average downloads and ratings but are saturated with apps like **Google Maps**, **Facebook**, and **Spotify**.

3. **Books & Reference Category**  
   - Shows promising engagement but is heavily skewed toward apps like **Bible**, **Dictionary.com**, and **Amazon Kindle**.  
   - Indicates potential for apps based on popular books, provided they include unique features.

Check out the complete code, *[Analysis Notebook](https://github.com/TSgthb/Python_Projects/blob/main/Analyzing%20Walmart%20Sales%20Data/Notebooks/analysis_notebook.ipynb).*

## Strategic Recommendations

Based on the analysis, the most promising app profile is:

- **App Concept**: An app based on a popular book (preferably recent and trending).  
- **Key Features**:
  - Daily quotes and highlights.
  - Audio version of the book.
  - Interactive quizzes and challenges.
  - Community forum for discussions.
  - Optional premium features for personalization.
- **Why this works**:
  - Aligns with entertainment and educational niches, which dominate both marketplaces.  
  - Adds unique engagement features to differentiate from existing library apps.  
  - Targets a broad audience while minimizing competition from major players.

## Conclusion

To maximize profitability across both Google Play and App Store:
- Focus on **entertainment-driven apps** with interactive elements.
- Avoid saturated categories dominated by global brands.
- Innovate within promising niches like **Books & Reference** by adding value beyond basic content.
