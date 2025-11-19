# UTM5 API Section: Reference_Books

This document describes the endpoints for the 'Reference_Books' API section for UTM5 isp billing system by Netup Co.

## Endpoint: Reference Books - Create bank
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/referencebooks/banks`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "id": 6,
    "result": "ok"
  }
```
---

## Endpoint: Reference Books - Create currencies
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/referencebooks/currencies`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Reference Books - Create houses
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/referencebooks/houses`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "id": 6,
    "result": "ok"
  }
```
---

## Endpoint: Reference Books - Create ip_zone
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/referencebooks/ip_zones`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "id": 6,
    "result": "ok"
  }
```
---

## Endpoint: Reference Books - Create payment methods
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/referencebooks/paymentmethods`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Reference Books - Create street
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/referencebooks/streets`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
      "id": 6,
      "result": "ok"
    }
```
---

## Endpoint: Reference Books - Delete Houses by id
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/referencebooks/houses`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
        "result": "ok"
      }
```
---

## Endpoint: Reference Books - Delete bank by id
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/referencebooks/banks`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
        "result": "ok"
      }
```
---

## Endpoint: Reference Books - Delete currency
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/referencebooks/currencies`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
        "result": "ok"
      }
```
---

## Endpoint: Reference Books - Delete street by id
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/referencebooks/streets`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
        "result": "ok"
      }
```
---

## Endpoint: Reference Books - Get banks by filter
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/referencebooks/banks_search`
- **Ready:** `false`
### Parameters:
  - **Name:** `value`
    - **Type:** `String`
    - **Description:** filter value
  - **Name:** `page`
    - **Type:** `Number`
    - **Description:** number of page
  - **Name:** `per_page`
    - **Type:** `Number`
    - **Description:** items per page
### Example Response:
```
{
	"banks": [{
		"bank_id": 1,
		"bic": "123",
		"city": "new york",
		"kschet": "123213213213",
		"name": "sber"
	}, {
		"bank_id": 2,
		"bic": "23213",
		"city": "moscow",
		"kschet": "1232321312312",
		"name": "mkb"
	}],
	"total_rows": 4
}
```
---

## Endpoint: Reference Books - Get banks
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/referencebooks/banks`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
    "bank_id" : "1",
    "bic" : "",
    "name" : "Bank",
    "city" : "",
    "kschet" : ""
  }
```
---

## Endpoint: Reference Books - Get currencies
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/referencebooks/currencies`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "currency_id" : "810",
  "currency_brief_name" : "RUR",
  "currency_full_name" : "someFullName",
  "rates" : [{"time" : "0","rate" : "1"}],
  "percent" : "0"
 }
```
---

## Endpoint: Reference Books - Get free ip from ip zone of house by uid
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/referencebooks/free_ips_for_house_by_uid`
- **Ready:** `false`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User id
### Example Response:
```
{
  "ip_address" : "1.2.3.4",
  "mask" : 32,
  "zone_name" : "ZoneName"
 }
```
---

## Endpoint: Reference Books - Get free ip from ip zone of house
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/referencebooks/free_ips_for_house`
- **Ready:** `false`
### Parameters:
  - **Name:** `house_id`
    - **Type:** `Number`
    - **Description:** house identifier
### Example Response:
```
{
  "ip_address" : "1.2.3.4",
  "mask" : 32,
  "zone_name" : "ZoneName"
 }
```
---

## Endpoint: Reference Books - Get houses by pages
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/referencebooks/houses_paged`
- **Ready:** `false`
### Parameters:
  - **Name:** `house_id`
    - **Type:** `number`
    - **Description:** House Identifier
  - **Name:** `filter`
    - **Type:** `string`
    - **Description:** search query
  - **Name:** `per_page`
    - **Type:** `number`
    - **Description:** per page number
  - **Name:** `page`
    - **Type:** `number`
    - **Description:** page number
### Example Response:
```
{
         "house_id" : "1",
         "connect_date" : "",
         "post_code" : "",
         "country" : "",
         "region" : "",
         "city" : "",
         "street" : "",
         "number" : "",
         "building" : "",
         "zones" : ["1"],
         "zones_detailed" : [ {"id": 1, "name": "test"}]
 }
```
---

## Endpoint: Reference Books - Get houses
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/referencebooks/houses`
- **Ready:** `false`
### Parameters:
  - **Name:** `house_id`
    - **Type:** `number`
    - **Description:** House Identifier
  - **Name:** `filter`
    - **Type:** `string`
    - **Description:** search query
  - **Name:** `per_page`
    - **Type:** `number`
    - **Description:** per page number
  - **Name:** `page`
    - **Type:** `number`
    - **Description:** page number
### Example Response:
```
{
         "house_id" : "1",
         "connect_date" : "",
         "post_code" : "",
         "country" : "",
         "region" : "",
         "city" : "",
         "street" : "",
         "number" : "",
         "building" : "",
         "zones" : ["1"],
         "zones_detailed" : [ {"id": 1, "name": "test"}]
 }
```
---

## Endpoint: Reference Books - Get ip zones by pages
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/referencebooks/ip_zones_paged`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
 "zones": {


            [
              {
                "networks": [
                  {
                    "gateway": "10.1.4.1",
                    "mask": "255.255.255.0",
                    "mask_dec": 24,
                    "net": "10.1.5.0"
                  }
                ],
                "id": 1,
                "name": "Ip zone"
              }
            ]
          },
        "total_rows" : 123
       }
```
---

## Endpoint: Reference Books - Get ip zones
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/referencebooks/ip_zones`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
        "networks": [
          {
            "gateway": "10.1.4.1",
            "mask": "255.255.255.0",
            "mask_dec": 24,
            "net": "10.1.5.0"
          }
        ],
        "id": 1,
        "name": "Ip zone"
      }
```
---

## Endpoint: Reference Books - Get payments methods
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/referencebooks/paymentmethods`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "id" : "1",
  "name" : "Cash"
 }
```
---

## Endpoint: Reference Books - Get streets
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/referencebooks/streets`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
  "city": "Москва",
  "country": "Россия",
  "region": "Московская область",
  "street": "Улофа Пальме",
  "street_id": 1
 }
```
---

## Endpoint: Reference Books - Update bank
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/referencebooks/banks`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
        "result": "ok"
      }
```
---

## Endpoint: Reference Books - Update currencies
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/referencebooks/currencies`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Reference Books - Update houses
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/referencebooks/houses`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result": "ok"}
```
---

## Endpoint: Reference Books - Update ip_zone
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/referencebooks/ip_zones`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result": "ok"}
```
---

## Endpoint: Reference Books - Update payment methods
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/referencebooks/paymentmethods`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{ "result" : "ok"}
```
---

## Endpoint: Reference Books - Update street
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/referencebooks/streets`
- **Ready:** `false`
### Parameters: None
### Example Response:
```
{
        "result": "ok"
      }
```
---

