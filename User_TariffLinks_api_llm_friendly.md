# UTM5 API Section: User_TariffLinks

This document describes the endpoints for the 'User_TariffLinks' API section for UTM5 isp billing system by Netup Co.

## Endpoint: User/TariffLinks - Get services in tariff link
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/services_in_tariff_link`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User id.
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** Account id.
  - **Name:** `tariff_link_id`
    - **Type:** `Number`
    - **Description:** Tariff link id.
### Example Response:

HTTP/1.1 200 OK
[
 {
  "slink_id" : 0,
  "service_id" : 1,
  "scheme_id":1,
  "service_name" : "Periodic",
  "service_type" : 1,
  "comment" : "",
  "policy_id":1
 }
]
```

---

## Endpoint: User/TariffLinks - Get tariff links
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/tarifflinks`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User id.
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** Account id.
### Example Response:

HTTP/1.1 200 OK
[
          {
            "accounting_period_id": 583,
            "current_tariff_id": 1,
            "id": 1,
            "next_tariff_id": 1,
            "change_date": 1676655117
          }
]
```

---

## Endpoint: User/TariffLinks - Post tariff link
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/tarifflinks`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "tariff_link_id" : 1}
```

---

## Endpoint: User/TariffLinks - Unschedule tariff link
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/unschedule_tarifflink`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

