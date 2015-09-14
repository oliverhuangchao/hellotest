import collections
rule_actions = {"alert_email":{"label":"Email", "alert_email_address":"Address", "alert_email_protocol":{"smtp":"SMTP", "pop":"POP", "imap":"IMAP"}},"alert_case":{"label":"Case"}}
res = {}
for key, value in rule_actions["alert_email"].items():
	res[key] = value

print res


# b = (("name", "Name"), ("index", "Index"), ("filter", "Filter"), ("timeframe", "Timeframe"),
#                        ("num_events", "Number events"), ("timestamp_field", "Timestamp field"),
#                        ("type", "Type"), ("action", "Action"))

# c = collections.OrderedDict(b)
# for key, value in c.items():
# 	print value