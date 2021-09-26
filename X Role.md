# Technologies Used

## Overview
- We browsed several websites with data and found one that matched our interests. It is information about house transactions in Beijing, China around 2017. When we browsed the database, the original author has cleaned up the data. But we found that this is far from enough. Then, we used web scraping in the same website to extract transaction information and on-sale information for different cities.

### Web Scraping
- BeautifulSoup will be used to extract information from the websites. However, it is time-consuming, each city will take around whole day.

### Data Cleaning & Analysis
- Pandas will be used for data cleaning and exploratory analysis.

### Database Storage
- Postgres will be used for data storage.

### Machine Learning
- SciKitLearn will be used to create a linear regression.

### Dashboard
- JavaScript, HTML, CSS will be used to create dashboard with price prediction. In addition, we will use flask add more pages with maps, using API of BAIDUMAP, to create heatmap to overview the price informaiton in different district. 