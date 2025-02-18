Project Proposal

Problem
Global Investment Solutions has helped its clients find appropriate investments for many years. With the increasing complexity of stock markets and the need for data-driven decision-making, many of our clients have been asking for more sophisticated tools to analyze stock prices and optimize their trading strategies. A recent article by Forbes highlighted the importance of leveraging machine learning and data analytics in financial markets to stay competitive. It’s crucial for our company to be equipped and ready for this evolving landscape.

As of today, Global Investment Solutions is not equipped with the advanced tools required to guide our clients in making data-driven investment decisions. Currently, our main offerings within the financial advising space are focused on traditional analysis methods. Many of our customers are more tech-savvy and would like to utilize advanced analytics for higher accuracy in their investments. This is an area we are currently lacking.

Solution
I believe we can enhance our business’s offerings with a new data product. This data product will enable the analysis of stock prices and the implementation of trading strategies. The Stock Price Analysis and Trading Strategy Platform will enable our employees to get the information they need to successfully recommend the best times for our customers to make stock investments. They will be able to make better-informed decisions that will lead to higher quality financial advisement.

This tool will display stock price data in several ways that will give a clear look at the current price trends. Based on these trends, we can make recommendations to those customers looking to optimize their stock portfolios. I believe this product will enable our company to branch out and create new revenue streams. This will also give us a competitive advantage over our competitors that don’t offer advanced data analytics.

Outline
The data product will be a standalone application written in the open-source programming language Python. It will support industry-appropriate security features such as a login page. The home page will be a dashboard with all the visual data in one place. A line graph will chart the stock price over time. A bar graph will display the daily volume of stock trades. There will be a section that displays potential future prices. This section will get its data from training a machine learning algorithm on past prices. It will use an XGBoost regression model to plot future data points based on price history.

Data Description
The data used to construct this product will be sourced from Yahoo Finance. This data includes daily price data such as:

• High (Integer)
• Low (Integer)
• Open (Integer)
• Close (Integer)
• Volume (Integer)
• Date (Text)

The product will pull fresh data every time it is launched, and then will store this data into a local
database. The data is limited in that it is single day price data. The product won’t have access to highly
detailed data, such as price changes every minute or second. Thus, high frequency trading is out of the
scope of this project.

Objectives and Hypothesis
There are several objectives of this product. One of the main objectives is to ensure the user of the
software has the most up to date and accurate data related to stock pricing. Another important
objective is to process and then visualize this raw data to make it useful. This will help to accomplish
our other main objective which is to improve our employees' decision-making abilities with the
processed information. These all work to solve the ultimate priority of our business, which is to provide
the highest level of customer service by providing our clients with the highest return on their
investments.

My hypothesis is that through XGBoost regression, semi-accurate price predictions can be obtained. This
future price data will enable our company to make better decisions for our clients. I believe if this
product is built and maintained, then both our company’s revenue and our client’s satisfaction level will
greatly improve.

Project Methodology
This project will use the Waterfall Methodology. This methodology was chosen because the
requirements for the project are well defined. The product's feature set is not overly complicated, so a
straightforward and linear methodology will work best. This will keep development on track and
enable delivery of the completed software on time and within budget. The following describes which
parts of the project align with this methodology’s phases:

1. Requirements – During this phase, we will meet with the end users of the proposed product and
gather all the requirements.

2. Design – Then, a design will be created that ensures all the requirements from the previous
phase are met.

3. Implementation – During this phase, the code will be written ensuring it adheres to both the
requirements and design.

4. Verification – Once the code is complete, a working version will be given to the end users to
ensure the product does what it is supposed to do.

5. Maintenance – As the end users use the product, any bugs, inadequate features, or other errors
will be fixed as needed.

Funding requirements
The majority of the product is created using free open-source software and tools. However, costs will
arise from several areas. The software developer team will consist of one software developer. The
estimated hours the project will take is ~110 hours. At $100/hour the developer’s salary will cost
$11,000. Upfront costs for acquiring the equipment the developer will need is estimated at $3,000.
Additionally, maintenance costs will be roughly $100/hour for 24 hours per year onward. So, this
product will require a total of $14,000 of upfront costs to get a working product plus an additional
$2,400 per year.