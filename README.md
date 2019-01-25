## Data Science and Data Engineering assesment.
There is one company that has this test project. Description is below.

#### 1. Machine Learning
There is **train.csv** and **test.csv**. **Test.csv** contains extrapolated data.

------------
1. Perform simple Exploratory Data Analysis on train.csv and test.csv
2. Use a suitable algorithm to train a machine learning model from the train.csv
3. Use the trained model to infer/predict the y values in test.csv. 
4. Write down your train and test RMSE. 
*For Reference* the base RMSE of **test data** is 25.36, average is 15.99 and the lowest recorded is 0.24

#### 2. Web & Data Engineering
It's necessary to use any python web framework to accomplish this task i.e flask or django. 

------------
1. Create a Command Line Interface (CLI) script to automate the steps of 
	- downloading the training data;
	- performing training task;
	- saving the trained model into file i.e pickle.
	- CLI  must accept an argument to skip the download step to use the existing downloaded training file.
2. Create a single page dashboard to display
	- a simple visualization from the training set 
	- input for user to manually enter x1 and x2
	- display the inferred value (y) to the user

The visualization must be **interactive** e.g. by utilizing plotly

#### 3. Probability and Uncertainty
Airlines are commonly known to utilize overbooking to earn extra profits or avoiding losses over the fact that not all passenger will show up on boarding day. We will use a simple scenario here to demonstrate how airline might do so.
The passenger travel in this scenario is assumed to be alone. Factors such as weather, festival season, time of the flight and other external factors is assumed to not affecting our model.
Historically passenger showed up rate is 80%
The number of ticket to be sold without overbooking is 200, and the cost of a ticket is $120.
The management of the airline is planning to overbook the seats by additional 50 tickets to achieve full capacity and avoid losses. Hence the total ticket to be sold is 250. (0.8x = 200, hence x = 250)
However the risk is if more than 200 passengers showed on boarding day, the airline must compensate each bumped passenger by $300.

------------
1. The revenue without overbook is $24,000 ($120\*200), while for **best case scenario** where 250 tickets are sold and 50 no show passengers is $30,000 ($120\*250).  Show the revenue calculation for **the worst case scenario**
2. Using python library from *matplotlib/seaborn* and *scipy.stats* write codes to plot the **probability mass function** (pmf) for the above scenario.
3. What is the probability of passengers showed up for:
	 - 200
	 - 250
4. What is the *expected revenue* of 250 ticket sold?
5. Does the 250 overbook tickets is the most optimal number? Run a simulation of *expected revenue* from 201 to 260 tickets sold.
6. Plot the number of ticket sold against expected revenue and draw a vertical line to mark the optimal number of ticket sold.
7. By using the optimal number of ticket from (f) and with the showed up rate of 80%, generate 10,000 random numbers to simulate the possible number of passenger show up .
8. What is the min, max and 95% percentile of the number of passenger show up from (g)?
9. What if the passenger isn’t travel alone, describe how it affects the model.

#### 4. Statistical Hypothesis Testing
ABC is an online advertisement firm, the management found adblocker used by the users is affecting the revenue. The firm has invested significantly to distribute custom adblock whitelist. Below is the table showing number of sample adblock detected before the distribution of the first 3 months (12 weeks) and the next 3 months after the whitelist has been distributed.

| Week  |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |  10   |  11   |  12   |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Count | 3100  | 2800  | 1900  | 2400  | 3200  | 2700  | 1600  | 4100  | 2300  | 3200  | 2900  | 3300  |

| Week  |  13   |  14   |  15   |  16   |  17   |  18   |  19   |  20   |  21   |  22   |  23   |  24   |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Count | 2300  | 2100  | 1900  | 2400  | 3500  | 1700  | 1800  | 2400  | 3300  | 2700  | 2100  | 2300  |

------------

1. Convert the above information into **numpy** array and compute the *average* difference between the first table and the second table.
2. Could the difference legit and not due to chance? Use *statistical approach* to demonstrate your assumptions.
3. Because the firm already spent vast amount of money, does the difference in number of adblocker detected for the next 3 months is *statistically significant* and worth the investment? You may provide your opinion here.
4. What’s the confidence intervals of the average difference? You may use 90% or 95% percentile for confidence intervals, state this percentile in the solution.
