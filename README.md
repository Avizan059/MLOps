# MLOps

I have taken 3 columns of random number and calculated y as function of first 3 column
used Linear regression model to predict y
 To calculate Drift, i have wrote a funtion that calculated following metrics for drift:<br>
 percentage of missing values and zeroz between train and prod data<br>
 ratio of mean,median,mini,max,std of prod to train data. <br>
 t test between columns of train and prod<br>
 i have defined boundries for each metrics, so the function will return dataframe of metrics if the drift has happened.<br>
 
 in flask in have pickled both model and function.<br>
 code is running without error<br>
 but while posting 2 files, there is an error which i couldnt decode.
