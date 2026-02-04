# Lab 1 . Network cable transmission & testing


# Networking Cable Connection Procedures

## 1. Parallel Connection
- Approximately 1 inch of the UTP cable jacket was removed from both ends.
- Wires were arranged according to **Standard A**.
- Wires were evenly trimmed and inserted into RJ-45 connectors.
- Crimping was done.
- The same process was repeated on the other end.
- Cable was tested using a **LAN tester**.

## 2. Crossover Connection
- Cable jacket was stripped from both ends.
- One end was terminated using **Standard A** and the other using **Standard B**.
- Both connectors were crimped.
- Cable was tested using a **LAN tester**.

## 3. Wall Routing RJ-45
- The cable was routed to the wall outlet box.
- Outer jacket was removed.
- Wires were placed into jack slots following **Standard B**.


# Cabling Installation Procedure

- Each wire was secured using a **punch down tool**.
- The **keystone jack** was fixed into the face plate and mounted on the wall.
- The other end of the cable was terminated with an **RJ-45 connector** and tested.

---
---
---
---
---
---
---
---
---
---




# Lab 2 . CISCO Packet Tracer Handeling

# Procedure: Network Connection Between Two PCs

## 1. Setup
- Two PCs, two switches, and two routers were placed.

## 2. Physical Layer
- A **copper cross-over cable** was used to link the Fast Ethernet ports.

## 3. Logical Addressing
- **PC0**: IP `192.168.1.1` | Subnet Mask `255.255.255.0`
- **PC1**: IP `192.168.1.2` | Subnet Mask `255.255.255.0`

## 4. Verification
- Connectivity was confirmed by executing a **ping request** from PC0 to PC1.


# Communication Between Two PCs & Router

## 1. Setup
- **Devices used**: 2 PCs, 2 switches, and 1 router.

## 2. Connection
- **PC0 → Switch 0 → Router (Gig 0/0)**
- **PC1 → Switch 1 → Router (Gig 0/1)**

## 3. Router Configuration
```bash
Router> enable
Router# config terminal
Router(config)# interface gig 0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
```


# Multi-Routing Between Two or More PCs

## 1. Setup
- **Devices used**: 2 PCs, 2 switches, 2 routers.

## 2. Connection
- **PC1 → Switch 0 → Router1**
- **Router1 (Gig 0/1) → Router2 (Gig 0/0)**
- **Router2 (Gig 0/1) → Switch → PC2**

## 3. IP Address Arrangement
| Interface         | IP Address     |
|-------------------|----------------|
| Router1 Gig 0/0   | 192.168.1.1    |
| Router1 Gig 0/1   | 10.0.0.1       |
| Router2 Gig 0/0   | 10.0.0.2       |
| Router2 Gig 0/1   | 192.168.3.1    |

## 4. Router Configuration Commands
```bash
Router> enable
Router# config terminal
```


## Router 1 Configuration

```bash
Router(config)# interface gig 0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit

Router(config)# ip route 192.168.3.0 255.255.255.0 10.0.0.2

Router(config)# interface gig 0/1
Router(config-if)# no shutdown
```

## Router 2 Configuration

```bash
Router> enable
Router# configure terminal
Router(config)# interface gig 0/0
Router(config-if)# exit
Router(config)# interface gig 0/1
Router(config-if)# exit

# Applying the static route to the router
Router(config)# ip route 192.168.1.0 255.255.255.0 10.0.0.1

# Testing connectivity from PC0 command prompt
PC0> ping 192.168.3.22

```