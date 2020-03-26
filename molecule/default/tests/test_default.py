import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_zabbix_repo(host):
    if host.system_info.distribution in ['debian', 'ubuntu']:
        c = host.run('apt-cache search zabbix-agent').rc
    else:
        c = host.run('yum --disablerepo="*" --enablerepo="zabbix" \
        list available').rc

    assert c == 0
