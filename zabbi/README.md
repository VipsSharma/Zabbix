# Zabbix
**Zabbix - Python API Module**

# Documentation
### Getting Started

Install *zabbi* using pip:

```bash
$ pip install zabbi
```

# You can now import and use zabbi like so:

```python
from zabbi import ZabbixAPI

zapi = ZabbixAPI("http://zabbixserver.example.com")
zapi.login("zabbix user", "zabbix pass")
print("Zabbix API Version %s using zabbi " % zapi.api_version())
```

#### All zabbix api requests can be made as defined in [Zabbix API Documentation](https://www.zabbix.com/documentation/4.2/manual/api/reference)

## The features added in zabbi are :

* Using host.get you can get all results for a host ( including hostInterface results )
* Now you can get host.get info by name also ( host.get with param host="example")
* Now you can get info for host by ip also ( hostinterface with param ip="0.0.0.0" )
  *Also the info would be returned for multiple hosts if there are with same ip or name**
