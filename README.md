# MLOps

I have taken 3 columns of random number and calculated y as function of first 3 column
used Linear regression model to predict y
 To calculate Drift, i have wrote a funtion that calculated following metrics for drift:<br>
 percentage of missing values and zeroz between train and prod data<br>
 ratio of mean,median,mini,max,std of prod to train data. <br>
 t test between columns of train and prod<br>
 i have defined boundries for each metrics, so the function will return dataframe of metrics if the drift has happened.<br>
 # udpate
 the Draft_status will return a text message mentioning which metric data drift occured and also the dataframe of metrics<br>
 
 
 in flask in have pickled both model and function.<br>
 code is running without error<br>
 currently draft can be checked in /draft, but if required can be clubbed with /predict by taking training data from hard coded location and comparing with the production data uploaded using the function Draft_status 
 but while posting 2 files, there is an error which i couldnt decode.
# update:
error due to file name was rectified


 I have not done any complex scenerio like categorical variable or checking normal distribution by using Shapiro Wilk test or simalar test and then performing relavent probability checks. i have also simplied the metric using ratios and percentage as it will be easier to have single value comparison than comparing between two values
 But i have explored other topics of drift and got my doubts clarified from Kuldeep and Prabir
