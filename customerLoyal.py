#-*- coding: utf-8 -*-
"""
Build Loyal Customer Dictionary:
    What is Loyal Customer?
    A Customer who has bought continuously in supermarket.
    Where is this data?
    It is in Transaction data.
    How do you find if the customer is Loyal?
    If He purchases Every Week in Year, he is Loyal
    And he has a purchase average of above 50

"""

import csv
import yaml
import sys


customerTimesVisit = {}
customerLoyalty = {}
patronLoyals = []




def readCSV():
    global customerTimesVisit
    global customerLoyalty
    with open('/Users/Rick/Desktop/projectFinalFolder/segments/moreSpentOverTime.yaml','r') as f:
        moreSpentOverTime = yaml.load(f)
    f.close()

    with open('/Users/Rick/Desktop/CSV/transaction_data.csv','r') as f:
        data = csv.reader(f, delimiter=',')
        next(data)
        for row in data:
            if row[0] in moreSpentOverTime:
                    if row[0] not in customerLoyalty:
                        customerLoyalty[row[0]] =[]
                    else:
                        if int(row[9]) not in customerLoyalty[row[0]]:
                            customerLoyalty[row[0]].append(int(row[9]))
    f.close()

    for customer, newlist in customerLoyalty.items():
        customerTimesVisit[customer] = len(newlist)

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/customerTimesVisit.yaml','w') as w:
        w.write(yaml.dump(customerTimesVisit,default_flow_style=False))
    w.close()

def loyalCustomers():
    global patronLoyals
    with open('/Users/Rick/Desktop/projectFinalFolder/segments/customerTimesVisit.yaml','r') as r:
        customerTimesVisit = yaml.load(r)
    r.close()

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/customerAverageDictionaryPerson.yaml','r') as f:
        customerAverageDict = yaml.load(f)
    f.close()

    for row,value in customerTimesVisit.items():
        for household_id, average in customerAverageDict.items():
            if row == household_id:
                if value < 30 and float(average) < 40:
                    patronLoyals.append(["Non-Loyal Customer:","Household_id:"+ str(row),"Visits:"+ str(value),"Average Purchase:"+ str(average)])
                elif value < 80 and value > 40 and float(average) < 80:
                    patronLoyals.append(["Likely to be Loyal Customer:","Household_id:"+ str(row),"Visits:"+str(value),"Average Purchase:"+ str(average)])
                else:
                    patronLoyals.append(["Loyal Customer:","Household_id:"+ str(row),"Visits:" + str(value),"Average Purchase:"+ str(average)])

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/customerLoyalAverage.yaml','w') as w:
        w.write(yaml.dump(patronLoyals, default_flow_style=False))
    w.close()

def main():
    readCSV()
    loyalCustomers()

if __name__ == '__main__':
    main()
