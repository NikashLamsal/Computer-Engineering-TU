# Lab 3 & 4 . Dynamic Routing configuration ( EIGRP , RIP & OSPF )


# Connection in Cisco Packet Tracer
## 1. EIGRP Protocol

- Three routers **R1, R2, R3** were connected in a network with a subnet ID `20.0.0.0`.
- IP address of subnet ID `20.0.0.0` was `20.0.0.2` (R1).
- Network protocol ID `20.0.0.0` with an assigned subnet protocol `1 & 2` with IP addresses `0.0.0.2` & `0.0.0.1`.
- A PC with IP address `10.0.0.1` via switch connected to router `20.0.0.1`. Similarly, PC & PC2 were connected with respective routers with respective IP addresses.
- Then **EIGRP protocol** was defined for each router.

```bash
Router(config-router)# router eigrp 10
Router(config-router)# network 10.0.0.0
Router(config-router)# network 20.0.0.0
Router(config-router)# no shutdown

```


# RIP Protocol

- **R1 & R2** were connected in a network with IP address `120.0.0.0` and were assigned IPs `120.0.0.1` & `120.0.0.2` respectively.
- Similarly, **R2 & R3** were connected in a network with IP address `100.0.0.0` and were assigned IPs `100.0.0.1` & `100.0.0.2` respectively.
- **R3** with IP address `100.0.0.2` was connected to a PC with IP `1.1.1.1` via switch.
- Similarly, **PC1 & PC2** were connected with respective routers with respective IPs.
- Then **RIP Protocol** was defined for each router.

```bash
Router(Config)# router rip
Router(Config-router)# version 2
Router(Config-router)# network 120.0.0.0
Router(Config-router)# network 100.0.0.0
Router(Config-router)# no shutdown

```

# OSPF Protocol (Cisco Packet Tracer)




- **Router 1, Router 2, Router 3** were connected in a network with IDs:
  - `10.0.0.0/8`
  - `20.0.0.1`
  - `30.0.0.1`
- **PC0** with IP `192.168.1.2`
- **PC1** with IP `192.168.2.2`
- **PC2** with IP `192.168.3.2`

Then OSPF protocol was defined for each router.

### Initial Setup
PC → Desktop → Terminal → OK




```bash
Router> enable
Router# config terminal
Router(config)# line console 0
Router(config-line)# enable secret cisco
Router(config-line)# end
Router(config)# exit

```

```
Router> enable
Password: cisco
```

# Router Configuration with OSPF

## Step 1: Enter Configuration Mode
```bash
Router> config terminal
Router(config)# hostname R1
R1(config)# interface gig 0/0
R1(config-if)# ip address 192.168.1.1 255.255.255.0
R1(config-if)# no shutdown

R1(config)# interface serial 0/3/0
R1(config-if)# ip address 10.0.0.1 255.0.0.0
R1(config-if)# clock rate 60000
R1(config-if)# no shutdown

R1(config)# interface serial 0/3/1
R1(config-if)# ip address 30.0.0.1 255.0.0.0
R1(config-if)# no shutdown



R1(config)# router ospf 1
R1(config-router)# network 192.168.1.0 0.0.0.255 area 0
R1(config-router)# network 10.0.0.0 0.255.255.255 area 0
R1(config-router)# network 30.0.0.0 0.255.255.255 area 0


```
