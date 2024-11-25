
import os
import subprocess
import yaml

SERVER_ROOT = os.path.join(os.path.dirname(__file__), "..")
CLIENT_ROOT = os.path.join(os.path.dirname("~/dti_dashboard")

from dataclasses import dataclass

@dataclass
class Client:
    user: str
    password: str
    host: float
    name: str



def _ssh_configure_ssh_client(ip, user, password):
    # Check server key exists
    if not os.path.exists(os.path.expanduser('~/.ssh/dti_server_ssh.pub')):
        cmd = 'ssh-keygen -t ed25519 -f ~/.ssh/dti_server_ssh -C 'dti_dashboard server key''
        subprocess.run(cmd.split(), check=True)

    # Grant acces from host to client
    cmd = f'ssh-copy-id -i ~/.ssh/dti_server_ssh.pub {user}@{ip}'
    subprocess.run(cmd.split(), check=True)

def update_and_sync_content_to_clients(clients):
    ### Update content loop ###
    while True:
        ### Run scripts ###
        # (simple plugin structure for now, load all files in a folder and run them)
        scripts = os.listdir('dashboard_scripts')
        for script in scripts:
            print(f"Running {script}")
            result = subprocess.run(["python3", f"dashboard_scripts/{script}"], check=True)
            print(result.returncode)

        ### Rsync content to clients ###
        for c in clients:
            ### Rsync content ###
            source = os.path.join(SERVER_ROOT, "client")
            destination = f'{c.user}@{c.host}:~/dti_dashboard/client'
            cmd = f"rsync --archive --delete --compress --partial --copy-links {source} {destination}"
            subprocess.run(cmd.split(), check=True)

            ### Trigger client startup / reload ###
            cmd = f'ssh {c.user}@{c.host} python3 ~/dti_dashboard/client/client.py'
            subprocess.run(cmd.split(), check=True)

        ### Sleep ###
        time.sleep(60)


def show_dashboard_of_dashboards()
    ### Start detached process how the dashboard of dashboards
    destination = os.path.join(SERVER_ROOT, "return_status")
    cmd = 'eog --slide-show -f .'
    subprocess.run(cmd.split(), check=True)

    # Not sure this will work. Might not see things in subfolders. 
    # Should probably be refined anyway


def rsync_client_status_to_server(clients):
    ### Rsync client status to server ###
    while True:
        for c in clients:
            source = f'{c.user}@{c.host}:~/dti_dashboard/return_status/'
            destination = os.path.join(SERVER_ROOT, "return_status", c.name)
            cmd = f"rsync --archive --delete --compress --partial --copy-links {source} {destination}"
            subprocess.run(cmd.split(), check=True)
        sleep(5)



if __name__ == '__main__':
    ### Load Config ###
    clients = []
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
        clients = [Client(**client) for client in config['clients']]

    ### Configure SSH and config files on clients###
    for c in clients:
        _ssh_configure_ssh_client(c.ip, c.user, c.password)
        config_file = {"name": c.name}
        content = yaml.dump(yaml.load(document), default_flow_style=False)
        cmd = f'ssh {user}@{ip} echo {content} > ~/dti_dashboard/config.yaml'
        subprocess.run(cmd.split(), check=True)    

    ### Start processes ###
    sync_to_client = Process(target=update_and_sync_content_to_clients, args=(clients,))
    sync_to_server = Process(target=rsync_client_status_to_server, args=(clients,))
    show_dashboard_of_dashboards = Process(target=show_dashboard_of_dashboards)

    sync_to_client.start()
    sync_to_server.start()
    show_dashboard_of_dashboards.start()

    sync_to_client.join()
    sync_to_server.join()
    show_dashboard_of_dashboards.join()




# # #!/usr/bin/env python3

# import os
# import argparse
# from dti_tools.common.common import get_root, print_json
# import json
# import requests

# # ROOT = get_root()

    # # #!/usr/bin/env python3

    # import json
    # import os
    # import re
    # import subprocess

    # from dti_tools.common.common import get_root

    # ROOT = get_root()

    # def attach_to_developer_container(args):
    #     find_container_cmd = 'docker container ls | grep "vcs-" | cut -d " " -f 1 | tr -d "\n" '
    #     container_name = subprocess.check_output(find_container_cmd, shell=True).decode('utf-8')
    #     os.execv("/usr/bin/docker", ["WIRED_PYTHON", "exec", "-it", container_name, "/bin/zsh"])

    # def build_developer_container(args):
    #     docker_file = os.path.join(ROOT, ".devcontainer/Dockerfile")
    #     context = ROOT
    #     docker_args = (
    #         f" --tag my_dev_container"
    #         f" --file {docker_file}"
    #     )
    #     if args.verbose:
    #         docker_args += " --progress=plain"
    #     cmd = f"docker build {docker_args} {context}"
    #     print(cmd)
    #     subprocess.check_call(cmd.split())

    # def _load_devcontainer_config():
    #     path = os.path.join(ROOT, ".devcontainer", "devcontainer.json")
    #     with open(path, "r", encoding="utf-8") as file:
    #         file_without_comments = "".join(re.split(r"(?://|#).*(?=\n|$)", file.read())).strip()
    #         print(file_without_comments)
    #         return json.loads(file_without_comments)

    # def _resolve_args(run_args):
    #     for i, arg in enumerate(run_args):
    #         run_args[i] = arg.replace("${env:", "{").format(**os.environ)
    #     return run_args

    #     # Replace ${env:ENVVAR} with os.environ["ENVVAR"]
    #     # for i, arg in enumerate(run_args):
    #     # if "${env:" in arg:
    #     #     start, rest = arg.split("${env:")
    #     #     var, end = rest.split("}")
    #     #     run_args[i] = start + os.environ[var] + end

    # def run_developer_container(args):
    #     config = _load_devcontainer_config()
    #     run_args = _resolve_args(config["runArgs"])

    #     import pathlib
    #     source_root = ROOT
    #     name = pathlib.PurePath(ROOT).name
    #     other_args = (" --rm"
    #                   " --name vsc-workspace-dti-tool-spawned"
    #                   " --detach"
    #                   " --tty"  # Allocating a tty connection prevents the container form exiting
    #                   f" -v {source_root}:/workspaces/{name}")

    #     args = " ".join(run_args) + other_args
    #     cmd = f"docker run {args} my_dev_container"
    #     print(cmd)
    #     subprocess.check_call(cmd.split())

    # def _list_base_images(**kwargs):
    #     containers = [
    #         "ubuntu:20.04",
    #         "ubuntu:22.04",
    #         "ubuntu:24.04",
    #         "ghcr.io/teknologisk-institut/242-mobile-robotics/dti_noetic_base",
    #         "ghcr.io/teknologisk-institut/242-mobile-robotics/dti_iron_base",
    #         "ghcr.io/teknologisk-institut/242-mobile-robotics/dti_jazzy_base",
    #     ]
    #     return containers

    # def init_developer_environment(args):

    #     pre_ubuntu_24_04 = True
    #     if args.base_image == "ubuntu:24.04":
    #         pre_ubuntu_24_04 = False
    #     if args.base_image == "ghcr.io/teknologisk-institut/242-mobile-robotics/dti_jazzy_base":
    #         pre_ubuntu_24_04 = False

    #     with open(os.path.join(path, "Dockerfile"), mode="w", encoding="utf-8") as out:
    #         out.write(content)

    # def add_parsers(parser):
    #     dev_parser = parser.add_parser('devcontainer', help='tools related to working within the development container')
    #     dev_subparser = dev_parser.add_subparsers()

    #     init_parser = dev_subparser.add_parser("init", help="""Init setup files and configures the dev container with Jinja2.""")
    #     init_parser.add_argument("--base_image", default='ubuntu:20.04', choices=_list_base_images(), help="The base image to use for the dev container")
    #     init_parser.add_argument("--exclude-bazel", action='store_true')
    #     init_parser.set_defaults(func=init_developer_environment)

    #     build_parser = dev_subparser.add_parser("build", help="""Builds the dev container using Docker build -- as an alternative to building/running in vs-code""")
    #     build_parser.add_argument("--verbose", action='store_true')
    #     build_parser.set_defaults(func=build_developer_container)

    #     run_parser = dev_subparser.add_parser("run", help="""Runs the dev container -- as an alternative to building/running in vs-code" """)
    #     run_parser.set_defaults(func=run_developer_container)

    #     run_parser = dev_subparser.add_parser("attach", help="""Attaches to the existing dev container.""")
    #     run_parser.set_defaults(func=attach_to_developer_container)
