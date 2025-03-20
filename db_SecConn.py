db_config = DbConfig(
    params={
        'secret_name': "test",
        'ip_address': "999.999.999.999",
        'port': 123456,
        'db_name': "database_name",
        'param_str': "charset=utf8&loc=Local",
    })
ssm_service_config = SsmAccount(
    params={
        'secret_id': "AKIDOiofIhy1pPrDKQZXJq91jDZidJlzyjT3",
        'secret_key': "NWQ7ZvHFzVnrgHiusb4II3YnocASWLuE",
        'url': test_url,
        'region': "ap-hongkong"
    })
config = Config(
    params={
        'db_config': db_config,
        'ssm_service_config': ssm_service_config,
        'WATCH_FREQ': 10
    })
