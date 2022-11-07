import datetime
unix=int(input("Enter unix timestamp :"))
print(datetime.datetime.fromtimestamp(unix)
	.strftime('%Y-%m-%d %H:%M:%S'))
