# UTM5 API Section: customer

This document describes the endpoints for the 'customer' API section for UTM5 isp billing system by Netup Co.

## Endpoint: customer - Delete customer 24tv service
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/customer/24tv_service`
- **Ready:** `false`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User id
  - **Name:** `packet_id`
    - **Type:** `Number`
    - **Description:** Packet id
  - **Name:** `sub_id`
    - **Type:** `Number`
    - **Description:** Subscription id
### Example Response:
```
{ "result" : "ok" }
```
---

## Endpoint: customer - Delete service links
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/customer/servicelinks`
- **Ready:** `false`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link id
### Example Response:
```
{ "result" : "ok" }
```
---

