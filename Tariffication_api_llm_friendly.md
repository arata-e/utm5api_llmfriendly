# UTM5 API Section: Tariffication

This document describes the endpoints for the 'Tariffication' API section for UTM5 isp billing system by Netup Co.

## Endpoint: Tariffication - Create accounting period
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/accounting_period`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "accounting_id": 2
}
```

---

## Endpoint: Tariffication - Create charge policy
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/charge_policy`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "policy_id": 2
}
```

---

## Endpoint: Tariffication - Create coeff scheme
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/coefficient_scheme`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "coeff_scheme_id": 1
}
```

---

## Endpoint: Tariffication - Create coefficient schedule
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/coefficient_schedule`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "coefficient_schedule_id" : "1"}
```

---

## Endpoint: Tariffication - Create contract type
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/contract_type`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "contract_type_id": 1
}
```

---

## Endpoint: Tariffication - Create payment
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/payments`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "payment_transaction_id" : "1"}
```

---

## Endpoint: Tariffication - Create promised payment
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/promised_payments`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: Tariffication - Create tariff
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/tariff`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "tariff_id": 6
}
```

---

## Endpoint: Tariffication - Create tclass
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/tclasses`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Create tel direction
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/tel_direction`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "teldir_id": 2
}
```

---

## Endpoint: Tariffication - Create telephony zone
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/tel_zone`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "zone_id": 4
}
```

---

## Endpoint: Tariffication - Create time range
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/time_ranges`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "timerange_id": 1
}
```

---

## Endpoint: Tariffication - Delete charge policy
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/tariffing/charge_policy`
### Parameters:
  - **Name:** `policy_id`
    - **Type:** `Number`
    - **Description:** Charge policy id
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Delete coeff scheme
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/tariffing/coefficient_scheme`
### Parameters:
  - **Name:** `coeff_scheme_id`
    - **Type:** `Number`
    - **Description:** Coefficient scheme id
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Delete contracttype
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/tariffing/contract_type`
### Parameters:
  - **Name:** `contract_type_id`
    - **Type:** `Number`
    - **Description:** Contract type id
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Delete radius attr
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/tariffing/radius_attrs`
### Parameters:
  - **Name:** `object_type`
    - **Type:** `Number`
    - **Description:** Object type ( OBJECT_NAS = 0, OBJECT_IPTRAFFIC_SERVICE = 3, OBJECT_HOTSPOT_SERVICE = 4, OBJECT_DIALUP_SERVICE = 5, OBJECT_TEL_SERVICE = 6, OBJECT_ISG_AUTH = 7, OBJECT_ISG_COA = 8, OBJECT_ISG_SIR = 9, OBJECT_RADIUS_ACCOUNT = 12, OBJECT_LINK = 10000, OBJECT_SHAPING = 10001)
  - **Name:** `object_id`
    - **Type:** `Number`
    - **Description:** item id (ISG profile/slink etc.)
  - **Name:** `radius_attr_id`
    - **Type:** `Number`
    - **Description:** radius attr identifier
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Delete service from tariff
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/tariffing/delete_service_from_tariff`
### Parameters:
  - **Name:** `tariff_id`
    - **Type:** `Number`
    - **Description:** Tariff id
  - **Name:** `service_id`
    - **Type:** `Number`
    - **Description:** Service id
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Delete service
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/tariffing/services`
### Parameters:
  - **Name:** `service_id`
    - **Type:** `Number`
    - **Description:** Service id
### Example Response:

HTTP/1.1 200 OK
```

---

## Endpoint: Tariffication - Delete tariff
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/tariffing/tariff`
### Parameters:
  - **Name:** `tariff_id`
    - **Type:** `Number`
    - **Description:** Traffic tariff id
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Delete tclass
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/tariffing/tclasses`
### Parameters:
  - **Name:** `tclass_id`
    - **Type:** `Number`
    - **Description:** Traffic class id
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Delete tel direction
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/tariffing/tel_direction`
### Parameters:
  - **Name:** `dir_id`
    - **Type:** `Number`
    - **Description:** Traffic direction id
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Delete tel zone
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/tariffing/tel_zone`
### Parameters:
  - **Name:** `zone_id`
    - **Type:** `Number`
    - **Description:** Traffic zone id
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Delete time range
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/tariffing/time_ranges`
### Parameters:
  - **Name:** `timerange_id`
    - **Type:** `Number`
    - **Description:** Time range identifier
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Get accounting periods
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/accounting_periods`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
  "id" : "1",
  "begin" : "",
  "end" : "",
  "periodic_type" : "",
  "next_accounting_period_id" : "",
  "charge_interval" : "",
  "canonical_len" : "",
  "custom_duration" : "",
  "static_id" : "",
  "invoice_month" : ""
 }
]
```

---

## Endpoint: Tariffication - Get charge polices
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/charge_polices`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
  "policy_id" : "1",
  "flags" : "1",
  "name" : "Policy",
  "blockchecktimemarks" : [1,2,3]
 }
]
```

---

## Endpoint: Tariffication - Get coefficient schedule
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/coefficient_schedule`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
  "id" : 1,
  "create_date" : 0,
  "change_date" : 0,
  "items" : [
     {
         "schedule_id" : 1,
                "delay" : 0,
                "duration" : 100,
                "coeff" : 1
     }
  ]
 }
]
```

---

## Endpoint: Tariffication - Get coefficient scheme
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/coefficient_scheme`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
  "id" : "1",
  "name" : "",
  "comment" : "",
  "create_date" : "",
  "change_date" : "",
  "items" : [
     {
         "scheme_id" : 1,
         "delay" : 1,
         "duration" : 1,
         "coeff" : 1
     }
  ]
 }
]
```

---

## Endpoint: Tariffication - Get contract type list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/contract_types`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
   {
    "id" : 5,
    "name" : "Name",
    "create_date" : 5111,
    "change_date" : 4444
   }
]
```

---

## Endpoint: Tariffication - Get group list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/groups`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "group_id": 1,
    "group_name": "Administrators"
  },
  {
    "group_id": 100,
    "group_name": "Hotspot"
  },
  {
    "group_id": 102,
    "group_name": "Users"
  },
  {
    "group_id": 200,
    "group_name": "Guests"
  }
]
```

---

## Endpoint: Tariffication - Get hotspot networks
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/hotspot_networks`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "mask": "255.255.255.255",
    "network": "0.0.0.0"
  },
  {
    "mask": "255.0.0.0",
    "network": "11.0.0.22"
  }
]
```

---

## Endpoint: Tariffication - Get ip pools list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/ippools`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
     "id" : 1,
     "name" : "ipPOOLname",
     "ip" : "1.2.3.4",
     "mask" : "240.0.0.0"
  }
]
```

---

## Endpoint: Tariffication - Get media contents list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/media_contents`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
    {
    "id" : 1,
    "name" : "comedyExample",
    "type" : 0,
    "genre_mask" : 1
    }
]
```

---

## Endpoint: Tariffication - Get media groups list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/media_groups`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
    {
    "id" : 1,
    "name" : "GroupExample",
    "type" : 0,
    }
]
```

---

## Endpoint: Tariffication - Get netflow providers
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/nf_providers`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "ip_address": "1.2.3.4",
    "collector_id": 0,
    "comments": "created during db update",
    "provider_id": 1,
    "name": "1.2.3.4"
  }
]
```

---

## Endpoint: Tariffication - Get radius attributes
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/radius_attrs`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "attr_type": 2,
    "attr_value": "trest",
    "code": 321,
    "expire_date": 2000000000,
    "properties": [],
    "tag": 0,
    "usage_flags": 63,
    "vendor": 123,
    "database_id" : 123
  },
  {
    "attr_type": 2,
    "attr_value": "ttttttttttt",
    "code": 245,
    "expire_date": 2000000000,
    "properties": [],
    "tag": 0,
    "usage_flags": 49,
    "vendor": 321,
    "database_id" : 123
  }
]
```

---

## Endpoint: Tariffication - Get suppliers list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/suppliers`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "account": "",
    "act_adress": "",
    "alt_number_seq": 0,
    "balance": 0.0,
    "bank_id": 0,
    "bookeeper": "",
    "client_prefix": "",
    "contract_number": "",
    "contract_place": "",
    "headman": "",
    "id": 1,
    "inn": "",
    "jur_adress": "",
    "kpp": "",
    "name": "",
    "number_format": "",
    "service_id": 0,
    "service_place": "",
    "short_bookeeper": "",
    "short_headman": "",
    "short_name": "",
    "tax_rate": 0.0,
    "type": 0
  }
]
```

---

## Endpoint: Tariffication - Get tariffs
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/tariffs`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK

[
 {
            "accounts_linked": 1,
            "balance_rollover": 0,
            "change_date": 1569848543,
            "comments": "",
            "create_date": 1569848513,
            "expire_date": 2000000000,
            "id": 1,
            "name": "123",
            "next_accounts_linked": 3,
            "services": [
              {
                "parent_id": 8,
                "service_id": 9
              }
            ],
            "who_change": -1,
            "who_create": -1
       }
      ]
```

---

## Endpoint: Tariffication - Get tarriffs history
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/tariffs_history`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
   "link_date" :   1634128896,
   "tariff_id" :   0,
   "tariff_name" : "Disable current tariff",
   "unlink_date" : 1634128950
  }
]
```

---

## Endpoint: Tariffication - Get tclasses
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/tclasses`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "color": 255,
    "flags": 2,
    "local_policy": 0,
    "name": "Incoming",
    "tclass_id": 10,
    "timerange_id": 0
  },
  {
    "color": 255,
    "flags": 2,
    "local_policy": 0,
    "name": "Outgoing",
    "tclass_id": 20,
    "timerange_id": 0
  },
  {
    "color": 0,
    "flags": 1,
    "local_policy": 0,
    "name": "EDITEDClassNAme",
    "tclass_id": 102,
    "timerange_id": 0
  }
]
```

---

## Endpoint: Tariffication - Get tel direction count
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/get_teldir_count`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
 "count": 0
}
```

---

## Endpoint: Tariffication - Get tel direction
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/tel_direction`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "called_prefix": "495",
  "called_prefix_regexp": false,
  "calling_prefix": "",
  "calling_prefix_regexp": false,
  "create_date": 1548775204,
  "dir_coverage_type": 0,
  "dir_id": 1000000,
  "incoming_trunk": "",
  "name": "495",
  "outgoing_trunk": "",
  "pbx_id": "",
  "skip": false,
  "supplier_id": 0,
  "update_date": 1573034746,
  "zone_id": 1
}
```

---

## Endpoint: Tariffication - Get tel directions list
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/get_tel_directions`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK

{
 total: 0,
 items: [
   {
     "called_prefix": "495",
     "called_prefix_regexp": true,
     "calling_prefix": "",
     "calling_prefix_regexp": true,
     "create_date": 1548775204,
     "dir_coverage_type": 0,
     "dir_id": 1000000,
     "incoming_trunk": "",
     "name": "495",
     "outgoing_trunk": "",
     "pbx_id": "",
     "skip": false,
     "supplier_id": 0,
     "update_date": 1573636052,
     "zone_id": 3
   }
 ]
}
```

---

## Endpoint: Tariffication - Get tel zone by zone_id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/tel_zone`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "create_date": 1573635071,
  "directions": [
    {
      "called_prefix": "495",
      "called_prefix_regexp": true,
      "calling_prefix": "",
      "calling_prefix_regexp": true,
      "create_date": 0,
      "dir_coverage_type": 0,
      "dir_id": 1000000,
      "incoming_trunk": "",
      "name": "495",
      "outgoing_trunk": "",
      "pbx_id": "",
      "skip": false,
      "supplier_id": 0,
      "update_date": 495,
      "zone_id": 3
    }
  ],
  "name": "Tel zone",
  "supplier_id": 0,
  "update_date": 1573636052,
  "zone_id": 3,
  "type": 2
}
```

---

## Endpoint: Tariffication - Get tel zone list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/tel_zones`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "create_date": 1573034733,
    "name": "123",
    "supplier_id": 0,
    "update_date": 1573635099,
    "zone_id": 1,
    "zone_type": 0
  },
  {
    "create_date": 1573633267,
    "name": "332name",
    "supplier_id": 0,
    "update_date": 0,
    "zone_id": 2,
    "zone_type": 0
  },
  {
    "create_date": 1573635071,
    "name": "telZONEEE",
    "supplier_id": 0,
    "update_date": 0,
    "zone_id": 3,
    "zone_type": 0
  }
]
```

---

## Endpoint: Tariffication - Get time ranges
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/time_ranges`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "days": [],
    "name": "All day",
    "priority": 0,
    "slices": [
      {
        "end_hour": 23,
        "end_min": 59,
        "end_sec": 59,
        "end_wday": 6,
        "start_hour": 0,
        "start_min": 0,
        "start_sec": 0,
        "start_wday": 0
      }
    ],
    "tr_id": 1
  }
]
```

---

## Endpoint: Tariffication - Get traffic class
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/traffic_class`
### Parameters:
  - **Name:** `tclass_id`
    - **Type:** `Number`
    - **Description:** Traffic class id
### Example Response:

HTTP/1.1 200 OK
{
  "info": {
    "color": -16777216,
    "flags": 1,
    "local_policy": 0,
    "name": "EDITEDClassNAme",
    "tclass_id": 102,
    "timerange_id": 0
  },
  "item": [
    {
      "daddr": "3.4.5.6",
      "daddr_mask": "255.192.0.0",
      "dport": 0,
      "dst_as": 0,
      "flags": 64,
      "from_addr": "0.0.0.0",
      "iface": 0,
      "item_id": 5,
      "nexthop": "0.0.0.0",
      "nfprovider_id": 0,
      "oface": 0,
      "proto": 0,
      "saddr": "1.2.3.4",
      "saddr_mask": "255.255.252.0",
      "sport": 0,
      "src_as": 0,
      "tcp_flags": 0,
      "tos": 0
    },
    {
      "daddr": "4.3.2.1",
      "daddr_mask": "255.255.255.255",
      "dport": 0,
      "dst_as": 0,
      "flags": 0,
      "from_addr": "0.0.0.0",
      "iface": 0,
      "item_id": 6,
      "nexthop": "0.0.0.0",
      "nfprovider_id": 0,
      "oface": 0,
      "proto": 0,
      "saddr": "1.2.3.4",
      "saddr_mask": "255.255.255.255",
      "sport": 0,
      "src_as": 0,
      "tcp_flags": 0,
      "tos": 0
    }
  ]
}
```

---

## Endpoint: Tariffication - Rewrite radius attrubutes
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/radius_attrs_rewrite`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "result" : "ok"
}
```

---

## Endpoint: Tariffication - Set networks for hotspots
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/hotspot_networks`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "result" : "ok"
}
```

---

## Endpoint: Tariffication - Set radius attrubutes
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/radius_attrs`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "result" : "ok"
}
```

---

## Endpoint: Tariffication - Update accounting period
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/accounting_period`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: Tariffication - Update charge policy
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/charge_policy`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: Tariffication - Update coeff scheme
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/coefficient_scheme`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Update contract type
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/contract_type`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok,
}
```

---

## Endpoint: Tariffication - Update tariff
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/tarrif`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Update tclass
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/tclasses`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Update tel direction
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/tel_direction`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
  {
    "result": "ok"
  }
```

---

## Endpoint: Tariffication - Update telephoning zone
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/tel_zone`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

## Endpoint: Tariffication - Update time range
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/time_ranges`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok"
}
```

---

