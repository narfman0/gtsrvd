# TODO make paramiko ssh server
# TODO upon receiving ssh connection, mount remote forward. optional: grab subdomain by username
# TODO upon receiving ssh connection, get updated zone lists by name: https://boto3.readthedocs.io/en/latest/reference/services/route53.html#Route53.Client.list_hosted_zones_by_name
# TODO create new record set https://boto3.readthedocs.io/en/latest/reference/services/route53.html#Route53.Client.change_resource_record_sets resolving to this ip
# TODO use nginx/whatever to proxy connections to mounted port (generated)
# TODO upon shutdown, remove record set
