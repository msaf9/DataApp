<h1>Market Summary</h1>
Design and development of Market Summary application using object-oriented programming language and libraries.

<h2>Table of contents</h2>

- [Introduction](#introduction)
  - [Usage](#usage)
  - [Deployment details](#deployment-details)
  - [Stock Data App's URL](#stock-data-apps-url)
- [Technology Stack](#technology-stack)
- [Project status](#project-status)
  - [Versions](#versions)
- [Installation](#installation)
  - [Get repository](#get-repository)
  - [Compile and run](#compile-and-run)
    - [Using Conda env](#using-conda-env)
- [License](#license)

## Introduction
Market Summary App helps to visualize the [8855 ticker's](tickers.csv 'Tickers') (stock) Close and Volume from a given date to date.

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
> [Market Summary App](https://market-summary-app.herokuapp.com/ 'Market Summary App')

## Technology Stack
- Python
- Libraries
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

1.1.0 (**From label added**)
- Default FROM value feature added.

1.1.1 (**Current stable version**)
- Modified headers and titles.

## Installation
### Get repository
```git
git clone https://github.com/msaf9/market-summary.git
cd market-summary
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
