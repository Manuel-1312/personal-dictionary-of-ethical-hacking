# Toolkit - Snapshots 💾

Referencia rápida de cómo creo snapshots para cada laboratorio: herramienta, comando y qué guardo en `snapshots/`.

| Herramienta | Enlace | Qué captura | Notas |
| --- | --- | --- | --- |
| VirtualBox | https://www.virtualbox.org/ | VMs completas | `VBoxManage snapshot lab-base take pre-web` y guardo la descripción en `snapshots/notes.md`. |
| VMware Workstation | https://www.vmware.com/ | VMs Windows | `vmrun snapshot lab-win pre-scan` y anoto el estado de los agentes en `snapshots/vmware/`.
| Docker | https://www.docker.com/ | Contenedores | `docker commit lab-web lab-web:v1` y `docker save lab-web:v1 -o snapshots/docker/lab-web.tar`. |
| Vagrant | https://www.vagrantup.com/ | Boxes | `vagrant snapshot save lab --name before-scan`; guardo el `.vagrant` en la carpeta del proyecto. |
| Packer | https://www.packer.io/ | Imágenes | `packer build lab.json` y mantengo los builds en `snapshots/packer/`.
