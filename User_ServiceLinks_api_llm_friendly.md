# UTM5 API Section: User_ServiceLinks

This document describes the endpoints for the 'User_ServiceLinks' API section for UTM5 isp billing system by Netup Co.

## Endpoint: User/ServiceLinks - Create coefficient schedule
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/coefficient_schedule`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "coefficient_schedule_link" : 1 }
```
---

## Endpoint: User/ServiceLinks - Create dialup
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/dialup`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "service_link_id" : 1 }
```
---

## Endpoint: User/ServiceLinks - Create hotspot
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/hotspot`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "service_link_id" : 1 }
```
---

## Endpoint: User/ServiceLinks - Create iptraffic
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/iptraffic`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "service_link_id" : 1 }
```
---

## Endpoint: User/ServiceLinks - Create iptv
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/iptv`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "service_link_id" : 1 }
```
---

## Endpoint: User/ServiceLinks - Create service link once
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/once`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "service_link_id" : 1 }
```
---

## Endpoint: User/ServiceLinks - Create service link periodic
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/periodic`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "service_link_id" : 1 }
```
---

## Endpoint: User/ServiceLinks - Create telephony
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/telephony`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "service_link_id" : 1 }
```
---

## Endpoint: User/ServiceLinks - Create vod
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/vod`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "service_link_id" : 1 }
```
---

## Endpoint: User/ServiceLinks - Enable turbo mode
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/enable_turbo_mode`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: User/ServiceLinks - Get all user service links
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** Users unique ID.
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** Users unique login.
### Example Response:
```
{
                "account_id" : "1",
                "service_id" : "1",
                "service_type" : "3",
                "service_type_name" : "periodic",
                "service_name" : "periodic123",
                "in_tariff" : "No",
                "cost" : "0",
                "service_link_id" : "1",
                "accounting_period_id" : "1",
                "comment": "",
         }
```
---

## Endpoint: User/ServiceLinks - Get coefficient schedule
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks/coefficient_schedule`
- **Ready:** `false`
### Parameters:
  - **Name:** `schedule_link_id`
    - **Type:** `Number`
    - **Description:** Schedule link id.
### Example Response:
```
{
  "id" : 1,
  "scheme_id" : 2,
  "slink_id" : 2,
  "schedule_id" : 2,
  "change_policy" : 2,
  "create_date" : 2,
  "change_date" : 2
 }
```
---

## Endpoint: User/ServiceLinks - Get dialup
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks/dialup`
- **Ready:** `false`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link id.
### Example Response:
```
{
        "dialupServiceLink": {
            "allowed_cid": "",
            "allowed_csid": "",
            "callback_enabled": 0,
            "login": "abc",
            "old_time": 0,
            "password": "111",
            "slink_id": 167,
            "time_in_curr_disc_period": 0
        },
        "periodicservicelink": {
            "accounting_period_id": 106,
            "charged_in_curr_period": 0.0,
            "house_comment": "",
            "comment": "",
            "cost_coef": 1.0,
            "expire_date": 2000000000,
            "fee_recalc": {
                "duration": 0,
                "start": 0
            },
            "house_id": 1,
            "ip_recalc": {
                "duration": 0,
                "start": 0
            },
            "is_invoice_set": false,
            "is_planning": false,
            "last_charge_date": 0,
            "need_del": false,
            "policy_id": 2,
            "repaid_in_curr_period": 0.0,
            "slink_id": 167,
            "start_date": 1565949405,
            "tel_recalc": {
                "duration": 0,
                "start": 0
            }
        },
        "servicedata": {
            "comment": "",
            "contract_type": 0,
            "invoice_sup_id": 1,
            "is_dynamic": 0,
            "link_by_default": 0,
            "links_count": 1,
            "multiple_linking": 0,
            "service_id": 34,
            "service_name": "dialup",
            "service_type": 5,
            "service_type_name": "dialup",
            "tariff_id": 0
        },
        "servicelink": {
            "account_id": 41,
            "is_dynamic": false,
            "service_id": 34,
            "slink_id": 167,
            "tariff_link_id": 0,
            "user_id": 41
        },
        "coefficientschedulelink":{
        "change_date":1696947929,
        "change_policy":0,
        "create_date":1696947929,
        "id":23,
        "schedule_id":23,
        "scheme_id":1,
        "slink_id":42
        },
      }
```
---

## Endpoint: User/ServiceLinks - Get freezed
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks/freezed`
- **Ready:** `false`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link id.
### Example Response:
```
{
            "cost_coef": 1.0,
            "discount_date": 1571209245,
            "is_executed": false,
            "slink_id": 165
        }
```
---

## Endpoint: User/ServiceLinks - Get hotspot
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks/hotspot`
- **Ready:** `false`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link id.
### Example Response:
```
{
        "hotspotservicelink": {
            "login": "as",
            "old_time": 0,
            "password": "as",
            "recv_bytes": 0,
            "slink_id": 166,
            "time_in_curr_disc_period": 0
        },
        "periodicservicelink": {
            "accounting_period_id": 106,
            "charged_in_curr_period": 0.0,
            "house_comment": "",
            "comment": "",
            "cost_coef": 1.0,
            "expire_date": 2000000000,
            "fee_recalc": {
                "duration": 0,
                "start": 0
            },
            "house_id": 1,
            "ip_recalc": {
                "duration": 0,
                "start": 0
            },
            "is_invoice_set": false,
            "is_planning": false,
            "last_charge_date": 0,
            "need_del": false,
            "policy_id": 2,
            "repaid_in_curr_period": 0.0,
            "slink_id": 166,
            "start_date": 1565949252,
            "tel_recalc": {
                "duration": 0,
                "start": 0
            }
        },
        "servicedata": {
            "comment": "",
            "contract_type": 0,
            "invoice_sup_id": 1,
            "is_dynamic": 0,
            "link_by_default": 0,
            "links_count": 1,
            "multiple_linking": 0,
            "service_id": 20,
            "service_name": "asd",
            "service_type": 4,
            "service_type_name": "hotspot",
            "tariff_id": 0
        },
        "servicelink": {
            "account_id": 41,
            "is_dynamic": false,
            "service_id": 20,
            "slink_id": 166,
            "tariff_link_id": 0,
            "user_id": 41
        }
      }
```
---

## Endpoint: User/ServiceLinks - Get iptraffic
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks/iptraffic`
- **Ready:** `false`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link id.
### Example Response:
```
{
         "bandwidth": {
           "in": 0,
           "out": 0
         },
         "ip_group": {
           "account_id": 41,
           "ipgroup_id": 28,
           "items": [
             {
               "allowed_cid": "",
               "dhcp_options": [
                 {
                   "addresses": [],
                   "id": 1,
                   "type": 3,
                   "value": "1.1.1.1"
                 },
                 {
                   "addresses": [],
                   "id": 2,
                   "type": 1,
                   "value": 13
                 },
                 {
                   "addresses": [
                     "1.1.1.1",
                     "2.2.2.2"
                   ],
                   "id": 3,
                   "type": 5
                 },
                 {
                   "addresses": [],
                   "id": 12,
                   "type": 2,
                   "value": "String"
                 },
                 {
                   "addresses": [],
                   "id": 26,
                   "type": 4,
                   "value": "ba0f"
                 }
               ],
               "flags": 3,
               "id": 88,
               "ip": "0.0.0.0",
               "ip_family": 4,
               "isg_attrs": [
                 {
                   "id": 136,
                   "ip_group_id": 88,
                   "isg_attr_id": 1,
                   "isg_attr_value": "test"
                 },
                 {
                   "id": 137,
                   "ip_group_id": 88,
                   "isg_attr_id": 2,
                   "isg_attr_value": "none"
                 },
                 {
                   "id": 138,
                   "ip_group_id": 88,
                   "isg_attr_id": 4,
                   "isg_attr_value": "none"
                 },
                 {
                   "id": 139,
                   "ip_group_id": 88,
                   "isg_attr_id": 5,
                   "isg_attr_value": "none"
                 },
                 {
                   "id": 140,
                   "ip_group_id": 88,
                   "isg_attr_id": 6,
                   "isg_attr_value": "none"
                 }
               ],
               "login": "Tredvv",
               "mac": "",
               "mask": 0,
               "nfprovider_id": 1,
               "password": "4624c562",
               "pool_id": 0,
               "pool_name": "1",
               "port_id": 1,
               "switch_id": 1,
               "vlan_id": 1
             }
           ],
           "slink_id": 240
         },
         "iptrafficServiceLink": {
           "custom_prepaid": [],
           "discounted": [],
           "downed_as_prepaid": [],
           "downloaded": [],
           "downloaded_id": 103,
           "group_id2leader": [],
           "ip_group_id": 28,
           "is_quota_executed": [],
           "old_prepaid": [],
           "slink_id": 240,
           "traffic_quota": [
             {
               "tclass": 10,
               "traffic_quota": 100
             },
             {
               "tclass": 20,
               "traffic_quota": 209
             }
           ]
         },
         "periodicservicelink": {
           "accounting_period_id": 108,
           "charged_in_curr_period": 0.0,
           "house_comment": "",
           "comment": "",
           "cost_coef": 0.1,
           "expire_date": 2000000000,
           "fee_recalc": {
             "duration": 640942,
             "start": 0
           },
           "house_id": 1,
           "ip_recalc": {
             "duration": 0,
             "start": 0
           },
           "is_invoice_set": false,
           "is_planning": false,
           "last_charge_date": 0,
           "need_del": false,
           "policy_id": 1,
           "repaid_in_curr_period": 0.0,
           "slink_id": 240,
           "start_date": 1567580542,
           "tel_recalc": {
             "duration": 0,
             "start": 0
           }
         },
         "servicedata": {
           "comment": "",
           "contract_type": 0,
           "invoice_sup_id": 1,
           "is_dynamic": 0,
           "link_by_default": 0,
           "links_count": 2,
           "multiple_linking": 0,
           "service_id": 2,
           "service_name": "ip_traffic_service",
           "service_type": 3,
           "service_type_name": "iptraffic",
           "tariff_id": 0
         },
         "servicelink": {
           "account_id": 41,
           "is_dynamic": true,
           "service_id": 2,
           "slink_id": 240,
           "tariff_link_id": 0,
           "user_id": 41
         }
       }
```
---

## Endpoint: User/ServiceLinks - Get iptv
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks/iptv`
- **Ready:** `false`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link id.
### Example Response:
```
{
          "periodicservicelink": {
            "accounting_period_id": 1,
            "charged_in_curr_period": 0.0,
            "comment": "",
            "cost_coef": 1.0,
            "expire_date": 2000000000,
            "fee_recalc": {
              "duration": 0,
              "start": 0
            },
            "house_id": 0,
            "ip_recalc": {
              "duration": 0,
              "start": 0
            },
            "is_invoice_set": false,
            "is_planning": false,
            "last_charge_date": 0,
            "need_del": false,
            "policy_id": 1,
            "repaid_in_curr_period": 0.0,
            "slink_id": 6,
            "start_date": 1571053237,
            "tel_recalc": {
              "duration": 0,
              "start": 0
            }
          },
          "servicedata": {
            "comment": "",
            "contract_type": 0,
            "invoice_sup_id": 1,
            "is_dynamic": 0,
            "link_by_default": 0,
            "links_count": 1,
            "multiple_linking": 0,
            "service_id": 1,
            "service_name": "iptv ORT",
            "service_type": 8,
            "service_type_name": "iptv",
            "tariff_id": 0
          },
          "servicelink": {
            "account_id": 4,
            "is_dynamic": false,
            "service_id": 1,
            "slink_id": 6,
            "tariff_link_id": 0,
            "user_id": 4
          },
            "coefficientschedulelink":{
                "change_date":1696947929,
                "change_policy":0,
                "create_date":1696947929,
                "id":23,
                "schedule_id":23,
                "scheme_id":1,
                "slink_id":42
                }
        }
```
---

## Endpoint: User/ServiceLinks - Get once
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks/once`
- **Ready:** `false`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link id.
### Example Response:
```
{
            "cost_coef": 1.0,
            "discount_date": 1571209245,
            "executing": false,
            "slink_id": 165
        }
```
---

## Endpoint: User/ServiceLinks - Get periodic service link stats
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks/periodic_slink_stats`
- **Ready:** `false`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link ID
### Example Response:
```
{
  "accounting_period_id": 1,
  "charged_in_curr_period": 591.3000000000001,
  "comment": "",
  "cost_coef": 45.0,
  "expire_date": 1577183351,
  "fee_recalc": {
    "duration": 0,
    "start": 0
  },
  "house_id": 0,
  "ip_recalc": {
    "duration": 0,
    "start": 0
  },
  "is_invoice_set": true,
  "is_planning": false,
  "last_charge_date": 1577104151,
  "need_del": false,
  "policy_id": 2147483646,
  "repaid_in_curr_period": 0.0,
  "slink_id": 37,
  "start_date": 1577104151,
  "tel_recalc": {
    "duration": 0,
    "start": 0
  }
}
```
---

## Endpoint: User/ServiceLinks - Get periodic
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks/periodic`
- **Ready:** `false`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link id.
### Example Response:
```
{
            "periodicservicelink": {
                "accounting_period_id": 3,
                "charged_in_curr_period": 4.052633633469427,
                "house_comment": "",
                "comment": "",
                "cost_coef": 1.0,
                "expire_date": 2000000000,
                "fee_recalc": {
                    "duration": 39155557,
                    "start": 0
                },
                "house_id": 0,
                "ip_recalc": {
                    "duration": 0,
                    "start": 0
                },
                "is_invoice_set": true,
                "is_planning": false,
                "last_charge_date": 1565771564,
                "need_del": false,
                "policy_id": 1,
                "repaid_in_curr_period": 0.0,
                "slink_id": 164,
                "start_date": 1565771557,
                "tel_recalc": {
                    "duration": 0,
                    "start": 0
                }
            },
            "servicedata": {
                "comment": "",
                "contract_type": 0,
                "invoice_sup_id": 1,
                "is_dynamic": 0,
                "link_by_default": 0,
                "links_count": 2,
                "multiple_linking": 0,
                "service_id": 3,
                "service_name": "service1",
                "service_type": 2,
                "service_type_name": "periodic",
                "tariff_id": 0
            },
            "servicelink": {
                "account_id": 41,
                "is_dynamic": false,
                "service_id": 3,
                "slink_id": 164,
                "tariff_link_id": 0,
                "user_id": 41
            }
        }
```
---

## Endpoint: User/ServiceLinks - Get service link shaping
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks/slink_shaping`
- **Ready:** `false`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link id.
### Example Response:
```
{
	"flags" : 123,
	"turbomode_settings_id" : 123,
	"incoming_rate" : "123",
	"outgoing_rate" : "123",
	"turbo_mode_start" : 123,
	"turbo_mode_end" : 123,
	"incoming_consumption_left" : 123,
	"outgoing_consumption_left" : 123
}
```
---

## Endpoint: User/ServiceLinks - Get telephony
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/servicelinks/telephony`
- **Ready:** `false`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link id.
### Example Response:
```
{
         "periodicservicelink": {
           "accounting_period_id": 3,
           "charged_in_curr_period": 0.0,
           "house_comment": "",
           "comment": "",
           "cost_coef": 1.0,
           "expire_date": 2000000000,
           "fee_recalc": {
             "duration": 0,
             "start": 1566295303
           },
           "house_id": 0,
           "ip_recalc": {
             "duration": 0,
             "start": 0
           },
           "is_invoice_set": false,
           "is_planning": false,
           "last_charge_date": 0,
           "need_del": false,
           "policy_id": 2,
           "repaid_in_curr_period": 0.0,
           "slink_id": 169,
           "start_date": 1566295276,
           "tel_recalc": {
             "duration": 0,
             "start": 0
           }
         },
         "servicedata": {
           "comment": "",
           "contract_type": 0,
           "invoice_sup_id": 1,
           "is_dynamic": 0,
           "link_by_default": 0,
           "links_count": 1,
           "multiple_linking": 0,
           "service_id": 38,
           "service_name": "1",
           "service_type": 6,
           "service_type_name": "telephony",
           "tariff_id": 0
         },
         "servicelink": {
           "account_id": 43,
           "is_dynamic": false,
           "service_id": 38,
           "slink_id": 169,
           "tariff_link_id": 0,
           "user_id": 43
         },
         "telephonyServiceLink": {
           "consumption": [],
           "numbers": [
             {
               "allowed_cid": "",
               "incoming_trunk": "1",
               "login": "1",
               "num_id": 1,
               "number": "",
               "outgoing_trunk": "",
               "password": "",
               "pbx_id": "",
               "slink_id": 169
             }
           ],
           "slink_id": 169
         }
       }
```
---

## Endpoint: User/ServiceLinks - Update coefficient schedule
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/servicelinks/coefficient_schedule`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok" }
```
---

## Endpoint: User/ServiceLinks - Update dialup
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/servicelinks/dialup`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok" }
```
---

## Endpoint: User/ServiceLinks - Update hotspot
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/servicelinks/hotspot`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok" }
```
---

## Endpoint: User/ServiceLinks - Update iptraffic
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/servicelinks/iptraffic`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok" }
```
---

## Endpoint: User/ServiceLinks - Update iptv
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/servicelinks/iptv`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok" }
```
---

## Endpoint: User/ServiceLinks - Update once
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/servicelinks/once`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok" }
```
---

## Endpoint: User/ServiceLinks - Update periodic
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/servicelinks/periodic`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok" }
```
---

## Endpoint: User/ServiceLinks - Update telephony
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/servicelinks/telephony`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok" }
```
---

## Endpoint: User/ServiceLinks - Update vod
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/servicelinks/vod`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok" }
```
---

