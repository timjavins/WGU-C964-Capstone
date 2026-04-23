# Post-Implementation Report
## Stakeholder Impact

This project created value for all stakeholders. End users—particularly those living paycheck-to-paycheck—stand to benefit from an accessible, low-cost investment platform that simplifies data-driven decision-making and lowers the entry barrier to investing. By delivering actionable buy/sell signals, the model proved the potential to empower users to make investment choices, ultimately improving financial outcomes. 

For internal stakeholders, such as executives, product managers, and technical leads, the iterative Agile process ensured continuous improvement and swift adaptation to feedback, fostering innovation and operational efficiency. Overall, the project proved not only the potential to enhance customer satisfaction and financial inclusion but also to position Global Investment Solutions to capture new market opportunities and drive sustainable growth.

## Solution Summary 

The Ensemble Model showed that it is possible to bridge the gap between raw financial data and investor insights by orchestrating end‑to‑end data management—from data pulling and preprocessing to model training and prediction. This approach ensured technical feasibility while addressing the business need for a simple yet effective investment decision tool.

The Ensemble Model implemented an end-to-end pipeline:
- It downloaded raw stock and S&P 500 data from Yahoo Finance.
- It performed data preprocessing (dropping NaNs, converting types, engineering features like returns, volatility, and momentum).
- It trained an XGBoost regression model to predict the following day's return.
- It backtested the trading strategy and computed key performance metrics, such as Mean Squared Error, Sharpe, Sortino, and Calmar ratios.

This full-cycle approach provided an accessible investment signal generation and validation system, addressing both the problem of information overload and the need for actionable insights.

## Data Summary

#### Data Governance & Privacy Considerations
The application pulled its data from API calls and stored it local to the model for further processing. The project relied exclusively on publicly available data sourced from Yahoo Finance API calls, which contained no personally identifiable information, so there were no concerns regarding PII or customer data privacy.

However, the project team considered future development advances and prepared the deliverables to be safeguarded in the proprietary aspects of the model, including its configurations, training data, and performance metrics. The team prepared measures such as secure storage, regular access audits, and proper version control to be implemented, ensuring that intellectual property and model integrity remain protected against unauthorized access or misuse. These precautions helped maintain data governance standards and secure the transition from a proof-of-concept to a production-ready platform.

**Collection:** The application downloaded stock data for tickers such as AAPL (Apple) and ^GSPC (S&P 500) within defined date ranges.  
**Preprocessing:** The application read and cleaned the data, dropping missing values and specific rows. Some columns were renamed/retyped.  
**Feature Engineering:** The application created new columns, such as Return, Volatility, and Momentum, and computed new values for these columns in order to capture the key predictors.  
**Management:** The application save processed data at multiple stages as CSV files, providing a layer of versioning through the design, development, and testing phases.  

## Machine Learning

**Method Employed:**  
**XGBoost Regression Model**

**What:**  
The Extreme Gradient Boosting (XGBoost) model was used to predict the next day’s stock return based on features such as Volatility and Momentum.

**How:**  
The model was trained via the following process.

The engineered features were split into training and test sets to evaluate the model's performance effectively. This process involved dividing the dataset into two distinct subsets:

- **Training Set:** This subset was used to train the XGBoost model. It included a portion of the data with known outcomes, allowing the model to learn the relationships between the features (such as Volatility and Momentum) and the target variable (next day's stock return). By exposing the model to a variety of data points, it could identify patterns and make accurate predictions.

- **Test Set:** This subset was used to evaluate the model's performance after training. It consisted of data that the model had not seen during the training phase. By assessing the model's predictions on this unseen data, we could gauge its ability to generalize and perform well on new, real-world data. The test set provided an unbiased evaluation of the model's accuracy and helped identify any overfitting issues.

Splitting the data into training and test sets ensured that the model's performance metrics, such as Mean Squared Error, reflected its true predictive capabilities and not just its ability to memorize the training data.

The model was constructed with an objective of `reg:squarederror`, which means it aimed to minimize the squared differences between the predicted and actual values, a common objective for regression tasks. This objective function helps the model focus on reducing large errors, leading to more accurate predictions.

Additionally, the model was trained with a high number of estimators, meaning it used a large number of boosting rounds to iteratively improve the model's performance. Each estimator in the boosting process corrected the errors of the previous ones, allowing the model to capture complex patterns and relationships in the data. This approach enhanced the model's ability to generalize and make accurate predictions on unseen data.

After the XGBoost model was trained, it was used to make predictions on the test set. These predictions represented the model's forecast of the next day's stock returns based on the features it had learned during training. The accuracy and effectiveness of these predictions were then evaluated using performance metrics, with Mean Squared Error (MSE) being a primary metric.

- **Predictions:** The model generated predicted values for the target variable (next day's stock return) for each data point in the test set. These predictions were compared to the actual observed values to assess the model's accuracy.

- **Evaluation:** The performance of the model was quantified using Mean Squared Error (MSE). MSE measures the average squared difference between the predicted values and the actual values. It is calculated as follows:

  ```python
  from sklearn.metrics import mean_squared_error

  mse = mean_squared_error(actual_values, predicted_values)
  ```

  Where `actual_values` are the true stock returns from the test set, and `predicted_values` are the returns predicted by the model.

- **Mean Squared Error (MSE):** MSE is a widely used metric for regression tasks. It penalizes larger errors more than smaller ones, making it sensitive to outliers. A lower MSE indicates that the model's predictions are closer to the actual values, signifying better performance. The formula for MSE is:

  \[
  \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
  \]

  Where \( n \) is the number of data points, \( y_i \) are the actual values, and \( \hat{y}_i \) are the predicted values.

By computing the MSE, the model's predictive accuracy was quantitatively assessed, providing a clear measure of how well the model performed in predicting stock returns. This evaluation helped identify areas for improvement and ensured that the model was reliable for making investment decisions.

**Why:**  
XGBoost was chosen because it is a powerful ensemble technique suitable for time series predictions. Its ability to model complex, non-linear relationships in financial data helped generate actionable buy/sell signals, making it an appropriate choice for the project’s goal of outperforming traditional strategies.

After the proof-of-concept model is validated, development teams could also explore community-driven investment models or social features that would amplify engagement. People often feel more confident and motivated when they can share experiences and progress with peers. Gamification elements might also make investing feel more accessible and enjoyable.

The model will need to update its training frequently, perhaps monthly or weekly. To demonstrate why, two versions of the model are provided with different performance time horizons.

## Validation

The model's performance was validated using MSE and established investment performance metrics. 
### Backtesting Performance Metrics

- **Backtesting Performance Metrics:**  
  The model's performance was further validated using several key financial metrics during the backtesting phase. These metrics provided a comprehensive evaluation of the trading strategy's effectiveness compared to the S&P 500 benchmark:

  - **Sharpe Ratio:**  
    The Sharpe Ratio measures the risk-adjusted return of the trading strategy. It is calculated by dividing the excess return (return above the risk-free rate) by the standard deviation of the returns. A higher Sharpe Ratio indicates better risk-adjusted performance. The formula is:

    \[
    \text{Sharpe Ratio} = \frac{R_p - R_f}{\sigma_p}
    \]

    Where \( R_p \) is the portfolio return, \( R_f \) is the risk-free rate, and \( \sigma_p \) is the standard deviation of the portfolio return.

  - **Sortino Ratio:**  
    The Sortino Ratio is similar to the Sharpe Ratio but focuses only on downside risk (negative returns). It is calculated by dividing the excess return by the downside deviation. This metric provides a more accurate measure of risk-adjusted performance for strategies that aim to minimize losses. The formula is:

    \[
    \text{Sortino Ratio} = \frac{R_p - R_f}{\sigma_d}
    \]

    Where \( \sigma_d \) is the downside deviation.

  - **Calmar Ratio:**  
    The Calmar Ratio measures the risk-adjusted return by comparing the annualized return to the maximum drawdown (largest peak-to-trough decline). A higher Calmar Ratio indicates better performance relative to the risk of significant losses. The formula is:

    \[
    \text{Calmar Ratio} = \frac{\text{Annualized Return}}{\text{Maximum Drawdown}}
    \]

  - **Annualized Return:**  
    The Annualized Return represents the geometric average of the returns over a year, providing a standardized measure of the strategy's performance. It allows for comparison with other investments and benchmarks like the S&P 500. The formula is:

    \[
    \text{Annualized Return} = \left( \prod_{i=1}^{n} (1 + R_i) \right)^{\frac{252}{n}} - 1
    \]

    Where \( R_i \) are the daily returns, and \( n \) is the number of trading days.

These metrics were calculated and compared against the S&P 500 benchmark to evaluate the trading strategy's performance. The model's ability to generate risk-adjusted returns was assessed by using these comprehensive performance metrics. This thorough validation process provided a sober degree of confidence in the model's real-world applicability and robustness.

## Visualizations

The application generated several visualizations in its final phase. 
 - **Candlestick Charts:** Using the `plotly` library, one chart was generated for the Apple stock and another for the S&P 500. These two charts showed the price movements over the testing period, which provided context for the real-world performance of these two investment vehicles.

 - **Line Charts:** Two line charts showed the comparative cumulative returns, generated with the `matplotlib` library.
 
 The first chart visualized the trading strategy's performance in comparison to the S&P 500 index. While the S&P 500 outperformed the EM, there were some periods in which the EM outperformed the index.
 
 The second chart was similar but compared the cumulative strategy return on Apple stock versus the cumulative market return—reflective of a buy-and-hold strategy—on Apple stock. This chart was very insightful as it proved the model generated performant trading signals and outperformed the Apple stock's market return.
 
 - **Bar Charts:** The application used the `plotly` library to generate two bar charts, each representing the application's generated performance metrics.

 The first bar chart showed the Calmar Ratios for the trading strategy and the S&P 500 over the testing period. The higher Calmar ratio of the S&P 500 reflected the less volatile nature of the diversity in the index: the stocks of the top 500 companies. Naturally, the single-stock strategy employed by the model in this proof-of-concept was more volatile, resulting in a lower Calmar ratio.

 The second bar chart showed the other performance metrics for each strategy, including Sharpe Ratio, MDD, Annualized Return, and Sortino Ratio. All four metrics showed investing in S&P 500 ETFs was a less volatile, more profitable strategy. For example, the MDD was larger in the Apple strategy and the Annualized Return was smaller. This difference was reflective of the Calmar Ratio and highlighted the advantage of diversification in the S&P 500 Index.
