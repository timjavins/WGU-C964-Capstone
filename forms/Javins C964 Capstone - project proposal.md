Project Proposal

## Problem
With the rising costs of living, unattainable single-family house prices, the increasing wealth chasm between rich and poor, and the ever-busier American lifestyle, Americans need a new entry point to wealth development. Though innovative companies, such as Robinhood and Acorns, have lowered the difficulty for Americans to invest, people still lack the time to investigate opportunities and actively participate during the work week. Americans need to make data-driven investment decisions but lack the ability to collect the data, much less analyze it.

LendingClub and PYMNTS.com published *Reality Check: The Paycheck-To-Paycheck Report* in March 2022, which highlighted how rising costs and economic shifts are impacting people's ability to save and invest. Most importantly, the report revealed that **61% of Americans live paycheck-to-paycheck**. Fusing this data with population data from the US Census Bureau, there are over 208 million people who would benefit from a solution to this problem, including over 45 million children. This means there are more than 162 million adults who may resonate with small-scale investment opportunities. (U.S. Census Bureau, 2024) 

The US Census Bureau lists about 78 million households (59%) earning less than $100,000 per year. In estimating the **annual buying power** of the paycheck-to-paycheck group, it would be simple to assume the lowest income bracket and derive from that demographic. However, an estimate of **$9.233 _trillion_**--based on 80,642,000 households and the average income of $114,500 (U.S. Census Buerau, 2024)--is supported by the fact that the *Reality Check* survey group included a significant number of *individuals* earning *over $100,000* annually. Notably, there was also a significant number who expressed interest in investing but felt barred by high entry points or lack of knowledge. This emphasizes the importance of creating accessible investment opportunities that cater to those starting with limited resources.

Younger generations, especially Millennials and Gen Z, are particularly intriguing here. They are tech-savvy, comfortable with apps, and open to non-traditional financial avenues. Even with limited funds, they show a keen interest in micro-investing platforms that allow them to start with as little as a dollar. This taps into a desire many have to take control of their financial destinies, even when starting small.

Still, many people hesitate to invest because it feels intimidating, complicated, or unfamiliar. **Global Investment Solutions does not currently present a low-cost offering for the cash-strapped, timebound, unsophisticated majority of American would-be investors.** While not investment savvy, these holders of trillions of dollars are often tech-savvy and find advanced analytics enticing. Providing a head start and simplifying investment processes could empower them to get started.

## Solution

By zeroing in on this demographic, this proposed project is tapping into a movement of people ready to grow, learn, and invest in their futures—even if only starting with a few dollars. GIS can enable investment for Americans who are juggling tight budgets but are eager to dip their toes into investing, even if starting with spare change. Some of these individuals earn between $20,000 and $50,000 annually. Though not swimming in disposable income, they are collectively controlling trillions of dollars and the spark is there to grow their financial future, bit by bit. This is an entirely new market for GIS to enter.

To distribute financial intelligence to the masses, the solution needs to be copyable. To be copyable, it needs to be artificial. By training a machine learning algorithm on a given stock's performance over time, a machine can predict whether a stock price will rise or fall. This is the bare minimum of knowledge that an investor needs. By providing quality signals like this daily, GIS stands to not only open up a vast market but also contribute to greater financial inclusion and empowerment.

The Ensemble Model (EM), proposed now, will be an early-stage example of the power of mathematically modeling stock performance. This model will provide buy/sell signals that will be understood without a background in finance. Anyone subscribed to the product will be able to begin investing with a jumpstart, making trades with an easy buy/sell signal. These new GIS customers will be able to generalize to other GIS products and investment vehicles over time, as their wealth grows and their intuition develops. 

## Deliverables

The Ensemble Model will be written in the open-source programming language Python, utilizing the Extreme Gradient Boosting (XGBoost) library for creating and training an ensemble of decision tree-based models. It will generate daily trade signals, which can be integrated into the final User Experience-optimized product.

A line graph will chart the perfomance of a trading strategy following the model's signals over time. For comparison, the same line graph will also chart a simple buy and hold strategy applied to a Standard & Poor's 500 Index (S&P 500) exchange-traded fund (ETF). This will answer the question, "Can this strategy outperform the S&P 500?"

A bar graph will display various performance metrics comparing the model's strategy to the S&P 500. These metrics will be well-known indicators, including Calmar, Sharpe, and Sortino ratios, annualized returns, and maximum drawdown.

For context, candlestick charts will show daily summary price data, including open, close, high, low, range, and direction.

## Data Summary

The data used to train the models will be sourced from Yahoo Finance, including daily price data such as:

• High (floating point decimal)
• Low (floating point decimal)
• Open (floating point decimal)
• Close (floating point decimal)
• Volume (floating point decimal)
• Date (Text)

Because the project will rely exclusively on publicly available data sourced from Yahoo Finance, which contains no personally identifiable information (PII), there are no immediate concerns regarding PII or customer data privacy. All intellectual property developed in the project will be safeguarded in accordance with existing policies and best practices.

The raw stock data will be enriched through a feature engineering process that extracts key predictors for the ensemble model. The preprocessed data will be transformed by computing the daily return as the percentage change of the closing price, the volatility as the 21-day rolling standard deviation of these returns, and the momentum as the 21-day rolling average of the closing price. These engineered features will capture essential trends and fluctuations, and after dropping any missing values, they will form a clean dataset that serves as the foundation for training the Ensemble Model.

Once fully developed, the product will pull fresh data after the closing bell each day, saving the data in a secure location local to the Ensemble Model. However, the initial evaluation model will use static timeframes.

The data will be time-series data, limited to summary metrics for each day. This simple daily time interval will make for an easily understood entry point for new investors, but will have other benefits as well. A finer granularity, such as price changes by the minute or by the second, would present higher costs and information overload for the user. To avoid these complications and others resulting from potential pattern day trading (PDT), more granular data and higher frequency signals are out of scope for this project.

# Objective and Hypothesis

The primary objective of this project is to establish a baseline proof-of-concept in support of devloping a low-cost, accessible investment platform that empowers Americans, especially those living paycheck-to-paycheck, to make data-driven investment decisions. By utilizing machine learning algorithms, the platform will aim to simplify the investment process and provide users with actionable buy/sell signals. This will help users, particularly those with limited financial knowledge and resources, to start investing with confidence and gradually build their wealth.

The hypothesis is that the Ensemble Model can generate reliable buy/sell signals that outperform traditional investment strategies, such as a simple buy and hold approach, by utilizing an XGBoost machine learning model to predict stock price movements. By providing users with accurate and timely investment recommendations, the platform will not only improve their financial outcomes but also increase their confidence and participation in the stock market. This, in turn, will contribute to greater financial inclusion and empowerment for a broader demographic, ultimately leading to higher customer satisfaction and increased revenue for Global Investment Solutions.

# Project Methodology

Instead of following a strict, sequential process, the project will benefit from an Agile approach, which embraces an iterative and incremental cycle. This will allows for building, testing, and refining the investment platform continuously in close collaboration with stakeholders. Below is an outline of the Agile process for the project:

1. **Backlog Creation & Prioritization**  
   - Collaborate with key stakeholders (target users, product managers, and technical leads) to gather user stories and define acceptance criteria.  
   - Create and maintain a prioritized product backlog that captures functional requirements, enhancements, and potential technical improvements.  
   - Continuously update and refine the backlog based on new insights, user feedback, and market changes.

2. **Sprint Planning**  
   - Organize the work into short, time-boxed iterations (sprints), typically lasting two to four weeks.  
   - Select a set of user stories from the backlog that can be feasibly developed, tested, and delivered within the sprint.  
   - Define clear sprint goals and outline tasks, ensuring that each chosen story has well-defined criteria for completion.

3. **Iterative Development & Testing**  
   - Develop features in small increments through cross-functional teams that collaborate on design, coding, and immediate testing.  
   - Integrate unit tests, functional tests, and user acceptance tests into the development process.  
   - Leverage continuous integration to ensure that new code is consistently merged, built, and tested, reducing integration issues and enabling early detection of defects.

4. **Sprint Review & Demo**  
   - At the end of each sprint, demonstrate the working product increment to stakeholders.  
   - Gather feedback on new features, usability, and performance against the defined acceptance criteria.  
   - Discuss any required adjustments and incorporate this feedback into the backlog for upcoming sprints.

5. **Sprint Retrospective & Continuous Improvement**  
   - Conduct team retrospectives to analyze the sprint process, identify successes and challenges, and propose actionable improvements.  
   - Adjust processes and practices to enhance productivity, collaboration, and quality in future sprints.  
   - Use the lessons learned from each retrospective to streamline workflow and better align the product with user needs.

6. **Ongoing Release & Maintenance**  
   - As product increments reach a sufficiently refined state, prepare for regular releases that provide value to end users.  
   - Monitor performance, gather continuous user feedback, and address bugs or enhancement opportunities through additional sprints.  
   - Ensure the platform evolves with market demands and user expectations, sustaining an agile response to change over time.

# Timeline

| Milestone                                 | Duration                 | Projected Start Date | Anticipated End Date |
|-------------------------------------------|--------------------------|----------------------|----------------------|
| Backlog Creation & Prioritization         | 2 hours                  | Feb. 11, 2025        | Feb. 11, 2025        |
| Sprint Planning                           | 2 hours                  | Feb. 11, 2025        | Feb. 11, 2025        |
| Iterative Development & Testing (Sprint 1)| 4 hours                  | Feb. 12, 2025        | Feb. 12, 2025        |
| Sprint Review & Demo (Sprint 1)           | 1 hours                  | Feb. 13, 2025        | Feb. 13, 2025        |
| Sprint Retrospective & Continuous Improvement (Sprint 1) | 2 hours   | Feb. 13, 2025        | Feb. 13, 2025        |
| Iterative Development & Testing (Sprint 2)| 4 hours                  | Feb. 14, 2025        | Feb. 14, 2025        |
| Sprint Review & Demo (Sprint 2)           | 1 hours                  | Feb. 17, 2025        | Feb. 17, 2025        |
| Sprint Retrospective & Continuous Improvement (Sprint 2) | 2 hours   | Feb. 17, 2025        | Feb. 17, 2025        |
| Ongoing Release & Maintenance             | Ongoing                  | Feb. 18, 2025        | Ongoing              |

# Evaluation Plan

During the initial phase, each module—whether it be data collection, preprocessing, or feature engineering—will be subjected to unit tests to ensure that individual functions are performing as expected. As new features are created (for instance, those generated by the feature engineering process), unit testing will be employed to verify that the transformations correctly handle missing values and produce a clean dataset.

Once these modules are integrated, continuous integration will be used to merge, build, and test the complete codebase, reducing integration issues.

Subsequent integration testing will verify whether the interaction between modules (such as between data preprocessing, model training, and strategy implementation) is seamless.

At the end of each sprint, system testing will be carried out by simulating real-use cases. This will include backtesting the trading strategy by using historical data. The team will also perform user acceptance testing with stakeholders to ensure the product meets the defined requirements and usability expectations.

Finally, upon project completion, the overall validation will be conducted by comparing key performance metrics—including Mean Squared Error, Annualized Return, and Sharpe, Sortino, and Calmar ratios—against established benchmarks. These metrics will serve as objective measures to confirm that the Ensemble Model reliably produces buy/sell signals and meets the hypothesis that it can outperform certain traditional investment strategies.

This comprehensive evaluation plan ensures all aspects of the product will be robustly tested and validated before deployment.

# Funding Requirements

For establishing the Ensemble Model proof-of-concept, the funding requirements are kept to a minimum by leveraging open-source tools and a lean development process. Key funding elements include:

- **Development Resources:**  
  A significant portion will cover the developer’s time. For developing the EM, an estimated 25 to 40 labor hours at an estimated rate of $65 per hour results in a budget range of $1,625 to $2,600.

- **Infrastructure & Tools:**  
  Since the project utilizes open-source libraries (e.g., Python, XGBoost) and local-to-the-model data storage during development, infrastructure costs are minimal. The project will piggyback on mainline business infrastructure, including for version control and continuous integration pipelines. However, there is a potential cost in cloud hosting if needed for scalability tests.

- **Contingency & Miscellaneous Costs:**  
  A small contingency reserve (around 10-15% of the total estimated costs) will be set aside to address unforeseen expenses such as additional testing tools or minor cloud computing costs.

This modest budget supports an agile, iterative approach, allowing us to rapidly develop and refine the proof-of-concept before considering investment in a full-scale, production-ready platform.


