# UTM5 API Section: Inventory

This document describes the endpoints for the 'Inventory' API section for UTM5 isp billing system by Netup Co.

## Endpoint: Inventory - Create dhcp options
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/inventory/dhcp_options`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Inventory - Create dhcp pool
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/inventory/dhcp_pool`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "pool_id" : 1}
```
---

## Endpoint: Inventory - Create switch
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/inventory/switches`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "switch_id" : 1}
```
---

## Endpoint: Inventory - Create type of switch
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/inventory/switch_types`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "profile_id" : 1}
```
---

## Endpoint: Inventory - Delete all dhcp options
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/inventory/dhcp_options`
- **Ready:** `false`
### Parameters:
  - **Name:** `owner_id`
    - **Type:** `Number`
    - **Description:** Owner id of dhcp option owner type - Type of owner
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Inventory - Delete dhcp lease
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/inventory/dhcp_lease`
- **Ready:** `false`
### Parameters:
  - **Name:** `lease_id`
    - **Type:** `Number`
    - **Description:** Lease id
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Inventory - Delete dhcp pool
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/inventory/dhcp_pool`
- **Ready:** `false`
### Parameters:
  - **Name:** `pool_id`
    - **Type:** `Number`
    - **Description:** pool id
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Inventory - Delete switch
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/inventory/switches`
- **Ready:** `false`
### Parameters:
  - **Name:** `switch_id`
    - **Type:** `Number`
    - **Description:** switch id
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Inventory - Delete type of switch
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/inventory/switch_types`
- **Ready:** `false`
### Parameters:
  - **Name:** `profile_id`
    - **Type:** `Number`
    - **Description:** Profile id of device
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Inventory - Expire dhcp lease
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/inventory/expire_dhcp_lease`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Inventory - Get dhcp leases active
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/inventory/dhcp_leases_active`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "binding_id": 4,
    "client_id": "3",
    "expired": 1574175039,
    "flags": 2,
    "ip": "0.0.43.103",
    "lease_id": 1,
    "mac": "aa:bb:ff:de:ad:ad",
    "server_id": "1",
    "updated": 1574173039
  }
```
---

## Endpoint: Inventory - Get dhcp leases expired
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/inventory/dhcp_leases_expired`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "binding_id": 4,
    "client_id": "3",
    "expired": 1574175039,
    "flags": 2,
    "ip": "0.0.43.103",
    "lease_id": 1,
    "mac": "aa:bb:ff:de:ad:ad",
    "server_id": "1",
    "updated": 1574173039
  }
```
---

## Endpoint: Inventory - Get dhcp leases
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/inventory/dhcp_leases`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "binding_id": 4,
    "client_id": "3",
    "expired": 1574175039,
    "flags": 2,
    "ip": "0.0.43.103",
    "lease_id": 1,
    "mac": "aa:bb:ff:de:ad:ad",
    "server_id": "1",
    "updated": 1574173039
  }
```
---

## Endpoint: Inventory - Get dhcp options list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/inventory/dhcp_options`
- **Ready:** `false`
### Parameters:
  - **Name:** `owner_id`
    - **Type:** `Number`
    - **Description:** owner id
  - **Name:** `type`
    - **Type:** `Number`
    - **Description:** type of owner
### Example Response:
```
{
    "data": "",
    "data_type": 5,
    "id": 10,
    "option_id": 4,
    "owner_id": 1,
    "owner_type": 1
  },
  {
    "data": "",
    "data_type": 5,
    "id": 11,
    "option_id": 5,
    "owner_id": 1,
    "owner_type": 1
  }
```
---

## Endpoint: Inventory - Get dhcp pools
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/inventory/dhcp_pools`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
        "block_action_type": 1,
        "block_pool_id": 0,
        "dns1_server": "8.8.8.8",
        "dns2_server": "0.0.0.0",
        "domain_name": "",
        "gateway": "10.1.5.29",
        "id": 1,
        "lease_time": 86400,
        "netmask": "255.255.255.0",
        "ntp_server": "0.0.0.0",
        "ranges": [
          {
            "first_addr": "10.1.5.0",
            "last_addr": "10.1.5.20"
          }
        ]
      }
```
---

## Endpoint: Inventory - Get switch pool links
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/inventory/dhcp_pool_links`
- **Ready:** `false`
### Parameters:
  - **Name:** `switch_id`
    - **Type:** `Number`
    - **Description:** Switch id
### Example Response:
```
{
                 "first_addr": "1.2.3.0",
                 "last_addr" : "1.2.3.254"
             }
```
---

## Endpoint: Inventory - Get switch ports usage
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/inventory/switch_ports_usage`
- **Ready:** `false`
### Parameters:
  - **Name:** `switch_id`
    - **Type:** `Number`
    - **Description:** Switch id
### Example Response:
```
{
 "port" : 1,
 "user_data" : [
     {
         "user_id" : 1,
         "login" : "uzver"
     }
   ]
 }
```
---

## Endpoint: Inventory - Get switches by page
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/inventory/switches_paged`
- **Ready:** `false`
### Parameters:
  - **Name:** `page`
    - **Type:** `Number`
    - **Description:** Page number
  - **Name:** `per_page`
    - **Type:** `Number`
    - **Description:** items per page
  - **Name:** `filter`
    - **Type:** `Number`
    - **Description:** search query
### Example Response:
```
{
 "switches" :
  [
     {
       "address": "0.0.0.0",
       "dhcp_pools": [
         1
       ],
       "id": 1,
       "location": "",
       "house_id": 2,
       "login": "",
       "name": "border router",
       "password": "",
       "ports_count": 3,
       "remote_id": "",
       "type": 4,
       "ports_num_offset": 1
     }
    ],
   "total_rows": 123
  }
```
---

## Endpoint: Inventory - Get switches
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/inventory/switches`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
        "address": "0.0.0.0",
        "dhcp_pools": [
          1
        ],
        "id": 1,
        "location": "",
        "house_id": 2,
        "login": "",
        "name": "border router",
        "password": "",
        "ports_count": 3,
        "remote_id": "",
        "type": 4,
        "ports_num_offset": 1
      }
```
---

## Endpoint: Inventory - Get types of switch
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/inventory/switch_types`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id": 1,
  "name": "Unmanaged Switch",
  "port_id_meta": {
    "disposition": 0,
    "len": 0,
    "offset": 0,
    "type": 0
  },
  "port_start_offset": 1,
  "supp_volumes": "5,8,12,16,24,26,28,48,50,52",
  "tec_id_meta": {
    "disposition": 0,
    "len": 0,
    "offset": 0,
    "type": 0
  },
  "vlan_id_meta": {
    "disposition": 0,
    "len": 0,
    "offset": 0,
    "type": 0
  }
}
```
---

## Endpoint: Inventory - Update dhcp pool
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/inventory/dhcp_pool`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Inventory - Update switch dhcp pool links
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/inventory/dhcp_pool_links`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Inventory - Update switch
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/inventory/switches`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Inventory - Update type of switch
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/inventory/switch_types`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

