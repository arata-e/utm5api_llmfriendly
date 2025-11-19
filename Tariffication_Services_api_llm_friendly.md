# UTM5 API Section: Tariffication_Services

This document describes the endpoints for the 'Tariffication_Services' API section for UTM5 isp billing system by Netup Co.

## Endpoint: Tariffication Services - Create dialup service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/services/dialup`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "service_id": 33
}
```
---

## Endpoint: Tariffication Services - Create freezed service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/services/freezed`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "service_id" : 1}
```
---

## Endpoint: Tariffication Services - Create hotspot service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/services/hotspot`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "service_id": 6,
}
```
---

## Endpoint: Tariffication Services - Create ip traffic service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/services/iptraffic`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "service_id": 33
}
```
---

## Endpoint: Tariffication Services - Create iptv service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/services/iptv`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "service_id": 33
}
```
---

## Endpoint: Tariffication Services - Create once service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/services/once`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "service_id" : 1}
```
---

## Endpoint: Tariffication Services - Create periodic service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/services/periodic`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "service_id": 19
}
```
---

## Endpoint: Tariffication Services - Create telephony service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/services/telephony`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "service_id": 25
}
```
---

## Endpoint: Tariffication Services - Create vod service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/tariffing/services/vod`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "service_id": 33
}
```
---

## Endpoint: Tariffication Services - Get charge policy by service id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/charge_policy`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
          "policy_id" : 1,
}
```
---

## Endpoint: Tariffication Services - Get dialup by service id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/dialup`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "dialup_service_data": {
    "costs": [
      {
        "cost": 12.0,
        "time_range_id": 1,
        "time_range_name": "All day"
      }
    ],
    "login_prefix": "",
    "max_timeout": 86400,
    "pool_name": "",
    "service_id": 32
  },
  "periodic_service_data": {
    "charge_method": 1,
    "cost": 0.0,
    "expire_date": 2000000000,
    "have_tried_to_del": 0,
    "policy_id": 1,
    "radius_sessions_limit": 0,
    "scheme_id": 0,
    "service_id": 32,
    "start_date": 1573461014
  },
  "service_data": {
    "comment": "dial",
    "contract_type": 0,
    "invoice_sup_id": 1,
    "is_dynamic": 0,
    "link_by_default": 1,
    "links_count": 0,
    "multiple_linking": 0,
    "parent_id": 22,
    "service_id": 32,
    "service_name": "dialup",
    "service_type": 5,
    "service_type_name": "dialup",
    "tariff_id": 4
  }
}
```
---

## Endpoint: Tariffication Services - Get freezed service
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/freezed`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "freezed_service_data": {
    "cost": 100.0,
    "service_id": 24,
    "charge_type_action" :1
  },
  "service_data": {
    "comment": "Edited ",
    "contract_type": 0,
    "invoice_sup_id": 1,
    "is_dynamic": 0,
    "link_by_default": 1,
    "links_count": 2,
    "multiple_linking": 0,
    "parent_id": 0,
    "service_id": 24,
    "service_name": "FREEEZE editedv3",
    "service_type": 10,
    "service_type_name": "freezed payments",
    "tariff_id": 0
  }
}
```
---

## Endpoint: Tariffication Services - Get hotspot by service id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/hotspot`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "hotspot_service_data": {
    "allowed_net": [
      {
        "network": "0.0.0.0",
        "mask": "255.255.255.255"
      }
    ],
    "costs": [
      {
        "cost": 1.0,
        "time_range_name": "All day",
        "timerange_id": 1
      }
    ],
    "max_timeout": 86400,
    "rate_limit": "",
    "recv_cost": 0.0,
    "service_id": 29
  },
  "periodic_service_data": {
    "charge_method": 1,
    "cost": 11.0,
    "expire_date": 2000000000,
    "have_tried_to_del": 0,
    "policy_id": 1,
    "radius_sessions_limit": 0,
    "scheme_id": 0,
    "service_id": 29,
    "start_date": 1573202780
  },
  "service_data": {
    "comment": "hspot",
    "contract_type": 0,
    "invoice_sup_id": 1,
    "is_dynamic": 0,
    "link_by_default": 0,
    "links_count": 0,
    "multiple_linking": 0,
    "parent_id": 21,
    "service_id": 29,
    "service_name": "hotSpot",
    "service_type": 4,
    "service_type_name": "hotspot",
    "tariff_id": 5
  }
}
```
---

## Endpoint: Tariffication Services - Get ip_tv by service id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/iptv`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "iptv_service_data": {
    "custom_data": "113",
    "media_content": 0,
    "media_group": 0
  },
  "periodic_service_data": {
    "charge_method": 1,
    "cost": 0.0,
    "expire_date": 2000000000,
    "have_tried_to_del": 0,
    "policy_id": 1,
    "radius_sessions_limit": 0,
    "scheme_id": 0,
    "service_id": 4,
    "start_date": 0
  },
  "service_data": {
    "comment": "lifestream",
    "contract_type": 0,
    "invoice_sup_id": 1,
    "is_dynamic": 0,
    "link_by_default": 1,
    "links_count": 0,
    "multiple_linking": 0,
    "service_id": 4,
    "service_name": "IpTV",
    "service_type": 8,
    "service_type_name": "iptv",
    "tariff_id": 0
  }
}
```
---

## Endpoint: Tariffication Services - Get iptraffic by service id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/iptraffic`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "iptraffic_service_data": {
    "aggregation_interval": 0,
    "borders": [],
    "group2tf": [],
    "null_service_prepaid": false,
    "prepaid": [],
    "prepaid_max": [],
    "service_id": 10,
    "tclass_id2group": []
  },
  "periodic_service_data": {
    "charge_method": 1,
    "cost": 1.0,
    "expire_date": 2000000000,
    "have_tried_to_del": 0,
    "policy_id": 1,
    "radius_sessions_limit": 0,
    "scheme_id": 0,
    "service_id": 10,
    "start_date": 1572961752
  },
  "service_data": {
    "comment": "",
    "contract_type": 0,
    "invoice_sup_id": 1,
    "is_dynamic": 0,
    "link_by_default": 1,
    "links_count": 0,
    "multiple_linking": 0,
    "parent_id": 2,
    "service_id": 10,
    "service_name": "inet",
    "service_type": 3,
    "service_type_name": "iptraffic",
    "tariff_id": 3
  }
}
```
---

## Endpoint: Tariffication Services - Get links count by service id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/links_count`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
          "links_count" : 1,
}
```
---

## Endpoint: Tariffication Services - Get multi linking by service id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/multi_linking`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
          "multiple_linking" : 1
}
```
---

## Endpoint: Tariffication Services - Get once service
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/once`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "once_service_data": {
    "cost": 0.0,
    "service_id": 0,
    "drop_from_group": 0,
  },
  "service_data": {
    "comment": "123",
    "contract_type": 1,
    "invoice_sup_id": 2,
    "is_dynamic": 0,
    "link_by_default": 0,
    "links_count": 0,
    "multiple_linking": 0,
    "parent_id": 0,
    "service_id": 63,
    "service_name": "321",
    "service_type": 1,
    "service_type_name": "once",
    "tariff_id": 0
  }
}
```
---

## Endpoint: Tariffication Services - Get periodic service by service id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/periodic`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "periodic_service_data": {
    "charge_method": 1,
    "cost": 4.0,
    "expire_date": 2000000000,
    "have_tried_to_del": 0,
    "policy_id": 1,
    "radius_sessions_limit": 0,
    "scheme_id": 0,
    "service_id": 18,
    "start_date": 0
  },
  "service_data": {
    "comment": "",
    "contract_type": 0,
    "invoice_sup_id": 0,
    "is_dynamic": 0,
    "link_by_default": 1,
    "links_count": 1,
    "multiple_linking": 1,
    "service_id": 18,
    "service_name": "test1",
    "service_type": 2,
    "service_type_name": "periodic",
    "tariff_id": 4
  }
}
```
---

## Endpoint: Tariffication Services - Get services
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
      "service_id" : 1,
      "service_type" : 1,
      "service_type_name" : "iptraffic",
      "service_name" : "iptraffic",
      "comment" : "",
      "tariff_id" : 1,
      "links_count" : 1,
      "link_by_default" : 0,
      "multiple_linking" : 0,
      "is_dynamic" : 0,
      "invoice_sup_id" : 0,
      "contract_type" : 1,
      "scheme_id" : 1
  }
```
---

## Endpoint: Tariffication Services - Get supplier_id by service id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/supplier_id`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
          "supplier_id" : 1,
}
```
---

## Endpoint: Tariffication Services - Get telephony by service id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/telephony`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "periodic_service_data": {
    "charge_method": 1,
    "cost": 0.0,
    "expire_date": 2000000000,
    "have_tried_to_del": 0,
    "policy_id": 1,
    "radius_sessions_limit": 0,
    "scheme_id": 0,
    "service_id": 27,
    "start_date": 1573138405
  },
  "service_data": {
    "comment": "telTEEEST",
    "contract_type": 0,
    "invoice_sup_id": 1,
    "is_dynamic": 0,
    "link_by_default": 1,
    "links_count": 0,
    "multiple_linking": 0,
    "parent_id": 23,
    "service_id": 27,
    "service_name": "TESTTEL",
    "service_type": 6,
    "service_type_name": "telephony",
    "tariff_id": 7
  },
  "telephony_service_data": {
    "cost_info": {
      "cost_table": [
        {
          "cost_info": {
            "borders": [
              {
                "border": 0,
                "cost_coefficient": 1.0
              }
            ],
            "costs": [
              {
                "cost": 0.0,
                "time_range_id": 1
              }
            ],
            "fixed_cost": 0.0,
            "prepaid": 0
          },
          "tariff_key": 1000000
        }
      ],
      "discount_free_time": true,
      "first_period_length": 0,
      "first_period_step": 0,
      "free_time": 0,
      "min_charge": 0.0,
      "second_period_step": 1,
      "supplier_id": 0,
      "time_unit_size": 3600
    },
    "service_id": 27,
    "session_timeout": 86400
  }
}
```
---

## Endpoint: Tariffication Services - Get vod service
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/tariffing/services/vod`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "periodic_service_data": {
    "charge_method": 1,
    "cost": 1.0,
    "expire_date": 2000000000,
    "have_tried_to_del": 0,
    "policy_id": 1,
    "radius_sessions_limit": 0,
    "scheme_id": 0,
    "service_id": 40,
    "start_date": 0
  },
  "service_data": {
    "comment": "vod COmment",
    "contract_type": 0,
    "invoice_sup_id": 1,
    "is_dynamic": 0,
    "link_by_default": 1,
    "links_count": 0,
    "multiple_linking": 0,
    "parent_id": 23,
    "service_id": 40,
    "service_name": "VODname",
    "service_type": 9,
    "service_type_name": "video on demand",
    "tariff_id": 2
  },
  "vod_service_data": {
    "custom_data": "123",
    "duration": 12312323,
    "media_content": 123,
    "media_group": 123,
    "type": 3
  }
}
```
---

## Endpoint: Tariffication Services - Set charge policy for service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/set_charge_policy`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result" : "ok"
}
```
---

## Endpoint: Tariffication Services - Set multi linking for service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/set_multi_linking`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result" : "ok"
}
```
---

## Endpoint: Tariffication Services - Set supplier id for service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/set_supplier_id`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result" : "ok"
}
```
---

## Endpoint: Tariffication Services - Update dialup service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/dialup`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result" : "ok"
}
```
---

## Endpoint: Tariffication Services - Update freezed service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/freezed`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Tariffication Services - Update hotspot service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/hotspot`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result" : "ok"
}
```
---

## Endpoint: Tariffication Services - Update ip traffic service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/iptraffic`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result" : "ok"
}
```
---

## Endpoint: Tariffication Services - Update iptv service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/iptv`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Tariffication Services - Update once service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/once`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Tariffication Services - Update periodic services
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/periodic`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result" : "ok"
}
```
---

## Endpoint: Tariffication Services - Update telephony service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/telephony`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result" : "ok",
}
```
---

## Endpoint: Tariffication Services - Update vod service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/tariffing/services/vod`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result" : "ok"
}
```
---

