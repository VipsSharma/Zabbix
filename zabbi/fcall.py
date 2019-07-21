import sys
import json

@author: vipul sharma

def func(self,attr,*args, **kwargs):

	out=self.parent.do_request(
                '{0}.{1}'.format(self.name, attr),
                args or kwargs
            )['result']

	if(self.name == "host"):
			host=self.parent.do_request(
                		'{0}.{1}'.format(self.name, "get"),
                		args or kwargs
            			)['result']

			hostin=self.parent.do_request(
                                '{0}.{1}'.format("hostinterface", "get"),
                                args or kwargs
                                )['result']
			
			hj = []
			for h in host:
				for hip in hostin:
					if( h["hostid"] == hip["hostid"]):
						h.update(hip)
						hj.append(h)
	return hj
