// New menu option on the device list cog wheel menu, context-configure-menu

Ext.ComponentMgr.onAvailable('context-configure-menu', function(config) {
  var origOnGet = config.onGetMenuItems;
  config.onGetMenuItems = function(uid) {
    var result = origOnGet.call(this, uid) || [];
    if( true ) {
        result.push( {
            text: _t('Model devices'),
            hidden: Zenoss.Security.doesNotHavePermission('Manage Device'),
            handler: function() {
            Zenoss.remote.runModeling.startModelingJob( uid, function(response) {
                                if (response.success) {
                                 Zenoss.message.success(_t('Add Device Job submitted. <a href="/zport/dmd/JobManager/jobs/{0}/viewlog">View Job Log</a>'), response.jobId);
                                } 
            });
            }
        });
    }
    return result;
  };
});

