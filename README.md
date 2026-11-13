# Data Portfolio: Excel to Power BI 


![excel-to-powerbi-animated-diagram](Assets/Images/kaggle_to_powerbi.gif)




# Table of contents 

- [Objective](#objective)
- [Data Source](#data-source)
- [Stages](#stages)
- [Design](#design)
  - [Mockup](#mockup)
  - [Tools](#tools)
- [Development](#development)
  - [Pseudocode](#pseudocode)
  - [Data Exploration](#data-exploration)
  - [Data Cleaning](#data-cleaning)
  - [Transform the Data](#transform-the-data)
  - [Create the SQL View](#create-the-sql-view)
- [Testing](#testing)
  - [Data Quality Tests](#data-quality-tests)
- [Visualization](#visualization)
  - [Results](#results)
  - [DAX Measures](#dax-measures)
- [Analysis](#analysis)
  - [Findings](#findings)
  - [Validation](#validation)
  - [Discovery](#discovery)
- [Recommendations](#recommendations)
  - [Potential ROI](#potential-roi)
  - [Potential Courses of Actions](#potential-courses-of-actions)
- [Conclusion](#conclusion)




# Objective 

- What is the key pain point? 

The Head of Marketing wants to find out who the top YouTubers are in 2026 to decide on which YouTubers would be best to run marketing campaigns throughout the rest of the year.


- What is the ideal solution? 

To create a dashboard that provides insights into the top India YouTubers in 2026 that includes their 
- subscriber count
- total views
- total videos, and
- engagement metrics

This will help the marketing team make informed decisions about which YouTubers to collaborate with for their marketing campaigns.

## User story 

As the Head of Marketing, I want to use a dashboard that analyses YouTube channel data in the India . 

This dashboard should allow me to identify the top performing channels based on metrics like subscriber base and average views. 

With this information, I can make more informed decisions about which Youtubers are right to collaborate with, and therefore maximize how effective each marketing campaign is.


# Data source 

- What data is needed to achieve our objective?

We need data on the top India YouTubers in 2026 that includes their 
- channel names
- total subscribers
- total views
- total videos uploaded



- Where is the data coming from? 
The data is sourced from Kaggle (an Excel extract), [see here to find it.](https://www.kaggle.com/)


# Stages

- Design
- Developement
- Testing
- Analysis 
 


# Design 

## Dashboard components required 
- What should the dashboard contain based on the requirements provided?

To understand what it should contain, we need to figure out what questions we need the dashboard to answer:

1. Who are the top 10 YouTubers with the most subscribers?
2. Which 3 channels have uploaded the most videos?
3. Which 3 channels have the most views?
4. Which 3 channels have the highest average views per video?
5. Which 3 channels have the highest views per subscriber ratio?
6. Which 3 channels have the highest subscriber engagement rate per video uploaded?

For now, these are some of the questions we need to answer, this may change as we progress down our analysis. 


## Dashboard mockup

- What should it look like? 

Some of the data visuals that may be appropriate in answering our questions include:

1. Table
2. Treemap
3. Scorecards
4. Horizontal bar chart 




![Dashboard-Mockup](Assets/Images/Dashboard_mockup.png.jpeg)


## Tools 


| Tool | Purpose |
| --- | --- |
| Excel | Exploring the data |
| SQL Server | Cleaning, testing, and analyzing the data |
| Power BI | Visualizing the data via interactive dashboards |
| GitHub | Hosting the project documentation and version control |
| Mokkup AI | Designing the wireframe/mockup of the dashboard | 


# Development

## Pseudocode

- What's the general approach in creating this solution from start to finish?

1. Get the data
2. Explore the data in Excel
3. Load the data into SQL Server
4. Clean the data with SQL
5. Test the data with SQL
6. Visualize the data in Power BI
7. Generate the findings based on the insights
8. Write the documentation + commentary
9. Publish the data to GitHub Pages

## Data exploration notes

This is the stage where you have a scan of what's in the data, errors, inconcsistencies, bugs, weird and corrupted characters etc  


- What are your initial observations with this dataset? What's caught your attention so far? 

1. There are at least 4 columns that contain the data we need for this analysis, which signals we have everything we need from the file without needing to contact the client for any more data. 
2. The first column contains the channel ID with what appears to be channel IDS, which are separated by a @ symbol - we need to extract the channel names from this.
3. Some of the cells and header names are in a different language - we need to confirm if these columns are needed, and if so, we need to address them.
4. We have more data than we need, so some of these columns would need to be removed





## Data cleaning 
- What do we expect the clean data to look like? (What should it contain? What contraints should we apply to it?)

The aim is to refine our dataset to ensure it is structured and ready for analysis. 

The cleaned data should meet the following criteria and constraints:

- Only relevant columns should be retained.
- All data types should be appropriate for the contents of each column.
- No column should contain null values, indicating complete data for all records.

Below is a table outlining the constraints on our cleaned dataset:

| Property | Description |
| --- | --- |
| Number of Rows | 100 |
| Number of Columns | 4 |

And here is a tabular representation of the expected schema for the clean data:

| Column Name | Data Type | Nullable |
| --- | --- | --- |
| channel_name | VARCHAR | NO |
| total_subscribers | INTEGER | NO |
| total_views | INTEGER | NO |
| total_videos | INTEGER | NO |



- What steps are needed to clean and shape the data into the desired format?

1. Remove unnecessary columns by only selecting the ones you need
2. Extract Youtube channel names from the first column
3. Rename columns using aliases







### Transform the data 



```sql
/*
# 1. Select the required columns
# 2. Extract the channel name from the 'NOMBRE' column
*/

-- 1.
SELECT
    SUBSTRING(NAME, 1, CHARINDEX('@', NAME) -1) AS channel_name,  -- 2.
    total_subscribers,
    total_views,
    total_videos

FROM
    Top_Youtubers_India_2026
```


### Create the SQL view 

```sql
/*
# 1. Create a view to store the transformed data
# 2. Cast the extracted channel name as VARCHAR(100)
# 3. Select the required columns from the Top_Youtubers_India_2026 SQL table 
*/

-- 1.
CREATE VIEW view_Top_Youtubers_India_2026 AS

-- 2.
SELECT
    CAST(SUBSTRING(NAME, 1, CHARINDEX('@', NAME) -1) AS VARCHAR(100)) AS channel_name, -- 2. 
    total_subscribers,
    total_views,
    total_videos

-- 3.
FROM
    Top_Youtubers_India_2026

```


# Testing 

- What data quality and validation checks are you going to create?

Here are the data quality tests conducted:

## Row count check
```sql
/*
# Count the total number of records (or rows) are in the SQL view
*/

SELECT
    COUNT(*) AS no_of_rows
FROM
    view_Top_Youtubers_India_2026;

```

![Row count check](Assets/Images/Row%20count.png)



## Column count check
### SQL query 
```sql
/*
# Count the total number of columns (or fields) are in the SQL view
*/


SELECT
    COUNT(*) AS column_count
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_NAME = 'view_Top_Youtubers_India_2026'
```
### Output 
![Column count](Assets/Images/column%20_count.png)



## Data type check
### SQL query 
```sql
/*
# Check the data types of each column from the view by checking the INFORMATION SCHEMA view
*/

-- 1.
SELECT
    COLUMN_NAME,
    DATA_TYPE
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_NAME = 'view_Top_Youtubers_India_2026';
```
### Output
![Data type check](Assets/Images/Data%20_type.png)


## Duplicate count check
### SQL query 
```sql
/*
# 1. Check for duplicate rows in the view
# 2. Group by the channel name
# 3. Filter for groups with more than one row
*/

-- 1.
SELECT
    channel_name,
    COUNT(*) AS duplicate_count
FROM
    view_Top_Youtubers_India_2026

-- 2.
GROUP BY
    channel_name

-- 3.
HAVING
    COUNT(*) > 1;
```
### Output
![Duplicate count check](assets/images/4_duplicate_records_check.png)

# Visualization 


## Results

- What does the dashboard look like?

![GIF of Power BI Dashboard](assets/images/top_uk_youtubers_2024.gif)

This shows the Top India Youtubers in 2026 so far. 


## DAX Measures

### 1. Total Subscribers (M)
```sql
Total Subscribers (M) = 
VAR million = 1000000
VAR sumOfSubscribers = SUM(view_Top_Youtubers_India_2026[total_subscribers])
VAR totalSubscribers = DIVIDE(sumOfSubscribers,million)

RETURN totalSubscribers

```

### 2. Total Views (B)
```sql
Total Views (B) = 
VAR billion = 1000000000
VAR sumOfTotalViews = SUM(view_Top_Youtubers_India_2026[total_views])
VAR totalViews = ROUND(sumOfTotalViews / billion, 2)

RETURN totalViews

```

### 3. Total Videos
```sql
Total Videos = 
VAR totalVideos = SUM(view_Top_Youtubers_India_2026[total_videos])

RETURN totalVideos

```

### 4. Average Views Per Video (M)
```sql
Average Views per Video (M) = 
VAR sumOfTotalViews = SUM(view_Top_Youtubers_India_2026[total_views])
VAR sumOfTotalVideos = SUM(view_Top_Youtubers_India_2026[total_videos])
VAR  avgViewsPerVideo = DIVIDE(sumOfTotalViews,sumOfTotalVideos, BLANK())
VAR finalAvgViewsPerVideo = DIVIDE(avgViewsPerVideo, 1000000, BLANK())

RETURN finalAvgViewsPerVideo 

```


### 5. Subscriber Engagement Rate
```sql
Subscriber Engagement Rate = 
VAR sumOfTotalSubscribers = SUM(view_Top_Youtubers_India_2026[total_subscribers])
VAR sumOfTotalVideos = SUM(view_Top_Youtubers_India_2026[total_videos])
VAR subscriberEngRate = DIVIDE(sumOfTotalSubscribers, sumOfTotalVideos, BLANK())

RETURN subscriberEngRate 

```


### 6. Views per subscriber
```sql
Views Per Subscriber = 
VAR sumOfTotalViews = SUM(view_Top_Youtubers_India_2026[total_views])
VAR sumOfTotalSubscribers = SUM(view_Top_Youtubers_India_2026[total_subscribers])
VAR viewsPerSubscriber = DIVIDE(sumOfTotalViews, sumOfTotalSubscribers, BLANK())

RETURN viewsPerSubscriber 

```




# Analysis 

## Findings

- What did we find?

For this analysis, we're going to focus on the questions below to get the information we need for our marketing client - 

Here are the key questions we need to answer for our marketing client: 
1. Who are the top 10 YouTubers with the most subscribers?
2. Which 3 channels have uploaded the most videos?
3. Which 3 channels have the most views?
4. Which 3 channels have the highest average views per video?
5. Which 3 channels have the highest views per subscriber ratio?
6. Which 3 channels have the highest subscriber engagement rate per video uploaded?


### 1. Who are the top 10 YouTubers with the most subscribers?

| Rank | Channel Name         | Subscribers (M) |
|------|----------------------|-----------------|
| 1    |T-Series              | 316.00          |
| 2    |SET Inadia            | 190.00          |
| 3    |Zee Music Company     | 123.00          |
| 4    |Goldmines             | 111.00          |
| 5    |Sony SAB              | 106.00          |
| 6    |Zee TV                | 99.40           |
| 7    |ChuChu TV             | 98.20           |
| 8    |Tips Offical          | 82.70           |
| 9    |Colors TV             | 82.60           |
| 10   |Aaj Tak               | 75.70           |


### 2. Which 3 channels have uploaded the most videos?

| Rank | Channel Name    | Videos Uploaded |
|------|-----------------|-----------------|
| 1    | T-Series        | 275,713         |
| 2    | SET Inadia      | 178,569         |
| 3    | Zee TV          | 226,313         |



### 3. Which 3 channels have the most views?


| Rank | Channel Name    | Total Views (B) |
|------|-----------------|-----------------|
| 1    |T-Series         | 19.78           |
| 2    |SET India        | 18.56           |
| 3    |Zee Music Company| 15.97           |


### 4. Which 3 channels have the highest average views per video?

| Channel Name  | Averge Views per Video (M) |
|---------------|-----------------|
|ChuChu TV      | 53.06          |
|Tips Official  | 5.63           |
|ZeeMusicCompany| 5.33            |


### 5. Which 3 channels have the highest views per subscriber ratio?

| Rank | Channel Name     | ViewsperSubscriber        |
|------|----------------- |---------------------------|
|1     |ChuChu TV Nursery |                           |
|      |Rhymes & Kids Song|	53.06                     |
|2     |Tips Official	  | 5.63                      |
|3	   |Zee Music Company |	5.33                      |






### Notes

For this analysis, we'll prioritize analysing the metrics that are important in generating the expected ROI for our marketing client, which are the YouTube channels wuth the most 

- subscribers
- total views
- videos uploaded



## Validation 

### 1. Youtubers with the most subscribers 

#### Calculation breakdown

Campaign idea = product placement 

1. T-Series
- Average views per video = 13.20 million
- Product cost = 5
- Potential units sold per video = 13.20 million × 2% conversion rate = 264,000 units sold
- Potential revenue per video = 264,000×5 = 1,320,000
- Campaign cost (one-time fee) = 50,000
- **Net profit = 1,320,000 − 50,000 = 1,270,000**

b. SET India
- Average views per video = 1.09 million
- Product cost = 5
- Potential units sold per video = 1.09 million × 2% conversion rate = 21,800 units sold
- Potential revenue per video = 21,800 × 5 = 109,000
- Campaign cost (one-time fee) = 50,000
- **Net profit = 109,000 − 50,000 = 59,000**

c. Zee Music Company
- Average views per video = 5.33 million
- Product cost = 5
- Potential units sold per video = 5.33 million × 2% conversion rate = 106,600 units sold
- Potential revenue per video = 106,600 × 5 = 533,000
- Campaign cost (one-time fee) = 50,000
- **Net profit = 533,000 − 50,000 = 483,000**


Best option from category: T-Series


#### SQL query 

```sql
/* 

# 1. Define variables 
# 2. Create a CTE that rounds the average views per video 
# 3. Select the column you need and create calculated columns from existing ones 
# 4. Filter results by Youtube channels
# 5. Sort results by net profits (from highest to lowest)

*/


-- 1. 
DECLARE @conversionRate FLOAT = 0.02;		-- The conversion rate @ 2%
DECLARE @productCost FLOAT = 5.0;			-- The product cost @ 5
DECLARE @campaignCost FLOAT = 50000.0;		-- The campaign cost @ 50,000	


-- 2.  
WITH ChannelData AS (
    SELECT 
        channel_name,
        total_views,
        total_videos,
        ROUND((CAST(total_views AS FLOAT) / total_videos), -4) AS rounded_avg_views_per_video
    FROM 
        youtube_db.dbo.view_Top_Youtubers_India_2026
)

-- 3. 
SELECT 
    channel_name,
    rounded_avg_views_per_video,
    (rounded_avg_views_per_video * @conversionRate) AS potential_units_sold_per_video,
    (rounded_avg_views_per_video * @conversionRate * @productCost) AS potential_revenue_per_video,
    ((rounded_avg_views_per_video * @conversionRate * @productCost) - @campaignCost) AS net_profit
FROM 
    ChannelData


-- 4. 
WHERE 
    channel_name in ('T-Series','SET India',
    'Zee Music Company')


-- 5.  
ORDER BY
	net_profit DESC

```

#### Output

![Most subsc](assets/images/youtubers_with_the_most_subs.png)

### 2. Youtubers with the most videos uploaded

### Calculation breakdown 

Campaign idea = sponsored video series  

1. **T-Series**
- Average views per video = 363.19 billion ÷ 275,713 = 1.32 million
- Product cost = 5
- Potential units sold per video = 1,317,276 × 2% conversion rate = 26,346 units sold
- Potential revenue per video = 26,346 × 5 = 131,730
- Total campaign revenue (11 videos) = 131,730 × 11 = 1,449,030
- Campaign cost (11 videos × 5,000 each) = 55,000
- **Net profit = 1,449,030 − 55,000 = 1,394,030**

b. **Zee TV**
- Average views per video = 122.43 billion ÷ 226,313 = 0.54 million
- Product cost = 5
- Potential units sold per video = 540,976 × 2% conversion rate = 10,820 units sold
- Potential revenue per video = 10,820 × 5 = 54,100
- Total campaign revenue (11 videos) = 54,100 × 11 = 595,100
- Campaign cost (11 videos × 5,000 each) = 55,000
- **Net profit = 595,100 − 55,000 = 540,100**

b. **SET India**
- Average views per video = 194.74 billion ÷ 178,569 = 1.09 million
- Product cost = 5
- Potential units sold per video = 1,090,558 × 2% conversion rate = 21,811 units sold
- Potential revenue per video = 21,811 × 5 = 109,055
- Total campaign revenue (11 videos) = 109,055 × 11 = 1,199,605
- Campaign cost (11 videos × 5,000 each) = 55,000
- **Net profit = 1,199,605 − 55,000 = 1,144,605**


Best option from category: Yogscast

#### SQL query 
```sql
/* 
# 1. Define variables
# 2. Create a CTE that rounds the average views per video
# 3. Select the columns you need and create calculated columns from existing ones
# 4. Filter results by YouTube channels
# 5. Sort results by net profits (from highest to lowest)
*/


-- 1.
DECLARE @conversionRate FLOAT = 0.02;           -- The conversion rate @ 2%
DECLARE @productCost FLOAT = 5.0;               -- The product cost @ 5
DECLARE @campaignCostPerVideo FLOAT = 5000.0;   -- The campaign cost per video @ 5,000
DECLARE @numberOfVideos INT = 11;               -- The number of videos (11)


-- 2.
WITH ChannelData AS (
    SELECT
        channel_name,
        total_views,
        total_videos,
        ROUND((CAST(total_views AS FLOAT) / total_videos), -4) AS rounded_avg_views_per_video
    FROM
        youtube_db.dbo.view_vTop_Youtubers_India_2026

)


-- 3.
SELECT
    channel_name,
    rounded_avg_views_per_video,
    (rounded_avg_views_per_video * @conversionRate) AS potential_units_sold_per_video,
    (rounded_avg_views_per_video * @conversionRate * @productCost) AS potential_revenue_per_video,
    ((rounded_avg_views_per_video * @conversionRate * @productCost) - (@campaignCostPerVideo * @numberOfVideos)) AS net_profit
FROM
    ChannelData


-- 4.
WHERE
    channel_name IN ('T-Series','Zee TV','SET India')


-- 5.
ORDER BY
    net_profit DESC;
```

#### Output

![Most videos](assets/images/youtubers_with_the_most_videos.png)


### 3.  Youtubers with the most views 

#### Calculation breakdown

Campaign idea = Influencer marketing 

a. T-Series
- Average views per video = 1.32 million
- Product cost = 5
- Potential units sold per video = 1.32 million × 2% conversion rate = 26,400 units sold
- Potential revenue per video = 26,400 × 5 = 132,000
- Campaign cost (3-month contract) = 130,000
- **Net profit = 132,000 − 130,000 = 2,000**

b. SET India
- Average views per video = 1.09 million
- Product cost = 5
- Potential units sold per video = 1.09 million × 2% conversion rate = 21,800 units sold
- Potential revenue per video = 21,800 × 5 = 109,000
- Campaign cost (3-month contract) = 130,000
- **Net profit = 109,000 − 130,000 = -21,000 (Potential Loss)**

c. Zee Music Company
- Average views per video = 5.33 million
- Product cost = 5
- Potential units sold per video = 5.33 million × 2% conversion rate = 106,600 units sold
- Potential revenue per video = 106,600 × 5 = 533,000
- Campaign cost (3-month contract) = 130,000
- **Net profit = 533,000 − 130,000 = 403,000**

Best option from category: T-Series



#### SQL query 
```sql
/*
# 1. Define variables
# 2. Create a CTE that rounds the average views per video
# 3. Select the columns you need and create calculated columns from existing ones
# 4. Filter results by YouTube channels
# 5. Sort results by net profits (from highest to lowest)
*/



-- 1.
DECLARE @conversionRate FLOAT = 0.02;        -- The conversion rate @ 2%
DECLARE @productCost MONEY = 5.0;            -- The product cost @ 5
DECLARE @campaignCost MONEY = 130000.0;      -- The campaign cost @ 130,000



-- 2.
WITH ChannelData AS (
    SELECT
        channel_name,
        total_views,
        total_videos,
        ROUND(CAST(total_views AS FLOAT) / total_videos, -4) AS avg_views_per_video
    FROM
        youtube_db.dbo.view_Top_Youtubers_India_2026
)


-- 3.
SELECT
    channel_name,
    avg_views_per_video,
    (avg_views_per_video * @conversionRate) AS potential_units_sold_per_video,
    (avg_views_per_video * @conversionRate * @productCost) AS potential_revenue_per_video,
    (avg_views_per_video * @conversionRate * @productCost) - @campaignCost AS net_profit
FROM
    ChannelData


-- 4.
WHERE
    channel_name IN ('T-Series', 'SET India','Zee Music Company')


-- 5.
ORDER BY
    net_profit DESC;

```

#### Output

![Most views](assets/images/youtubers_with_the_most_views.png)



