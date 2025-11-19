# UTM5 API Section: Settings

This document describes the endpoints for the 'Settings' API section for UTM5 isp billing system by Netup Co.

## Endpoint: Settings - Check radius logins on unique
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/is_unique_radius_logins`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "is_unique": true,
}
```
---

## Endpoint: Settings - Close hotspot session
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/close_hs_session`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "key" : "key",
  "ip_address" : "1.2.3.4"
}
```
---

## Endpoint: Settings - Create DB archive
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/db_archives`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Create DB archive
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/db_archives_with_connection`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Create DB scheduled for archive db
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/db_archives_schedule`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Create NAS
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/nases`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "nas_id": 2,
}
```
---

## Endpoint: Settings - Create NetFlow provider
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/netflow_providers`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "provider_id": 3,
}
```
---

## Endpoint: Settings - Create additional params
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/additionalparams`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "aparam_id": 2,
}
```
---

## Endpoint: Settings - Create and Update hotspot session
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/refresh_hs_session`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "ip_address": "1.2.3.3",
  "key" : "key",
  "login" : "someLogin",
  "pass" : "myPass"
}
```
---

## Endpoint: Settings - Create hotspot session
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/init_hs_session`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "ip_address": "1.2.3.3",
  "key" : "key",
  "login" : "someLogin",
  "pass" : "myPass"
}
```
---

## Endpoint: Settings - Create available activating card
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/available_activating_card`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "group_id" : 1,
  "is_enabled" : 1
}
```
---

## Endpoint: Settings - Create available docs settings
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/available_docs`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id":1,
  "group_id" : 1,
  "is_enabled" : 1,
  "available_docs" : 1
}
```
---

## Endpoint: Settings - Create collector
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/collectors`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "collector_id": 2,
}
```
---

## Endpoint: Settings - Create document profiles
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/documents/profiles`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "profile_id": 2,
}
```
---

## Endpoint: Settings - Create document replacements
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/documents/replacements`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Create document templates
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/documents/templates`
- **Ready:** `false`
### Parameters:
  - **Name:** `name`
    - **Type:** `String`
    - **Description:** Name of odt file
  - **Name:** `type`
    - **Type:** `Number`
    - **Description:** Search value
  - **Name:** `file`
    - **Type:** `object`
    - **Description:** ODT file in request body
### Example Response:
```
{
  "template_id": 2,
}
```
---

## Endpoint: Settings - Create edit profile settings
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/edit_profile`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "group_id" : 1,
  "is_enabled" : 1,
  "available_fields" : 1
}
```
---

## Endpoint: Settings - Create fw rule
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/fw_rules`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "rule_id": 2,
}
```
---

## Endpoint: Settings - Create http server setting
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/http_servers`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "name" : "key",
  "url" : "http://test.com/subrout",
  "method" : 1
}
```
---

## Endpoint: Settings - Create ip v4/v6 pool
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/ippools`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "pool_id": 2,
}
```
---

## Endpoint: Settings - Create isg attribute
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/isg_attrs`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "isg_attr_id": 2,
}
```
---

## Endpoint: Settings - Create isg profiles
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/isg_profiles`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "isg_profile_id": 2,
}
```
---

## Endpoint: Settings - Create payment systems
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/payment_systems`
- **Ready:** `false`
### Parameters: None
### Example Response: Not available
---

## Endpoint: Settings - Create post funds flow settings
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/funds_flow_settings`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Create promised payment setting
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/promised_payments`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Create radius account
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/radius_accounts`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "account_id": 2,
}
```
---

## Endpoint: Settings - Create radius attr tunnel type
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/attr_tunnel_types`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "attr_type" : 1,
  "data_type" : 1
}
```
---

## Endpoint: Settings - Create rentsoft settings
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/rentsoft_settings`
- **Ready:** `false`
### Parameters: None
### Example Response: Not available
---

## Endpoint: Settings - Create router
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/routers`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "router_id": 2,
}
```
---

## Endpoint: Settings - Create services and tariffs which user can connect by himself
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/independent_connect_services`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
 "name" : "Name",
 "group_id" : 1,
 "service_id" : 1,
 "tariff_id" : 1,
 "is_enabled" : 1,
 "is_bonus_enabled" : 1,
 "is_can_be_disabled" : 1,
 "accounting_period_id" : 1,
 "multiple_linking" : 1,
 "is_search_ap_in_services" : 1
}
```
---

## Endpoint: Settings - Create shaping service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/shaping`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok",
}
```
---

## Endpoint: Settings - Create supplier with service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/suppliers_full`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "supplier_id": 2,
}
```
---

## Endpoint: Settings - Create supplier
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/suppliers`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "supplier_id": 2,
}
```
---

## Endpoint: Settings - Create tech support chat settings
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/ts_chat_settings`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "group_id" : 1,
  "is_enabled" : 1
}
```
---

## Endpoint: Settings - Create tel supplier service
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/tel_suppliers/service`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "service_id": 2,
}
```
---

## Endpoint: Settings - Create user by hotSpot login
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/add_user_hs_tariff`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "ip_address": "1.2.3.3",
  "key" : "key",
  "login" : "someLogin",
  "pass" : "myPass"
}
```
---

## Endpoint: Settings - Create user`s tariff data for captive portal user
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/captive_portal_udata`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
 "tariff_id" : 666,
 "name" : "someName",
 "accounting_period_id" : 666,
 "is_enabled" : 1,
 "group_id" : 22
}
```
---

## Endpoint: Settings - Create voluntary suspensions
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/voluntary_suspensions`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok",
}
```
---

## Endpoint: Settings - Create/Update emergency calls
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/settings/emergency_calls`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete NAS
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/nases`
- **Ready:** `false`
### Parameters:
  - **Name:** `nas_id`
    - **Type:** `Number`
    - **Description:** Radius nas id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete additional parameters
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/additionalparams`
- **Ready:** `false`
### Parameters:
  - **Name:** `aparam_id`
    - **Type:** `Number`
    - **Description:** Add param identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete archive scheduled
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/db_archives_schedule`
- **Ready:** `false`
### Parameters:
  - **Name:** `archive_id`
    - **Type:** `Number`
    - **Description:** Archive schedule ID
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete available activating card
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/available_activating_card`
- **Ready:** `false`
### Parameters:
  - **Name:** `id`
    - **Type:** `Number`
    - **Description:** delete activating card
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete available docs settings
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/available_docs`
- **Ready:** `false`
### Parameters:
  - **Name:** `id`
    - **Type:** `Number`
    - **Description:** edit avail report setting id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete available radius attr tunnel type
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/attr_tunnel_types`
- **Ready:** `false`
### Parameters:
  - **Name:** `id`
    - **Type:** `Number`
    - **Description:** delete radius attr tunnel with id
  - **Name:** `attr_type`
    - **Type:** `Number`
    - **Description:** delete radius attr tunnel with attr_type
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete available reports settings
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/available_reports`
- **Ready:** `false`
### Parameters:
  - **Name:** `id`
    - **Type:** `Number`
    - **Description:** edit avail report setting id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete collector
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/collectors`
- **Ready:** `false`
### Parameters:
  - **Name:** `collector_id`
    - **Type:** `Number`
    - **Description:** traffic collector identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete doc profile
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/documents/profiles`
- **Ready:** `false`
### Parameters:
  - **Name:** `profile_id`
    - **Type:** `Number`
    - **Description:** profile identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete doc templates
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/documents/templates`
- **Ready:** `false`
### Parameters:
  - **Name:** `template_id`
    - **Type:** `Number`
    - **Description:** template identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete edit profile settings
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/edit_profile`
- **Ready:** `false`
### Parameters:
  - **Name:** `id`
    - **Type:** `Number`
    - **Description:** edit profile setting id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete emergency calls
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/emergency_calls`
- **Ready:** `false`
### Parameters:
  - **Name:** `service_id`
    - **Type:** `Number`
    - **Description:** service identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete firewall rules
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/fw_rules`
- **Ready:** `false`
### Parameters:
  - **Name:** `rule_id`
    - **Type:** `Number`
    - **Description:** FW rule identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete funds flow settings
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/funds_flow_settings`
- **Ready:** `false`
### Parameters:
  - **Name:** `funds_flow_settings_id`
    - **Type:** `Number`
    - **Description:** Funds flow settings id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete http server setting
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/http_servers`
- **Ready:** `false`
### Parameters:
  - **Name:** `id`
    - **Type:** `Number`
    - **Description:** http server id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete ippool
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/ippools`
- **Ready:** `false`
### Parameters:
  - **Name:** `pool_id`
    - **Type:** `Number`
    - **Description:** pool identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete tel supplier service
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/tel_suppliers/service`
- **Ready:** `false`
### Parameters:
  - **Name:** `supplier_id`
    - **Type:** `Number`
    - **Description:** telephone supplier service identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete isg attrs
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/isg_attrs`
- **Ready:** `false`
### Parameters:
  - **Name:** `isg_attr_id`
    - **Type:** `Number`
    - **Description:** ISG attribute id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete isg profiles
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/isg_profiles`
- **Ready:** `false`
### Parameters:
  - **Name:** `isg_profile_id`
    - **Type:** `Number`
    - **Description:** ISG profile id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete key/value doc replacement
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/documents/replacements`
- **Ready:** `false`
### Parameters:
  - **Name:** `key`
    - **Type:** `Number`
    - **Description:** key of key/value replacement
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete netflow provider
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/netflow_providers`
- **Ready:** `false`
### Parameters:
  - **Name:** `provider_id`
    - **Type:** `Number`
    - **Description:** NF profider identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete payment systems
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/payment_systems`
- **Ready:** `false`
### Parameters:
  - **Name:** `payment_system_id`
    - **Type:** `Number`
    - **Description:** Payment system id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete promised payment settings
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/promised_payments`
- **Ready:** `false`
### Parameters:
  - **Name:** `promised_payment_settings_id`
    - **Type:** `Number`
    - **Description:** Promised payment settings id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete radius account
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/radius_accounts`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** Radius account id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete rentsoft settings
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/rentsoft`
- **Ready:** `false`
### Parameters:
  - **Name:** `rentsoft_setting_id`
    - **Type:** `Number`
    - **Description:** Rentsoft setting ID
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete router
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/routers`
- **Ready:** `false`
### Parameters:
  - **Name:** `router_id`
    - **Type:** `Number`
    - **Description:** Router identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete services and tariffs which user can connect by himself
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/independent_connect_services`
- **Ready:** `false`
### Parameters:
  - **Name:** `independent_connect_services_id`
    - **Type:** `Number`
    - **Description:** Setting identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete shaping service
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/shaping`
- **Ready:** `false`
### Parameters:
  - **Name:** `shaping_id`
    - **Type:** `Number`
    - **Description:** Shaping service id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete supplier
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/suppliers`
- **Ready:** `false`
### Parameters:
  - **Name:** `supplier_id`
    - **Type:** `Number`
    - **Description:** supplier identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete ts chat settings
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/ts_chat_settings`
- **Ready:** `false`
### Parameters:
  - **Name:** `id`
    - **Type:** `Number`
    - **Description:** ts chat setting id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete user`s tariff data for captive portal user by id
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/captive_portal_udata`
- **Ready:** `false`
### Parameters:
  - **Name:** `cp_utariff_data_id`
    - **Type:** `Number`
    - **Description:** captive portal user tariff data identifier
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete voluntary suspension data
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/customer_voluntary_suspension`
- **Ready:** `false`
### Parameters:
  - **Name:** `id`
    - **Type:** `Number`
    - **Description:** Voluntary suspension ID
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Delete voluntary suspensions
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/settings/voluntary_suspensions`
- **Ready:** `false`
### Parameters:
  - **Name:** `voluntary_suspension_id`
    - **Type:** `Number`
    - **Description:** Voluntary suspensions id
### Example Response:
```
{
  "result": "ok,
}
```
---

## Endpoint: Settings - Download document template file
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/documents/template_download`
- **Ready:** `false`
### Parameters:
  - **Name:** `template_id`
    - **Type:** `Number`
    - **Description:** Template ID.
### Example Response:
```

```
---

## Endpoint: Settings - Get  tech support chat settings
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/ts_chat_settings`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id": 2,
  "group_id" : 1,
  "is_enabled" : 1
}
```
---

## Endpoint: Settings - Get Radius Accounts
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/radius_accounts`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** if exist return data by id, else array of all.
### Example Response:
```
{
    "add_nas_attributes": false,
    "id": 1,
    "name": "test",
    "password": "test"
  },
  {
    "add_nas_attributes": true,
    "id": 2,
    "name": "trea",
    "password": "tea"
  }
```
---

## Endpoint: Settings - Get additional params
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/additionalparams`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id" : "1",
  "name" : "extra_param",
  "display_name" : "Extra Param",
  "visible" : "1"
 }
```
---

## Endpoint: Settings - Get all doc replacements
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/documents/replacements`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "key": "Apr",
    "value": "aprelya"
  }
```
---

## Endpoint: Settings - Get available activating card
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/available_activating_card`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id": 2,
  "group_id" : 1,
  "is_enabled" : 1
}
```
---

## Endpoint: Settings - Get available docs settings
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/available_docs`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id": 2,
  "group_id" : 1,
  "is_enabled" : 1,
  "available_docs" : 1
}
```
---

## Endpoint: Settings - Get available reports settings
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/available_reports`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id": 2,
  "group_id" : 1,
  "is_enabled" : 1,
  "available_reports" : 1
}
```
---

## Endpoint: Settings - Get collector statistics
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/collector_stats`
- **Ready:** `false`
### Parameters:
  - **Name:** `collector_id`
    - **Type:** `Number`
    - **Description:** collector identifier
### Example Response:
```
{
  "nf_errors_count": 0,
  "nf_errors_count_last": 0,
  "nf_records_count": 0,
  "nf_records_count_last": 0,
  "uptime": 76,
  "uptime_last": 76
}
```
---

## Endpoint: Settings - Get collectors
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/collectors`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "comments": "Default",
    "collector_id": 0,
    "name": "System"
  }
```
---

## Endpoint: Settings - Get config dhcp6 server
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/dhcp6/config`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "arguments": {
    "Dhcp6": {
      "calculate-tee-times": true,
      "client-classes": [
        {
          "name": "ClinetIfEth5",
          "option-data": [
          ],
          "test": "substring(option[1].hex,12,2) == 0xB200"
        },
        {
          "name": "ClinetIfEth6",
          "option-data": [
          ],
          "test": "substring(option[1].hex,13,2) == 0xCAFE"
        }
      ],
      "ddns-generated-prefix": "myhost",
      "ddns-override-client-update": false,
      "ddns-override-no-update": false,
      "ddns-qualifying-suffix": "",
      "ddns-replace-client-name": "never",
      "ddns-send-updates": true,
      "decline-probation-period": 86400,
      "dhcp-ddns": {
        "enable-updates": false,
        "max-queue-size": 1024,
        "ncr-format": "JSON",
        "ncr-protocol": "UDP",
        "sender-ip": "0.0.0.0",
        "sender-port": 0,
        "server-ip": "127.0.0.1",
        "server-port": 53001
      },
      "dhcp-queue-control": {
        "capacity": 500,
        "enable-queue": false,
        "queue-type": "kea-ring6"
      },
      "dhcp4o6-port": 0,
      "expired-leases-processing": {
        "flush-reclaimed-timer-wait-time": 25,
        "hold-reclaimed-time": 3600,
        "max-reclaim-leases": 100,
        "max-reclaim-time": 250,
        "reclaim-timer-wait-time": 10,
        "unwarned-reclaim-cycles": 5
      },
      "hooks-libraries": [
      ],
      "host-reservation-identifiers": [
        "hw-address",
        "duid"
      ],
      "interfaces-config": {
        "interfaces": [
          "brDHCPv6"
        ],
        "re-detect": true
      },
      "lease-database": {
        "host": "localhost",
        "name": "UTM5",
        "password": "root",
        "port": 3306,
        "type": "mysql",
        "user": "root"
      },
      "mac-sources": [
        "any"
      ],
      "option-data": [
      ],
      "option-def": [
      ],
      "preferred-lifetime": 3000,
      "rebind-timer": 2000,
      "relay-supplied-options": [
        "65"
      ],
      "renew-timer": 1000,
      "reservation-mode": "all",
      "sanity-checks": {
        "lease-checks": "warn"
      },
      "server-id": {
        "enterprise-id": 0,
        "htype": 0,
        "identifier": "",
        "persist": true,
        "time": 0,
        "type": "LLT"
      },
      "server-tag": "",
      "shared-networks": [
      ],
      "subnet6": [
        {
          "calculate-tee-times": true,
          "client-class": "ClinetIfEth5",
          "id": 1,
          "option-data": [
          ],
          "pd-pools": [
          ],
          "pools": [
            {
              "option-data": [
              ],
              "pool": "fe80::2-fe80::ffff"
            }
          ],
          "preferred-lifetime": 3000,
          "rapid-commit": false,
          "rebind-timer": 2000,
          "relay": {
            "ip-addresses": [
            ]
          },
          "renew-timer": 1000,
          "reservation-mode": "all",
          "reservations": [
          ],
          "subnet": "fe80::/64",
          "t1-percent": 0.5,
          "t2-percent": 0.8,
          "valid-lifetime": 4000
        }
      ],
      "t1-percent": 0.5,
      "t2-percent": 0.8,
      "valid-lifetime": 4000
    }
  },
  "result": 0
}
```
---

## Endpoint: Settings - Get core time
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/core_time`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "time": 12321232,
  "tm_zone" : "tz name",
  "tm_gmtoff" : 10800
}
```
---

## Endpoint: Settings - Get custom isg attrs
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/custom_isg_attrs`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "id": 1,
    "attr_id": 1,
    "vendor_id": 1,
    "attr_name": "attr"
  }
```
---

## Endpoint: Settings - Get db archive list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/db_archives`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
	"id" : 1,
	"begin" : "123",
	"end" : "231",
	"status" : 2
}
```
---

## Endpoint: Settings - Get db archive schedule list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/db_archives_schedule`
- **Ready:** `false`
### Parameters:
  - **Name:** `start_date`
    - **Type:** `Number`
    - **Description:** Start date
### Example Response:
```
{
	"error": "",
	"hour": 12,
	"id": 18,
	"is_archived": false,
	"min": 0,
	"name": "tes",
	"run_date": 1684008270,
	"sec": 0,
	"type": 1,
	"use_connection": true
}
```
---

## Endpoint: Settings - Get default system setting  tax
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/system_vat_tax`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
   "value": 13.0
}
```
---

## Endpoint: Settings - Get document profiles
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/documents/profiles`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
     "created": 1567756397,
     "modified": 1567756397,
     "name": "Documents for legal entity (default)",
     "profile_id": 1,
     "templates": [
         {
         "type": 2,
         "template_id" : 3
         }
      ]
   },
   {
     "created": 1567756397,
     "modified": 1567756397,
     "name": "Documents for invididual",
     "profile_id": 2,
     "templates": []
   }
```
---

## Endpoint: Settings - Get document templates
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/documents/templates`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
     "created": 0,
     "modified": 0,
     "name": "Invoice for legal entity",
     "odt": "",
     "path": "invoice.odt",
     "template_id": 1,
     "type": 1
   }
```
---

## Endpoint: Settings - Get dynamic shaped services
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/shaping_services`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
     "service_id" : 405,
     "service_name" : "MyServiceName",
     "comment" : "Mycomment"
 }
```
---

## Endpoint: Settings - Get edit profile settings
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/edit_profile`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id": 2,
  "group_id" : 1,
  "is_enabled" : 1,
  "available_fields" : 1
}
```
---

## Endpoint: Settings - Get emergency calls list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/emergency_calls`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "service_id": 0,
    "tel_directions": [
      2
    ]
  },
  {
    "service_id": 6,
    "tel_directions": [
      2
    ]
  }
```
---

## Endpoint: Settings - Get firewall rules
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/fw_rules`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
   "affector_id": 0,
   "affector_type": 0,
   "comment": "123",
   "events": 1,
   "flags": 0,
   "group_id": 200,
   "rule_id": 1,
   "tariff_id": 0,
   "text": "ls -lah",
   "user_id": 332
 }
```
---

## Endpoint: Settings - Get funds flow settings
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/funds_flow_settings`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
                "id": 1,
                "group_id": 0,
                "priority": 0,
                "is_enabled": 0
            }
```
---

## Endpoint: Settings - Get fw event masks
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/fw_subst`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "events": 4093103734527,
    "subst_info": "EMAIL"
  },
  {
    "events": 4093103734527,
    "subst_info": "ACCOUNT_ID"
  }
```
---

## Endpoint: Settings - Get fw events mask
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/fw_events`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
 "events_human_readable": [
   "inet on",
   "inet off",
   "block changed",
   "user added",
   "user modified",
   "user deleted",
   "tech parameters added",
   "tech parameters modified",
   "tech parameters deleted",
   "iptraffic added",
   "iptraffic modified",
   "iptraffic deleted",
   "raw file closed",
   "log file closed",
   "session opened",
   "session closed",
   "balance notification",
   "new payment for account",
   "user log added",
   "set bandwidth limit in",
   "change bandwidth limit in",
   "delete bandwidth limit in",
   "set bandwidth limit out",
   "change bandwidth limit out",
   "delete bandwidth limit out",
   "hotspot enable",
   "hotspot disable",
   "hotspot user added",
   "dialup added",
   "dialup modified",
   "dialutp deleted",
   "tel added",
   "tel modified",
   "tel deleted"
 ],
  "events_mask": 4677219385343
}
```
---

## Endpoint: Settings - Get http servers setting
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/http_servers`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id": 3,
  "name" : "key",
  "url" : "http://test.com/subrout",
  "method" : 1
}
```
---

## Endpoint: Settings - Get ip pools
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/ippools`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "id": 1,
    "ip": "10.1.5.0",
    "mask": "255.255.255.0",
    "mask_dec": 24,
    "name": "1"
  }
```
---

## Endpoint: Settings - Get isg attrs list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/isg_attrs`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "attr_id": 15,
    "attr_name": "moscEDITEDow",
    "id": 2,
    "vendor_id": 66
  }
```
---

## Endpoint: Settings - Get isg profiles
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/isg_profiles`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "blocked_account_code": 3,
    "id": 3,
    "lease_address": false,
    "login_type": 1,
    "name": "33",
    "password_type": 1,
    "send_coa": true,
    "session_time": 5,
    "static_password": "",
    "switch_type_id": 1,
    "unblocked_account_code": 2
  },
  {
    "blocked_account_code": 2,
    "id": 4,
    "lease_address": true,
    "login_type": 1,
    "name": "profi",
    "password_type": 2,
    "send_coa": true,
    "session_time": 123,
    "static_password": "pass",
    "switch_type_id": 5,
    "unblocked_account_code": 2
  }
```
---

## Endpoint: Settings - Get license
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/license`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "cur_accounts": 10,
  "cur_users": 10,
  "license_type": "Telecom",
  "max_accounts": 500,
  "max_users": 500,
  "till": 1852255976
}
```
---

## Endpoint: Settings - Get list of captive portal user tariff data
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/captive_portal_udata_list`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "cp_utariff_data_id" : 13,
  "name": "name",
  "tariff_id" : 666,
  "accounting_period_id" : 666,
  "is_enabled" : 1
  "group_id" : 22
 },
 {
  "cp_utariff_data_id" : 15,
  "tariff_id" : 666,
  "name": "name2",
  "accounting_period_id" : 666,
  "is_enabled" : 0
  "group_id" : 22
 }
```
---

## Endpoint: Settings - Get nas list OR get Nas by id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/nases`
- **Ready:** `false`
### Parameters:
  - **Name:** `nas_id`
    - **Type:** `Number`
    - **Description:** if nas identifier exist, else all nas list
### Example Response:
```
{
    "affector_id": 0,
    "comment": "123",
    "events": 1,
    "flags": 0,
    "group_id": 200,
    "rule_id": 1,
    "tariff_id": 0,
    "text": "ls -lah",
    "user_id": 332
  }
```
---

## Endpoint: Settings - Get netflow providers
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/netflow_providers`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "ip_address": "127.0.0.1",
    "collector_id": 0,
    "comments": "",
    "provider_id": 1,
    "name": "local"
  }
```
---

## Endpoint: Settings - Get payment systems template
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/payment_systems_template`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
   "data": [
     {
       "id": 1,
       "name": "username",
       "payment_system_id": 1,
       "value": ""
     },
     {
       "id": 2,
       "name": "password",
       "payment_system_id": 1,
       "value": ""
     },
     {
       "id": 3,
       "name": "currency",
       "payment_system_id": 1,
       "value": ""
     },
     {
       "id": 4,
       "name": "language",
       "payment_system_id": 1,
       "value": ""
     }
   ],
   "id": 1,
   "name": ""
 }
```
---

## Endpoint: Settings - Get payment systems
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/payment_systems`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
   "data": [
     {
       "id": 1,
       "name": "username",
       "payment_system_id": 1,
       "value": ""
     },
     {
       "id": 2,
       "name": "password",
       "payment_system_id": 1,
       "value": ""
     },
     {
       "id": 3,
       "name": "currency",
       "payment_system_id": 1,
       "value": ""
     },
     {
       "id": 4,
       "name": "language",
       "payment_system_id": 1,
       "value": ""
     }
   ],
   "id": 1,
   "name": "",
   "group_id": 0
 }
```
---

## Endpoint: Settings - Get promised payments settings
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/promised_payments`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
            "flags": 0,
            "free_balance": 0.0,
            "group_id": 0,
            "id": 1,
            "interval_duration": 0,
            "is_enabled": 0,
            "last_payment_date": 0,
            "max_duration": 0,
            "max_value": 0.0,
            "min_balance": 0.0,
            "priority": 0,
            "service_id": 0,
            "use_free_balance": 0,
            "use_min_balance": 0
        }
```
---

## Endpoint: Settings - Get registry settings form
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/registry_settings_form`
- **Ready:** `false`
### Parameters:
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** Group ID from settings/registry_settings_group request
  - **Name:** `object_id`
    - **Type:** `Number`
    - **Description:** Object ID ( 0 - core, 1..n - (id)traffic collector)
### Example Response:
```
{
   "validation_flags": 0,
   "value_type": 4,
   "description": "path to .utm file with detailed traffic",
   "name": "raw_prefix",
   "raw_values": [
     {
       "value": "/netup/utm5/db/"
     }
   ],
   "setting_id": 65537
 }
```
---

## Endpoint: Settings - Get registry settings group
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/registry_settings_group`
- **Ready:** `false`
### Parameters:
  - **Name:** `comp_id`
    - **Type:** `Number`
    - **Description:** component identifier (1 - core, 2 - traffic collector)
### Example Response:
```
{
    "allow_multiple_objects": false,
    "component_id": 1,
    "description": "Tariffication settings",
    "group_id": 2
  },
  {
    "allow_multiple_objects": false,
    "component_id": 1,
    "description": "Card user settings",
    "group_id": 3
  }
```
---

## Endpoint: Settings - Get registry value REG_BYTES_IN_KBYTE
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/bytes_in_kb`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": 1024,
}
```
---

## Endpoint: Settings - Get rentsoft settings
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/rentsoft_settings`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "cp_utariff_data_id" : 13,
  "name": "name",
  "tariff_id" : 666,
  "accounting_period_id" : 666,
  "is_enabled" : 1
  "group_id" : 22
 }
```
---

## Endpoint: Settings - Get response config reload dhcp6 server
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/dhcp6/config_reload`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": 0,
  "text": "Configuration successful."
}
```
---

## Endpoint: Settings - Get response config reload dhcp6 server
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/dhcp6/config_write`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "arguments": {
    "filename": "/netup/utm5/dhcpv6_config_helper.json",
    "size": 2875
  },
  "result": 0,
  "text": "Configuration written to /netup/utm5/dhcpv6_config_helper.json successful"
}
```
---

## Endpoint: Settings - Get result of making payment for supplier
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/make_payment_for_supplier`
- **Ready:** `false`
### Parameters:
  - **Name:** `supplier_id`
    - **Type:** `Number`
    - **Description:** supplier identifier
  - **Name:** `sum`
    - **Type:** `Number`
    - **Description:** amount of payment
  - **Name:** `reason_of_payment`
    - **Type:** `Number`
    - **Description:** comment for payment
  - **Name:** `currency_type`
    - **Type:** `Number`
    - **Description:** type of currency
  - **Name:** `in_type`
    - **Type:** `Number`
    - **Description:** type of payment
### Example Response:
```
{
  "absolute_sum": 1.2
}
```
---

## Endpoint: Settings - Get result of start to update status of all DB archives
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/db_archives_update`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok",
}
```
---

## Endpoint: Settings - Get result of start to verify all DB archives
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/db_archives_verify`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok",
}
```
---

## Endpoint: Settings - Get routers
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/routers`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "address": "0.0.0.0",
    "comments": "Local",
    "id": 1,
    "login": "",
    "name": "127.0.0.1",
    "ns_state": 0,
    "password": "",
  }
```
---

## Endpoint: Settings - Get services and tariffs which user can connect by himself
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/independent_connect_services`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id" : 1,
  "name" : "Name",
  "group_id" : 1,
  "service_id" : 1,
  "tariff_id" : 1,
  "is_enabled" : 1,
  "is_bonus_enabled" : 1,
  "is_can_be_disabled" : 1,
  "accounting_period_id" : 1,
  "multiple_linking" : 0
 }
```
---

## Endpoint: Settings - Get setting by name
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/setting`
- **Ready:** `false`
### Parameters:
  - **Name:** `setting_name`
    - **Type:** `Number`
    - **Description:** setting name
### Example Response:
```
{
    "value": "/netup/utm5/db/"
  }
```
---

## Endpoint: Settings - Get shaping
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/shaping`
- **Ready:** `false`
### Parameters:
  - **Name:** `service_id`
    - **Type:** `Number`
    - **Description:** Service ID.
### Example Response:
```
{
  "ingress_egress": [
    {
      "shaping": [
        {
          "account_state": 0,
          "border": 1232,
          "limit": "34",
          "timerange": 3
        }
      ],
      "tclass": [
        10,
        20
      ]
    },
    {
      "shaping": [
        {
          "account_state": 0,
          "border": 231232,
          "limit": "1",
          "timerange": 3
        },
        {
          "account_state": 0,
          "border": 1231232123,
          "limit": "22",
          "timerange": 3
        }
      ],
      "tclass": [
        20,
        10
      ]
    }
  ],
  "flags": 0,
  "radius_attrs": [],
  "turbo_mode_settings": []
}
```
---

## Endpoint: Settings - Get supplier
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/supplier`
- **Ready:** `false`
### Parameters:
  - **Name:** `supplier_id`
    - **Type:** `Number`
    - **Description:** Supplier ID.
### Example Response:
```
{
  "account": "123",
  "act_adress": "rio",
  "alt_number_seq": 0,
  "balance": 0.0,
  "bank_id": 666,
  "bookeeper": "Some Bank",
  "client_prefix": "user",
  "contract_number": "123",
  "contract_place": "mos",
  "headman": "Mr. User",
  "id": 13,
  "inn": "123",
  "jur_adress": "moscow",
  "kpp": "456",
  "name": "nameJUR",
  "number_format": "num",
  "service_id": 0,
  "service_place": "serv",
  "short_bookeeper": "SB",
  "short_headman": "mr.",
  "short_name": "short",
  "tax_rate": 13.11,
  "type": 0
}
```
---

## Endpoint: Settings - Get suppliers directions
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/tel_suppliers/directions`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
     "dir_id": 2,
     "supplier_id": 3
 }
```
---

## Endpoint: Settings - Get suppliers zones
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/tel_suppliers/zones`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
     "dir_id": 2,
     "supplier_id": 3
 }
```
---

## Endpoint: Settings - Get switch tariff  settings
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/switch_tariffs`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
	"id" :  11,
	"group_id" : 2 ,
	"priority" :  3,
	"is_enabled" : 0 ,
	"instant_change" : true ,
	"instant_change_count" : 2 ,
	"data" :  [
     {
     	"id" : 1,
     	"tariff_id" : 2,
     	"min_balance" : 1.1,
     	"use_min_balance" : 4,
     	"free_balance" : 4.1,
     	"use_free_balance" : 3,
     	"service_id" : 12
 }
]
}
```
---

## Endpoint: Settings - Get switch tariff settings full data
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/switch_tariffs_full`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
	"id" :  11,
	"group_id" : 2 ,
	"priority" :  3,
	"is_enabled" : 0 ,
	"instant_change" : true ,
	"instant_change_count" : 2 ,
	"data" :  [
     {
     	"id" : 1,
     	"tariff_id" : 2,
         "tariff_nae": "test"
     	"min_balance" : 1.1,
     	"use_min_balance" : 4,
     	"free_balance" : 4.1,
     	"use_free_balance" : 3,
     	"service_id" : 12
 }
]
}
```
---

## Endpoint: Settings - Get tech params slinks
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/tech_params_slinks`
- **Ready:** `false`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User ID.
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** Account ID.
### Example Response:
```
{
   "service_name": "iptv ORT",
   "slink_id": 6
 }
```
---

## Endpoint: Settings - Get tech params
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/tech_params`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
   "id": 1,
   "name": "web"
 },
 {
   "id": 2,
   "name": "email"
 }
```
---

## Endpoint: Settings - Get tel supplier report of charges
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/tel_suppliers/report_of_charges`
- **Ready:** `false`
### Parameters:
  - **Name:** `supplier_id`
    - **Type:** `Number`
    - **Description:** supplier identifier
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start data ,in sec from epoch
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end data ,in sec from epoch
### Example Response:
```
{
    "user_id" : 1,
    "user_login" : "loging",
    "account_id" : 1,
    "session_id" : 1,
    "customer_cost" : 1.2,
    "customer_cost_with_tax" : 1.3,
    "supplier_cost" : 1.4,
    "supplier_cost_with_tax" : 1.5,
    "duration" : 121,
    "charge_duration" : 1231232,
    "called_station_id" : "123",
    "calling_station_id" : "421",
    "charge_date" : 12131232
}
```
---

## Endpoint: Settings - Get tel supplier report of invoices
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/tel_suppliers/report_of_invoices`
- **Ready:** `false`
### Parameters:
  - **Name:** `supplier_id`
    - **Type:** `Number`
    - **Description:** supplier identifier
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start data ,in sec from epoch
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end data ,in sec from epoch
### Example Response:
```
{
    "account_id" : 1,
    "invoice_id" : 1,
    "alt_number" : 1,
    "invoice_date" : 1123,
    "expire_date" : 132131232,
    "zone_type" : 1,
    "dir_type" : 1,
    "vat_rate" : 1,
    "cost" : 1,
    "qnt" : 1,
    "client" : "cli3",
    "formatted_num" : "form",
    "service_place" : "someplace"
}
```
---

## Endpoint: Settings - Get tel supplier report of payments
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/tel_suppliers/report_of_payments`
- **Ready:** `false`
### Parameters:
  - **Name:** `supplier_id`
    - **Type:** `Number`
    - **Description:** supplier identifier
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start data ,in sec from epoch
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end data ,in sec from epoch
### Example Response:
```
{
		"currency_type": 1,
		"sum": 1.2,
		"payment_date": 1123123213,
		"reason_of_payment": "myreason"
	},
	{
		"currency_type": 0,
		"sum": 1.2,
		"payment_date": 1123123213,
		"reason_of_payment": "myreason"
	}
```
---

## Endpoint: Settings - Get tel supplier report of users
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/tel_suppliers/report_of_users`
- **Ready:** `false`
### Parameters:
  - **Name:** `supplier_id`
    - **Type:** `Number`
    - **Description:** supplier identifier
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start data ,in sec from epoch
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end data ,in sec from epoch
### Example Response:
```
{
 "client" : {
  	"account_id" : 1,
  	"is_juridical" : 1,
  	"full_name" : "name",
  	"juridical_address" : "address",
  	"inn" : "123",
  	"kpp" : "321",
  	"contract_begin_date" : 1123123,
  	"contract_end_date" : 13213213
     },
 "contract_place" : "Pupkino town"
}
```
---

## Endpoint: Settings - Get tel suppliers service
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/tel_suppliers/service`
- **Ready:** `false`
### Parameters:
  - **Name:** `supplier_id`
    - **Type:** `Number`
    - **Description:** Supplier identifier
### Example Response:
```
{
  "service_data": {
    "comment": "Supplier-1TelServiceComment",
    "contract_type": 0,
    "invoice_sup_id": 1,
    "is_dynamic": 0,
    "link_by_default": 0,
    "links_count": 0,
    "multiple_linking": 0,
    "parent_id": 0,
    "service_id": 49,
    "service_name": "Supplier-1TelServiceName",
    "service_type": 7,
    "service_type_name": "telephony supplier",
    "tariff_id": 0
  },
  "tel_service_data": {
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
          "tariff_key": 1000001
        }
      ],
      "discount_free_time": true,
      "first_period_length": 0,
      "first_period_step": 0,
      "free_time": 0,
      "min_charge": 0.0,
      "second_period_step": 1,
      "supplier_id": 6,
      "time_unit_size": 60
    },
    "service_id": 49,
    "session_timeout": 86400
  }
}
```
---

## Endpoint: Settings - Get tunnel types
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/attr_tunnel_types`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id": 2,
  "attr_type" : 1,
  "data_type" : 1
}
```
---

## Endpoint: Settings - Get voluntary all suspensions
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/all_voluntary_suspensions`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
     "account_id":1,
     "block_date_end":1679950800,
     "block_date_start":1679941756,
     "block_id":10,
     "id":1
 }
```
---

## Endpoint: Settings - Get voluntary suspensions settings
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/settings/voluntary_suspensions`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
           "block_end": 0,
           "block_id": 0,
           "block_start": 0,
           "block_type": 0,
           "free_balance": 15.0,
           "group_id": 0,
           "id": 1,
           "interval_duration": 259200,
           "is_enabled": 1,
           "max_duration": 172800,
           "min_balance": 12.0,
           "min_duration": 86400,
           "priority": 0,
           "self_unlock": 1,
           "service_id": 0,
           "use_free_balance": 1,
           "use_min_balance": 1
       }
```
---

## Endpoint: Settings - Notifier for captive user login
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/login_captive_user`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Put payment systems
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/payment_systems`
- **Ready:** `false`
### Parameters: None
### Example Response: Not available
---

## Endpoint: Settings - Put registry setting
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/registry_setting`
- **Ready:** `false`
### Parameters: None
### Example Response: Not available
---

## Endpoint: Settings - Put switch tariffs
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/switch_tariffs`
- **Ready:** `false`
### Parameters: None
### Example Response: Not available
---

## Endpoint: Settings - Test db connection
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/test_db_connection`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "connection": "database=utm_archive1; database_host=127.0.0.1; database_login=root; database_password=root; database_port=3307; dbcount=6;database_reconnect_count=5; database_reconnect_sleep=2; database_charset=utf8",
}
```
---

## Endpoint: Settings - Update NAS by Id
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/nases`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update NetFlow provider
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/netflow_providers`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update additional params
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/additionalparams`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update available activating card
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/available_activating_card`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id":1,
  "group_id" : 1,
  "is_enabled" : 1
}
```
---

## Endpoint: Settings - Update available docs settings
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/available_docs`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id":1,
  "group_id" : 1,
  "is_enabled" : 1,
  "available_docs" : 1
}
```
---

## Endpoint: Settings - Update available reports settings
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/available_reports`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id":1,
  "group_id" : 1,
  "is_enabled" : 1,
  "available_reports" : 1
}
```
---

## Endpoint: Settings - Update collector
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/collectors`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update config dhcpv6 server
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/dhcp6/set_config`
- **Ready:** `false`
### Parameters: None
### Example Response: Not available
---

## Endpoint: Settings - Update document profiles
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/documents/profiles`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update document templates
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/documents/templates`
- **Ready:** `false`
### Parameters:
  - **Name:** `name`
    - **Type:** `String`
    - **Description:** Name of odt file
  - **Name:** `template_id`
    - **Type:** `Number`
    - **Description:** template identifier
  - **Name:** `type`
    - **Type:** `Number`
    - **Description:** Search value
  - **Name:** `file`
    - **Type:** `object`
    - **Description:** ODT file in request body
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update edit profile settings
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/edit_profile`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id": 2,
  "group_id" : 1,
  "is_enabled" : 1,
  "available_fields" : 1
}
```
---

## Endpoint: Settings - Update funds flow settings
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/funds_flow_settings`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update fw rule
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/fw_rules`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "rule_id": 2,
}
```
---

## Endpoint: Settings - Update http server setting
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/http_servers`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id" : 3,
  "name" : "key",
  "url" : "http://test.com/subrout",
  "method" : 1
}
```
---

## Endpoint: Settings - Update ip v4/v6 pool
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/ippools`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update isg attribute
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/isg_attrs`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update isg profiles
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/isg_profiles`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update promised payment setting
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/promised_payments`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update radius account
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/radius_accounts`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "account_id": 2,
}
```
---

## Endpoint: Settings - Update radius attr tunnel types
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/attr_tunnel_types`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id": 2,
  "attr_type" : 1,
  "data_type" : 1
}
```
---

## Endpoint: Settings - Update rentsoft settings
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/rentsoft_settings`
- **Ready:** `false`
### Parameters: None
### Example Response: Not available
---

## Endpoint: Settings - Update router
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/routers`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update services and tariffs which user can connect by himself
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/independent_connect_services`
- **Ready:** `false`
### Parameters: None
### Example Response: Not available
---

## Endpoint: Settings - Update shaping service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/shaping`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update supplier
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/suppliers`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update tech support chat settings
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/ts_chat_settings`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id": 2,
  "group_id" : 1,
  "is_enabled" : 1
}
```
---

## Endpoint: Settings - Update tel supplier service
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/tel_suppliers/service`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update user`s tariff data for captive portal user
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/captive_portal_udata`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Update voluntary suspensions
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/voluntary_suspensions`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "result": "ok"
}
```
---

## Endpoint: Settings - Validate tel supplier directions
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/settings/tel_suppliers/validate_dirs`
- **Ready:** `false`
### Parameters:
  - **Name:** `supplier_id`
    - **Type:** `Number`
    - **Description:** Supplier identifier
### Example Response:
```
{
 "founded_dir_id": 0,
 "founded_supplier_id": 0,
 "founded_zone_id": 0
}
```
---

