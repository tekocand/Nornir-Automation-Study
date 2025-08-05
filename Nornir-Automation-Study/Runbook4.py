from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file

nr = InitNornir(config_file="config.yaml")

def test_template(task):
    template = task.run(
        task=template_file,
        template="snmp.j2",
        path=f"{task.host.platform}-templates")

    task.host["rendered_template"] = template.result
    rendered = task.host["rendered_template"]
    configuration = rendered.splitlines()
    task.run(
        task=send_configs,
        configs=configuration)

results = nr.run(task=test_template)
print_result(results)