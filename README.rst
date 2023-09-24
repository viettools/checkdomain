============
CHECK DOMAIN
============

Port
====

Port: 6996

Support: Whois Socket, RDAP

Docker IPv4: docker-compose -f docker-compose-ipv4.yml build

If your server support connect IPv6 (whois .pt domain). Please using docker-compose-ipv6.yml

Docker IPv6: docker-compose -f docker-compose-ipv6.yml build

IPv6-Docker:

.. code-block:: text

    root@box-739909:~/project/checkdomain# cat /etc/docker/daemon.json
    {
        "ipv6": true,
        "fixed-cidr-v6": "2001:db8:1::/64",
        "experimental": true,
        "ip6tables": true
    }
    root@box-739909:~# docker network create --ipv6 --subnet 2001:0DB8::/112 checkdomainnet
    8f15c6a1446f0417b359f11946bb481526999f123851ca65be8c6bfc283c0cc7
    root@box-739909:~# docker network list
    NETWORK ID     NAME                  DRIVER    SCOPE
    7be54c1a16b7   bridge                bridge    local
    81aed8cb6def   checkdomain_default   bridge    local
    8f15c6a1446f   checkdomainnet        bridge    local
    cfccdba49f9c   host                  host      local
    db160d2facaa   none                  null      local

    ============== https://docs.docker.com/config/daemon/ipv6/ ==============


