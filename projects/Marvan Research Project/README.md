### Introduction

#### Marvan, a strategic think tank, has asked your company to build a catalog of open data at the **national** level for the following countries:
- [United States](https://catalog.data.gov/dataset/?q=&sort=views_recent+desc&ext_location=United+States&ext_bbox=-124.733253%2C24.544245%2C-66.954811%2C49.388611&ext_prev_extent=)
- [United Kindom](https://www.data.gov.uk/)
- [Canada](https://search.open.canada.ca/opendata/)
- [Singapore](https://data.gov.sg/)

They are investigating the relationship between pharmaceutical development and drug abuse and drug crimes. They would like for you to retrieve the data related to *drugs*, *pharmaceuticals*, *drug crimes*, and *drug-related social problems* in the following categories:
 - Health and Well-Being
 - Crime and Justice
 - Social

A listing of the datasets they have identified as relevant to the project can be found in `<this csv file>`.    

Marvan would like the data to be stored in this format:    

| Country | Category | Dataset Name | Last Updated | Data |    
 ------ | ------- | ------- | -------- | ---------- 
| Canada  | Health | Drug Product Database | 5/8/2025 | `<data>`
| Singapore | Social | Information on Quantity of Controlled Drugs Seized | 12/9/2022 | `<data>` |

They would like to be able to retrieve the data based on a combination of filters for Country, Category, and keyword (Dataset Name)

### Process

#### Plan your approach for getting and storing the data and then execute that plan.
1. Look at each site to determine what data is available for the two areas of interest and how that data can be accessed.
2. Decide where you will store the data.
3. Create a repo that you connect to your chosen cloud provider.
4. Get the data and store it in the cloud.

#### Create a pipeline that performs ELT
1. Read the data from the cloud.
2. Clean the data.
3. Store the cleaned data in a data warehouse.
4. Use SQL to transform the data as needed.
5. Simulate reverse ETL by moving the data from the data warehouse into an OLTP database (in the real world this could be salesforce, or other operations SAAS tools).

#### Create an API in Python that Marvan researchers can use (in place of step 5 above) to acquire data from the data warehouse. 
*Do not worry about advanced features here, ie - auth, middleware, etc.*

### Stretch Goal
- Deploy the API you created using Github Actions