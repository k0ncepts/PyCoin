#!/usr/bin/env python3.6

#PyBtc - Texts you based on btc price to keep an eye of when to buy or sell
import config
from twilio.rest import Client as twilio_Client
from coinbase.wallet.client import Client


def coinBase():
	client = Client(config.coinbase_auth, config.coinbase_api, api_version='2017-12-03')

	currency_code = 'USD'  # can also use EUR, CAD, etc.

	# Make the request
	price = client.get_spot_price(currency=currency_code)
	if float(price.amount) <= 10000:
		return('Current bitcoin price in %s: %s - You should buy now' % (currency_code, price.amount))
	else:
		return('Current bitcoin price in %s: %s' % (currency_code, price.amount))


def twilio():

	client = twilio_Client(config.account_sid, config.auth_token)
	message = client.messages.create(to=config.my_num, from_=config.twilio_num, body=coinBase())
	return message

#print(coinBase())
print(twilio())