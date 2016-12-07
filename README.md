# Kanban Card Metrics
Hacky python script to generate metrics for Kanban board using pysical cards. Expects an .xlsx spreadsheet with the started and finished dates for the your cards.

Spits out average cycle time data and a couple of useful charts (in .pdf format).

## Input Spreadsheet
* Must be names _carddata.xlsx_ and must be placed alongside kanbancardmetrics.py script
* Data must be on first sheet and must have the following columns:
    * ID - a unique card ID
    * Started - Date that work on card was started
    * Finished - Date that work on card as finished
    * Type - Type of card "Story", "Technical" etc etc
    
  All other columns are ignored  

## Installation
Requires Python 3.5 or greater

```
pip install pandas
pip install numpy
pip install pip install matplotlib
```

## Running the script

```
python kanbancardmetrics.py
```  

Stats will be dumped to console and two .pdfs charts will be generated