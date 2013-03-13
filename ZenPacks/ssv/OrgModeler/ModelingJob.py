# Zenoss 4.2
from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products.Jobber.jobs import SubprocessJob

class runModeling(DirectRouter):
  def startModelingJob(self,id):
    _dmd = self.context.dmd
    _zpName='ZenPacks.ssv.OrgModeler'
    _orgModeler = _dmd.getObjByPath('/zport/dmd/ZenPackManager/packs/' + _zpName ).eggPath() + '/' + _zpName.replace('.','/') + '/lib/orgModeler.py'
    _cmd = ['python' , _orgModeler, id ]
    jobStatus=_dmd.JobManager.addJob(SubprocessJob, description="Model organizer job for %s" % id,args=(_cmd,) )
    return DirectResponse.succeed(jobId=jobStatus.id)
