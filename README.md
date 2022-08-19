# Hetzner Server Traffic Alert Bot

## Description

Get persnoal Hetzner Cloud Server's daily traffic 

## Install & Run

### Install requirements.txt

```python
pip install -r requirements.txt
```

Install requirements.txt file that includes **python-telegram-module**, **hcloud**, **schedule**

### Run main.py

```python
$HetznerTrafficAlertBot python3 main.py
```

Run main.py from Project main folder, which main.py file located.

## HOW TO USE

### Edit keys.json

```json
{
	"telegram": {
		"token": "",
		"chatID": ""
	},
	"hetzner": {
		"token": ""
	}
}
```

* "telegram" Section
  * Get bot_token from @Bot_Father and Get chatID from telegram.
* "hetzner" Section
  * Get API Token from Hetzner Cloud.

