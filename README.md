### Authors: Freddy Martinez & Joseph Burnitz

# Python Date Stripper

I recently received a log of every single FOIA request that Chicago Police Department has received. This python code is to parse the dates of the requests and do some quick calculations on the log. Read in the dates, add the number of business days since it was received (use a custom calendar due to Chicago having non-standard holidays for local reasons) and calculate when responses are due. This should give us a first order approximation. Also in the interest of transparency, this is a public git repo so that others can check my work. 

## Files In Repository
 * analysis.py does the meat of the calculations
 * negativedays.txt are requests that are completed before they are received, likely a typo on CPD's end
 * data.csv_original is the original data we got from CPD, we exported the excel speadsheet to a csv.
 * dava.csv some slight modifications to the original, you can diff them to see how much we had to clean up the data
 * compliance_distribution.csv shows how long it took CPD to complete a request. 70% are completed within a day.
 * chicago_observed_holiday is a text file that includes the business holidays that City of Chicago observers, there are more days than the federal holidays.  

tl;dr how often is CPD out of compliance with FOIA law.
with example dataset returns, including some erroneous entries:
compliant:  13636  Non Compliant >5 days:  2119  Percent violated:  13.4496985084
