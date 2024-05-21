import yaml
from netmiko import ConnectHandler
  vxr = ConnectHandler(host="192.168.0.15",
    username="mohamed",password="mohamed@123",device_type="cisco_ios")

project = input("for static press 1 for ospf press 2 for bgp press 3: ")


if int(project) == 1:

    from jinja2 import Environment,FileSystemLoader
    env=Environment(loader=FileSystemLoader("."))
    temp=env.get_template("static.j2")

    with open("static.yml") as file:
        data = yaml.full_load(file)
    output1=temp.render(i=data)
    print(output1)
    print(data)

    print(vxr.find_prompt())
    vxr.enable()
    print(vxr.find_prompt())
    vxr.config_mode()
    print(vxr.find_prompt())
    show = vxr.send_command_timing("show ip inter br ")


elif int(project)== 2:
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader("."))
    temp = env.get_template("ospf.j2")

    with open("ospf.yml") as file:
        data = yaml.full_load(file)
    output1 = temp.render(i=data)
    print(output1)
    print(data)
  
    print(vxr.find_prompt())
    vxr.enable()
    print(vxr.find_prompt())
    vxr.config_mode()
    print(vxr.find_prompt())
    show = vxr.send_command_timing("show ip inter br ")
else:
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader("."))
    temp = env.get_template("bgp.j2")

    with open("bgp.yaml") as file:
        data = yaml.full_load(file)
    output1 = temp.render(i=data)
    print(output1)
    print(data)
   
    print(vxr.find_prompt())
    vxr.enable()
    print(vxr.find_prompt())
    vxr.config_mode()
    print(vxr.find_prompt())
    show = vxr.send_command_timing("show ip inter br ")
    print(show)




