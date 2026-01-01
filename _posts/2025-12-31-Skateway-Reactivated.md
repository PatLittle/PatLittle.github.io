---
title: "Reactivating the Skateway Repo"
category: "Product"
mermaid: true
---

<iframe
  id="inlineFrameExample"
  title="Inline Frame Example"
  width="800"
  height="800"
  sandbox="allow-same-origin allow-scripts allow-popups allow-forms"
  src="https://geojson.io/#id=github:PatLittle/skateway_data/blob/main/status_styled.geojson&map=13.23/45.40468/-75.69245" >
</iframe>


```mermaid
---
topAxis: true
displayMode: compact
config:
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

1. **Limit work in progress.** Choose fewer big bets so the team can win.
2. **Share the why.** Every roadmap item should explain the customer impact.
3. **Review monthly.** Make small course corrections before they become pivots.
