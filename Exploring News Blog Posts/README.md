# Exploring Hacker News Posts

<p align="justify">
Hacker News is a popular platform in technology and startup circles where users share posts, receive votes, and engage in discussions. 
<p>

<p align="justify">
This project analyzes a curated dataset of approximately <b>20,000 posts</b> (originally ~300,000 rows) sourced from <i><a href="https://www.kaggle.com/hacker-news/hacker-news-posts">kaggle</a></i>. The dataset includes attributes such as post title, URL, points, comments, author, and creation time.
<p>

<p align="justify">
The primary goal is to uncover patterns in user engagement by comparing <b>Ask HN</b> and <b>Show HN</b> posts and analyzing how posting time influences comments and points.
<p>

Jump to end for *[Analysis & Findings](https://github.com/TSgthb/Python_Projects/tree/main/#analysis--findings).*

## Project Outline

1. **Data Acquisition and Setup**  
   - Imported Hacker News dataset `hacker_news.csv` and loaded it into Python for analysis.  
   - Removed incomplete records (e.g., posts with zero comments or points).

2. **Data Cleaning and Preparation**  
   - Extracted relevant columns: `id`, `title`, `url`, `num_points`, `num_comments`, `author`, `created_at`.  
   - Segregated posts into three categories:  
     - **Ask HN**: Posts where users ask questions.  
     - **Show HN**: Posts where users showcase projects or ideas.  
     - **Other Posts**: All remaining posts.

3. **Exploratory Analysis**  
   - Compared **Ask HN** and **Show HN** posts for average comments and points.  
   - Analyzed posting time to identify hours with maximum engagement.  
   - Converted time zones from **EST** to **IST** for global relevance.

4. **Advanced Insights**  
   - Determined top hours for maximum comments on **Ask HN** posts.  
   - Identified top hours for maximum points on **Show HN** posts.  
   - Compared engagement metrics of Ask/Show HN posts with all other posts.

## Analysis & Findings

1. **Ask HN vs Show HN Engagement**  
   - **Ask HN** posts receive more comments on average (**14.04**) compared to **Show HN** posts (**10.32**).  
   - **Show HN** posts earn more points on average (**27.56**) than **Ask HN** posts (**15.06**).

2. **Best Posting Times for Comments (Ask HN)**  
   - Highest engagement occurs between **15:00–16:00 EST (01:00–02:00 IST)** with **38.59 average comments per post**.  
   - Other high-performing hours: **02:00 EST**, **20:00 EST**, **16:00 EST**, and **21:00 EST**.

3. **Best Posting Times for Points (Show HN)**  
   - Maximum points occur between **23:00 EST (09:00 IST)** with **42.39 average points per post**.  
   - Other top hours: **12:00 EST**, **22:00 EST**, **00:00 EST**, and **18:00 EST**.

4. **Comparison with Other Posts**  
   - Posts outside Ask/Show HN categories outperform both in engagement:  
     - **Average Points**: ~55.41 (≈28% higher than Show HN).  
     - **Average Comments**: ~26.87 (≈13% higher than Ask HN).  
   - Time impact is less pronounced for these posts, indicating consistent engagement throughout the day.

## Strategic Recommendations

1. **For Maximum Comments**  
   - Create **Ask HN** posts between **15:00–16:00 EST (01:00–02:00 IST)**.

2. **For Maximum Points**  
   - Publish **Show HN** posts between **23:00–00:00 EST (09:00–10:00 IST)**.

3. **General Posting Strategy**  
   - If the goal is overall engagement (points + comments), consider posting outside Ask/Show HN categories, as these posts consistently perform better.

4. **Further Analysis**  
   - Explore additional factors such as post length, topic category, and seasonal trends for deeper insights.
