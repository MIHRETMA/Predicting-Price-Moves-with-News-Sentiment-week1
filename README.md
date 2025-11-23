First off, the necessary setups were done (setting up the python virtual environment, creating the necessary directories needed for the folder structure setup, creating the necessary git branches). 

After the setup the data was loaded to a pandas dataframe after importing the necessary modules.

The analysis performed were as follows

Descriptive Statistics

Here I first performed statistics analysis for the headline column. This was to see the length of text which showed the maximum and minimum length.
 
Then a comparative analysis was done to see the most performing (count of publications made by a single publisher) publisher. From there the top 10 publishers were extracted. Here it was observed that Paul Quintaro had made the most publishings, demonstrating that he was the most active publisher. 

I finished off with doing an analysis on publication dates to see the trends over time. A crucial step and a bit of a challenge I encountered here was normalizing the date column because it included null values. So a work-around I used was to set the errors to coerce. I then resampled the dates to values of interest (i.e. day, time and year). From this the publication frequency by day of the week and year was observed chronologically.

Text Analysis

Here I started off with downloading and importing the necessary modules to perform analysis related to NLP - nltk. I then tried to extract headlines that included phrases related to significant events like FDA approval and price targets by applying the defined function. A separate dataframe for the filtered dataset was defined.


Time Series Analysis

I used the matplotlib library to visualize the trends. And from the visualizations it can be observed that publications decreased over the weekends. Additionally, the highest time of publication was around 10 AM. In a more panoramic view, it can be seen that the publications have increased over the years. 

Publisher Analysis 

In this part publisher specific analysis was done. I used a horizontal bar graph for viewing the publications done by the top 10 publishers. Afterwards, weekly publications of the top 5 publishers were observed. Although the top publisher was Paul Quintaro, from the weekly publication count, the majority of the contribution was made by other publishers. This was because I grouped it by day and then resampled it to weekly totals. So this part was challenging because when I tried to resample and group it by day I kept getting the overall time on the x-axis, not the one grouped by day.

Afterwards, I tried to see the relationship between publishers and significant events (which were the key phrases filtered in the Text Analysis part). Here, Vick Meyer was the top publisher which made publications related to FDA approval and price targets. 

Additionally, there were publishers who made their publication as an organization or instead of their full name their email address was captured under the publishers column. To filter out these entries I defined a function using the regular expression library and then applied the function to the dataframe. A separate dataframe for domain specific entries was filtered using the ‘@’ string. And from there I tried to view the top domains registered and their respective count of publications.

Finally I committed the python notebook I worked on and merged it to the main branch using a pull request.

Once I was done with the EDA analysis, I carried on with the Quantitative analysis. For this task, I created another branch with the name task-2. I then downloaded the TA-lib package and imported it. I continued with loading the datasets, to separate dataframes, related to this task. From then on I calculated various technical indicators for each dataframes (each company in the dataset), such as SMA, EMA, RSI, MACD, MACD_signal, MACD_hist. Here I used different time periods for the indicators, however I only calculated them for the Close price. 

From these indicators, it can be observed that Meta and Microsoft have the highest moving averages and Nvidia has the least. For all companies, the Moving Average (both simple and exponential) shows a gradual increase. Additionally, Meta has the highest RSI.
