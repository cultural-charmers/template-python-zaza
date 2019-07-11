#!/usr/bin/env python3

import os
import sys

sys.path.append('lib/')

from charmhelpers.core.hookenv import action_fail, action_get, action_set


# A dictionary of all the defined actions to callables (which take
# parsed arguments).
ACTIONS = {
}


def main(args):
    action_name = os.path.basename(args[0])
    try:
        action = ACTIONS[action_name]
    except KeyError:
        return "Action %s undefined" % action_name
    else:
        try:
            action(args)
        except Exception as e:
            action_fail(str(e))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
