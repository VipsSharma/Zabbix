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
print("Connected to Zabbix API Version %s" % zapi.api_version())
```

#### All zabbix api requests can be made as defined in [Zabbix API Documentation](https://www.zabbix.com/documentation/4.2/manual/api/reference)

## The features added in zabbi are :

* Using host.get you can get all results for a host ( including 'hostInterface'  results ).
