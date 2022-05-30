# MLOps

I have taken 3 columns of random number and calculated y as function of first 3 column
used Linear regression model to predict y
 To calculate Drift, i have wrote a funtion that calculated following metrics for drift:
 percentage of missing values and zeroz between train and prod data
 ratio of mean,median,mini,max,std of prod to train data. 
 t test between columns of train and prod
 i have defined boundries for each metrics, so the function will return dataframe of metrics if the drift has happened.
 
 in flask in have pickled both model and function
 code is running without error
 but while posting 2 files, there is an error which i couldnt decode.
