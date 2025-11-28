# UTM5 API Section: User

This document describes the endpoints for the 'User' API section for UTM5 isp billing system by Netup Co.

## Endpoint: User - Get user data
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** Users unique ID.
  - **Name:** `login`
    - **Type:** `Number`
    - **Description:** Users unique login.
### Example Response:

HTTP/1.1 200 OK
{
  "user_id" : "1",
  "login" : "test",
  "password" : "0177c054",
  "basic_account" : "1",
  "full_name" : "",
  "email" : "",
  "contract_id" : "0",
  "advance_payment" : "0",
  "card_user" : "0",
  "slinks" : [1],
  "groups" : [1],
  "accounts" : ["1"],
  "till" : "0"
 }
```

---

## Endpoint: User - Add account to group
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/link_account_group`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Add account to group
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/link_groups_to_account`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Add card pool owner
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/card_pool_owner`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Add group to user
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/add_group_to_user`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Cancel payment
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/cancel_payment`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Change account balance
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/change_account_balance`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Create acc group
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/accounts_groups`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Create account
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/accounts`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "account_id" : "1" }
```

---

## Endpoint: User - Create account with ID ( BE CAREFUL, UNSAFE API )
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/accounts_with_id`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "account_id" : "1" }
```

---

## Endpoint: User - Create card pool
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/card_pool`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "pool_id" : 3}
```

---

## Endpoint: User - Create dealer
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/dealer`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "dealer_id" : -10}
```

---

## Endpoint: User - Create netup IPTV access card
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/access_card`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Create netup IPTV activation code
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/activation_codes`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Create service link freezed
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/freezed`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "service_link_id" : 1 }
```

---

## Endpoint: User - Create system group
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/system_groups`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "group_id" : 3}
```

---

## Endpoint: User - Create system user
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/system_users`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "sys_user_id" : -10}
```

---

## Endpoint: User - Create user contracts
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/contracts`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "contract_id" : "1" }
```

---

## Endpoint: User - Create user group
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/groups`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Create user tech param
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/tech_params`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Create user
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "user_id" : 1,
  "account_id" : 1 }
```

---

## Endpoint: User - Create user with ID ( BE CAREFUL, UNSAFE API )
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/users_with_id`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "user_id" : "1",
  "account_id" : "1" }
```

---

## Endpoint: User - Delete access card
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/access_card`
### Parameters:
  - **Name:** `card_id`
    - **Type:** `Number`
    - **Description:** card identifier
  - **Name:** `card_number`
    - **Type:** `Number`
    - **Description:** iptv card number
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete account
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/accounts`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** Account id.
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete accounts groups
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/accounts_groups`
### Parameters:
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** Group id.
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete accs from group
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/unlink_accounts_group`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete card owner from pool
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/card_pool_owner`
### Parameters:
  - **Name:** `pool_id`
    - **Type:** `Number`
    - **Description:** pool identifier
  - **Name:** `owner_id`
    - **Type:** `Number`
    - **Description:** owner identifier
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete contracts
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/contracts`
### Parameters:
  - **Name:** `contract_id`
    - **Type:** `Number`
    - **Description:** Contract id.
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete recurrent payments
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/recurrent_payments`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User identifier
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete service links
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/servicelinks`
### Parameters:
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link unique ID
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete system user
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/system_users`
### Parameters:
  - **Name:** `sys_user_id`
    - **Type:** `Number`
    - **Description:** System User identifier.
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete tariff link
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/tarifflinks`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User id.
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** Account id.
  - **Name:** `tplink_id`
    - **Type:** `Number`
    - **Description:** Tariff link id.
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete tech param
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/tech_params`
### Parameters:
  - **Name:** `tech_param_id`
    - **Type:** `Number`
    - **Description:** Tech param id.
  - **Name:** `slink_id`
    - **Type:** `Number`
    - **Description:** Service link id.
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete user block
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/blocks`
### Parameters:
  - **Name:** `block_id`
    - **Type:** `Number`
    - **Description:** block identifier
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete user from group
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/user_from_group`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** user identifier
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** group identifier
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete user from group
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/remove_user_from_group`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** user identifier
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** group id
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete user groups
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users/groups`
### Parameters:
  - **Name:** `group_id`
    - **Type:** `Number`
    - **Description:** Group id.
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Delete user
### Details:
- **Method:** `DELETE`
- **URL:** `{{api_url}}api/users`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User id.
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Deleted users search
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/deleted_search`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
  "user_id" : "1",
  "login" : "test",
  "password" : "0177c054",
  "basic_account" : "1",
  "full_name" : "",
  "email" : "",
  "card_user": 0,
  "accounts":[]
 }
]
```

---

## Endpoint: User - Download contract
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/contracts/download`
### Parameters:
  - **Name:** `contract_id`
    - **Type:** `Number`
    - **Description:** Contract ID.
  - **Name:** `is_conv`
    - **Type:** `Number`
    - **Description:** Is conversion
### Example Response: Not available

---

## Endpoint: User - Execute freezed link
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/servicelinks/execute_freezed`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result": "ok" }
```

---

## Endpoint: User - Extended search users
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/extended_search`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
  "user_id" : "1",
  "login" : "test",
  "password" : "0177c054",
  "basic_account" : "1",
  "full_name" : "",
  "email" : "",
  "contract_id" : "0",
  "advance_payment" : "0",
  "card_user" : "0",
  "slinks" : [1],
  "groups" : [1],
  "accounts" : [1],
  "till" : "0"
 }
]
```

---

## Endpoint: User - Get account group
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/accounts_group`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK

 {
     "group_id": "1",
     "group_name": "Users",
     "accounts": [1,2]
 }
```

---

## Endpoint: User - Get accounts all groups
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/accounts_all_groups`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
     "group_id": "1",
     "group_name": "Users"
 }
]
```

---

## Endpoint: User - Get accounts group info
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/accounts_group_info`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "group_name": "Guests",
  "grups_users": [
         "user_id": 2,
         "login" : "login",
         "account_id": 2
     ]
}
```

---

## Endpoint: User - Get accounts groups by aid
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/accounts_groups_by_aid`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** Acc unique ID.
### Example Response:

HTTP/1.1 200 OK
[
 {
     "group_id": "1",
     "group_name": "Users"
 }
]
```

---

## Endpoint: User - Get accounts groups
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/accounts_groups`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
     "group_id": "1",
     "group_name": "Users"
 }
]
```

---

## Endpoint: User - Get accounts
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/accounts`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** Users unique ID(Not required).
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** User account unique ID(Not required).
  - **Name:** `external_id`
    - **Type:** `String`
    - **Description:** User external ID(Not required).
### Example Response:

HTTP/1.1 200 OK
[{
	"access_card_number": 0,
	"access_card_timeout": 0,
	"account_id": 40,
	"active_block_id": 0,
	"balance": 0.0,
	"block_info_ids": [50],
	"block_type": "0",
	"blocks_info": [{
		"account_id": 40,
		"block_type": 2,
		"expire_date": 1672488000,
		"flags": 0,
		"id": 50,
		"is_deleted": false,
		"is_planning": false,
		"start_date": 1671794100
	}],
	"contract_close_date": 0,
	"contract_number": "",
	"credit": 0.0,
	"credit_info_ids": [],
	"external_id": "",
	"flags": 0,
	"freezed_balance": 0.0,
	"int_status": 0,
	"irdeto_access_card_number": "0",
	"irdeto_stb_serial_number": "0",
	"login": "carmen",
	"ptimed_info_ids": [],
	"sale_tax_rate": 0.0,
	"signature_date": 0,
	"slinks": [],
	"tariffs": [],
	"unlimited": false,
	"user_id": 31,
	"vat_rate": 0.0
}]
```

---

## Endpoint: User - Get accounts
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/list_accounts`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
{
  "user_id" : "1",
  "login" : "test",
  "account_id" :1
 }
]
```

---

## Endpoint: User - Get admin info
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/who_am_i`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "ip4": "0.0.0.0",
  "ip6": "::",
  "is_dealer": false,
  "login": "init",
  "mask4": 0,
  "mask6": 0,
  "password": "init",
  "sys_groups": [
    1
  ],
  "token": "init",
  "user_id": -1
}
```

---

## Endpoint: User - Get all user bonuses
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/all_bonuses`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
    {
      "id" : 1,
      "user_id" : 1,
      "amount" : 100.0,
      "burn_time" : 1625753527,
      "charged" : 50.0,
      "type" : 0
     },
...
]
```

---

## Endpoint: User - Get all users data
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/all_users`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
	{
		"accounts": [
			39
		],
		"advance_payment": false,
		"balance": 123.0,
		"basic_account": 39,
		"card_user": 0,
		"contract_id": 0,
		"email": "",
		"full_name": "",
		"groups": [],
		"is_active_block": true,
		"login": "1",
		"password": "zEmZdNV9o3",
		"slinks": [],
		"telephones": "",
		"till": 0,
		"user_id": 30
	}
]
```

---

## Endpoint: User - Get allowed fids
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/fids`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
 [
  {
      "fid_id": 1,
      "fid_name": "name",
      "fid_module" : "mod"
  }
]
```

---

## Endpoint: User - Get blocks info
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/blocks_info`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
{
	"access_card_number": 0,
	"access_card_timeout": 0,
	"account_id": 1,
	"active_block_id": 0,
	"balance": 13.0,
	"block_end": null,
	"block_info_ids": [3, 4],
	"block_start": null,
	"block_type": "0",
	"blocks_info": [{
		"account_id": 1,
		"block_type": 2,
		"expire_date": 1677607313,
		"flags": 0,
		"id": 3,
		"is_deleted": false,
		"is_planning": false,
		"start_date": 1677088913
	}, {
		"account_id": 1,
		"block_type": 2,
		"expire_date": 1679079319,
		"flags": 0,
		"id": 4,
		"is_deleted": false,
		"is_planning": false,
		"start_date": 1677696919
	}],
	"contract_close_date": 0,
	"contract_number": "",
	"credit": 0.0,
	"credit_info_ids": [],
	"external_id": "",
	"flags": 0,
	"freezed_balance": 0.0,
	"int_status": 0,
	"irdeto_access_card_number": "0",
	"irdeto_stb_serial_number": "0",
	"ptimed_info_ids": [],
	"sale_tax_rate": 0.0,
	"signature_date": 0,
	"slinks": [17],
	"tariffs": [4],
	"unlimited": false,
	"user_id": 1,
	"vat_rate": 0.0
}
]
```

---

## Endpoint: User - Get card pool info
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/card_pool`
### Parameters:
  - **Name:** `pool_id`
    - **Type:** `Number`
    - **Description:** Card pool identifier
### Example Response:

HTTP/1.1 200 OK
{
  "info": [
    {
      "balance": 3.0,
      "card_id": 1,
      "currency": 810,
      "days": 0,
      "expire": 1591909200,
      "is_blocked": 1,
      "is_used": 0,
      "pool_id": 2,
      "secret": "02949035",
      "tp_id": 0
    },
    {
      "balance": 3.0,
      "card_id": 100,
      "currency": 810,
      "days": 0,
      "expire": 1591909200,
      "is_blocked": 0,
      "is_used": 0,
      "pool_id": 2,
      "secret": "21658866",
      "tp_id": 0
    }
  ],
  "owners": [
    -5,
    -3
  ]
}
```

---

## Endpoint: User - Get card pools list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/card_pools`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "cards": 0,
    "cards_used": 0,
    "first_update": 0,
    "last_update": 0,
    "pool_id": 1
  },
  {
    "cards": 100,
    "cards_used": 0,
    "first_update": 1576152886,
    "last_update": 1576152887,
    "pool_id": 2
  }
]
```

---

## Endpoint: User - Get contracts
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/contracts`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** Users unique login.
### Example Response:

HTTP/1.1 200 OK
 [
  {
                "contract_id" : "1",
                "template_id" : "1",
                "created" : "",
                "name" : "",
                "path" : ""
         }
 ]
```

---

## Endpoint: User - Get dealer info
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/dealer`
### Parameters:
  - **Name:** `dealer_id`
    - **Type:** `Number`
    - **Description:** Dealer unique identifier (negative value)
### Example Response:

HTTP/1.1 200 OK

{
  "dealer": {
    "act_address": "zhopinsk",
    "change_date": 1575908100,
    "comments": "commen",
    "create_date": 1575907043,
    "dealer_id": -13,
    "email": "deal@mail.com",
    "full_name": "Deallllll",
    "home_tel": "+14",
    "icq_number": "66613",
    "mob_tel": "2222222222",
    "passport": "4511166",
    "web_page": "satan.com",
    "who_change": 0,
    "who_create": -1,
    "work_tel": "+666"
  },
  "system_account": {
    "groups": [
      {
        "group_id": 9999,
        "group_name": "Dealer"
      }
    ],
    "ip4": "1.2.3.4",
    "ip6": "::0.1.0.0",
    "is_dealer": true,
    "login": "editeddeeeeeal22",
    "mask4": "255.255.254.0",
    "mask6": "ffff:ffff:ffff:ffff:8000::",
    "password": "pass",
    "sys_groups": [
      9999
    ],
    "user_id": -13
  }
}
```

---

## Endpoint: User - Get dealer privileges
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/dealer_privileges`
### Parameters:
  - **Name:** `dealer_id`
    - **Type:** `Number`
    - **Description:** Dealer unique identifier (negative value)
  - **Name:** `entity_type`
    - **Type:** `Number`
    - **Description:** Privilege param (one of enum {acl_user,acl_house,acl_service,acl_tariff,acl_discount_period})
### Example Response:

HTTP/1.1 200 OK

[0,1]
```

---

## Endpoint: User - Get dealers list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/dealers`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK

[
  {
    "ip4": "1.2.3.4",
    "ip6": "::0.1.0.0",
    "is_dealer": true,
    "login": "editeddeeeeeal22",
    "mask4": "255.255.254.0",
    "mask6": "ffff:ffff:ffff:ffff:8000::",
    "password": "pass",
    "sys_groups": [
      9999
    ],
    "token": "",
    "user_id": -13
  },
  {
    "ip4": "1.2.3.4",
    "ip6": "::0.1.0.0",
    "is_dealer": true,
    "login": "deeeeeal",
    "mask4": "255.255.254.0",
    "mask6": "ffff:ffff:ffff:ffff:8000::",
    "password": "pass",
    "sys_groups": [
      9999
    ],
    "token": "",
    "user_id": -12
  }
]
```

---

## Endpoint: User - Get documents
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/documents`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** Users unique ID.
  - **Name:** `doc_type`
    - **Type:** `Number`
    - **Description:** 
  - **Name:** `base_id`
    - **Type:** `Number`
    - **Description:** 
  - **Name:** `file_type`
    - **Type:** `Number`
    - **Description:** 
### Example Response: Not available

---

## Endpoint: User - Get group info
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/group_info`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "group_name": "Guests",
  "grups_users": [
         "user_id": 2,
         "login" : "login"
     ]
}
```

---

## Endpoint: User - Get groups for user
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/recurrent_payments`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
    {
      "id" :  1,
      "customer_id" :  1,
      "account_id" :  1,
      "amount" :  100.0,
      "charge_policy" :  2,
      "charge_day" :  1,
      "next_charge_date" :  1,
      "charge_min_balance" :  100.0,
      "payment_system_type" :  13,
      "payment_system_name" : "Tinkoff",
      "service_key" : "",
      "service_client_id" : ""
    }
]
```

---

## Endpoint: User - Get invoices
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/invoices`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** Users unique ID.
  - **Name:** `login`
    - **Type:** `Number`
    - **Description:** Users unique login.
### Example Response:

HTTP/1.1 200 OK
 [
 {
     "account_id" : "",
     "date" : "",
     "invoice_id" : "",
     "invoice_external_number" : "",
     "system_currency_sum" : "",
     "binded_currency_sum" : "",
     "total" : ""
 }
 ]
```

---

## Endpoint: User - Get ip groups by user_id OR account_id
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/ip_groups_specific`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User identifier
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** Account identifier
### Example Response:

HTTP/1.1 200 OK
[
  {
    "account_id": 2,
    "allowed_cid": "",
    "dhcp_options": [],
    "flags": 0,
    "id": 18,
    "ip": "46.43.206.84",
    "ip_family": 4,
    "ipgroup_id": 1,
    "isg_attrs": [],
    "login": "46.43.206.84",
    "mac": "",
    "mask": 32,
    "nfprovider_id": 0,
    "password": "8e7a547e",
    "pool_id": 0,
    "pool_name": "",
    "port_id": 0,
    "slink_id": 2,
    "switch_id": 0,
    "user_id": 2,
    "vlan_id": 0
  },
  {
    "account_id": 2,
    "allowed_cid": "",
    "dhcp_options": [],
    "flags": 0,
    "id": 22,
    "ip": "11.22.33.33",
    "ip_family": 4,
    "ipgroup_id": 1,
    "isg_attrs": [],
    "login": "qerqwer",
    "mac": "",
    "mask": 32,
    "nfprovider_id": 0,
    "password": "qerqewr",
    "pool_id": 0,
    "pool_name": "",
    "port_id": 0,
    "slink_id": 2,
    "switch_id": 0,
    "user_id": 2,
    "vlan_id": 0
  }
]
```

---

## Endpoint: User - Get ip groups
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/ip_groups`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
  {
    "account_id": 0,
    "ipgroup_id": 1,
    "items": [
      {
        "allowed_cid": "",
        "dhcp_options": [],
        "flags": 0,
        "id": 6,
        "ip": "0.0.0.0",
        "ip_family": 4,
        "isg_attrs": [],
        "login": "",
        "mac": "02:42:af:11:d0:ae",
        "mask": 0,
        "nfprovider_id": 0,
        "password": "",
        "pool_id": 1,
        "pool_name": "",
        "port_id": 0,
        "switch_id": 0,
        "vlan_id": 0
      },
      {
        "allowed_cid": "",
        "dhcp_options": [],
        "flags": 4,
        "id": 8,
        "ip": "192.168.0.2",
        "ip_family": 4,
        "isg_attrs": [],
        "login": "",
        "mac": "",
        "mask": 32,
        "nfprovider_id": 0,
        "password": "",
        "pool_id": 0,
        "pool_name": "",
        "port_id": 0,
        "switch_id": 0,
        "vlan_id": 0
      }
    ],
    "slink_id": 1
  }
]
```

---

## Endpoint: User - Get irdeto activate result
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/irdeto/activate`
### Parameters:
  - **Name:** `card_number`
    - **Type:** `string`
    - **Description:** Irdeto card number
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok";
}
```

---

## Endpoint: User - Get irdeto deactivate result
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/irdeto/deactivate`
### Parameters:
  - **Name:** `card_number`
    - **Type:** `string`
    - **Description:** Irdeto card number
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok";
}
```

---

## Endpoint: User - Get irdeto pair chipset result
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/irdeto/pair_chipset`
### Parameters:
  - **Name:** `card_number`
    - **Type:** `string`
    - **Description:** Irdeto card number
  - **Name:** `stb_number`
    - **Type:** `string`
    - **Description:** Irdeto card number
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok";
}
```

---

## Endpoint: User - Get irdeto unpair all chipsets result
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/irdeto/unpair_all_chipsets`
### Parameters:
  - **Name:** `card_number`
    - **Type:** `string`
    - **Description:** Irdeto card number
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok";
}
```

---

## Endpoint: User - Get map of users for dealer
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/dealer_user_map`
### Parameters:
  - **Name:** `start`
    - **Type:** `Number`
    - **Description:** User id start from range
  - **Name:** `offset`
    - **Type:** `Number`
    - **Description:** Get next users by id from start (<1000)
### Example Response:

HTTP/1.1 200 OK

[
  {
    "accounts": [
      3
    ],
    "advance_payment": false,
    "basic_account": 3,
    "card_user": 0,
    "contract_id": 0,
    "dealer_id": 0,
    "email": "ttttttes_root@ya.ru",
    "full_name": "",
    "groups": [],
    "login": "root",
    "password": "2a97af7c",
    "slinks": [
      3,
      5
    ],
    "till": 0,
    "user_id": 3
  },
  {
    "accounts": [
      4,
      5
    ],
    "advance_payment": false,
    "basic_account": 4,
    "card_user": 0,
    "contract_id": 0,
    "dealer_id": 0,
    "email": "userovich@user.ru",
    "full_name": "Userman",
    "groups": [],
    "login": "new_uvser",
    "password": "3e439507",
    "slinks": [
      6,
      7,
      8
    ],
    "till": 0,
    "user_id": 4
  }
]
```

---

## Endpoint: User - Get new secret password
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/new_secret`
### Parameters:
  - **Name:** `size`
    - **Type:** `Number`
    - **Description:** size of generated password in symbols.
### Example Response:

HTTP/1.1 200 OK

{
  "error": "",
  "secret": "ad50158d05"
}
```

---

## Endpoint: User - Get overwrite parental pin code result
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/irdeto/overwrite_parental_pin_code`
### Parameters:
  - **Name:** `card_number`
    - **Type:** `string`
    - **Description:** Irdeto card number
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok";
}
```

---

## Endpoint: User - Get synchronize result
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/irdeto/overwrite_synchronize`
### Parameters:
  - **Name:** `card_number`
    - **Type:** `string`
    - **Description:** Irdeto card number
### Example Response:

HTTP/1.1 200 OK
{
  "result": "ok";
}
```

---

## Endpoint: User - Get system group
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/system_group`
### Parameters:
  - **Name:** `sys_group_id`
    - **Type:** `string`
    - **Description:** System group id
### Example Response:

HTTP/1.1 200 OK
{
  "group_name": "name",
  "group_info": "info",
  "fids": [
  {
      "fid_id": 1,
      "fid_name": "name",
      "fid_module" : "mod",
      "is_allowed": false
  }
]
}
```

---

## Endpoint: User - Get system groups
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/system_groups`
### Parameters:
  - **Name:** `schedule_link_id`
    - **Type:** `Number`
    - **Description:** Schedule link id.
### Example Response:

HTTP/1.1 200 OK
{
  "group_id" : 1,
  "group_name" : "Wheel",
  "group_info" : "",
  "users" : [-1],
  "fids" : [1,2]
 }
```

---

## Endpoint: User - Get system users short data
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/systemusersshort`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{
  "user_id" : "1",
  "login" : "test"
 }
```

---

## Endpoint: User - Get system users
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/system_users`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
          {
            "ip4": "0.0.0.0",
            "ip6": "::",
            "is_dealer": false,
            "login": "init",
            "mask4": 0,
            "mask6": 0,
            "password": "init",
            "sys_groups": [
              1
            ],
            "user_id": -1
          }
        ]
```

---

## Endpoint: User - Get tel numbers
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/tel_numbers`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
{
	"num_id" : 1,
	"slink_id" : 2,
	"login" : "login",
	"number" : "123123",
	"incoming_trunk" : "321",
	"outgoing_trunk" : "3211",
	"pbx_id" : "22",
	"password" : "pass",
	"allowed_cid" : "cid"
}
]
```

---

## Endpoint: User - Get user activation codes
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/activation_codes`
### Parameters:
  - **Name:** `account_id`
    - **Type:** `Number`
    - **Description:** Account id.
### Example Response:

HTTP/1.1 200 OK

[
         {
           "access_card_number": 1,
           "created": 1571051245,
           "deleted": 0,
           "modified": 1571126299,
           "part_1": 51094,
           "part_2": 57273,
           "part_3": 14510,
           "part_4": 93751,
           "part_5": 89638,
           "part_6": 25588,
           "state": 32768055
         }
       ]
```

---

## Endpoint: User - Get user contacts
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/contacts`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** Users unique id.
### Example Response:

HTTP/1.1 200 OK
 [
  {
                "id" : "1",
                "uid" : "1",
                "person" : "",
                "person_short" : "",
                "descr" : "",
                "reason" : "",
                "contact" : "",
                "email" : "",
                "id_exec_man" : ""
         }
 ]
```

---

## Endpoint: User - Get user full info
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/full_info`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** Users unique ID.
### Example Response:

HTTP/1.1 200 OK
{
  "accounts": [
    2
  ],
  "actual_address": "",
  "registry_address":"",
  "additional_params": [],
  "mobile_telephone_second":""
  "advance_payment": false,
  "bank_account": "",
  "bank_id": 0,
  "bank_name": "mkb",
  "basic_account": 2,
  "binded_currency_id": 810,
  "building": "",
  "card_user": 0,
  "comments": "",
  "connect_date": 1643259600,
  "contract_id": 0,
  "create_date": 1643269223,
  "district": "",
  "doc_profile_id": 1,
  "email": "",
  "entrance": "",
  "flat_number": "",
  "floor": "",
  "full_name": "",
  "groups": [
    1
  ],
  "home_telephone": "",
  "house_id": 1,
  "icq_number": "",
  "is_juridical": false,
  "is_send_invoice": false,
  "juridical_address": "",
  "kpp_number": "",
  "last_change_date": 1646909224,
  "login": "testweb",
  "mobile_telephone": "",
  "passport": "",
  "password": "aX7ufI25lk",
  "personal_manager": "",
  "port_number": 0,
  "router_id": 0,
  "slinks": [
    2,
    3,
    4,
    5,
    19
  ],
  "tax_number": "",
  "till": 0,
  "user_id": 2,
  "web_page": "",
  "who_change": -1,
  "who_create": -1,
  "work_telephone": ""
}
```

---

## Endpoint: User - Get user groups
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/groups`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
     "group_id": "1",
     "group_name": "Users"
 }
]
```

---

## Endpoint: User - Get groups for user
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/get_groups_for_user`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `number`
    - **Description:** User ID
### Example Response:

HTTP/1.1 200 OK
[
    {
      "group_id" :  111
      "group_name" : "users"
    }
]
```

---

## Endpoint: User - Get user tech params
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/tech_params`
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
           "id": 1,
           "param": "asd",
           "passwd": "123",
           "reg_date": 1571150222,
           "service_name": "iptv ORT",
           "slink_id": 6,
           "type_id": 1,
           "type_name": "web"
         },
         {
           "id": 2,
           "param": "123123",
           "passwd": "213",
           "reg_date": 1571151340,
           "service_name": "iptv ORT",
           "slink_id": 6,
           "type_id": 1,
           "type_name": "web"
         }
       ]
```

---

## Endpoint: User - Get user total bonus
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/total_bonus`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK

{
  "total" : 500.5
}
```

---

## Endpoint: User - Get user unused prepaid traffic
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/unused_prepaid`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `number`
    - **Description:** User ID
### Example Response:

HTTP/1.1 200 OK

{
  "bytes_in_mbyte" : 1048576,
  "units" : [
     {"tclass_id" : 1,
     "prepaid" : 1024}
  ]
}
```

---

## Endpoint: User - Get users access cards
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/access_cards`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `number`
    - **Description:** User ID
### Example Response:

HTTP/1.1 200 OK
{
  [
     "id": 1,
     "user_id": 1,
     "card_number": 1,
     "username": "user",
     "password": "pass"
  ]
}
```

---

## Endpoint: User - Get users count
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/users_count`
### Parameters:
  - **Name:** `is_card`
    - **Type:** `number`
    - **Description:** 1 = true or 0 = false
### Example Response:

HTTP/1.1 200 OK
{
  "count": 498
}
```

---

## Endpoint: User - Get users in group
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/group_users`
### Parameters:
  - **Name:** `group_id`
    - **Type:** `number`
    - **Description:** Group ID
### Example Response:

HTTP/1.1 200 OK
```

---

## Endpoint: User - Get users list
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/users_list`
### Parameters:
  - **Name:** `from`
    - **Type:** `number`
    - **Description:** from what num return list
  - **Name:** `to`
    - **Type:** `number`
    - **Description:** to what num return list
  - **Name:** `is_card`
    - **Type:** `number`
    - **Description:** 1 = true or 0 = false
### Example Response:

HTTP/1.1 200 OK
{
 "count": 1,
 "users": [
   {
     "balance": 0.0,
     "basic_account": 590,
     "block_type_to_flags": 0,
     "full_name": "",
     "ip_adr": [],
     "login": "card_222tyr",
     "user_id": 590,
     "user_int_status": 0
   }
 ]
}
```

---

## Endpoint: User - Get web settings
### Details:
- **Method:** `GET`
- **URL:** `{{api_url}}api/users/web_settings`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
    {
      "user_id" : "1",
      "login" : "test",
      "password" : "0177c054",
      "basic_account" : "1",
      "full_name" : "",
      "email" : "",
      "contract_id" : "0",
      "advance_payment" : "0",
      "card_user" : "0",
      "slinks" : [1],
      "groups" : [1],
      "accounts" : ["1"],
      "till" : "0"
     },
...
]
```

---

## Endpoint: User - Move all expired cards
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/clear_expired_card`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Post user contacts
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/contacts`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** Search value
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Restore user
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/restore_user`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Search accounts
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/accounts/search`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
     "account_id" : "1",
     "user_id" : "1",
     "balance" : "800",
     "credit" : "0",
     "vat_rate" : "0",
     "sale_tax_rate" : "0",
     "int_status" : "1",
     "unlimited" : "0",
     "active_block_id" : "0",
     "flags" : "0",
     "block_start": 1677430543,
     "block_end": 1677430543,
     "access_card_number" : "0",
     "access_card_timeout" : "0",
     "irdeto_access_card_number" : "",
     "irdeto_stb_serial_number" : "",
     "external_id" : "",
     "slinks" : [],
     "tariffs" : [],
     "ptimed_info_ids" : [],
     "credit_info_ids" : [],
     "block_info_ids" : [],
     "block_type": 1,
     "username" : "User"
 }
]
```

---

## Endpoint: User - Search users
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/search`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
  "user_id" : "1",
  "login" : "test",
  "password" : "0177c054",
  "basic_account" : "1",
  "full_name" : "",
  "email" : "",
  "contract_id" : "0",
  "advance_payment" : "0",
  "card_user" : "0",
  "slinks" : [1],
  "groups" : [1],
  "accounts" : [1],
  "till" : "0"
 }
]
```

---

## Endpoint: User - Set user 1c status
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/set_1c_status`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Short search users
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/short_search`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
[
 {
  "user_id" : "1",
  "login" : "test",
  "password" : "0177c054",
  "basic_account" : "1",
  "full_name" : "",
  "email" : "",
  "card_user": 0,
  "accounts":[]
 }
]
```

---

## Endpoint: User - Transfer service links between accounts
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/servicelinks/transfer`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "service_link_id" : 1 }
```

---

## Endpoint: User - Update account
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/accounts`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Update accounts group
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/accounts_group`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Update card user info (block card)
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/block_card`
### Parameters:
  - **Name:** `card_id`
    - **Type:** `Number`
    - **Description:** card unique ID.
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Update card userinfo (unblock card)
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/unblock_card`
### Parameters:
  - **Name:** `card_id`
    - **Type:** `Number`
    - **Description:** card unique ID.
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Update dealer
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/dealer`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Update group
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/group`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Update groups operations
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/groups_op`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Update privilege to dealer
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/grant_priv_to_dealer`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Update service link freezed
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/servicelinks/freezed`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result": "ok" }
```

---

## Endpoint: User - Update system groups
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/system_groups`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Update system user
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/system_users`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok"}
```

---

## Endpoint: User - Update user lifestream_id
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/lifestream_id`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** User unique ID.
  - **Name:** `lifestream_id`
    - **Type:** `String`
    - **Description:** New lifestream_id.
### Example Response:

HTTP/1.1 200 OK
{ "result" : "ok" }
```

---

## Endpoint: User - Update user tech params
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users/tech_params`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "service_id" : "1"}
```

---

## Endpoint: User - Update user
### Details:
- **Method:** `PUT`
- **URL:** `{{api_url}}api/users`
### Parameters: None
### Example Response:

HTTP/1.1 200 OK
{ "user_id" : "1"}
```

---

## Endpoint: User - Upload user contract
### Details:
- **Method:** `POST`
- **URL:** `{{api_url}}api/users/contracts/upload`
### Parameters:
  - **Name:** `user_id`
    - **Type:** `Number`
    - **Description:** Search value
  - **Name:** `name`
    - **Type:** `String`
    - **Description:** Search value
  - **Name:** `file`
    - **Type:** `object`
    - **Description:** ODT file in request body
### Example Response:

HTTP/1.1 200 OK
{ "contract_id" : "1" }
```

---

