# IPv6 Shortener
IPv6 is a 8x16=128 bits IP address and an example
IPv6 address is: 2022:0db8:85a3:0000:0000:8a2e:0850:7990
With 3 rule the IPv6 representation can be shortened.

Rule 1: If IPv6 address has continuous zeros then these zeros can be replaced with '::'
Rule 2: If there is a leading zeros in 16 bits, these zeros
can be removed.
Rule 3: If IPv6 address has discontinous zeros, only one of the junction, the zeros can be replaced with "::"

ipv6shortener.py, according to the above rules, shortens a given IPv6 address.