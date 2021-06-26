# Consul

![Molecule](https://github.com/DaazKu/ansible-consul/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)
[![Galaxy](https://img.shields.io/badge/Galaxy-ansible__consul-informational?logo=Ansible&logoColor=848c96)](https://galaxy.ansible.com/daazku/consul_vault)

This ansible role install Consul and expect you to **supply your own configuration templates**.

See: 
- [`consul_config_template`](#consul_config_template)
- [`consul_extra_config_templates`](#consul_extra_config_templates)

Consul has MANY configuration parameters and trying to cover all of them with ansible variables makes things awfully complicated, 
hard to maintain and frustrating when some options are not handled. You might also prefer to use HCL over the JSON format...
For these reasons, this role handles the installation of consul and use your supplied configuration templates so that everyone's life is made easier!

## Role Variables

### `consul_bin_dir`
- Consul binary directory
- Default value: `/usr/local/bin`

### `consul_config_dir`
- Base configuration directory
- Default value: `/etc/consul`

### `consul_config_template`
- Path to the configuration template to use
  - **Must be supplied**
  - Resulting config will be the file name without the `.j2` extension. ie. `/some/path/config.hcl.j2` would result in `{{ consul_config_dir }}/config.hcl`

### `consul_data_dir`
- Consul data directory
  - Should be used in your config as it will be created by this role
- Default value: `/var/consul/data`

### `consul_extra_config_dir`
- Extra configuration directory
- Default value: `{{ consul_config_dir }}/consul.d`

### `consul_extra_config_templates`
- Extra configuration templates to render
    - Resulting configs will be the files name without the `.j2` extension. ie. `/some/path/my-extra-config.hcl.j2` would result in `{{ consul_extra_config_dir }}/my-extra-config.hcl`
- Default value: `[]`

### `consul_group`
- Consul unix group
- Default value: `consul`

### `consul_run_path`
- Directory for PID file
- Default value: `/var/run/consul`

### `consul_user`
- Consul unix user
- Default value: `consul`

### `consul_version`
- Consul version to install
- Default value: `1.10.0`
