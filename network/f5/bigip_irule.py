#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2013, Matt Hite <mhite@hotmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
documentation = '''
---
module: bigip_irule
short_description: "Manages F5 IRules"
description:
   - "This module allows for the addition and deletion of IRules; it is recommended that one run this module via local_actions."
author: Igor Gueths
notes:
   - "This module requires Bigsuds, please see http://devcentral.f5.com for more details."
'''
import bigsuds
from ansible.module_utils.basic import *
# Supporting methods.
def bigip_api(bigip, username, password):
    api = bigsuds.BIGIP(hostname=bigip, username=user, password=password)
    return api

def delete_rule(api, rulename):
# Simple method to delete an IRule that is passed in.
    api.LocalLB.Rule.delete_rule(rulename)

def create_rule(api, rulename, ruledata):
"""
This method takes three parameters:
@api - The object that we use to talk to the BigIP device itself.
@rulename - A descriptive name for our IRule.
@data - The data that comprises the rule itself, for precise information
on syntax, see Devcentral docs for more details.
"""
    api.LocalLB.Rule.create_rule(api, rulename, ruledata)

def main():
# Specify arguments that are required and optional by this module.
    module = AnsibleModule(
        argument_spec = dict(
            host = dict(type='str', required=True),
            user = dict(type='str', required=True),
            password = dict(type='str', required=True),
                    rulename = dict(type='str', required=True),
            ruledata = dict(type='str', required=True),
            state = dict(type='str', default='present', choices=['present', 'absent']),
            partition = dict(type='str', default='common'),
        supports_check_mode=True
    )
    host = module.params['host']
    user = module.params['user']
    password = module.params['password']
    state = module.params['state']
    partition = module.params['partition']
    rulename = module.params['rulename']
    ruledata = module.params['ruledata']
