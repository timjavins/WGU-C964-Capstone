Project Proposal

## Problem
With the rising costs of living, unattainable single-family house prices, the increasing wealth chasm between rich and poor, and the ever-busier American lifestyle, Americans need a new entry point to wealth development. Though innovative companies, such as Robinhood and Acorns, have lowered the difficulty for Americans to invest, they still lack the time to investigate opportunities and actively participate during the work week. Americans need to make data-driven investment decisions without the ability to collect the data, much less analyze it.

LendingClub and PYMNTS.com published *Reality Check: The Paycheck-To-Paycheck Report* in March 2022, which highlighted how rising costs and economic shifts are impacting people's ability to save and invest. Most importantly, the report revealed that **61% of Americans live paycheck-to-paycheck**. Fusing this data with population data from the US Census Bureau, there are over 208 million people who would benefit from a solution to this problem, including over 45 million children. This means there are more than 162 million adults who may resonate with small-scale investment opportunities. (U.S. Census Bureau, 2024) 

The US Census Bureau lists about 78 million households (59%) earning less than $100,000 per year. In estimating the annual buying power of the paycheck-to-paycheck group, it would be simple to assume the lowest income bracket and derive from that demographic. However, an estimate of *$9.233 trillion*--based on 80,642,000 households and the average income of $114,500 (U.S. Census Buerau, 2024)--is supported by the fact that the *Reality Check* survey group included a significant number of **_individuals_** earning *over $100,000* annually. Notably, there was also a significant number who expressed interest in investing but felt barred by high entry points or lack of knowledge. This emphasizes the importance of creating accessible investment opportunities that cater to those starting with just a few dollars.

Younger generations, especially Millennials and Gen Z, are particularly intriguing here. They are tech-savvy, comfortable with apps, and open to non-traditional financial avenues. Even with limited funds, they show a keen interest in micro-investing platforms that allow them to start with as little as $1. This taps into a desire many have to take control of their financial destinies, even when starting small.

Still, many people hesitate to invest because it feels intimidating, complicated, or unfamiliar. Simplifying investment processes could empower them to get started. 

Global Investment Solutions does not currently present a low-cost offering for the cash-strapped, timebound, unsophisticated majority of American would-be investors. While not investment savvy, these holders of trillions of dollars are often tech-savvy and find advanced analytics enticing.

## Solution
On a related note, exploring community-driven investment models or social features could amplify engagement. People often feel more confident and motivated when they can share experiences and progress with peers. Gamification elements might also make investing feel more accessible and even enjoyable.

By zeroing in on this demographic, you're tapping into a movement of people ready to grow, learn, and invest in their futures—even if they're starting with just a few dollars. It's about building bridges between where they are now and the financial stability they aspire to achieve. Imagine focusing on Americans who are juggling tight budgets but are eager to dip their toes into investing, even if it's just spare change. These are individuals often earning between $20,000 and $50,000 annually. They're not swimming in disposable income, but they've got that spark to grow their financial future bit by bit.

Expanding your project to engage this group could have a profound impact. Not only does it open up a vast market, but it also contributes to greater financial inclusion and empowerment.

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