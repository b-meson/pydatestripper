# Python Date Stripper

I recently received a log of every single FOIA request that Chicago Police Department has received. This python code is to parse the dates of the requests and do some quick calculations on the log. Read in the dates, add the number of business days since it was received (use a custom calendar due to Chicago having non-standard holidays for local reasons) and calculate when responses are due. This should give us a first order approximation. Also in the interest of transparency, this is a public git repo so that others can check my work. 

tl;dr how often is CPD out of compliance with FOIA law.
with example dataset returns, including some erroneous entries:
compliant:  12709  Non Compliant >5 days:  3046 
