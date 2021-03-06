# Supermarket
We build a Django prototype in Python to improve revenues for Supermarket data.

Our Dataset has information about product details, purchases, demographics, coupons. Using this, our goal is to improve revenues by targeting Segments in the Dataset.

We use dunnhumby's data for a Supermarket.

___________________________________________________________

#### Data Set:

This dataset contains household level transactions over two years from a group of 2,500 households who are frequent shoppers at a retailer. It contains all of each household’s purchases, not just those from a limited number of categories. For certain households, demographic information as well as direct marketing contact history are included.

Below is the link for whole data-Set:

* [CSV-Files]  (https://www.dropbox.com/sh/6lz05ehkt31x81j/AADxV_STvuCwDujql3VwarGja?dl=0)
* [YAML-FILES](https://www.dropbox.com/sh/lz522q4z2119vh2/AACtNhemZOf4EtCojHccSHBBa?dl=0)

--------------------------------------------------------------------------------------------------

## DATA TABLES:
The following contains the structure of the Dataset, which we used for the whole prototype.

We use (a) to denote that a record is connected to another table.

--------------
##### CAMPAIGN_TABLE
(1584 households mailed 30 Campaigns)

This table lists the campaigns received by each household in the study. Each household received a different set of campaigns.
File: campaign_table.csv
```
HOUSEHOLD_KEY -- Uniquely identifies each household

(a)CAMPAIGN_TABLE -- Uniquely identifies each campaign. Ranges 1-30

DESCRIPTION -- Type of campaign(TypeA, TypeB or TypeC )
```

--------------
##### CAMPAIGN_DESC
This table gives the length of time for which a campaign runs. So, any coupons received as part of a campaign are valid within the dates contained in this table.
(30 Campaigns)

*File: campaign_desc.csv*
```
(a)CAMPAIGN -- Uniquely identifies each campaign. Ranges 1-30

DESCRIPTION -- Type of Campaign(TypeA, TypeB, TypeC)

START_DAY -- Start Date of Campaign

END_DAY -- End Date of Campaign
```

--------------
#####  COUPON_REDEMPT
(434 households redeemed 556 coupons from 30 Campaigns)

This table identifies the coupons that each household redeemed.

*File: coupon_redempt.csv*


```
HOUSEHOLD_KEY -- Uniquely identifies each household

DAY -- Day when transaction occurred

COUPON_UPC -- Uniquely identifies each coupon

CAMPAIGN -- Uniquely identifies each campaign

```

--------------
#####  COUPON
(1135 coupons promoted 44133 products for the 30 campaigns)

This table lists all the coupons sent to customers as a part of a campaign, as well as the products for which each coupon is redeemable. Some coupons are redeemable for multiple products. One example is a coupon for any private label frozen vegetable.

For campaign TypeA, this table provides pool of possible coupons. Each customer participating in a TypeA campaign received 16 coupons out of the pool. The 16 coupons were selected based on the customer's prior purchase behavior. Identifying the specific 16 coupons that each customer received is outside the scope.

*File: coupon.csv*

```
CAMPAIGN -- Uniquely identifies each campaign. Ranges 1-30

COUPON_UPC -- Uniquely identifies each coupon( unique to household and campaign)

PRODUCT_ID -- Uniquely identifies each product

```
___________________________________________
##### HH_DEMOGRAPHIC
(801 household)
This table contains demographic information for a portion of household.



*File: hh_demographic.csv*
```
HOUSEHOLD_KEY -- Uniquely Identifies each household

AGE_DESC -- Estimated age range

MARITAL_STATUS_CODE -- Marital Status (A - Married, B- Single, U-Unknown)

INCOME_DESC -- Household income

HOMEOWNER_DESC -- Homeowner, renter

HH_COMP_DESC -- Household composition

HOUSEHOLD_SIZE_DESC -- Size of household up to 5+

KID_CATEGORY_DESC -- Number of children present up to 3+
```
___________________________________________
##### TRANSACTION_DATA.csv
(2500 Households shopped 92339 products)

This table contains all products purchased by household within this study. Each line found in this table is essentially the same line that would be found on a store receipt.

*File: transaction_data2.csv*
```
HOUSEHOLD_KEY -- Uniquely identifies each household

BASKET_ID -- Uniquely identifies a purchase occasion

DAY -- Day when transaction occurred

PRODUCT_ID -- Uniquely identifies each product

QUANTITY -- Number of the products purchased during the trip

SALES_VALUE -- Amount of dollars retailer receives from sale

STORE_ID -- Identifies unique stores

COUPON_MATCH_DISC -- Discount applied due to retailer's match of manufacturer coupon

COUPON_DISC -- Discount applied due to manufacturer coupon

RETAIL_DISC -- Discount applied due to retailer's loyalty card program

TRANS_TIME -- Time of day when transaction occurred

WEEK_NO -- Week of transaction. Ranges 1 -102
```

--------------
##### PRODUCT.csv
(92353 products)

This table contains information on each product sold such as type of product, national or private label and a brand identifier.

*File:product.csv*

```
PRODUCT_ID -- Number that uniquely identifies each product

DEPARTMENT -- Groups similar products together

COMMODITY_DESC -- Groups similar products together at a lower level

SUB_COMMODITY_DESC -- Groups similar products together at a lowest level

MANUFACTURER -- Code that links products with same manufacturer together

BRAND -- Indicates Private or National label brand

CURR_SIZE_OF_PRODUCT -- Indicates package size
```

--------------

##### CASUAL_DATA
(68377 products)

This table signifies whether a given product was featured in the weekly mailer or was part of an in-store display.

*File:causal_data.csv*
```
PRODUCT_ID -- Uniquely identifies each product

STORE_ID -- identifies unique stores

WEEK_NO -- Week of the transaction

DISPLAY -- Display location

MAILER -- Mailer Location
```
--------------
## Code:


######File: firstQuestion.py

###### Functions: readCSV(), buildCompleteTopCustomer(), selectCustomerOverTrend().

How many Customers are spending more over time, less over time?

```
--
readCSV()- reads transaction_data2.csv
and dumps total sales value of each household, And 4 quarters sales of each household
Output: customerSaleDict.yaml ['1':4430.0
  '10':233.0
  '100':2310.0]
Output: customerQuarterSaleDict.yaml
['1':
0:780.0
1:1103.0
2:1211.0
3:1336.0]


buildCompleteTopCustomer() -
a) Creates Top Household List by sales value
Output: topCompleteHouseHoldList.yaml
[-'1023'
 -'1609'
 -'2322']

selectCustomerOverTrend() -
Reads customerQuarterSaleDict and topCompleteHouseHoldList to find out users who purchased more over time and less over time

moreSpentOverTime.yaml
- [-'1023'
  -'1453'
  -'1653'
  -'328']
lessSpentOverTime.yaml
-[-'1803'
  -'2448'
  -'2185']
```
```
secondQuestion.py -- readCSV(), plotCatergory(), plot()

Of Customers who are spending more over time, which categories are growing at a faster rate?


readCSV() - Reads moreSpentOverTime.yaml,  product.csv and transaction_data2.csv


Output:
customerMoreQuarterProductDictOverTime.yaml
['1':
  0:
    '':0.0
    DELI: 53:0
    DRUG GM: 102.0
    GROCERY: 497.0
    MEAT: 14.0
    MEAT-PCKGD:47.0
    PASTRY: 35.0
    PRODUCE: 28.0
    SALAD BAR:4.0
   1:
   '':0
   DELI:60.0]


productIDCatergoryDict.yaml -

'1000002':DELI
'1000029':DRUG GM
'1000050':GROCERY
'1000057':GROCERY
'1000059':GROCERY


plotCatergory() -- Plot for Django
plot() -- Plot for Django


```
---------------------------------------------------------------

thirdQuestion.py

Functions - readCSV()

Of those customers who are spending less over time, with which categories are they becoming less engaged?


```
Input -- We read lessSpentOverTime.yaml, product.csv and transaction_data2.csv

Output -- We have customerLessQuarterProductDictOverTime.yaml
['1013':
0:
  DELI: 8.0
  DRUG GM: 74.0
  GROCERY: 700.0
  KIOSK-GAS: 10.0
  MEAT: 142.0
  MEAT-PCKGD:34.0
  SALAD BAR: 26.0
  SEAFOOD: 24:0
 1:
  DRUG GM: 92.0
  GROCERY: 408.0
  MEAT: 208.0
  MEAT-PCKGD: 136.0
  PRODUCE: 40.0
  ]

----------------------------------------------
productIDCatergoryDict.yaml -

['1000002': DELI
'1000029': DRUG GM
'1000050': GROCERY
'1000057': GROCERY
'1000059': DRUG GM
'1000092': DRUG GM
'1000099': GROCERY
'1000106': GROCERY]




```
--------------------------------------------------------------


File: thirdApproach.py

Functions: readCSV(), buildTopList(), selectIncreasedTrendCustomer(), selectDecreasedTrendCustomer()

```
Of those Customers, which ones are spending less over Time with which categories are less engaged?

Input -- transaction_data2.csv


Output --

customerSaleDict.yaml
['1': 4430.0
'10': 233.0
'100': 2310.0
'1000': 4215.0
'1001': 4123.0]

customerQuarterSalesDict.yaml
['1':
  0: 780.0
  1: 1103.0
  2: 1211.0
  3: 1336.0
'10':
  0: 131.0
  1: 0
  2: 30.0
  3: 72.0
'100':
  0: 370.0
  1: 500.0
  2: 704.0
  3: 736.0
]

buildTopList() -- Reads customerSaleDict

Output --

topCompleteHouseHoldList.yaml
['- '1023'
- '1609'
- '2322'
- '1453'
- '2459'
- '1430'
- '718'
- '1653'
- '707'
- '1111'
- '982'']

selectIncreasedTrendCustomer() -- Reads customerQuarterSalesDict.yaml, topCompleteHouseHoldList.yaml

Prints increased purchase trend

[
1023 [['week_no', 'sales_value'], [0, 3507.0], [1, 8305.0], [2, 12119.0], [3, 14455.0]]
1453 [['week_no', 'sales_value'], [0, 2155.0], [1, 5853.0], [2, 6252.0], [3, 7381.0]]
1653 [['week_no', 'sales_value'], [0, 2636.0], [1, 5041.0], [2, 5401.0], [3, 6352.0]]
328 [['week_no', 'sales_value'], [0, 3163.0], [1, 4688.0], [2, 4729.0], [3, 4786.0]]
2351 [['week_no', 'sales_value'], [0, 2090.0], [1, 4450.0], [2, 4943.0], [3, 5338.0]]
900 [['week_no', 'sales_value'], [0, 2067.0], [1, 4660.0], [2, 4758.0], [3, 5064.0]]
371 [['week_no', 'sales_value'], [0, 2092.0], [1, 3781.0], [2, 4428.0], [3, 5650.0]]
1995 [['week_no', 'sales_value'], [0, 1566.0], [1, 3273.0], [2, 4136.0], [3, 6550.0]]
113 [['week_no', 'sales_value'], [0, 2230.0], [1, 4290.0], [2, 4298.0], [3, 4660.0]]
1142 [['week_no', 'sales_value'], [0, 2472.0], [1, 3430.0], [2, 4443.0], [3, 5001.0]]  
]
---------------------------------------------------------------
selectDecreasedTrendCustomer()

Prints decreased purchase trend

[
1803 [['week_no', 'sales_value'], [0, 4072.0], [1, 4031.0], [2, 3768.0], [3, 2590.0]]
2448 [['week_no', 'sales_value'], [0, 3008.0], [1, 2288.0], [2, 2088.0], [3, 2053.0]]
2185 [['week_no', 'sales_value'], [0, 3262.0], [1, 2110.0], [2, 1742.0], [3, 1484.0]]
472 [['week_no', 'sales_value'], [0, 2596.0], [1, 2588.0], [2, 2483.0], [3, 763.0]]
2260 [['week_no', 'sales_value'], [0, 2541.0], [1, 2259.0], [2, 1491.0], [3, 1281.0]]
99 [['week_no', 'sales_value'], [0, 1944.0], [1, 1785.0], [2, 1707.0], [3, 1606.0]]
1206 [['week_no', 'sales_value'], [0, 1745.0], [1, 1693.0], [2, 1582.0], [3, 1268.0]]
437 [['week_no', 'sales_value'], [0, 1823.0], [1, 1743.0], [2, 1275.0], [3, 1118.0]]
1828 [['week_no', 'sales_value'], [0, 3359.0], [1, 2047.0], [2, 306.0], [3, 129.0]]
81 [['week_no', 'sales_value'], [0, 2429.0], [1, 2075.0], [2, 750.0], [3, 337.0]]
]
```
---------------------------------------------------------------

###### fourthQuestion.py --

Which demographic factors (e.g. household size, presence of children, income) appear to affect customer spend?

This contains demographic details of consumers who purchased less over time

###### Functions: readCSV()

```
Input -- The Script reads lessSpentOverTime.yaml, hh_demographic.csv

Output --
customerDemographicsLessOverTime.yaml
['123':
- 45-54
- B
- 35-49K
- '2'
- None/Unknown
'17':
- 65+
- B
- Under 15K
- '2'
- None/Unknown
'1803':
- 19-24
- A
- 50-74K
- '3'
- '1']


```
---------------------------------------------------------------


###### File: fourthQuestionMore.py

Which demographic factors (e.g. household size, presence of children, income) appear to affect customer spend?

This contains demographic details of consumers who purchased more over time

###### Functions: readCSV()

```
Input -- moreSpentOverTime.yaml, hh_demographic

Output --

Demographics of household which purchased more over time

customerDemographicsMoreOverTime.yaml
['1':
- 65+
- A
- 35-49K
- '2'
- None/Unknown
'1020':
- 45-54
- A
- 25-34K
- '2'
- None/Unknown
'1041':
- 25-34
- U
- 35-49K]
```
--------------------------------------------------------------

###### File: fourthQuestionMarriedUnMarried.py --
This Script has output of people who are married, unmarried

###### Functions: readCSV()

List of people from moreSpentOverTime with demographic details (income)
```
Input: moreSpentOverTime.yaml, hh_demographic.csv

Output --

customerMaritalStatusMoreOverTime.yaml

[
A:
  '1': 35-49K
  '1020': 25-34K
  '1074': 35-49K
  '113': 125-149K
  '1142': 50-74K
B:
  '1131': 50-74K
  '1137': 35-49K
  '1172': 50-74K
  '1285': 25-34K
U:
  '1041': 35-49K
  '1057': 50-74K
  '1082': 35-49K
  '1151': Under 15K
  '119': 125-149K
  '1228': 100-124K
]

```
---------------------------------------------------------------
###### File: fourthQuestionAgeGroup.py

###### Functions: readCSV()

List of people from moreSpentOverTime with Age/Income (income)

```
Input: moreSpentOverTime.yaml, hh_demographic.csv


Output:

customerAgeMoreOverTime.yaml

[19-24:
  '1481': 35-49K
  '1923': 35-49K
  '2064': 50-74K
  '567': 25-34K
  '955': Under 15K
25-34:
  '1041': 35-49K
  '1172': 50-74K
  '1267': 75-99K
]

```

---------------------------------------------------------------

###### File: fourthQuestionMoreIncomeHousehold.py

###### Functions: readCSV()

List of People with Household size from moreSpentOverTime

```
Details of Household size with Income

Output:

customerIncomeMoreOverTime.yaml

[100-124K:
  '2172': 2 Adults No Kids
125-149K:
  '2406': 2 Adults Kids
15-24K:
  '2405': Single Female
150-174K:
  '2374': 2 Adults No Kids
175-199K:
  '2102': 2 Adults No Kids
200-249K:
  '976': 2 Adults Kids
25-34K:
  '2186': Single Female
250K+:
  '1844': 2 Adults No Kids
35-49K:
  '2488': Single Female
50-74K:
  '2427': 2 Adults Kids
75-99K:
  '2483': Single Male
Under 15K:
  '1949': Single Female]

```

---------------------------------------------------------------

###### File: fourthQuestionMaritalHouseholdIncome.py

###### Functions: readCSV()

Details of Household by married/unmarried from moreSpentOverTime

```

Input: moreSpentOverTime.yaml, hh_demographic.csv


Output Details: customerStatusMoreOverTime.yaml
[
A:
  25-34:
    '1534': 75-99K
    '166': 50-74K
    '1680': 15-24K
    '1693': 35-49K
B:
  19-24:
    '1923': 35-49K
  25-34:
    '1172': 50-74K
    '1285': 25-34K
    '1475': 50-74K
U:
  19-24:
    '1481': 35-49K
    '2064': 50-74K
    '567': 25-34K
    '955': Under 15K
  25-34:
    '1041': 35-49K    
]

```
---------------------------------------------------------------

###### File: fourthQuestionFullStatusMarried.py

###### Functions: readCSV()

Full details of Household who purchased moreOverTime.

```
Input: moreSpentOverTime.yaml, hh_demographic.csv

Output:

customerFullStatusMoreOverTime.yaml

A:
  25-34:
    '1534': 75-99K
    '166': 50-74K
    '1680': 15-24K
    '1693': 35-49K
    '1785': 35-49K
    '2147': 75-99K
    '2172': 100-124K
    '2378': 50-74K
    '2406': 125-149K
    '283': 50-74K
    '761': 125-149K
    '911': 125-149K
    '971': 35-49K
    '976': 200-249K
  35-44:

```
---------------------------------------------------------------

###### File: customerAllProductsInEveryQuarter.py

###### Functions: Product(), findQuarterSale()

Script creates dictionary of all products of customers who bought in each quarter

Three levels of Dictionary

1)Customer Household_ID:
2) Quarter:[0,1,2,3]
3) Product Details
    a) Brand
    b) commodity
    c) Revenue
    d) Sub-commodity

```
Input -- moreSpentOverTime, product.csv, transaction_data2.csv

Output:

customerAllProductsInEveryQuarter.yaml

['1':
  0:
    '1001908':
      BRAND: National
      COMMODITY: CAKES
      DEPARTMENT: PASTRY
      REVENUE: 5.0
      SUB-COMMODITY: 'CAKES: CREME/PUDDING'
    '1004906':]
```

---------------------------------------------------------------

###### File: customerAveragePurchase.py

###### Functions: readCSV(), AverageCSV()

######Find out the average purchase of Customer
######Average revenue per customer = Customers Total Purchase/Number of Visits

```
Output:
    CustomerAverageDictionaryPerson.yaml: household_id:'Average Purchase'
    CustomerSaleDictionary.yaml: household_id:'Total Sales'
    customerAverageDictionary.yaml: household_id:'quarter':Average
    Eg:

    customerAverageDictionaryPerson.yaml

    '1': '60.90'
    '100': '89.12'
    '1008': '10.33'
    '1010': '39.71'
    '1011': '42.79'
    '1020': '104.25'

    customerSaleDictionary.yaml

    '1': 1766.0
    '10': 131.0
    '100': 713.0
    '1000': 1717.0
    '1001': 873.0
    '1002': 369.0
    '1003': 1190.0

    customerAverage.yaml
    '1':
  0: 0
  1: 0
  2: 44.0
  3: 146.0
  4: 137.0
  5: 135.0
  6: 526.0
  7: 0
  8: 0
  9: 74.0
  10: 105.0
  11: 599.0
  12: 0
```
---------------------------------------------------------------

###### File: customerEveryQuarterMoreProducts.py

###### Functions: product()

This script prints out all the values of selected customers in moreOverTime

```
Output -- for this code
Three levels of Dictionary
12 Quarters.


1)Customer Household_ID:
2) Quarter:[0,1,2,3,4,5,6,7,8,9,10,11]
3) Product Details
    a) Brand
    b) commodity
    c) Revenue
    d) Sub-commodity

Output File:

customerEveryQuarterMoreProducts.yaml

['1':
  0: {}
  1: {}
  2:
    '1006546':
      BRAND: National
      COMMODITY: DRY MIX DESSERTS
      DEPARTMENT: GROCERY
      QUANTITY: 1.0
      REVENUE: 1.0
      SUB-COMMODITY: PUDDINGS DRY]
```
---------------------------------------------------------------
###### File: customerLoyal.py

###### Functions: readCSV(), loyalCustomers()

We find out list of customers who are loyal to the store

```
Build Loyal Customer Dictionary:
    What is Loyal Customer?
    A Customer who has bought continuously in supermarket.
    Where is this data?
    It is in Transaction data.
    How do you find if the customer is Loyal?
    If He purchases Every Week in Year, he is Loyal
    And he has a purchase average of above 50

Output:

customerTimesVisit.yaml

['1': 29
'100': 8
'1008': 9
'1010': 17
'1011': 34
'1020': 32
'1023': 30
'1025': 18
'1041': 26
'1050': 25
'1057': 36
'1061': 20
'1073': 21
'1074': 25
]



customerLoyalAverage.yaml

[
- - 'Loyal Customer:'
  - Household_id:1142
  - Visits:42
  - Average Purchase:128.40
- - 'Loyal Customer:'
  - Household_id:1788
  - Visits:27
  - Average Purchase:110.96
- - 'Non-Loyal Customer:'
]

```

---------------------------------------------------------------

###### File: price_sensitive_0.1.py

###### Functions: coupon(), findConsumer(), couponDetails(), productDetails()

###### Objective: To find Price Sensitive consumers

i) Find out coupon redeemed by top 20 consumers
ii) Find out product Details by top 20 Consumers

Code:
```

coupon():

(What it does?)
  i) Reads Coupon redemp csv files
  ii) Divides Days into Quarters
  ii) Creates a dictionary with

 Output:

 couponDictionary.yaml

  couponRedemptDict[housholdkey][quarter] = (Campaign, COUPON_UPC)

[
'1':
  11: !!python/tuple
  - '18'
  - '54200029176'
'1000':
  11: !!python/tuple
  - '13'
  - '53700040075'
'1005':
  11: !!python/tuple
  - '13'
  - '10000089128'
'101':
  11: !!python/tuple
  - '18'
  - '54900050076'
'1011':
]

---------------------------------------------------------------

findConsumer()

Objective: Find the people in top20 who redeemed

What's happening inside?
    i) Opening moreSpentOverTime
    ii) Opening coupon_redem.csv
    iii) In Both, we find the people who have redeemed
    iv) Storing it in Consumer_coupon_redemp.yaml

Output:

Consumer_coupon_redemp.yaml

['1':
- '10000085364'
'1011':
- '10000085427'
'1020':
- '50000540082'
'1074':
- '10000085425'
'1098':
- '51111075533'
'113':
- '53500000076'
'1142':
- '51111120076']
---------------------------------------------------------------
couponDetails()

Output:

couponUPC_ProductID.yaml

['10000085361': '105358'
'10000085363': '5592689'
'10000085364': '2281854'
'10000085369': '1115451'
'10000085378': '12385916'
'10000085425': '14077327'
'10000085426': '1104659'
'10000085427': '961866']
---------------------------------------------------------------

productDetails()

Output:


productDetails_couponsRedeemed.yaml

[
'1':
- '10000085364'
'1011':
- '10000085427'
'1020':
- '50000540082'
'1074':
- '10000085425'
'1098':
- '51111075533'
]
---------------------------------------------------------------


```
---------------------------------------------------------------

## Release Notes
#### `v1.0.0`

## Contributors
[Rick](https://github.com/ludwigwittgenstein2)
