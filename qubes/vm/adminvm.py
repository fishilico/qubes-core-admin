#!/usr/bin/python2 -O

import qubes
import qubes.vm.qubesvm

class AdminVM(qubes.vm.qubesvm.QubesVM):
    '''Dom0'''

    netvm = qubes.property('netvm', setter=qubes.property.forbidden,
        default=None,
        doc='Dom0 cannot have netvm')

    @property
    def xid(self):
        '''Always ``0``.

        .. seealso:
           :py:attr:`qubes.vm.qubesvm.QubesVM.xid`
        '''
        return 0

    @property
    def libvirt_domain(self):
        '''Always :py:obj:`None`.

        .. seealso:
           :py:attr:`qubes.vm.qubesvm.QubesVM.libvirt_domain`
        '''
        return None


    # XXX probably unneeded, will return None as we don't have netvm
#   @property
#   def ip(self):
#       return "10.137.0.2"


    def is_running(self):
        '''Always :py:obj:`True`.

        .. seealso:
           :py:meth:`qubes.vm.qubesvm.QubesVM.is_running`
        '''
        return True


    def get_power_state(self):
        '''Always ``'Running'``.

        .. seealso:
           :py:meth:`qubes.vm.qubesvm.QubesVM.get_power_state`
        '''
        return 'Running'


    def get_mem(self):
        '''Get current memory usage of Dom0.

        Unit is KiB.

        .. seealso:
           :py:meth:`qubes.vm.qubesvm.QubesVM.get_mem`
        '''

        #return psutil.virtual_memory().total/1024
        for line in open('/proc/meminfo'):
            if line.startswith('MemTotal:'):
                return int(line.split(':')[1].strip().split()[0])
        raise NotImplementedError()


    def get_mem_static_max(self):
        '''Get maximum memory available to Dom0.

        .. seealso:
           :py:meth:`qubes.vm.qubesvm.QubesVM.get_mem_static_max`
        '''
        return self.app.vmm.libvirt_conn.getInfo()[1]


    def get_disk_utilization(self):
        '''Always ``0``.

        .. seealso:
           :py:meth:`qubes.vm.qubesvm.QubesVM.get_disk_utilization`
        '''
        return 0

    def get_disk_utilization_private_img(self):
        '''Always ``0``.

        .. seealso:
           :py:meth:`qubes.vm.qubesvm.QubesVM.get_disk_utilization_private_img`
        '''
        return 0

    def get_private_img_sz(self):
        '''Always ``0``.

        .. seealso:
           :py:meth:`qubes.vm.qubesvm.QubesVM.get_private_img_sz`
        '''
        return 0


    def verify_files(self):
        '''Always :py:obj:`True`

        .. seealso:
           :py:meth:`qubes.vm.qubesvm.QubesVM.verify_files`
        '''
        return True


    def start(self, **kwargs):
        '''Always raises an exception.

        .. seealso:
           :py:meth:`qubes.vm.qubesvm.QubesVM.start`
        '''
        raise qubes.QubesException('Cannot start Dom0 fake domain!')


    def suspend(self):
        '''Does nothing.

        .. seealso:
           :py:meth:`qubes.vm.qubesvm.QubesVM.suspend`
        '''
        # XXX shouldn't we spew an exception?
        return


#   def __init__(self, **kwargs):
#       super(QubesAdminVm, self).__init__(qid=0, name="dom0", netid=0,
#                                            dir_path=None,
#                                            private_img = None,
#                                            template = None,
#                                            maxmem = 0,
#                                            vcpus = 0,
#                                            label = defaults["template_label"],
#                                            **kwargs)
