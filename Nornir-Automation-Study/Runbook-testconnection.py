
from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")

def run_command(task):
    result = task.run(task=netconf_get_config, source="running")
#    task.host["facts"] = xmltodict.parse(result.result)

 #vrf_name = task.host["facts"]["rpc-reply"]["data"]["native"]["vrf"]["definition"]["name"]
#    print(f"{task.host} has VRF name of: {vrf_name}")

#    task.host["running_config"] = result.result
#    print(f"{task.host.name} running config:\n{task.host['running_config']}")
results = nr.run(task=run_command)
print_result(results)
#import ipdb; ipdb.set_trace()
