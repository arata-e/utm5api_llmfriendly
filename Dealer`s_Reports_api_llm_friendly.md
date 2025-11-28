# UTM5 API Section: Dealer`s_Reports

This document describes the endpoints for the 'Dealer`s_Reports' API section for UTM5 isp billing system by Netup Co.

## Endpoint: Dealer`s Reports - Get blocking info
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/dealer/blocks`
### Parameters:
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end] from request
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end date of report
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start date of report
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** user identifier
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** account identifier
  - **Name:** `dealer_id`
    - **Type:** `Number`
    - **Description:** dealer unique identifier
  - **Name:** `is_show_all`
    - **Type:** `Number`
    - **Description:** show only admin and not deleted,or all [0|1]
### Example Response:

HTTP/1.1 200 OK
[
  {
    "account_id": 3,
    "block_data": {
      "account_id": 3,
      "block_type": 1,
      "expire_date": 1572452080,
      "flags": 0,
      "id": 2,
      "is_deleted": true,
      "is_planning": false,
      "start_date": 1572451024
    },
    "login": "root"
  },
  {
    "account_id": 3,
    "block_data": {
      "account_id": 3,
      "block_type": 1,
      "expire_date": 2000000000,
      "flags": 0,
      "id": 6,
      "is_deleted": false,
      "is_planning": false,
      "start_date": 1573289476
    },
    "login": "root"
  }
]
```

---

## Endpoint: Dealer`s Reports - Get dealer traffic report
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/dealer/traffic`
### Parameters:
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end] from request
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end date of report
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start date of report
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** user identifier
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** account identifier
  - **Name:** `dealer_id`
    - **Type:** `Number`
    - **Description:** dealer unique identifier
  - **Name:** `type`
    - **Type:** `Number`
    - **Description:** type of grouped ;enum {by hour :1,by_day,by_month,by_ip}
### Example Response:

HTTP/1.1 200 OK
[
 {
   "account_id": 4,
   "accounting_period_id": 0,
   "base_cost": 1245.0,
   "bytes": 1245,
   "charge": 1245.0,
   "charge_with_tax": 1245.0,
   "date": 1245,
   "human_date" : "Thu Jan  1 03:00:00 1970",
   "ip_id": "0.0.0.0",
   "is_prepaid": false,
   "login": "new_uvser",
   "slink_id": 1245,
   "tclass": 1245
 }
]
```

---

## Endpoint: Dealer`s Reports - Get dealer's invoices report
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/dealer/invoices`
### Parameters:
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end date of report
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start date of report
  - **Name:** `dealer_id`
    - **Type:** `Number`
    - **Description:** dealer unique identifier
### Example Response:

HTTP/1.1 200 OK
[
  {
    "currency_rate": 1.0,
    "doc_type": 1,
    "invoice": {
      "acc_invc": {
        "date": 0,
        "id": 0,
        "invc_id": 0,
        "is_printed": 0,
        "payed_date": 0,
        "payment_ext_number": ""
      },
      "account_id": 3,
      "alt_number": 2,
      "arrearage": 0.0,
      "balance_on_set": 10.0,
      "entries": [
        {
          "accounting_period_id": 276,
          "alt_amount": 0,
          "base_cost": 1.0,
          "details": [],
          "id": 2,
          "invoice_id": 2,
          "name": "inet",
          "qnt": 1.0,
          "service_type": 2,
          "slink_id": 4,
          "sum_cost": 1.0,
          "tax_amount": 0.0,
          "version": 0
        }
      ],
      "expire_date": 0,
      "ext_num": "",
      "id": 2,
      "invoice_date": 1572511125,
      "is_payed": 0,
      "is_printed": 0,
      "payment_transaction_id": 0,
      "period_end": 1572511125,
      "period_start": 1572382800,
      "supplier_id": 1,
      "uid": 3,
      "user_invoice_date": 1572511125,
      "version": 1
    },
    "is_odt_mailed": 0,
    "is_pdf_mailed": 0,
    "odt_created": 0,
    "odt_modified": 0,
    "odt_status": -1,
    "pdf_created": 0,
    "pdf_modified": 0,
    "pdf_status": -1
  }
]
```

---

## Endpoint: Dealer`s Reports - Get dealer's payments report
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/dealer/payments`
### Parameters:
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end] from request
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end date of report
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start date of report
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** user identifier
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** account identifier
  - **Name:** `dealer_id`
    - **Type:** `Number`
    - **Description:** dealer unique identifier
### Example Response:

HTTP/1.1 200 OK
[
 {
   "account_id": 3,
   "actual_date": 1572452076,
   "admin_comment": "",
   "burnt_date": 0,
   "comment": "",
   "currency_id": 810,
   "currency_rate": 1.0,
   "external_id": "",
   "hash": "",
   "id": 4,
   "login": "root",
   "method": 1,
   "payment": 11.0,
   "payment_enter_date": 1572452080,
   "payment_ext_number": "",
   "payment_incurrency": 11.0,
   "user_id": -1
 },
 {
   "account_id": 4,
   "actual_date": 1572601259,
   "admin_comment": "",
   "burnt_date": 0,
   "comment": "",
   "currency_id": 810,
   "currency_rate": 1.0,
   "external_id": "",
   "hash": "",
   "id": 6,
   "login": "new_uvser",
   "method": 1,
   "payment": -12.0,
   "payment_enter_date": 1572601264,
   "payment_ext_number": "",
   "payment_incurrency": -12.0,
   "user_id": -1
 }
]
```

---

## Endpoint: Dealer`s Reports - Get dealer's services report
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/dealer/services`
### Parameters:
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end] from request
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end date of report
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start date of report
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** user identifier
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** account identifier
  - **Name:** `dealer_id`
    - **Type:** `Number`
    - **Description:** dealer unique identifier
### Example Response:

HTTP/1.1 200 OK
[{
	"account_id": 1,
	"accounting_period_id": 5,
	"charge": 12.0,
	"charge_with_tax": 12.0,
	"date": 1667154251,
	"full_name": "testFull name",
	"login": "adres",
	"outgoing_rest": -913.0,
	"service_name": "period",
	"service_type": 2
}]
```

---

## Endpoint: Dealer`s Reports - Get dealer's sessions report
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/dealer/sessions`
### Parameters:
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end] from request
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end date of report
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start date of report
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** user identifier
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** account identifier
  - **Name:** `dealer_id`
    - **Type:** `Number`
    - **Description:** dealer unique identifier
### Example Response:

HTTP/1.1 200 OK
[
 {
   "account_id": 3,
   "acct_delay_time": 0,
   "acct_inp_giga": 666,
   "acct_inp_oct": 555,
   "acct_inp_pack": 44444,
   "acct_out_giga": 4311,
   "acct_out_oct": 324321,
   "acct_out_pack": 3432,
   "acct_sess_time": 2311,
   "acct_session_id": "sessionID",
   "acct_status_type": 2,
   "acct_term_cause": 366,
   "called_station_id": "calledID",
   "calling_station_id": "callingID",
   "details": [],
   "flags": 3,
   "framed_ip": "0.16.244.71",
   "framed_ip6": "0:19:debd:1c7::8474:6b8e",
   "framed_protocol": 2,
   "id": 1,
   "last_update_date": 1574414696,
   "login": "root",
   "nas_id": "nasiae",
   "nas_ip": "0.5.22.21",
   "nas_port": 2,
   "nas_port_type": 3,
   "radius_attrs": [],
   "recv_date": 1574414676,
   "service_type": 3,
   "slink_id": 4,
   "uname": "useER"
 }
]
```

---

## Endpoint: Dealer`s Reports - Get dealer's telephony report
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/dealer/telephony`
### Parameters:
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end] from request
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end date of report
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start date of report
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** user identifier
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** account identifier
  - **Name:** `dealer_id`
    - **Type:** `Number`
    - **Description:** dealer unique identifier
### Example Response:

HTTP/1.1 200 OK
[
  {
    "account_id": 3,
    "acct_delay_time": 0,
    "acct_sess_time": 45,
    "acct_session_id": "accid",
    "acct_status_type": 2,
    "acct_term_cause": 0,
    "called_station_id": "calledID",
    "calling_station_id": "callingID",
    "details": [],
    "dir_id": 31,
    "flags": 64,
    "framed_protocol": 4,
    "h323_call_origin": "calORR",
    "h323_call_type": "TYpe",
    "h323_conf_id": "confID",
    "h323_connect_time": "22-13",
    "h323_disconnect_cause": "Valid cause code not yet received",
    "h323_disconnect_time": "13-55",
    "h323_gw_id": "gw_id",
    "h323_remote_address": "1.2.3.4",
    "h323_setup_time": "11:22:44",
    "id": 1,
    "incoming_trunk": "someTruncInc",
    "last_update_date": 1574413676,
    "login": "root",
    "nas_id": "nasID",
    "nas_ip": "0.16.244.71",
    "nas_port": 11,
    "nas_port_type": 1,
    "outgoing_trunk": "someTrOut",
    "pbx_id": "idpbx",
    "radius_attrs": [],
    "recv_date": 1574414676,
    "service_type": 3,
    "setup_time": 1111,
    "slink_id": 2,
    "tel_supplier_id": 444444,
    "uname": "USSSS",
    "zone_id": 13
  }
]
```

---

## Endpoint: Dealer`s Reports - Get dealer`s general report
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/dealer/general`
### Parameters:
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end] from request
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end date of report
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start date of report
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** user identifier
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** account identifier
  - **Name:** `dealer_id`
    - **Type:** `Number`
    - **Description:** dealer unique identifier
### Example Response:

HTTP/1.1 200 OK
[
  {
    "account_id": 1,
    "incoming_found": true,
    "incoming_rest": 0.0,
    "other_charges": 0.0,
    "outgoing_rest": 6.0,
    "payments": 6.0,
    "services_discount": [
      {
        "discount": -6.0,
        "service_type": 0
      },
      {
        "discount": -6.0,
        "service_type": 0
      }
    ],
    "services_discount_with_tax": []
  }
]
```

---

