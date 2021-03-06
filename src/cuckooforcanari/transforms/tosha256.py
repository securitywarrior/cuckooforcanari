#!/usr/bin/env python

from canari.framework import configure
from common.entities import CuckooHash, FileDetails, CuckooMalwareFilename, CuckooTaskID
from common.cuckooapi import report
from common.cuckooparse import target_info

__author__ = 'bostonlink'
__copyright__ = 'Copyright 2014, Cuckooforcanari Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '1.1'
__maintainer__ = 'bostonlink'
__email__ = 'bostonlink@pentest-labs.org'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


@configure(
    label='To SHA256 [Cuckoo Sandbox]',
    description='Returns filename of the initial file analyzed.',
    uuids=[ 'cuckooforcanari.v2.IDToSHA256_Cuckoo',
            'cuckooforcanari.v2.FileToSHA256_Cuckoo',
            'cuckooforcanari.v2.SectionToSHA256_Cuckoo' ],
    inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ),
        ( 'Cuckoo Sandbox', CuckooMalwareFilename ),
        ( 'Cuckoo Sandbox', FileDetails ) ],
    remote=False,
    debug=False
)
def dotransform(request, response, config):

    if 'taskid' in request.fields:
        task = request.fields['taskid']
    else:
        task = request.value

    target = target_info(report(task))['file']
    response += CuckooHash(target['sha256'].decode('ascii'),
                           taskid=task)

    return response
