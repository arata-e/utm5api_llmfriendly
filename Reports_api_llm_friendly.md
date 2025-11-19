# UTM5 API Section: Reports

This document describes the endpoints for the 'Reports' API section for UTM5 isp billing system by Netup Co.

## Endpoint: Reports - Get currency rate
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/currency_rate_rbc`
- **Ready:** `false`
### Parameters:
  - **Name:** `id`
    - **Type:** `Number`
    - **Description:** currency id
### Example Response:
```
{
 "rate" = 1.1
}
```
---

## Endpoint: Reports - Get report blocks
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/blocks`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
### Example Response:
```
{
       "block_id": 1,
       "account_id": 2,
       "block_end": 2000000000,
       "human_block_start" : "Thu Jan  1 03:00:00 1970"
       "block_start": 1548775390,
       "human_block_end": "Thu Jan  1 03:00:00 1970"
       "block_type": 1,
       "is_deleted": false,
       "login": "4952"
     }
```
---

## Endpoint: Reports - Get report general info
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/general`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end]
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** User group ID, if zero , then user_id or account_id != 0
  - **Name:** `limit`
    - **Type:** `Number`
    - **Description:** Limit of report rows
### Example Response:
```
{
	"account_id": 1,
	"dialup": 4.0,
	"full_name": "testFull name",
	"hotspot": 2.0,
	"incoming_rest": -901.0,
	"ip_traffic": 0.0,
	"iptv": 0.0,
	"login": "adres",
	"once": 0.0,
	"other": 0.0,
	"outgoing_rest": 1089.0,
	"payments": 1167.0,
	"periodic": 48.0,
	"sum_with_tax": 54.0,
	"tax": 0.0,
	"telephony": 0.0,
	"vod": 0.0
}
```
---

## Endpoint: Reports - Get report of burning payments
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/burning_payments`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end]
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** User group ID, if zero , then user_id or account_id != 0
### Example Response:
```
{
	"account_id": 36,
	"already_discounted": 0.0,
	"amount": 8.0,
	"burn_date": 1670095440,
  "human_burn_date": "Thu Jan  1 03:00:00 1970",
	"first_date": 1668712814,
  "human_first_date": "Thu Jan  1 03:00:00 1970",
	"last_date": 1668713068,
  "human_last_date": "Thu Jan  1 03:00:00 1970",
	"login": "34"
}
```
---

## Endpoint: Reports - Get report of custom services
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/custom_services`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
### Example Response:
```
{
      "account_id": 1,
      "amount": 0.0,
      "amount_with_tax": 0.0,
      "date": 0,
      "human_date":"Thu Jan  1 03:00:00 1970",
      "login": "4951",
      "mark": "yohoo",
      "revoked": true,
      "service_key": "servKEY",
      "service_name": "servName"
    }
```
---

## Endpoint: Reports - Get report of dhcp leases
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/dhcp_leases`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end]
### Example Response:
```
{
    "expired": 1570270250,
    "ip": "192.168.0.2",
    "mac": "02:42:af:11:d0:ae",
    "relay_agent_info": "",
    "updated": 1570183850,
    "human_updated":"Thu Jan  1 03:00:00 1970",
    "human_expired": "Thu Jan  1 03:00:00 1970",
    "user_id": 1,
    "user_login": "zhora"
  },
  {
    "expired": 1570280696,
    "ip": "192.168.0.2",
    "mac": "02:42:af:11:d0:ae",
    "relay_agent_info": "",
    "updated": 1570194296,
    "human_updated":"Thu Jan  1 03:00:00 1970",
    "human_expired": "Thu Jan  1 03:00:00 1970",
    "user_id": 1,
    "user_login": "zhora"
  }
```
---

## Endpoint: Reports - Get report of funds flows
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/funds_flows`
- **Ready:** `false`
### Parameters:
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
### Example Response:
```
{
	"account_id_from": 0,
	"account_id_to": 0,
	"amount": 0.0,
	"date": 0,
 "human_date": "Thu Jan  1 03:00:00 1970",
	"full_name": "unknown",
	"login": "unknown",
	"user_id": 0
}
```
---

## Endpoint: Reports - Get report of invoices doc list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/invoices_doc_list`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** accounts from group
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `type`
    - **Type:** `Number`
    - **Description:** type of documents
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `limit`
    - **Type:** `Number`
    - **Description:** list limit
  - **Name:** `download`
    - **Type:** `Number`
    - **Description:** download doc or list it
### Example Response:
```
{
	"account_id": 1,
	"alt_id": "1",
	"entries": [{
		"accounting_period_id": 3,
		"agg_service_type": 2,
		"base": 12.0,
		"invoice_id": 1,
		"name": "period",
		"qnt": 1.0,
		"service_type": 2,
		"slink_id": 5,
		"sum": 12.0,
		"tax": 0.0
	}],
	"expire_date": 0,
	"human_expire_date": "Thu Jan  1 03:00:00 1970",
	"ext_num": "",
	"full_name": "testFull name",
	"id": 1,
	"invoice_date": 1666025175,
	"human_invoice_date": "Thu Jan  1 03:00:00 1970",
	"is_odt_mailed": 0,
	"is_payed": 0,
	"is_pdf_mailed": 0,
	"is_printed": 0,
	"kpp": "",
	"odt_created": 0,
	"odt_modified": 0,
	"odt_status": -1,
	"payment_transaction_id": 0,
	"pdf_created": 0,
	"pdf_modified": 0,
	"pdf_status": -1,
	"tax": "",
	"total_sum": 12.0,
	"total_sum_with_tax": 12.0,
	"total_tax": 0.0,
	"uid": 1
}
```
---

## Endpoint: Reports - Get report of other charges
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/other_charges`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end]
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** User group ID, if zero , then user_id or account_id != 0
### Example Response:
```
{
	"account_id": 34,
	"charge": 33.0,
	"charge_with_tax": 33.0,
	"date": 1668823182,
 "human_date" : "Thu Jan  1 03:00:00 1970",
	"full_name": "",
	"login": "4",
	"service_type": 18
}, {
	"account_id": 36,
	"charge": 2.0,
	"charge_with_tax": 2.0,
	"date": 1668712305,
 "human_date" : "Thu Jan  1 03:00:00 1970",
	"full_name": "",
	"login": "34",
	"service_type": 18
}, {
	"account_id": 36,
	"charge": 2.0,
	"charge_with_tax": 2.0,
	"date": 1668712205,
 "human_date" : "Thu Jan  1 03:00:00 1970",
	"full_name": "",
	"login": "34",
	"service_type": 18
}
```
---

## Endpoint: Reports - Get report of sessions
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/sessions`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end]
### Example Response:
```
{
	"account_id": 0,
	"acct_inp_giga": 0,
	"acct_inp_oct": 0,
	"acct_inp_pack": 0,
	"acct_out_giga": 0,
	"acct_out_oct": 0,
	"acct_out_pack": 0,
	"acct_sess_time": 0,
	"acct_session_id": "",
	"acct_status_type": 0,
	"acct_term_cause": 0,
	"active_session_bool": false,
	"called_station_id": "",
	"calling_station_id": "",
	"flags": 0,
	"framed_ip": "0.0.0.0",
	"framed_ip6": "0.0.0.0",
	"framed_protocol": 0,
	"id": 0,
	"last_update_date": 0,
 "human_last_update_date" : "Thu Jan  1 03:00:00 1970",
	"nas_id": "",
	"nas_ip": "0.0.0.0",
	"nas_port": 0,
	"nas_port_type": 0,
	"recv_date": 0,
 "human_recv_date" : "Thu Jan  1 03:00:00 1970",
	"service_type": 0,
	"slink_id": 0,
	"total_cost": 0.0,
	"uname": ""
}
```
---

## Endpoint: Reports - Get report of traffic detailed
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/traffic_detailed`
- **Ready:** `false`
### Parameters:
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end] from request
  - **Name:** `stop`
    - **Type:** `Number`
    - **Description:** flag of stop request sending and deleting report
  - **Name:** `count`
    - **Type:** `Number`
    - **Description:** count of desired items in reply, be default(if zero) = 1000
### Example Response:
```
{
       "is_finish": 1,
       "traffic_stat_list": [
         {
           "account_id": 0,
           "d_addr": "172.23.0.3",
           "d_oct": 666,
           "d_pkt": 999,
           "dport": 0,
           "dst_as": 8,
           "dst_mask": 0,
           "iface": 14,
           "ip": "0.0.0.0",
           "login": "",
           "nexthop_addr": "192.168.0.1",
           "oface": 15,
           "proto": 6,
           "router_ip_netflow_from": "172.23.0.1",
           "s_addr": "127.0.0.1",
           "slink_id": 0,
           "sport": 0,
           "src_as": 192,
           "src_mask": 0,
           "tclass": 0,
           "tcp_flags": 4,
           "timestamp": 1572010245,
           "human_timestamp" :  "Thu Jan  1 03:00:00 1970",
           "tos": 14,
           "ts_first": 0,
           "ts_last": 0
         }
       ]
     }
```
---

## Endpoint: Reports - Get report of traffic
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/traffic`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end]
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** User group ID, if zero , then user_id or account_id != 0
  - **Name:** `type`
    - **Type:** `Number`
    - **Description:** type of grouping
### Example Response:
```
{
    "account_id": 123,
    "base_cost": 123.0,
    "bytes": 123,
    "charge": 123.0,
    "login": "unknown",
    "tclass": 123
  }
```
---

## Endpoint: Reports - Get report of user log
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/users_log`
- **Ready:** `false`
### Parameters:
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
  - **Name:** `action_id`
    - **Type:** `Number`
    - **Description:** action_id from enum
### Example Response:
```
{
       "action": 3,
       "comment": "4951",
       "date": 1548775240,
       "human_date": "Thu Jan  1 03:00:00 1970",
       "login": "4951",
       "staff_id": -1,
       "system_acc": "init",
       "user_id": 1,
       "what": ""
     },
     {
       "action": 13,
       "comment": "account ID 1",
       "date": 1548775240,
       "human_date": "Thu Jan  1 03:00:00 1970",
       "login": "4951",
       "staff_id": -1,
       "system_acc": "init",
       "user_id": 1,
       "what": ""
     }
```
---

## Endpoint: Reports - Get report payment orders
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/payment_orders`
- **Ready:** `false`
### Parameters:
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** Date start.
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** Date end.
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User unique ID.
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** User accout unique ID.
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** User accounting period unique ID.
### Example Response:
```
{
	"amount": 0.0,
	"created": 0,
  "human_created": "Thu Jan  1 03:00:00 1970",
	"deleted": 0,
	"extended_id": "",
	"full_name": "unknown",
	"id": 0,
	"iso_currency_code": 0,
	"login": "unknown",
	"modified": 0,
  "human_modified": "Thu Jan  1 03:00:00 1970",
	"payment_system_name": "",
	"payment_system_type": 0,
	"personal_account_id": 0,
	"state": 0,
	"transaction_id": "",
	"transaction_time": 0
}
```
---

## Endpoint: Reports - Get report payments
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/payments`
- **Ready:** `false`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User unique ID.
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** User accout unique ID.
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** User accounting period unique ID.
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** Group identifier
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** unix timestamp start
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** unix timestamp end
  - **Name:** `current_page`
    - **Type:** `Number`
    - **Description:** page number
  - **Name:** `per_page`
    - **Type:** `Number`
    - **Description:** items per page
  - **Name:** `filter`
    - **Type:** `Number`
    - **Description:** search value
  - **Name:** `sort_field`
    - **Type:** `Number`
    - **Description:** sort field value [account_id|actual_date|admin_comment|burnt_date|comment|currency_id|currency_rate|external_id ...]
  - **Name:** `is_desc`
    - **Type:** `Number`
    - **Description:** sorting order [0|1] 0 = false, 1 = true
  - **Name:** `download`
    - **Type:** `Number`
    - **Description:** download as csv [0|1] 0 = false, 1 = true
### Example Response:
```
{
	"payments": [{
		"account_id": 33,
		"actual_date": 1669223119,
		"admin_comment": "",
		"burnt_date": 0,
		"comment": "",
		"currency_id": 810,
		"currency_rate": 1.0,
		"external_id": "",
		"full_name": "",
		"hash": "",
		"id": 18,
		"login": "3",
		"method": 1,
		"method_name": "Cash payment",
		"payment": -10.0,
		"payment_enter_date": 1669223119,
      "human_actual_date" : "Thu Jan  1 03:00:00 1970",
      "human_payment_enter_date" : "Thu Jan  1 03:00:00 1970",
      "human_burnt_date": "Thu Jan  1 03:00:00 1970",
		"payment_ext_number": "",
		"payment_incurrency": -10.0,
		"user_id": -1,
		"who_recieved": "init [-1]"
	}, {
		"account_id": 34,
		"actual_date": 1668100502,
		"admin_comment": "CREDIT CLOSED",
		"burnt_date": 1669137302,
      "human_actual_date" : "Thu Jan  1 03:00:00 1970",
      "human_payment_enter_date" : "Thu Jan  1 03:00:00 1970",
      "human_burnt_date": "Thu Jan  1 03:00:00 1970",
		"comment": "",
		"currency_id": 810,
		"currency_rate": 1.0,
		"external_id": "555",
		"full_name": "",
		"hash": "",
		"id": 11,
		"login": "4",
		"method": 7,
		"method_name": "Credit",
		"payment": 100.0,
		"payment_enter_date": 1668100502,
		"payment_ext_number": "",
		"payment_incurrency": 100.0,
		"user_id": -1,
		"who_recieved": "init [-1]"
	},
	...
	],
	"summary": [{
		"account_id": "Summary by method",
		"actual_date": 0,
		"admin_comment": "",
		"burnt_date": 0,
		"comment": "",
		"currency_id": 0,
		"currency_rate": 0.0,
		"external_id": "",
		"full_name": "",
		"hash": "",
		"id": 452933168,
		"login": "",
		"method": 0,
		"method_name": "Cash payment",
		"payment": 1764.0,
		"payment_enter_date": 0,
		"payment_ext_number": "",
		"payment_incurrency": 1764.0,
		"user_id": 0,
		"who_recieved": ""
	}, {
		"account_id": "Summary by method",
		"actual_date": 0,
		"admin_comment": "",
		"burnt_date": 0,
		"comment": "",
		"currency_id": 0,
		"currency_rate": 0.0,
		"external_id": "",
		"full_name": "",
		"hash": "",
		"id": 452933168,
		"login": "",
		"method": 0,
		"method_name": "Credit",
		"payment": 100.0,
		"payment_enter_date": 0,
		"payment_ext_number": "",
		"payment_incurrency": 100.0,
		"user_id": 0,
		"who_recieved": ""
	}, {
		"account_id": "Total Summary",
		"actual_date": 0,
		"admin_comment": "",
		"burnt_date": 0,
		"comment": "",
		"currency_id": 0,
		"currency_rate": 0.0,
		"external_id": "",
		"full_name": "",
		"hash": "",
		"id": 452933168,
		"login": "",
		"method": 0,
		"method_name": "",
		"payment": 1864.0,
		"payment_enter_date": 0,
		"payment_ext_number": "",
		"payment_incurrency": 1864.0,
		"user_id": 0,
		"who_recieved": ""
	}],
	"total_rows": 18
}
```
---

## Endpoint: Reports - Get report services
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/services`
- **Ready:** `false`
### Parameters:
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** Date start.
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** Date end.
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User unique ID.
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** User accout unique ID.
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** User accounting period unique ID.
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** User group ID.
### Example Response:
```
{
     "account_id": 39,
     "accounting_period_id": 430,
     "charge": 1000.0,
     "charge_with_tax": 10002.0
     "date": 1569602916,
     "human_date": "Thu Jan  1 03:00:00 1970",
     "full_name": "",
     "login": "test",
     "service_name": "service_1000",
     "service_type": 2
   }
```
---

## Endpoint: Reports - Get report telephone directions
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/tel_directions`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end]
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** User group ID, if zero , then user_id or account_id != 0
### Example Response:
```
{
    "calls_cnt": 2,
    "cost": 2.0,
    "dir_id": 1000000,
    "dir_name": "495",
    "duration": 120,
    "nonzero_duration_calls_cnt": 2
  }
```
---

## Endpoint: Reports - Get report telephone numbers
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/tel_numbers`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** unique id, if zero ,then all related accounts
  - **Name:** `limit`
    - **Type:** `Number`
    - **Description:** number of items in response, zero for all
  - **Name:** `download`
    - **Type:** `Number`
    - **Description:** is download report ? [0,1]
### Example Response:
```
{
 "num_id" : 1,
 "slink_id" : 2,
 "login" : "login",
 "number" : "123123",
 "incoming_trunk" : "321",
 "outgoing_trunk" : "3211",
 "pbx_id" : "22",
 "password" : "pass",
 "allowed_cid" : "cid",
 "account_id": 1,
 "comment" : ""
}
```
---

## Endpoint: Reports - Get report telephony
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/telephony`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
  - **Name:** `accs_group_id`
    - **Type:** `Number`
    - **Description:** Accounts Group identifier (Non required)
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique id , if zero ,then all related accounts
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** unique id, if zero ,then all related accounts
  - **Name:** `accounting_period_id`
    - **Type:** `Number`
    - **Description:** desired accounting period, if zero ,then resp for time range [start;end]
  - **Name:** `is_by_call-`
    - **Type:** `Number`
    - **Description:** bool(1,0), if set will fetch by call date, instead of upload date
### Example Response:
```
{
     "account_id": 2,
     "acct_sess_time": 60,
     "acct_session_id": "asklnalskd",
     "acct_status_type": 2,
     "base_cost": 1.0,
     "called_station_id": "4952",
     "calling_station_id": "4951",
     "cost_mult": 1.0,
     "dir_id": 1000000,
     "duration": 60,
     "flags": 0,
     "framed_protocol": 0,
     "h323_disconnect_cause": "0 (Valid cause code not yet received)",
     "id": 1,
     "incoming_trunk": "",
     "nas_id": "",
     "nas_ip": 0,
     "nas_port": 0,
     "nas_port_type": 0,
     "outgoing_trunk": "",
     "pbx_id": "",
     "recv_date": 1548775390,
     "human_recv_date" : "Thu Jan  1 03:00:00 1970",
     "service_type": 0,
     "setup_time": 1548749471,
     "human_setup_time": "Thu Jan  1 03:00:00 1970",
     "slink_id": 2,
     "sum_cost": 1.0,
     "uname": "",
     "zone_id": 0
   }
```
---

## Endpoint: Reports - Get response from request of traffic detailed
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/reports/request_traffic_detailed`
- **Ready:** `false`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** subscriber`s account_id; if = 0 ,then all accounts
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** unique user identifier
  - **Name:** `collector_id`
    - **Type:** `Number`
    - **Description:** of netflow provider
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** start of desired period
  - **Name:** `end`
    - **Type:** `Number`
    - **Description:** end of desired period
### Example Response:
```
{
  "account_id": "all",
  "is_request_done": true
}
```
---

