---
title: "Reactivating the Skateway Repo"
category: "Product"
mermaid: true
---

For the last two Rideau Canal skating seasons I've had a little data collection project running to automatically collect the ice conditions from NCC's open data, and then store it as timeseries in a CSV.
Along the way I've used this little project as example data to learn & practice, share, and talk about data science and analytics. 

The original post talks about using python to dump the geospatial data from ESRI into CSV for analysts not from a geo data background - https://www.linkedin.com/pulse/opendatadays-geospatial-data-non-geo-users-patrick-little-mba-udclc and there is also a example notebook [here](https://gist.github.com/PatLittle/413eef25fae1d1a2e1d5be7ee38c79d0)

As of 2025-12-27 I reenabled the automated data collection, and the third year of data is now being added to the longitudinal dataset. 

<a style="text-align:right;" target="_blank" href="https://flatgithub.com/PatLittle/skateway_data?filename=current_conditions.csv&sort=Current_Datetime%2Cdesc&stickyColumnName=Current_Datetime">
  open in new tab↗
</a>

<iframe
  src="https://flatgithub.com/PatLittle/skateway_data?filename=current_conditions.csv&sort=Current_Datetime%2Cdesc&stickyColumnName=Current_Datetime"
  title="conditions"
  width="800"
  height="600"> 
</iframe>

## Visual Export

I also was interested to see how exporting a PNG of the GeoJSON and keeping the image file in source control would work for creating an animation, or just having the GH visual diff to view the changes. 

This image will recieve changes daily and the GH has 3 different ways to visually compare the changes. More info here https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files#viewing-differences 


![condition status](https://raw.githubusercontent.com/PatLittle/skateway_data/main/skateway_status_map.png)


## Mermaid Gantt Chart as a timeseries visualization

This was also a experiment with using mermaid gantt chart as a way to visualize the conditions overtime, while keeping the spatial context of how the geography appears on a map. 

```mermaid
---
topAxis: true
displayMode: compact
config:
  theme: 'dark'
  themeCSS: " #vg { fill: Green } #g {fill: yellow} #f {fill: orange} #p {fill: red}      \n
#c {fill: Black} #cs {fill: Black} #sc {fill: White} #wo {fill: saddlebrown} \n
            text[id^=cs] { fill: red; } text[id^=sc] { fill: red; }
        "
---

gantt
  title Skateway segment statuses (2025-12)
  dateFormat  YYYY-MM-DD HH:mm:ss
  axisFormat  %Y %m %d
  section Rideau-Mackenzie King
  Closed: c, 2025-12-27 19:17:23, 2026-01-01 03:54:16
  section Mackenzie King-Laurier
  Closed: c, 2025-12-27 19:17:23, 2026-01-01 03:54:16
  section Laurier-Waverley
  Closed: c, 2025-12-27 19:17:23, 2026-01-01 03:54:16
  section Waverley-Concord
  Closed: c, 2025-12-27 19:17:23, 2025-12-31 16:28:10
  Fair: f, 2025-12-31 16:28:10, 2026-01-01 03:54:16
  section Concord-Pretoria
  Closed: c, 2025-12-27 19:17:23, 2025-12-31 16:28:10
  Fair: f, 2025-12-31 16:28:10, 2026-01-01 03:54:16
  section Pretoria-Fifth
  Closed: c, 2025-12-27 19:17:23, 2025-12-31 16:28:10
  Fair: f, 2025-12-31 16:28:10, 2026-01-01 03:54:16
  section Patterson Creek-Patterson Creek
  Closed for the Season: cs, 2025-12-27 19:17:23, 2025-12-31 16:28:10
  Poor: p, 2025-12-31 16:28:10, 2026-01-01 03:54:16
  section Fifth-Lansdowne
  Closed: c, 2025-12-27 19:17:23, 2025-12-31 16:28:10
  Closed for the Season: cs, 2025-12-31 16:28:10, 2026-01-01 03:54:16
  section Lansdowne-Bank
  Closed: c, 2025-12-27 19:17:23, 2025-12-31 16:28:10
  Poor: p, 2025-12-31 16:28:10, 2026-01-01 03:54:16
  section Bank-Bronson
  Closed: c, 2025-12-27 19:17:23, 2025-12-31 16:28:10
  Poor: p, 2025-12-31 16:28:10, 2026-01-01 03:54:16
  section Bronson-Dow's Lake
  Closed: c, 2025-12-27 19:17:23, 2026-01-01 03:54:16
  section Dow's Lake Loop-Dow's Lake Loop
  Closed: c, 2025-12-27 19:17:23, 2026-01-01 03:54:16
  section Dow's Lake-Library
  Closed: c, 2025-12-27 19:17:23, 2026-01-01 03:54:16
  section Dow's Lake-Library
  Closed: c, 2025-12-31 16:28:10, 2026-01-01 03:54:16
```

More info on the Gantt Chart Syntax here - https://docs.mermaidchart.com/mermaid-oss/syntax/gantt.html#output-in-compact-mode
