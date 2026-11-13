/*
# Data quality tests

1.The data needs to be 100 records of youtube channels(row count test)
2.The data needs 4 fields (colums count test)
3.The channel name colums must be string format,and the other colums must be numerical data type(data type check)
4.Each record must be unique in the dataset (duplicate count check)

Row count - 100
Columns count - 4

Data Types

channel_name = VARCHAR
total_subscribers = INTEGER
total_views = INTEGER
total_videos = INTERGER

Duplicate count = 0

*/

--1.Row count check
SELECT COUNT(*) as no_of_rows
FROM view_Top_youtube_data_india_2026

----2.colums count test
--SELECT COUNT(*) as colunm_count
--FROM 
--    INFORMATION_SCHEMA.COLUMNS
--WHERE 
--    TABLE_NAME = 'view_Top_youtube_data_india_2026'

----3.Data type check
--SELECT 
--    COLUMN_NAME,
--    DATA_TYPE
--FROM 
--    INFORMATION_SCHEMA.COLUMNS
--WHERE 
--    TABLE_NAME = 'view_Top_youtube_data_india_2026'

--4.Duplicate count check

SELECT channel_name,
       COUNT(*) as duplicate_count
FROM view_Top_youtube_data_india_2026
GROUP BY channel_name
HAVING COUNT(*) > 1
