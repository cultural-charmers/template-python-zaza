#!/usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.join(os.environ['CHARM_DIR'], 'lib'))

from charmhelpers.core import (
    hookenv,
)
import {{ cookiecutter.charm_name_lc }} as {{ cookiecutter.charm_name_lc }}

hooks = hookenv.Hooks()


@hooks.hook('install')
def install():
    hookenv.log('Installing {{ cookiecutter.charm_name }}')


@hooks.hook('config-changed')
def config_changed():
    hookenv.log('Upgrading {{ cookiecutter.charm_name }} config')
    # Do things!
    hookenv.status_set('active', '{{ cookiecutter.charm_name }} is ready')


@hooks.hook('start')
def start():
    hookenv.log('Starting {{ cookiecutter.charm_name }}')


@hooks.hook('stop')
def stop():
    hookenv.log('Stopping {{ cookiecutter.charm_name }}')


@hooks.hook('upgrade-charm')
def upgrade_charm():
    hookenv.log('Upgrading {{ cookiecutter.charm_name }}')


@hooks.hook('update-status')
def update_status():
    hookenv.log('Checking {{ cookiecutter.charm_name }} status')


if __name__ == "__main__":
    # execute a hook based on the name the program is called by
    hooks.execute(sys.argv)
