#
# Copyright (C) 2020 FreeIPA Contributors see COPYING for license
#

from ipahealthcheck.core import constants
from ipahealthcheck.core.plugin import Result, duration
from ipahealthcheck.ds.plugin import DSPlugin, registry
from lib389.monitor import MonitorDiskSpace


@registry
class DiskSpaceCheck(DSPlugin):
    """
    Check the all the disks that the DS uses
    """
    requires = ('dirsrv',)

    @duration
    def check(self):
        results = self.doCheck(MonitorDiskSpace)
        if len(results) > 0:
            for result in results:
                yield result
        else:
            yield Result(self, constants.SUCCESS)
