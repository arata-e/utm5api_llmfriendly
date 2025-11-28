# UTM5 API Section: Integrations_Netup

This document describes the endpoints for the 'Integrations_Netup' API section for UTM5 isp billing system by Netup Co.

## Endpoint: Integrations/Netup - Customer buy movie
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/integrations/netup/buy-movie`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: Integrations/Netup - Get account info for access card
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/integrations/netup/account-info`
### Parameters:
  - **Name:** `access-card`
    - **Type:** `Number`
    - **Description:** Access card id
### Example Response:

HTTP/1.1 200 OK
{
  "balance" : 1,
  "credit" : 10,
  "current_tariff_plan" : "All included",
  "current_tariff_plan_id" : 1,
  "current_tariff_plan_till" : 0
}
```

---

## Endpoint: Integrations/Netup - Get movie-prices for access card
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/integrations/netup/movie-prices`
### Parameters:
  - **Name:** `access-card`
    - **Type:** `Number`
    - **Description:** Access card id
### Example Response:

HTTP/1.1 200 OK
{
  "code" : 1,
  "service_id" : 10,
  "price" : 100.15,
  "currency" : "р."
}
```

---

