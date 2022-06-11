# Role: server-onboarding
Deze rol kan gebruikt worden om een server te onboarden aan Ansible. Deze rol zorgt ervoor dat Ansible deze machine kan beheren met zo min mogelijk menselijke inspanning. Op dit moment zijn debian en redhat ondersteund.

## _**Role variables**_
Onderstaand is een lijst van alle variabele te vinden:
- **target_server** | *required*<br>
- **default_username** | *required* -> Gebruikt in playbook<br> 
- **default_password** | *required* -> Gebruikt in playbook<br>

