## Overview

    The system ingests search term data from Google Adwords into a S3 Data Lake, one possible format is CSV.
    
    Once ingested we score each search term with its Return On Ad Spend (ROAS). 
    
    ROAS = conversion value / cost

## The main application
    1. Monitors a directory for new csv files.
    2. When a file arrives, parse it and calculate the ROAS for each search term and write out
    a new csv file.
    3. Output file format :
    
        a. “processed/$currency/search_terms/$timestamp.csv” of the format:
        search_term, clicks, cost, impressions, conversion_value, roas

## Pre-requirements
    python 3
    virtual environment
    pip
    python-daemon

#####Once you have the source you can test the program by running

	$ make run
	
## Pip Installation

	$ pip install search-term-data==0.3
	



    
