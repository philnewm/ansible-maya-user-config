# Maya-user-config-Role

[![AlmaLinux9-CI](https://github.com/philnewm/ansible-maya-user-config/actions/workflows/almalinux9-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-maya-user-config/actions/workflows/almalinux9-ci-caller.yml) [![Rocky9-CI](https://github.com/philnewm/ansible-maya-user-config/actions/workflows/rocky9-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-maya-user-config/actions/workflows/rocky9-ci-caller.yml) [![Fedora43-CI](https://github.com/philnewm/ansible-maya-user-config/actions/workflows/fedora43-ci-caller.yml/badge.svg)](https://github.com/philnewm/ansible-maya-user-config/actions/workflows/fedora43-ci-caller.yml)

Role description

This role includes a vagrant based molecule testing setup as a submodule at `molecule/`

## Structure

```code
📦 ansible-maya-user-config
 ┣ 📂 defaults
 ┃ ┗ 📜 main.yml
 ┣ 📂 files
 ┃ ┗ 📜 file_placeholder.yml
 ┣ 📂 meta
 ┃ ┗ 📜 main.yml
 ┣ 📂 molecule
 ┃ ┗ 📂 default
 ┃   ┗ 📜, 📜, 📜, scenario_files
 ┣ 📂 tasks
 ┃ ┣ 📜 main.yml
 ┃ ┣ 📜 present.yml
 ┃ ┣ 📜 dependencies.yml
 ┃ ┣ 📜 absent.yml
 ┃ ┗ 📜 init.yml
 ┣ 📂 vars
 ┃ ┗ 📜 main.yml
 ┗ 🗒️ README.md
 ┗ 📓 requirements.yml

```

Describe and explain role structure.

## Requirements

Elaborate external dependencies and how to use them.

## Role Variables

* defaults/main.yml
  * first_var
  * sec_var
  * third_var
* vars/main.yml
  * first_var
  * sec_var
  * third_var

## Dependencies

List role ansible-galaxy dependencies - if any.

## Example Playbook

Add an example playbook

```yaml
---

tasks:
  - name: Include ansible-maya-user-config present
    ansible.builtin.include_role:
      name: ansible-maya-user-config
    vars:
      state: present

...
```

## License

Add license - if any.
