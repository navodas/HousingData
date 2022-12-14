# Housing price prediction for Västra Götaland region in Sweden.

### Introduction 
This project contains housing prices data collected in the Västra Götaland region in Sweden using the hemnet real estate website. The project is carried out in below steps. These data are purely for personal/ academic purposes.


![Tableau dashboard on the housing data](https://github.com/navodas/HousingData/blob/main/dashboard.png?raw=true)



### Project steps
1. A Web scraper is developed to grab **basic information** on the house sales on the hemnet website. BeautifulSoup and Selenium python packages are used for the task. After cleaning 63877 data instances were retained. Refer to (Webscraper.ipynb).
2. A comprehensive **EDA** is perfomed on the collected housing data. Refer to (EDA_housing_data.ipynb).
3.  **Additional information** were collected for a subset of instances (21611) usinng an updated web scraper. Refer to (Webscraper_for_additional_data.ipynb)
4. A **polynomial regression model** is developed for predicting the housing prices. Refer to (Linear_Regression_with_full_data.ipynb)
5. The model is deployed as a **Flask web aplication** on Heroku. Refer to  (app.py) and (templates/index.html).
    - https://h-predictor.herokuapp.com/

![Flask webapp on the housing data](https://github.com/navodas/HousingData/blob/main/webapp.png?raw=true)


7. Two **interactive Tableau dashboards** are cretaed and hosted on public Tableau platform.
    - https://public.tableau.com/app/profile/navodas/viz/Housingprices_16646201439710/Housingprices
    - https://public.tableau.com/app/profile/navodas/viz/Housingpricespermunicipality/Municipalityinfo


### Data Files - Not shared to do possible copy right violations.

### Data description
  - Soldprice	 - The target variable to predict that indicates the actual sale price of the property.
  - Monthly_fee	- Mortgage
  - Agent	- The real estate agent who sold the property.
  - Municipality - The municipality where the property is located.
  - Municipality_tax_rate	- The local tax rate of the Municipality.
  - Number of rooms	- Number of available rooms including the living room.
  - House type - Property type? Apartment, House, Farm House, w/o agriculture, Holiday Home, Unspecified (Town/Semi-detached/Chain), Town House, Semi-detached House, Chain house
  - Asking price - Price demanded by the seller.
  - Balcony	- A balcony is available or not?
  - Construction year	- year the building is constructed.
  - Operating cost - Monthly operations cost.	
  - Letting form - Type of ownership.	
  - Floor Number - Floor the apartment is located.	
  - Lift Availability	- A lift is available or not?
  - Year - Year the property is sold.

### Other Files
1. Webscraper.ipynb - This workbook contains the webscraper for crawling the hemnet site to collect housing prices.
2. EDA_housing_data.ipynb - Comprehensive analysis on the basic housing price information collected using Webscraper.ipynb. 
3. Linear_Regression_with_basic_data.ipynb - Training linear regression models on the basic data.
4. Webscraper_for_additional_data.ipynb -  Webscraper for collecting additional attributes on a subset of housing data previously collected.
5. Linear_Regression_with_full_data.ipynb - Training linear regression models on the additional data collected. 
6. Model_selection.ipynb - This note book contains training a RandomForestRegressor for predicting the housing prices along with feature selection, outlier handling, and model selection based on randomized grid search.
6. lr_predictor.pkl - Final polynomial regression model saved for deploying.
7. app.py - Flask web app.
8. templetes/index.html - Front-end of the web app.
9. mean_sd.json - Mean and standard deviation values for each of the numerical variables. They were  used for standadizing the incoming numerical features after deploying the model.



    
Note - Not all the municipalities in the region are covered in the data collection.

