Ansible role for icecc
==================================

This will install icecream (icecc) and point it to the correct scheduler in the config file.  It also tweaks systemd to make sure the daemon restarts if it goes down.

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-icecc/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-icecc/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-icecc/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-icecc/actions?query=workflow%3A%22Release%22)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| name | desc | type | default | required |
| icecc_scheduler_hostname | The scheduler used by icecc | string | | yes|

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-icecc
```

License
-------

[Apache License](LICENSE)
