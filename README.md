# Purchasing power evolution in Argentina
Socioeconomic analysis of Argentina focused on purchasing power, examining how **inflation, wages, housing costs, and interest rates** have shaped and impact on **living conditions** in recent years. The **tools used** for this analysis were **Python, Excel and Power BI**. 

## Project Overview

This project presents a data-driven socioeconomic analysis of Argentina, focused on understanding how cost of living and purchasing power have evolved over time.
The primary objective is to compare the evolution of wages against key cost indicators such as inflation and housing (rental prices), in order to assess changes in economic pressure on households. Special attention is given to housing affordability and overall cost-of-living dynamics.

Additionally, the project explores the role of financial variables such as interest rates and exchange rates, providing context on how macroeconomic conditions may influence consumption and access to credit.
Beyond the analysis itself, this project also highlights the limitations and challenges of working with official public datasets (e.g., INDEC, Central Bank), particularly in terms of consistency, methodology changes, and data availability.

This work is intended as a foundational analysis, designed to support future extensions incorporating additional dimensions such as education, health, and broader social indicators.

## Economic Context & Objective

Argentina has experienced persistent macroeconomic instability over the past decade, characterized by high inflation, currency depreciation, and recurrent adjustments in monetary policy.
Since 2016, different economic frameworks have shaped the evolution of key variables such as wages, prices, and access to housing. These dynamics have had a direct impact on purchasing power and household financial stability.

In this context, understanding how wages evolve relative to the cost of living becomes critical. Rising inflation, increasing rental prices, and volatile financial conditions can significantly affect consumption capacity and overall quality of life.
The objective of this analysis is to quantify these dynamics by comparing wage growth against inflation and housing costs, while incorporating financial indicators such as interest rates and exchange rates to provide additional macroeconomic context.

Rather than focusing on short-term fluctuations, this project aims to identify structural trends that help explain changes in economic pressure on households over time. These dynamics have unfolded under different economic policy approaches over time.

## Content Table

1.	[Project Overview](#project-overview)
2.	[Economic Context & Objective](#economic-context--objective)
3.	[Dashboard Preview](#dashboard-preview)
4.	[Key Insights](#key-insights)
5.	[Data Sources](#data-sources)
6.	[Data Preparation](#data-preparation)
7.	[Challenges & Limitations](#limitations--assumptions)
8.	[Conclusions](#conclusions)
9.	[Terminology & Dashboard Use](#terminology--dashboard-use)

## Dashboard Preview

The following dashboard provides an interactive view of the main indicators analyzed in this project.
It is composed of four main visual components (one of which includes interactive buttons on the side):

- A line chart displaying the evolution of purchasing power over time, along with housing burden and overall cost-of-living burden.
- A comparative table showing RIPTE (registered wages) against the basic food basket and different household basket levels.
- A second line chart illustrating the evolution of key interest rates (BADLAR and personal loans).
- A bar chart, ordered by descending year, representing the evolution of the exchange rate.

Additionally, the dashboard includes smaller supporting elements such as KPI cards in the top-right corner (highlighting current BADLAR, personal loan rates, and exchange rate values), as well as a period filter to dynamically explore the data.

![Dashboard preview](images/dashboard_preview.png)

## Key Insights

### Purchasing power

![Purchasing power 2017-21](images/purchasing_power_2017-21.png)

![Purchasing power 2021-26](images/purchasing_power_2021-26.png)

### Housing burden index

![Housing burden 2021-26](images/housing_burden_2021-26.png)

### Living cost burden index

![Living cost burden 2017-21](images/living_cost_2017-21.png)

![Living cost burden 2021-26](images/living_cost_2021-26.png)

## Data Sources

## Data Preparation

## Limitations & Assumptions

## Conclusions

## Terminology & Dashboard Use

The main dashboard is presented in Spanish, as the primary audience of this analysis is local. This glossary is intended to facilitate interpretation for non-Spanish-speaking readers. Below is a reference guide for key terms used throughout the project:

| English Term | Spanish Term | Description |
|-------------|-------------|------------|
| Purchasing Power | Poder Adquisitivo (PA) | Real income adjusted by inflation |
| Inflation | IPC (Índice de Precios al Consumidor) | Consumer price index |
| Housing Cost | ICL (Índice de Contratos de Locación) | Rental price index |
| Housing Burden | Esfuerzo de vivienda | Relative cost of housing vs wages |
| Living Cost Burden | Esfuerzo económico | Relative cost of living vs wages |
| Living Cost | Costo de vida | General price level (proxied by IPC) |
| Salary Index | Índice de salarios | Wage index (INDEC) |
| Wages (RIPTE) | RIPTE | Registered private sector wages (may overestimate average income) |
| Basic Food Basket | Canasta Básica Alimentaria (CBA) | Minimum food consumption (indigence line) |
| Total Basic Basket | Canasta Básica Total (CBT) | Poverty threshold |
| Household Basket | Canasta básica hogar | Estimated cost for a representative household |
| Interest Rates | Tasas de interés (BCRA) | Monetary and financial rates |
| Exchange Rate | Tipo de cambio | ARS/USD reference rate |
| Personal Loans | Préstamos personales | Consumer credit rates |
| BADLAR | BADLAR | Interest rate for large deposits (banking system reference) |

Basic instructions for extra information:

Place the cursor over "?" bottom to read the equivalent adult rate used for the household basket

![Instructions 1](images/instructions_1.png)

Place the cursor over the dashboard to read the description for each household basket

![Instructions 2](images/instructions_2.png)

