gabops.zabbix_repo
==================
[![Build Status](https://travis-ci.org/gabops/ansible-role-zabbix-repo.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-zabbix-repo)

Installs and configures Zabbix official repository.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| zabbix_repo_version | 4.0 | Defines the repository's package version to install. Possible values are `3.0`, `4.0`, `4.4` and `4.5` |
| zabbix_repo_apt_pin | true | Controls whether or not pin configuration is applied for the Zabbix official repository. |
| zabbix_repo_apt_pin_priority | 999 | Defines the pin priority for the Zabbix repo. A high value will make apt to prefer **zabbix related** packages from the Zabbix official repo. |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
    - hosts: servers
      vars:
        zabbix_repo_version: 4.4
      roles:
         - role: gabops.zabbix_repo
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
