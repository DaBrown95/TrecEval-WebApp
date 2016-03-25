# TrecEval-WebApp

http://trec.nist.gov

"The purpose of this application is to provide a tool that lets researchers evaluate how good their search system is and how it compares to other systems (already submitted)."

## Setup Instructions

To install requirements… pip install -r requirements.txt

To add requirements… pip freeze > requirements.txt

Population Script for the database exists in TrecEval folder, usage is

1. First use Django's makemigration followed by migrate to create the datbase
2. Next, use python populate_trecapp.py to populate the database. The requirements file will need to be installed before
this works correctly as it makes use of fake-factory().

Default users are bob, jill and jen. Passwords are respective of usernames.
Population script add's another 500 users to the database.

### Team Members - TRECies

| GitHub Username | Name | Matric Number|
|-----------------|:----:|-------------:|
|DaBrown95        |David |2137184b      |
|robbmcquiston    |Robb  |2136188       |
|joelever         |Joe   |2079568L      |
|NSaiyara         |Noshin|2167932       |

Changes since presentation are all commits from approx midday on the 22/03/2016 onwards.

