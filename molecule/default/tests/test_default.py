import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_host(host):
    assert host.file("/etc/hosts").exists


def test_icecc_is_installed(host):
    icecc = host.package("icecc")
    assert icecc.is_installed


def test_icecc_conf_file(host):
    icecc_conf_file = '/etc/icecc/icecc.conf'
    assert host.file(icecc_conf_file).exists
    assert host.file(icecc_conf_file).is_file
    content = host.file(icecc_conf_file).content_string
    icecc_scheduler_config = \
        'ICECC_SCHEDULER_HOST="iceccd-scheduler-lb-placholder.amazonaws.com"'
    assert icecc_scheduler_config in content


def test_icecc_systemd_override(host):
    icecc_systemd_override_file = \
        '/etc/systemd/system/iceccd.service.d/override.conf'
    assert host.file(icecc_systemd_override_file).exists
    assert host.file(icecc_systemd_override_file).is_file
    content = host.file(icecc_systemd_override_file).content_string
    assert 'Restart=on-failure' in content
