from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

def test_snmp(task):
    print(f"{task.host.platform}-template")

nr.run(task=test_snmp)