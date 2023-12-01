# Purpose of Study

The primary objective of this study is to examine and determine whether there exist statistically significant differences in price among vehicles listed by individual owners on Asheville Craigslist and Greenville Craigslist. The motivation is to see if this significance will empower consumers to buy vehicles at a lower price in the corresponding regions.
# Methodology & Data Collection

To gather a comprehensive dataset for analysis, a web scraping approach was employed to extract information from both Asheville and Greenville Craigslist. The listings from the "Cars & Trucks - By Owner" section were targeted to ensure a focus on vehicles listed by individual owners. 

The data collection process initiated with the use of the wget command-line utility to download the HTML pages of relevant Craigslist listings. This involved scripting the retrieval of web pages to obtain detailed information about each vehicle listing, including attributes such as price, title, and additional relevant details.
After gathering the HTML page, The data was then converted into a JSON format using the built-in formatter of Visual Studio Code. In order to perform testing, the data then had to be converted into a CSV. 

The utilization of web scraping techniques ensures that the dataset is a representative sample of the vehicles listed on Craigslist during the specified time frame and is within fifteen miles of the corresponding area. This approach also enables the study to capture a diverse range of vehicles listed by individual owners, providing a foundation for statistical analysis.
## Resources
| Category                 | URL                                 |
|--------------------------|-------------------------------------|
| Google Sheet             | https://docs.google.com/spreadsheets/d/1kbFHRB-ZJ3D35ZVT6yQ_4sUBhXv8VIFlXr2581Lb99k/edit#gid=1881392164               |
| Source Code              | https://github.com/nburnet1/craigslist-ANOVA/blob/main/ANOVA.py |
| Asheville Craigslist URL | https://asheville.craigslist.org/search/cta?max_price=100000&min_price=100&postal=28806&purveyor=owner&search_distance=15#search=1~gallery~0~0      |
| Greenville Craigslist URL| https://greenville.craigslist.org/search/cta?max_price=100000&min_price=100&postal=29605&purveyor=owner&search_distance=15#search=1~gallery~0~0      |

*Note: All calculations can be found via the Google sheet link and along with the Source Code.*
# Summary Statistics


|                        | Asheville      | Greenville     |
|------------------------|-----------------|-----------------|
| **Sum**                | 1650595         | 1485936         |
| **Mean**               | 13529.46721     | 12179.80328     |
| **Standard Deviation** | 11086.25578     | 11629.94316     |
| **Sample Size**        | 122             | 122             |


| **Sum of Squares**    |                 |                  |     
|-----------------------|-----------------|------------------|
| **Total**             | 31348555219     | 3123676.365      |
| **Between**           | 111117156.9     |                 |
| **Within**            | 31237438062     |                 |


| **Degrees of Freedom**   |              |    
|-----------------------|-----------------|
| **Between**           | 1               |
| **Within**            | 242             |


| **Mean Squares**   |              |    
|-----------------------|-----------------|
| **Between**           | 111117156.9     |
| **Within**            | 129080322.6     |

|   |   |
|---|---|
| **Grand Mean**        | 12854.63525     |
| **F-Statistic**       | 0.8608373041    |
| **P-Value**           | 0.3544289258    |




# Graphical Analysis

![Boxplot](https://github.com/nburnet1/craigslist-ANOVA/blob/main/img/boxplot.png)
*Boxplot of prices in Asheville and Greenville (Figure 0)*

![Line Graph](https://github.com/nburnet1/craigslist-ANOVA/blob/main/img/plot.png)
*Line graph showing the distribution of Asheville and Greenville in increments of 5000 (Figure 1)*

![Scatter Plot](https://github.com/nburnet1/craigslist-ANOVA/blob/main/img/scatter.png)
*Scatter plot of prices sorted by price (Figure 2)*

# Assumptions for ANOVA

## A. Be independent from one another
Considering the proximity of Asheville and Greenville, it's important to assess their independence. Despite their closeness, factors like distinct locations and varied industries make them independent. State and local legislation differences further support this independence.
## B. Have a normal distribution
The data's normal distribution is confirmed through the Shapiro-Wilk test and visual assessments (see Figures 1 and 2), ensuring that the data aligns closely with a normal distribution.
## C. Have standard deviations for each group approximately the same
Examining standard deviations in the summary statistics, both groups show similar values, differing by only about 543. This consistency validates the assumption of roughly equal variability.
These assessments assure the validity of the data and will allow for an ANOVA analysis.
# One-Way ANOVA

## Results

### Program Output
```txt
Asheville Mean: 13529.47
Greenville Mean: 12179.80
Asheville Standard Deviation: 11040.73
Greenville Standard Deviation: 11582.18
Grand Mean: 12854.64
SST: 31348555218.54
SSB: 111117156.89
SSW: 31237438061.65
MS Between: 111117156.89
MS Within: 129080322.57
DF Between: 1
DF Within: 242
Shapiro-Wilk Test for Asheville: 0.8721591830253601
Shapiro-Wilk Test for Greenville: 0.7615530490875244
F-statistic: 0.86
Alpha: 0.05
P-value: 0.35
Fail to reject the null hypothesis. There is no significant difference in prices.
```
# Conclusions
After analyzing price data for Asheville and Greenville, it was found that the mean prices in Asheville ($13,529.47) and Greenville ($12,179.80) exhibited no statistically significant difference. The overall average (grand mean) was $12,854.64. The groups’ data can be considered normally distributed based on tests mentioned above. The One-Way ANOVA results, with an F-statistic of 0.86 and a p-value of 0.35, failed to reject the null hypothesis. Based on the data available, there is no strong evidence to support the existence of a substantial difference in prices between Asheville and Greenville.





