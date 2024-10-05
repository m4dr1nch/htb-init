#!/bin/env python3
import os, argparse, validators

# Parse arguments
PARSER = argparse.ArgumentParser()
PARSER.add_argument("-n", "--name", required=True, help="CTF name")
PARSER.add_argument("-i", "--ip", required=True, help="Host IP")
ARGS = vars(PARSER.parse_args())

# Add more in future
def validate() -> bool:
    if not validators.ipv4(ARGS['ip']):
        print('[E] Invalid IP address.')
        return False

    return True


# Create a directory with messages & error handling
def create_dir(dir) -> None:
    try:
        os.mkdir(dir)
        print(f'[I] {dir} created.')
    except FileExistsError: print(f'[I] Found {dir}')
    except:
        print(f'[E] Failed to create {dir}')
        exit(1)


# Create all required dirs
def create_dirs() -> None:
    create_dir('/work')
    create_dir('/work/ctf')
    create_dir('/work/ctf/htb')
    create_dir('/work/ctf/htb/Machines')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/scans')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/scans/nmap')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/scans/gobuster')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/scans/ffuf')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/scans/cme')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/scans/nxc')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/scans/enum4linux')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/scans/ldapsearch')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/loot')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/expl')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/sandbox')
    create_dir(f'/work/ctf/htb/Machines{ARGS["name"]}/www')


def update_zshrc() -> None:
    os.system(f'sed -i "s/export IP=\'.*\'/export IP=\'{ARGS["ip"]}\'/g" ~/.zshrc')
    os.system(f'sed -i "s/export CHD=\'.*\'/export CHD=\'\\/work\\/ctf\\/htb\\/Machines\\/{ARGS["name"]}\'/g" ~/.zshrc')


def main() -> None:
    if not validate():
        print('[E] Invalid parameters.')
        exit(1)

    create_dirs()
    update_zshrc()


if __name__ == '__main__':
    main()
