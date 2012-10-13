from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products.Jobber.jobs import Job, ShellCommandJob

class ModelOrganizerJob(ShellCommandJob):
  def __init__(self, jobid, orgPath, dmd):
    _zpName='ZenPacks.ssv.OrgModeler'
    _orgModeler = dmd.getObjByPath('/zport/dmd/ZenPackManager/packs/' + _zpName ).eggPath() + '/' + _zpName.replace('.','/') + '/lib/orgModeler.py'
    _cmd = ['python' , _orgModeler, orgPath, jobid ]
    super(ModelOrganizerJob, self).__init__( jobid, _cmd )

class runModeling(DirectRouter):
  def startModelingJob(self,id):
    _dmd = self.context.dmd
    jobStatus=_dmd.JobManager.addJob(ModelOrganizerJob, id , _dmd )
    return DirectResponse.succeed(jobId=jobStatus.id)
