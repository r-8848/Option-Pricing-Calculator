# Option Pricing Calculator

Welcome to the Option Pricing Calculator! This Django web application allows you to calculate the price of call and put options for stocks using different models. You can choose between the Two-Step Binomial Model, the N-Step Binomial Model, and the Black-Scholes Model to perform your calculations.

## Features

- **Two-Step Binomial Model**: Calculates option prices using a two-step binomial tree.
- **N-Step Binomial Model**: Allows you to specify the number of steps for a more detailed calculation.
- **Black-Scholes Model**: Uses the Black-Scholes formula to calculate option prices.

## Getting Started

### Required Libraries Installation if needed
You can install the required libraries using pip:

```bash
pip install django numpy pandas matplotlib

### Usage

1. **Choose a Model**: On the home page, select one of the three models:
   - Two-Step Binomial Model
   - N-Step Binomial Model
   - Black-Scholes Model

2. **Enter Stock Information**: Provide the necessary details for the stock and the option, such as:
   - Current stock price
   - Strike price
   - Time to expiration
   - Volatility
   - Risk-free interest rate
   - Dividend yield (if any)

3. **Calculate Option Price**: Click the button to calculate the option price. The result will display the prices for both call and put options

