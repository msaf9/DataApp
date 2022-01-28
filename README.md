# Stock Data App
Design and development of Stock Data application using object-oriented programming language and libraries.

## Table of contents
1. Introduction
2. Technologies
3. Project status
4. Installation
5. License

## Introduction
Stock Data App helps to visualize the [8855 ticker's](tickers.csv 'Tickers') (stock) Close and Volume from a given date to date.

### Usage
```
How to use the App?
1. Select a ticker symbol from the drop-down.
2. Select From and To date from the Calendar widget.
3. Scroll down and watch out for Stock Close and Volume.
```

### Deployment details
Deployed on Heroku.

### Stock Data App's URL 
> [Stock Data App](https://stock-data-app-streamlit.herokuapp.com/ 'Stock Data App')

## Technologies
- Python
- streamlit
- pandas
- yfinance
- get-all-tickers
- Git
- Heroku

## Project status
> **Completed**

### Versions
1.0.0 (**Beta**)
- First version.

1.0.1 (**Live**)
- Updated libraries to fix [JSONDecodeError](https://discuss.streamlit.io/t/json-decoder-jsondecodeerror/14830).

1.1.0 (**Current stable version**)
- Default FROM value feature added.

## Installation
### Get repository
```git
git clone https://github.com/msaf9/DataApp.git
cd DataApp
```

### Compile and run
#### Using Conda env
```conda
conda activate env_name
pip install streamlit
streamlit run main.py
```

## License
[MIT License](LICENSE)
