# UTM5 API Section: Integrations_24tv

This document describes the endpoints for the 'Integrations_24tv' API section for UTM5 isp billing system by Netup Co.

## Endpoint: Integrations/24tv - Get 24 tv users
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/integrations/24tv/users`
- **Ready:** `false`
### Parameters:
  - **Name:** `offset`
    - **Type:** `Number`
    - **Description:** Offset
  - **Name:** `limit`
    - **Type:** `Number`
    - **Description:** Limit
### Example Response:
```
{
 "total" : 1,
 "items" :
[
   {
     "id": 0,
     "username": "string",
     "first_name": "string",
     "last_name": "string",
     "email": "string",
     "phone": "string",
     "is_active": true,
     "is_provider_free": true,
     "parental_code": "string",
     "device_limit": 0,
     "timezone": "string",
     "timezone_utcoffset": 0,
     "accounts": [
       null
     ],
     "sources": [
       null
     ],
     "provider": {
       "id": 0,
       "name": "string",
       "proxy": "string"
     },
     "provider_uid": "string"
   }
```
---

