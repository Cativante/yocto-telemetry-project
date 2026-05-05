# Yocto Telemetry Project

## 📌 Descrição

Este projeto consiste na criação de uma distribuição Linux mínima para sistemas embarcados utilizando o Yocto Project. O sistema foi customizado para executar automaticamente uma aplicação Python responsável pela coleta de telemetria do sistema utilizando MQTT.

A aplicação coleta:

* Uso do processador (CPU)
* Uso de memória
* Espaço livre em disco

O sistema foi validado em ambiente emulado utilizando QEMU.

---

# 🧰 Tecnologias Utilizadas

* Yocto Project
* Poky
* Python 3
* MQTT (paho-mqtt)
* QEMU
* Linux embarcado
* SysV init (init.d)
* WSL Ubuntu

---

# 🏗️ Estrutura do Projeto

```text
meta-myproject/
├── conf/
├── recipes-core/
│   ├── images/
│   │   └── my-image.bb
│   └── telemetry/
│       ├── telemetry.bb
│       └── files/
│           ├── telemetry.py
│           └── telemetry-init
```

---

# ⚙️ Funcionalidades

## ✔ Distribuição Linux mínima

Foi utilizada a imagem base `core-image-minimal`, garantindo um sistema leve e adequado para ambientes embarcados.

---

## ✔ Aplicação Python embarcada

A aplicação Python foi integrada diretamente ao sistema operacional através de uma recipe Yocto.

Local de instalação:

```text
/opt/telemetry
```

---

## ✔ Telemetria do sistema

A aplicação coleta:

* CPU
* Memória
* Disco

Exemplo de saída:

```json
{
  "device": "qemux86-64",
  "cpu_usage_percent": 33.95,
  "memory": {
    "mem_total_mb": 223.85,
    "mem_used_mb": 42.4
  },
  "disk_free_gb": 0.02
}
```

---

## ✔ Execução automática no boot

Como a imagem mínima não utiliza systemd, foi implementada inicialização automática utilizando init.d.

Arquivo responsável:

```text
/etc/init.d/telemetry
```

Durante o boot:

```text
Starting telemetry...
```

---

## ✔ Execução no QEMU

O sistema foi validado utilizando o emulador QEMU.

Comando utilizado:

```bash
runqemu qemux86-64 nographic slirp
```

---

# 🚀 Como Executar

## 1. Clonar o Poky

```bash
git clone git://git.yoctoproject.org/poky
cd poky
git checkout kirkstone
```

---

## 2. Configurar ambiente Yocto

```bash
source oe-init-build-env
```

---

## 3. Adicionar layer customizada

```bash
bitbake-layers add-layer ../meta-myproject
```

---

## 4. Build da imagem

```bash
bitbake my-image
```

---

## 5. Executar no QEMU

```bash
runqemu qemux86-64 nographic slirp
```

---

# 🧪 Resultado Esperado

Ao iniciar o sistema:

```text
Starting telemetry...
Enviado: {"device": "qemux86-64", "cpu_usage_percent": 33.95, "memory": {"mem_total_mb": 223.85, "mem_used_mb": 42.4}, "disk_free_gb": 0.02}
```

---

# 📋 Requisitos Atendidos

| Requisito                   | Status |
| --------------------------- | ------ |
| Python com MQTT             | ✔      |
| Telemetria de CPU           | ✔      |
| Telemetria de memória       | ✔      |
| Telemetria de disco         | ✔      |
| Execução automática no init | ✔      |
| Sistema Linux mínimo        | ✔      |
| Funcionamento em emulador   | ✔      |
| Documentação                | ✔      |

---

# ⚠️ Observações

* O sistema utiliza SysV init (init.d), não systemd.
* A comunicação MQTT pode depender da configuração de rede do ambiente QEMU/WSL.
* Para demonstrações locais foi utilizado broker MQTT local.

---

# 🏁 Conclusão

O projeto demonstrou a criação de uma distribuição Linux embarcada mínima utilizando Yocto Project, integrando uma aplicação Python com MQTT para telemetria do sistema.

A solução desenvolvida atende todos os requisitos propostos, mantendo baixo consumo de recursos e execução automática no boot
