# NPPES Project

You work for a healthcare analytics company interested in identifying the healthcare providers located in each US county.

### Part 1
You've been provided the first 1000 rows from the April 2025 NPPES Data Dissemination File. 

* 'NPI' 
* Entity Type, indicated by the 'Entity Type Code' field:
    - 1 = Provider (doctors, nurses, etc.)
    - 2 = Facility (Hospitals, Urgent Care, Doctors Offices) 
* Entity Name: Either First/Last or Organization or Other Organization Name contained in the following fields:
    - 'Provider Organization Name (Legal Business Name)'
    - 'Provider Last Name (Legal Name)'
    - 'Provider First Name'
    - 'Provider Middle Name'
    - 'Provider Name Prefix Text'
    - 'Provider Name Suffix Text'
    - 'Provider Credential Text'
* Practice Address: Use the Business Practice Location (not the mailing address) found in:
    - 'Provider First Line Business Practice Location Address'
    - 'Provider Second Line Business Practice Location Address'
    - 'Provider Business Practice Location Address City Name'
    - 'Provider Business Practice Location Address State Name'
    - 'Provider Business Practice Location Address Postal Code'
* The provider's taxonomy code, which is contained in one of the 'Healthcare Provider Taxonomy Code*' columns. A provider can have up to 15 taxonomy codes, but we want the one which has Primary Switch = Y in the associated 'Healthcare Provider Primary Taxonomy Switch*' field. Note that this does not always occur in spot 1.

You can find taxonomy code details (Grouping, Classification, and Specialization) in the NUCC Taxonomy file. Add in the Grouping, Classification, and Specialization for each provider.

To associate each provider with a county, you've been given:
- A ZIP code to county crosswalk file
- A FIPS code to county name crosswalk
- 2025 population figures from the U.S. Census

**Note:** Some ZIP codes cross county boundaries. In those cases, assign the county with the larger population, according to the provided 2025 figures.

### Part 2

Now, scale what you have to the full NPI Data Dissemination file. Create stored procs that can be used to process the data in chunks and add it to the database.

