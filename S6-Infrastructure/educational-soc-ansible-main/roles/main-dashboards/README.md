# Role: main-dashboards
Deze rol kan gebruikt worden om een een instelling van een main dashboard te wijzigen of een main dashboard te configureren vanaf de basis installatie.


## _**Role variables**_
Onderstaand is een lijst van alle variabele te vinden:
- **type** | *required*<br>
  Options<br>
  - configure
  - modify
  - reboot
  - turn on hdmi
  - turn off hdmi
- **target_dashboard** | *required*<br>
  Options<br>
  - esoc-sdb01-til-p8-ph-0021
  - esoc-sdb02-til-p8-ph-0022
  - esoc-ndb01-til-p8-ph-0023
  - esoc-ndb02-til-p8-ph-0024
- **target_url** | *optional*
  Default: https://google.com
