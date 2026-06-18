---
title: "Leveraging Open Data for Data Products across GC Web"
category: "Data Produts"

---

## Using Open Government Portal APIs
The Open Government Portal provides two main APIs that departments can use to bring content from `open.canada.ca` onto other web platforms.

**Metadata API**

The Metadata API contains information about datasets such as the title, description, and date last updated.

**DataStore API**

The DataStore API provides access to the actual tabular data for datasets that were uploaded directly to the system and passed validation checks for structural consistency.

### Atom Feeds

Each organization also automatically has an Atom feed of recent updates or new publications.

`https://open.canada.ca/data/feeds/organization/{organization_name}.atom`


Example:

`https://open.canada.ca/data/feeds/organization/tbs-sct.atom`



### CKAN API docs
These APIs are part of CKAN, the open source data platform used by the Open Government Portal. 

The CKAN Action API exposes methods such as `package_show`, `resource_show`, and `datastore_search` for retrieving metadata and table records in JSON. 

In practice, this means a web page can call the metadata endpoint to identify a resource, then call the DataStore endpoint to render the live records directly.

[CKAN API documentation↗️](https://docs.ckan.org/en/latest/api/)

## Previous Technical Blocker
These demos below retrieve data directly from open.canada.ca using browser-based API calls.

However, Open.Canada.ca like most Government of Canada APIs did not allow cross-origin requests from `.gc.ca` or `canada.ca` websites. This is due to browser security controls known as Cross-Origin Resource Sharing (CORS).

When a web page hosted on <kbd>domain X</kbd> makes a request to get data from <kbd>domain Y</kbd>, a users browser will block the request, unless the server at <kbd>domain Y</kbd> adds an extra piece of infomation (header) saying that it is cool to shares resources, with either specific domains, or all domains.

### How It Can Be Worked Around

This doesn't get enforced the same way outside browsers, like from a program installed by a user, or by applications or simple scripts running on a server.

>[!NOTE]
>This is inconvenient for Web Content Developers, as runing servers in the backend to make these requests is complicated and slow to get setup, in the GC working environment. 


## Demos

### [GCDS Table Componet for Displaying Tables](https://patlittle.github.io/assets/CkanBackGcdsTableFront.html)

![GC Tables](/assets/images/GCDStables.png)




### [Service Inventory Lookup](https://patlittle.github.io/assets/service-inventory-lookup.html)
![Service Lookup](/assets/images/ServiceLook.png)




### [Quality Lens](https://patlittle.github.io/assets/OpenDataQualityLens.html)
![Quality](/assets/images/OpenDataQualityLens.png)
![Qualitymore](/assets/images/OpenDataQualityLens2.png)
