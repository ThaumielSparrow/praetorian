# praetorian

`praetorian` is a utility package containing wrappers for common cybersrcurity modules, wrapping
functionality from libraries such as Scapy, Nmap, and Sentry.

In addition to threat detection and neutralization, `praetorian` contains a full suite of the
Offensive Security utilities designed to simplify the creation, injection and monitoring of
payloads. `praetorian.utils` contains several generic-use helper functions that are desgined to
natively accelerate many properties of core function.

`praetorian` contains high-level recipies and reduced gateways for cryptographic primitives such
as key derivation algorithms and symmetrical cyphers. These should be considered 'hazmat', as they
have the potential to be hazardous.

Package is early alpha and still under construction. Use responsibly, and at your own risk.

Developed by Luzhou Zhang from Team Sparrow (c) 2022

# Example Usage

```
import praetorian

test_socket = praetorian.TestingSocket('https://google.com', 80)
test_socket.initialize_socket('TCP')
```
