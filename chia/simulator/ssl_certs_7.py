from __future__ import annotations

from typing import Dict, Tuple

SSL_TEST_PRIVATE_CA_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIUHoeobLQu3yMmraIDXDF+F6M4j9IwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMB4XDTIyMDMyMzE3MjkyOVoXDTMyMDMy
MDE3MjkyOVowRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8G
A1UECwwYT3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAskK29xVfnH/4tpM+loZOOZX3d0u/NARRkgnPeoTs14M0
dKP+dZ+FRuuqKmJQHuO8+MFfeTFIiI671rWobtdGCXVD+TZ3g4btdtGdvPjIBXJs
RFhYkP/fIjzq0MoJ9O6qlhXh3skispfHRY2ysVHpT4d63tixhycDsMn82Jh92OGm
BaO8UpjIk1twEnfxsKm5MtPbvNJGVzAkwYXWVFdV7GdEYCKsVm94Sd85TpDg0xFq
q5YWOg5mpFbGAExBjFerHSuVBuNsBap0mjL3aIb6MXvQeYp+lKrzeUfkUH06e/Pr
AY+TQPO9ktcUHHZ8+HrXhOODdeDlbC8mWzR9I59AfQIDAQABoxMwETAPBgNVHRMB
Af8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQBQ/s/lX6Tbdg1g1FIShK+BH+5q
msfNkAQG+mXYGbn6SYQQspYFZdZp4kXLdSKSjok5eWoMnfYN+hy29A5HgeJfdbM4
4Nmt5OUvWT0EOTD1VtdVnsH8tac5Q1XevE0ZK9DXYBSEXqO8sVSt6VWmNT98lmEZ
AVWtawc0zt/31QAZEa5Jjghq/HRbIi6KUX1t3Hx/yVa9Uxiz1dBVE8A+QBwVKOzv
egKu6T94xBCcOeOh0NgluRdFiTr9cXAYNQAUM+WdmyAvFZ4qwuUKam7C7zX+td6M
r80F1SD8qbQgxYS1bwqx6K06xbFRLXpWbyHXG18v6ia+sifWblg6JQnYhxZg
-----END CERTIFICATE-----
"""

SSL_TEST_PRIVATE_CA_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAskK29xVfnH/4tpM+loZOOZX3d0u/NARRkgnPeoTs14M0dKP+
dZ+FRuuqKmJQHuO8+MFfeTFIiI671rWobtdGCXVD+TZ3g4btdtGdvPjIBXJsRFhY
kP/fIjzq0MoJ9O6qlhXh3skispfHRY2ysVHpT4d63tixhycDsMn82Jh92OGmBaO8
UpjIk1twEnfxsKm5MtPbvNJGVzAkwYXWVFdV7GdEYCKsVm94Sd85TpDg0xFqq5YW
Og5mpFbGAExBjFerHSuVBuNsBap0mjL3aIb6MXvQeYp+lKrzeUfkUH06e/PrAY+T
QPO9ktcUHHZ8+HrXhOODdeDlbC8mWzR9I59AfQIDAQABAoIBAFm7l5qdWbnP+YT+
bf0bsnjuctnMeX1Xxy/6XETScN6zn04v10GigVaH/urC/o3uGgwmW0cIdfi30Ppu
C1FwcEMGkqb6sgK1gwfS0NJ1cUq8pJ9q0Xp8MvhrLdDYQ1bWZWyTq1WYbiz0lkz+
3TrBfu6XxlQzRHpCO2tc4jit2nu3k92I8EHo8sRPcFssgEH7JdFpGOm/G6ATWGpU
mSJZTxBOzR5iprR8Hl2RXIBDGXqVKXApLJ3OlchSOodeFt2h7ffiNJmuGZ/cnxs0
05eXzIg0zJ5CffoQdO5s63SPRg+x8O+L+hN0k6Kh5CmFpAcn1jzZatvGO47ndBUx
kSyrH0ECgYEA2a1n+84y6A35LOeUvTE0m3c+DXoI7jl6zUSffXJ5PVH7lKro2hq8
P5TDG2NV9qFv4KFJVy8hvy6Ie0+HTNP+QSUB2LvJSp4GhlQNP4/J6oY4NGfocfbK
+rc8/jEVQaoySq1ODLchEaxMjwgKOVcUqh6tCQjiTZ3dqpZuwUGALoUCgYEA0aTR
UYcynBWPyt5OT98EkVX4Nu+NqONAyKlDYJqU2NHP4xHFxVPPwYR1C4vZJEmC1z3C
Rad+svwBhCXsh54hTBhZkF+BV8ll4/BqiuHiaqF95VRz8B4wjv+0QKN1fCQO4RT5
dEqbAkJYPq+vYCJew3iPWODLkaK/B8yc1hQ3l5kCgYAkYhGBSwPDOaKuWL7JqJHM
cm/SvNUFTGI0MQYfZ6TQFQXh4XcuDU3tqqW5zC6wHGeguhSSF/SiCdsSEUbiFoTm
ypK2cRzB9gvNI/ta5mOvaWO3jq6Rbdibc0kki3usEBB73t+uzGUgmRXqykM7Nkzj
6mCto+h/ZKWKP76fWp1cKQKBgH2KEiKdMExRiRr1xrWDmkuhzJKxHwZsl6XR3lwi
FVJFShTy1piU2MtMk36Hj09wid50yDpH09JAoHPO9fY8VjooNrICzwSPwOkfVd22
6IvsCuTijs7SdUecjgdLGxZszVAx7DOcXXib3BYlxIJv8olhT43sh1q9t2FnQN/d
mXC5AoGAN5klrbJVgUE8kRik5GvpcoasyDktJQ8KKDD2u/TDkRaCJf6H0ZP145aM
k0Mg5DMG5M8+Eb6l+iEOX1lrrJ3EPtcQraUiFAPXF8slboUs7k5HZ6rVckHqMvBC
ZTAxfIdR90eFK6q0PTRYH2ZfxKKpPDORQvzt59reHexvOVTuozk=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUFNReIWFnacmYlEf+oXKER30rJfAwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyOVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDdivRLL/onTCvG9JKzYXCxW6hrwYRgmiyG4ISrIWlainW3
ZCduM13t4qlWp2lVYCIez8K3NYb+m9Jk4tYJujzU9FhusvAy2D7SeGJGkAvDuYMK
LCRM0m3/Q0fls0RMHyNd7Csg26LNyGukdvEyKmonqA8q5MZENtsRx1tQtHORLlio
kEXjyd67J1wm5m4rOk+DqdrIzSAuomj+M/D1lRh0icjiSE0Wm9PXJllzSp/JyLqN
AMIDIjkG5CZc7cD2yM7OZQ+haCxIbAmxzyWVhLeuGiTP2qZ2ZRML2HXGVkQfbE+c
vFkPKVoY6pOI0USzM6ipqmYO9Y6357SIeSWhNNG1AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBGWHpJNp8iDR5uy14qFYwY
1wwIvQUem0IYADuTXIP3Y+kSKyZpuZeYWFlKzrfTf6wTlmZchcqpidUfkqPS8sFL
4LLRlDFTCWhIiBSs25gLLwRiMTErStedojGS9+smMVpp+/LguAp+kR0zyov7+Qe/
05DW/fgtZFZIuDa9DX2aLcr2LHLpQU2+nKFM5E4dOEEwaf2rDkpqITME00bZRipF
yytQq6MIG+W2dl48b32B+VhU3UtjeJ4bYDY2BUvAoI69XN/RWO2JVZqEcuAKXjIY
m/+snrJJ8RNATWZ0XgFUQ3UL2j98qHwY5XtGNvLfkot6EC48t0jmuPICg/mTxCPV
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA3Yr0Sy/6J0wrxvSSs2FwsVuoa8GEYJoshuCEqyFpWop1t2Qn
bjNd7eKpVqdpVWAiHs/CtzWG/pvSZOLWCbo81PRYbrLwMtg+0nhiRpALw7mDCiwk
TNJt/0NH5bNETB8jXewrINuizchrpHbxMipqJ6gPKuTGRDbbEcdbULRzkS5YqJBF
48neuydcJuZuKzpPg6nayM0gLqJo/jPw9ZUYdInI4khNFpvT1yZZc0qfyci6jQDC
AyI5BuQmXO3A9sjOzmUPoWgsSGwJsc8llYS3rhokz9qmdmUTC9h1xlZEH2xPnLxZ
DylaGOqTiNFEszOoqapmDvWOt+e0iHkloTTRtQIDAQABAoIBACHjhJUPxLtIKpYn
iV1JNXzb4XqCQqaoTtFe/MxUsxH3hiREfMedseuWtYKc3z8BEpcV/toZpQnDej6W
eFlKlM2ahwB//MA6VfnKEnZqyHHrKcFfmTnrIopel1vqvTLLvJQ8cSh4kIHb+6NP
0ntzA4QHcDKGhlGe9onUrgI9aEQ3wrHZvChyyAV8P/sxY2IseOf5PkJ/fBqttGPZ
9aRdpzvMCyfbhygHAVklucefuQehpc2duv6BUwCd1HgAIwZ42gaTQ8h8Yh2SxDiV
9DKkkQEJoG8ZXYGHfKpXo7u+RgTtpMPmRnls5uIt34qECRJGmXr1pC9iBx1oRIi6
Qdno4q0CgYEA/lcKRnpjrnWfGYgLZpIPEr4pV328BZ1I7FjzaCcfDEU70gxFpCXa
ViHP8TEWG3+yH+WPodHMfLQ3UzLzSBu/o/XYfU0Nk4A7QrGt4heDRmPGGY+WEKs/
LoiXlLrF4rOKw3feuR2wagg6NpP5uDraVJFCDG5O0/SIyWSc5ZW7DEMCgYEA3v0d
jfm0n6dNpJDgvCz50qhI6ijUT/Wvnl1VVXHpGSVJjDMSffLsGe9G9bHJCz0s3E0B
NfGJlixmkpzmtNmb4qt4ahdEY/ltYUFlWTvY84JjvJTFrjV0if3LLlVWeHm0aEcB
rBsp0Z+/qpoY6AJhWmN0jX2pS8WbsjHO9OM8xqcCgYEA603rm7ivcEAxqZVLtuF6
QITeCquwwCD7zm2dA8bt2pRS+8mOxIagsP8nOqWHJnnFee0QLU3EObshVD/XA+do
LXDNkV8wKD6ClPl9PaczNHQqWouU8mb8VTjZxCfn3AzvXFgSHoFxLSffc48DgYYx
Z/vbd1S2aTHbOzdyUJVuL7ECgYAUApC5YdQEk6XTA7E3Ea4lajaI1LsgpcJpqqRy
s3Mgb4knDJo3NSpctW0ftSF+YbH53ush5RfcowVdWLkXN4PWll6K3qWjdwmKtayb
klRIncXHcW4/0Moxa9XkxYGp8/ntdZm/0PwytGwlqghcIYKM8unNnJ4pj4UGO5P/
w7h7dwKBgQDYqai2lM4mtud8Xn77maR1olSScon+S9eG6GGyRQPVom4NyvfaQxvb
qFQZnwoQuh5ugsbyCA0qkm2RhBIqNWo4j8rM7AHb27qkB9F5tHA6S+DYG9kEvgmn
HFxiZCY+Lu6wRP5Ssnz444i2Tr6kUnIcj4XRyOQjcwKqhMYNod5XGg==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUfZLZhnra/z8yyJivw/7O2simIzowDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkzMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDAkSC0hl+/EeP4XUtJDAWCBRosaU7munJ8XX4fZDcmXzsg
p2zdv9UZp2zkfXTYP5zFAnjG9QEiiURMZ4rIKdr/cJXY/93H6dwfrjZTS1gCSlpc
gkuq/cdbOeU6xCX8X/dotSQupbYr6ccPVf22iON/FotilEpP2yOFZi0d54uKnBoq
x6GP22b9/Ij+tQNacPZavQjZD2i7ChtLigtMDmrrFMOrsQjSCQPpGKsXmyNqTo+/
BKAKEs+WghuoVh6G5BeC2EY/PoUohUxBUWlAXThA73yrq/nGQRWfPeNZ2r0d1z9m
AlUakb4a54M8tDO+OOqw985KyhPYRGxOgPDFy4cdAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAQRNledZvjT6+Rtb29W8pN
11WfUj5+QW7DX7/AFd59PXQkPbTf9EPiNtbriPaeOQ/B+jJ10/hGGGUhft4IEzpX
ffQ09CPNAFMiyvvnOQdykH9lvDMcoVYi4EjzFsCa7uVbKSZApeO07hCWRtlEeDrx
QU//I1F/BcGQGh9Evh4LiZZUzRxqlGE11jSBNIpSNkVE0DO90lBwEujvb1OC4YUh
x8Ef3hzI8EkR4VHG8SwX+VlasHAvM06ouKAQeMMNTWxeShaTI+mZkVUgkWJvTxf6
LwmU1B8s9M9hNUailBda/7ztvcZHWxghBhsWICZIngUvt8M5/rrgph+e0rI2QMiP
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAwJEgtIZfvxHj+F1LSQwFggUaLGlO5rpyfF1+H2Q3Jl87IKds
3b/VGads5H102D+cxQJ4xvUBIolETGeKyCna/3CV2P/dx+ncH642U0tYAkpaXIJL
qv3HWznlOsQl/F/3aLUkLqW2K+nHD1X9tojjfxaLYpRKT9sjhWYtHeeLipwaKseh
j9tm/fyI/rUDWnD2Wr0I2Q9ouwobS4oLTA5q6xTDq7EI0gkD6RirF5sjak6PvwSg
ChLPloIbqFYehuQXgthGPz6FKIVMQVFpQF04QO98q6v5xkEVnz3jWdq9Hdc/ZgJV
GpG+GueDPLQzvjjqsPfOSsoT2ERsToDwxcuHHQIDAQABAoIBADweEsPJH6MbBrzH
A3Xultmclis/RS6rDorc9T7/nmgQWvk6y7X+6Zx0tH4w3IWWdm7a8rHKU2xgxj3E
JYOP7ZrJnz57wtVioSIS1UrzvqoYZFV1KAJd8Br+3B2YlvNPUoIR6xXVDiZveYHE
Ks0Nt1g5xZIlEX4Uv+Ypm/Q2EU5YGnxs238K8kwkPtNTLyAQ7v40YAyZ8uehUu+T
vaMKi4GwX/+TaXWW8dek2fsktWGf10drMckvv0fyo3CdYlSMs0PFZkIHqMQuQv9/
E+XI8viMovrnhU53jLbs4Tt+f3kDtWVUrd+kqWw5MXzT2K5z6OGQtjK2enACwilj
kbv/ntECgYEA8hUfsihlCFKZdJHZW6mldFY5Ld8YEsAqTter4r9iid8+R6yrSr2k
ZcdAyNFcDBGWkX51nupteU/LFHojlRymxVD2AVGanknYrJ4DNvvc08bCgVZOx7vz
u9KQb8E1xsi9T7uzoGfDqOapQSqPrFvxIPkqKWpOeqY5Jq4UZD7onmcCgYEAy6NA
oqFjbz8/6ImpOaR7cQMFgPnw749qmiRoIMHSL0ULkKq/XF8pN3/mxzKxmLGXGYm/
yXbpcpuS5oIE2vhwxg1XAgUjpEG7stWtv0tlzpy230/TzwTJO2OOEaVcND+9nawV
T0ufX7c9CRcH4csgG4eJR749rG7jdLiGoqdms9sCgYEAng8YwNQLE2IK+8d2qZic
hNb/QmoVZ7i8Zvn+KnBXQDnYiie9N3GW8zUjoXrApMifDKQK3BWoILrul5IfxW4N
nWt9E+NaFtuUczBAXRgZWNS/jn7xtQuM2idjUvRNzlqm8HZXk/XsFE12WSwW3qyx
RZwp4Ryd3QrG6fBjNAi3DSUCgYEAoTvHR30lL8YSodmtZXh4TIip6O7895DERPui
fp04ADlY6Nho34hxKAJbBUl8GHw0OQI6GhfOyvGnJF+53G5tTELvqyfKipmJNhW9
lgLqvuaSXMnl2LnfYuh2aj5VfQEi7x57WOd1buG0r+fOU9byuxlbdrSIPGkoKxiX
cV2+EZUCgYEA3rMsb5/F1nCsuhPS1DNlurMwSmodFaYasg2+cg3hQPtHe4LO86U8
doW1c97sdKLLkH09E7ZmZafXTj4uKwQlLa35UmaRvPM+mWdPLr0Nkkm1dEAi298g
zD1u3pg1jQE1Ta4kuE65u8lwu0JKvje8pvHBRRcXuLvr2oyJ1VWVfvA=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUZmWsnGgQgJO07P9Mrqx1hHBfQbkwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkzMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDjcVLjFq2N6GKxvke2xGntOo62h4ze0fNrdj/OifXvpzxf
qnPkhBcb7+6GL/gO9IT6hnTCDSjNQG/Coi1grjoPT9T+DkamwioBcFdIOYwEqPCd
Fk5ZnqwAWWg94+dkb/jlRcFlShNcgDriH/MrgfQ03A4VfqzcNT8GzZ4zwFqAyhiV
KQ56q0qrnIrHQDERII3QMH72EGCVX+32IIkz2CJvo56yngwF+tDzYJYHMJnNTCG8
iVD71v6qBM52G/6bKFRJhyZkKkVqPwptIXInDPY5ETgfZYgD67ffQ5+W1kXlCmmH
PuK8w48Fw7LjRDzLTYRFyDSIT1H5sdRvHLIl9BEnAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBvOTJdNGUD5Zc976Q5SJre
15KN8PaOsLePPISn7e/2DwMGuq7GXnGa4JCb35XTGjX+Wxgnv/0/8asMimay6gwE
YZBcRwakm3l3//4W1ELc6SREoFcUTV49rnccq/N3u7ZrDubf1U9uKvFEpwp9TM8a
nq7tVOe3j+Msyvq4/q/l0nnHX/uuWYrZrC+Cm6tjytmOr6JzAhURFoVx3QnwaD8z
qm+cisSE3/lLuyTzgNUiQkdIC6bCg5KVOrTXFo3T72F7+oeM7h+OiDO71y79x9UH
r6YE8Ab1nYz6Cw1fwy3/QzxtazuTrJ5gBotF0oqCoayEtiOMZr+aQuM/qRs0EeTy
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA43FS4xatjehisb5HtsRp7TqOtoeM3tHza3Y/zon176c8X6pz
5IQXG+/uhi/4DvSE+oZ0wg0ozUBvwqItYK46D0/U/g5GpsIqAXBXSDmMBKjwnRZO
WZ6sAFloPePnZG/45UXBZUoTXIA64h/zK4H0NNwOFX6s3DU/Bs2eM8BagMoYlSkO
eqtKq5yKx0AxESCN0DB+9hBglV/t9iCJM9gib6Oesp4MBfrQ82CWBzCZzUwhvIlQ
+9b+qgTOdhv+myhUSYcmZCpFaj8KbSFyJwz2ORE4H2WIA+u330OfltZF5Qpphz7i
vMOPBcOy40Q8y02ERcg0iE9R+bHUbxyyJfQRJwIDAQABAoIBAHyCXDLPBmGqNuVA
2nd2XNqudNP9rqOIYe6RRGrn4Ye5kHZ6lIkjupbjqTsyZWSifW28T4yvsYdzX/s3
1wmXN1eMh3gxDoJZxq8U9eMnBbzDUz1bqbasA1MJnuRKsDCuj53LqwytGZ5I4HNL
tE48DRkm4lroBu9iAsfRpmqEQcdAUtXGLvGGkX+V9j2exREyVXrxALC5N+4i4w7E
f5aidhH79IGuMbfp88QS7NbjrpEwd1uyP3J7KCiyXwWIJnJyF8pcd7ZUsP95msE9
STeoKBaV+cIE03jvTT4fpuQ2Cn2WYSxkgVdWM+XdxGouIQvboOBNvPdWfdQCLSHa
acRhzGkCgYEA/nd/BXmm9pkGKHm9XDHy97pYm1PSOihsgjZq148hY33gdA/ibUtK
X7nSlmGAUzVTU01nfPmjkHp0YyoDn+NejAyPhBUqPoxfC7p2In1MiibOlMDxOpPl
199+gvadHk59g5Ap02iCu1lnlR9DhFY+42XcBSLba8MdplOL4lhnx9UCgYEA5NAk
45Dt0NXnaKKLbMW5EOZA1zLUcomO8AH1dEF+l3e5UOm9g+YnYtUVALKM1nBc0EJ3
fu8fmKhDqieLxb42o7j8yQqeKUXZW3XeDGPdLhR8coxICZv8f2j59Qgx6gwQ0ipy
IUan/0rDUm7dinu+07Va4hqnvpuPbUco3VclDwsCgYEAvwScyVNkzkBYqxGX4Blu
th+gXBkz+oxVx/lpgp7jBXh8gSNbaYfXMLyhJFnUpqGlBydXxCzxZ4dEzxu+1Mst
MhxLr27j40gkIP27qHA+gIZZFLkxXDOhmccfhNfzYcix14zkmNofKNwYMYzidfj4
BGN2IjTkWaSCIVUd8K9EWHECgYB6wKu5pivfaJIgEWvJK/4P8ecBTFSrKd8UJYjg
GK7oZaN2pB823sdsfzIoUKG7/UXduHrRD0odJNBAPbz/lf9MMFb1KAwXylBEf+Rj
M0Qaj4UAEwAmn5eDZvcKHJ5imJyBk6Hs9jH0hNBqre2OeLq0a0vZl0E8wcndb1qd
/D12ZwKBgQCDKNhzVlKwtG5hF9rG0FLxUtOduOEH9OI4N0BaptoJncGw/LEqZI9R
ZWim7eYzst6zGvsm6hiCZXR9pt1IUNVC0YxaP38YoolFKYxwcraPIfhteXx5CF2D
EfVRIx4ZL8Ec0nKeG7sfzl1AM30kOT1sZ74ZnoS6iYNXGbkXIeecUA==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUJg7OmxTb+nSse9yCvMecvDQ995gwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkzMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCoMxRs8WLspmYqmfcq6MqZI2h1bNRqXkdXdDpRTNkdfusp
8Xm5/Oncd2ewVbOIWNtaw0c5Uq6futXmo3cMAf4fTCpQUxEeWcMw1KWK5vudfXFY
w0VNxS9fAR4ByRbNGDcW7HXu0silleuD8onSKxBEyUpNHksqmuWLJ+Av9zvRfl4V
P5WUVr84dpaotLXYx4PxoPINRloIKIrzsEAVwrmV8OxsbsxdlvokUYy6kezTRNqN
7izl2CCi5PvklOHYr9Bf5NgfAE4VMMTcVrQKebTkGAdlJipJ3N7gf75Yi/mMTXnW
SjMSRjJWGub0iowNUEXLXLaSQurQRJ5iCoMCZr4tAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAw9TzzcnbQvjEC4zF4nPr4
w6cNUog8tfiUx3Oh2Hf4+//Urhu+9rO2ylV90apT2kR5qUT0yod3s/9WGMe56P1b
3qES6PTN2LipOT0js9SmmhHmcy+tiQxeKk37SWjFMHMmfpaZHLZROxIAsHUlisYo
Pb45Lm9zd/yofyh0xTHC36KaU7R3mVzE0cKtFKHZIiwpd5BUp638lY6tngQzOOe/
hhxRyJ4XoafugAgW9nykm+zMG9LxhHpoMFIZuZQZED4RKG7gKA8l0VqKm9Cg9DTm
xqhRHtHY9hS47dsHL9Ggv8XsBy4nnkemVhB33DPK9kYRmz+J4Y8gjoqlL7ZL8bnr
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAqDMUbPFi7KZmKpn3KujKmSNodWzUal5HV3Q6UUzZHX7rKfF5
ufzp3HdnsFWziFjbWsNHOVKun7rV5qN3DAH+H0wqUFMRHlnDMNSliub7nX1xWMNF
TcUvXwEeAckWzRg3Fux17tLIpZXrg/KJ0isQRMlKTR5LKprliyfgL/c70X5eFT+V
lFa/OHaWqLS12MeD8aDyDUZaCCiK87BAFcK5lfDsbG7MXZb6JFGMupHs00Taje4s
5dggouT75JTh2K/QX+TYHwBOFTDE3Fa0Cnm05BgHZSYqSdze4H++WIv5jE151koz
EkYyVhrm9IqMDVBFy1y2kkLq0ESeYgqDAma+LQIDAQABAoIBACodB/szARrRmvkF
rc4vlTJ8nBXylsi/LEuoTUW34RCyi3zn+htoSMGrn+mVu6ri3KFADaA7pH9Xz2C9
Avydrxv0/Q85jSq1PNsIEx7RMKTBGNUppzuOqIq4A+RcjfnyGzEBKZIPcq+K9voF
ix51K9CdOZ5PfHCBcgHCjS5VT8Pm4QtUnH7Ak+unT8QZ2DaK1PY9lnsburr2o7ax
kk7DLSsb60pb7XBDLrv0c5i4/XIhSP/GBUJ0GLTEutWG9iXwa5Nzlxoz4UGjnljP
80KQB1TGiZnFYiolrKaj+rmcuXeApYuiAwFI8B58DYyol3KJXmUCzilw38ycArd0
nIkhyJ0CgYEA0TXHfUKZnF9X7Vig3hCCfHZFJy8g3L8RklIjZVn9VUGFZhCIPiMN
zgSI5fK8sx1oLKz4vYvT4+4QoS3kb13pWGRoG8ooF76R/0soXckKG/0Nl2fq6YHR
9Bygxvn9XxxGHToIJfxfcmzfE8h+wmpdd4t1vuWzIzrAqyoBDf2nxIcCgYEAzdFD
Bb+J9CZviAtsOAEiouZby/rtZ9ayLUulRTDZuKpVnVHRnzckA6cLEqECC4dr5WsH
bDFasktvx5chl5SuE3NFR8cznMyFN5rpWOpYdl1QwwOQ15sBJ2LuT+mafXpu1/7x
RhZyw5oaDDrpaqOLTvQbxlrXjpXYlNsIeXALyKsCgYB1uTtuIuHpekUyC6NKEiQ7
ARpcuEpXrTSoD4xXZdIF/X6hNkBUJsmH2klmi7bfW3bZXOQDVQGAyt+UswxOFpxN
3wIuUQ1KfzQMYjBuxcfog/b38cPgberE4K8gCGAo+vIBVDxtk5vp+ZV1vmaF4/CA
antxVjP9aPwt1M8PHmMfVQKBgQCNrFYuRsJ3RV3Qj8xWYLGu4FKf/oIc0DSl6URC
dHXqH5X/TKq2pgYsXXfJwvrdZMJokVvypaaAxFyVTvrYlIee6+HsnrpwXHf25rNp
eSabk3BcTMAPKauJqRfR+kNVzEkwdVUvoZQuAI2djY/Oz/S8zFuyFiX7CDqlfIBA
11fFMQKBgEBlJNb5pEhu9tdULlOEroG0XeCcAKDfS0WULrbk1VCeRNOOXYdoiG2v
YImM6jUSIrHmZaMu7aaLYKDbC3xwd4ZyRRq4KjBYKHM6o4h+bZbxl3Eagjb0UQnr
vIsFw4+VWa5DOrdVtpoKBANUY0MSAfUPlBDBMGUuQ/q3X8GgxZ5B
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUBK/eOJ8iPyAfvjMt3GSSInfW8+owDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkzMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC6Z/5RC7RCEceZktvq4CJeAaGlKGJFpF3z/THIWoVjJ03N
KpDMprhq8N2HM1pM5I0HPDze0hDCRGpGh3wby3FmVAxb1vJyDTT/DLw5KYDBQaCY
TXwschPu3MYfSJIUXlJVWRC7di3xV6si3L1ALdfmK2des/YWCYP0qIjc1E8j/OVc
wD2PdyHR+p129SsO6WB8KIH/ocTw5YJisQBebUo4m495FhKLcKPiczUpRL4CmZUa
dFkrTWz1Vcr33f6fFybYaWI3lxHHYxOSB3MilDd8Au55tLhkpwpkaqPKWDP6b7au
WFuc3q8DegbYRLyq7qEudsG/u4afrHfI+vovHLVBAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQB/MflzZFEWhLZ/ZcHfmVkO
nTs74yALWjdld24er665E/tbRUScuGwpGJDhxoLE3JrsM8wIyqw/dOLqGscNprl2
u5MBRMwzbQncE1kZ9YNyT/1oC84Fee3IFni47hBUJK3o1zOuRlU9cMTj3dttBEG2
hByAv/ZP56H/dQN1/LIGoOHNSRhdzuY33rFYg6ZjV5mnFh4BHQ8jElA6lTiz2uBL
98RePraQx1ONCXyrjBV5o0G1Ra1UmRo/DBvkQu03eZXIyqSrZJKX1xM8345p9SjI
Ztpr9N0YFHRkMrj8SCiqYeRX0LdUW/D5e/gBf5j+dJzFiB6NHgyD6mKORQgxmIPY
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAumf+UQu0QhHHmZLb6uAiXgGhpShiRaRd8/0xyFqFYydNzSqQ
zKa4avDdhzNaTOSNBzw83tIQwkRqRod8G8txZlQMW9bycg00/wy8OSmAwUGgmE18
LHIT7tzGH0iSFF5SVVkQu3Yt8VerIty9QC3X5itnXrP2FgmD9KiI3NRPI/zlXMA9
j3ch0fqddvUrDulgfCiB/6HE8OWCYrEAXm1KOJuPeRYSi3Cj4nM1KUS+ApmVGnRZ
K01s9VXK993+nxcm2GliN5cRx2MTkgdzIpQ3fALuebS4ZKcKZGqjylgz+m+2rlhb
nN6vA3oG2ES8qu6hLnbBv7uGn6x3yPr6Lxy1QQIDAQABAoIBAGV238aLwWXJOcWN
W+mgcPSMnMlCjyNrUbzSkDuHkl2jckUAK2tKQM3tKBhEyp1aNq2+iz+aRocIKHUV
oGecuLBDhaqj+Lo+GB/QddADmFMZfuoIG1QyEEmPoMQ8g09U/Cn63hG8RUu+Nag3
UUhS69ccvxqciJH8Qfh1mHHjmuRyAMMsYlbiq2qJxcwPQQO8S+ieywfz5KtYKkLD
2Gwzvmit29r1APhp2jFaTIsrMkzY5nYc5+gp6K8+XZ3Bm2au50P/YnzBuXFDB6Tc
gDSPfaho5HawsHHyIop15fajn8dvJzzMTux4kdxXcsJcpasTyc1bW8v1VrcGgHcc
7yhogLUCgYEA6A6Nk8gfcrN7oTW47ECy+TfwiP47lCm3Mi+XrW6TdKL6fQ0mhfvv
WsvuHfmDH6b+yN+TZXQI49VTxJoIUbvNdKr+3i9rp+2vahib4+zEkos28ODei5fO
FJcZrjsM204kVpVz6j0HQRHE8SjAfUYO1jHLI4h0FyEFedF22nMlwSMCgYEAzaOl
HxZwiI1eUto2SdmT2TZZWE75uTn3ihk0wfJar//LG1uAxrqHN0g4KVMqgQN+IFJd
NZ2FPtIQ2E0P42lID2fGtpwDnMCAn/drpvhxDU5i2gNEZQ7LIpeZOLKC6NDQqb92
8ReuKdPQ3QmMJ9uWn9A4IPkS7c1WvkIrEkTgYEsCgYEA0gEhlOTduOK+9kR05rEi
hrFeJ8vTxSD/XhZ98IEKRtqbT4IQI968XPICuvOr+4AYQVc7v+uDhBPxrBEtiDIq
G/QHlLFbfux1+9DrexgxSOFdxh3qqG+oGzAnGGruFqWf8w9riEbUgsl+7jPQB07Y
bHVBfhWl4ayLlRO/uK/OMfsCgYEAvYLbkIvQh7eovrhFIcf3Xk2dByo5L/+A5m8W
VMqx0tLsbjjks8CBDmxq/YKcgCsk2EqvhdK2Uk+roHtcchq7gx8DXZToK1So9UNC
na0GGtordXlfVbbNdAK7/SleRYrzUgyWY9eL9RY0vQ+ob68J4Bw3LgP88tSy5UH7
iamaEoMCgYEAmuf1w3Sa8cunGBrzljwhr/5CjG3zDI1+fdFUePivoU5NocsKrLPp
KpkaBa2jcLXxf23NQBNNDWBqfsi9w28/5kl/gURT7ohOcf4YR+Ypnywpb8HI5mb4
XxOG7la3Y9Mhaw/iC/JWbDgb2JORQmfEGhTn89ggy7yu52brz6t/MNQ=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUDuk4yYHfeEkTr0RtsKoTAPWmWRYwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkzMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDjKy/CjxjtUi82UKxLzsR39LAoE9BUZwLlkvPrugeudoLq
EHlKTolTuvlFJAi1e5PKjJiHdKW2vSrpt9yBj56qw2xt7eJOQKxIE1kdeCdLoK1M
WaVWVekONJSlSqcHkW3NuBVtbAKJO+KIdTMMolYJlheQKBZp3JsSjLakDUQEoGyb
GT/+/xo3OZciBk1acmOBh9mJ///p8LO/oFZXZCXSau3+9K9vzcwS5J3HkDjkNVxb
AJny8gEe6ux0rXzkZLfG8WA7F0SVu+493kDHB4TO6o7UxAWatGVcyG+M3ujJ9iEg
0oeyoCghgpBSX02gM0alwW2cWNrkgisf0tyuJBRdAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAqtpdHxteYdjGDUaNuVzRN
1qmnmD8m+scvNpqYU5wQ4xawZVFyx6k9dl40BYeYvTcvSpBmNoy9fTpuTYVeeOae
glreJiKnulsbMRHwxDjCKvhoCge8ZTsX/0Atfkb+AHNMEN/QXS857ovSy8JoV71Y
S3ZGa01vG6AdHfpin+xHuDBh/B7bCHPBEwNc943PgAeQ09X0ZP/EFb31h2sK/eoR
jytU7Aw/NwCnSaA689xoTmtJp2p7INSTXJNO/rJeRKPxKNF3Jcg9Ngtci7CxkXzi
4+Hs2aSkIAYj05UcYdiLs4TNR2ZrPKA4/ZSZUCCDQAogOEUg+SOMGPkevqpojYvf
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA4ysvwo8Y7VIvNlCsS87Ed/SwKBPQVGcC5ZLz67oHrnaC6hB5
Sk6JU7r5RSQItXuTyoyYh3Sltr0q6bfcgY+eqsNsbe3iTkCsSBNZHXgnS6CtTFml
VlXpDjSUpUqnB5FtzbgVbWwCiTviiHUzDKJWCZYXkCgWadybEoy2pA1EBKBsmxk/
/v8aNzmXIgZNWnJjgYfZif//6fCzv6BWV2Ql0mrt/vSvb83MEuSdx5A45DVcWwCZ
8vIBHursdK185GS3xvFgOxdElbvuPd5AxweEzuqO1MQFmrRlXMhvjN7oyfYhINKH
sqAoIYKQUl9NoDNGpcFtnFja5IIrH9LcriQUXQIDAQABAoIBAQCXviRUAQQ0mp5A
2NiOdtqUClWVH88cYgb0VRosTwKMjktakJCEizt+O7oAblaG67pIJWxJpyh+jZPZ
tOBNhyMEjC+kqq9teBPcvVfcsIMHKJg6FPO1XQOlYogcdWZnTsSbEyj1A54aD299
mVP1T4bLNoAc4jo+kobfeDEUGmxh7Yj3LICr+D9yPzqKsNJAzbWILhtYzR/hNqb2
JGBdDXu0usls/oSjNUYTAmtATQjVs5TbL7Ver+bdfDYaScBR8GqfavCTOrjGUaU/
26yPpPKpycxL4biULej6SwmQm8AXaftb68+TaZ767DpxY5/3goqBfjKlu20WQyj/
pTfxaasdAoGBAPdhtDkFddD12+tsm4F17RHAp7ODZ5w0Wd7/DuyRPbpq74fXCYuA
5VSj1SPE4t5tAqUn9Vo7zgxBoZIdeHWBAIdunQw4bst11PD0uckzE5oMDxj+lT6B
7XFZXXJgcRtYI8c2na9/ISf9I4WtE8Y422xPZl/U/FV1+k2sKuOLm6r3AoGBAOsV
NiDuMqR1/IopAkdZIeMMiunaLCdwkfJ12TQzG4hGDxE5Nfog90cEoJO4F6d9IZcG
qtmlLiJjLYILX5vvthoQ2STVxLxSWVcWdbhYth8PTBm6waAfJH/00lmZtI0bHxlu
eK6jr3QK7Rm8PFKP3xbnKr6BkTeL5aOfs139EXJLAoGBAL0MMnD9BjspF+ZCulfl
6cSOSNo7iltp+mAa5KnOmLC0ddaGc6njV94l0YUjOgimn8Xc0nghieX95d5GnT6W
1fOpiWTEX48mvhNhwfTLDqjDnGoKa704B19+3pXAs88kvTrJNxndelYX8iR+zsTF
wJF14BNOLYOVxDHFZ4U6tDyjAoGAWGfjsUKi3OJaFIMTjk1gxwgCfatEi5hz6mCT
TGQj6H2gUPPY7rXTCGwfDy5eBuix5x/kxHCwBtKRXKR2Uig1rVvErWuOztuRKYUS
xD7oTonsLojjJBpSGaSyLmv1UFNwwJmg3NxFsTgirljxvoLIfM52bqo/OEpuE7iN
Nb1kAD0CgYBb60T8GmoWRS4rS20J8KMs2Cmk0XmJHHNlSweYwO1fNFXXUwYG+bWj
ZNdOc5eLtNBi8at5vbK+c5fq+IRfgYZbdbFMqZwq366kUc5+BnCphdKOb4M9M60t
PtpalMa4s+J0SM3snolKUz45Lnz2KXVu3vy+rXScdo5+RJCNsD/xxg==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_HARVESTER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUF+41lzP8r7pBiPCZFG7cMvOPcnowDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkzMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC2wkXkBcUaOlajfjIsrbJPbKnSspyB9PbJ2nT/Nga/za94
79C2tTntMhbh40hT6E00HHxmwDOpzEEH+C+vkmhR3zkTFmP9uV2jSyylwBwWnTru
9io58MA/G25FMYH7a/3lKYspeh/mSKWqhV2xN07Mov9JbNAUVT13oHvUMlmhxaoX
pTKehNH6u3dm8ovYlZyimVRbu8d88Ke5atjV613Ci1zV63b/Vt5YmWR3bAw6h10W
UMSrh5pDEXuKplS9dTYOwfkVLhIinFSbyw66k9X1qNZIF2M10rvW8FsZxwtHbdAI
ArD4kB7FrsoezBW2+Drap4aeHD1cMOYZPh9XnW05AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAs7LdVyhNjP4DiXaKCy9De
7skX66TzJiwBBQ+fXjvAcOZCmn6lrje5ZA1pEE2e26huygXcADPntZJWgaV8uQ0M
SXml0t5eSbDFlxOOOVTk7bRyt3+Wj3kz4N0P9ehLKtemKd7A0kYrgcFhylQrEHFq
Ijo8uEhv77AzhJfNHDbqw+qax3rvOG2b1H+7yyn6u6kdiOVbGUd1ChIh1zTFFYrT
WJbF+67bEFy/AEUYFdK53x6M94NWoBKqkIrgvbjf6G+++6IiL+PpaR0j3Dnu86ea
anXRdbkhy36143Kk8GUy/Vx0e0L+aAbLDwobngzvMYactqDo7pqcDaORLSLKiQT5
-----END CERTIFICATE-----
"""

SSL_TEST_HARVESTER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAtsJF5AXFGjpWo34yLK2yT2yp0rKcgfT2ydp0/zYGv82veO/Q
trU57TIW4eNIU+hNNBx8ZsAzqcxBB/gvr5JoUd85ExZj/bldo0sspcAcFp067vYq
OfDAPxtuRTGB+2v95SmLKXof5kilqoVdsTdOzKL/SWzQFFU9d6B71DJZocWqF6Uy
noTR+rt3ZvKL2JWcoplUW7vHfPCnuWrY1etdwotc1et2/1beWJlkd2wMOoddFlDE
q4eaQxF7iqZUvXU2DsH5FS4SIpxUm8sOupPV9ajWSBdjNdK71vBbGccLR23QCAKw
+JAexa7KHswVtvg62qeGnhw9XDDmGT4fV51tOQIDAQABAoIBAGS74kAT+hdBzp1h
IpDD0MO8dkJ/Voq/FgQemFxPUBsKaUy0iosaiuo1sK0jVKuDIIK3rM4J5LATuEiH
QOl6PmvaKSBfOBASyw0Fk39sy06frWsnXhD/pUdjfD1BU47ccF6OrnjXKpwIsN+z
kPfsL0/WC/ZRtsNuVGoKmBZXBlaGqXqJyuK4ZUpY/qkhgmc16BZyUpYbe2dAjaEo
PoVri1pWGCnrOxOiBakwDAh4NQ340WKROIZi1/Z6q+oTEDBiPh17TVt6IBvL4IOl
fAXHocnksr4GatfiGEPnLkIeIo6OLNQ+bln11Qhpemmyr12eRbdpjBGcV/Pupp8q
fqrrWYECgYEA3e6LmnMqGHNg3HMUj3nUY1K5aRtTo2O/SsCH7hUXf43EXG6cSgo0
W87cs3e5FgXmxId62CQsZF9jLYtvjN23TQMbqQnbSeUJH+gElRLowyD3x2jD9u2Q
+bG3QlJIFGjxvfVd24+Zj9OvWRNdk/pzbqHq/zFCwdTNB5P3E+qWCukCgYEA0tBQ
Ozw4HowUMJdwSLDgJFNAkeAsX6MnXUk9EIr+vP2fusKxKLpHBP/Ojk/X1MaBQyE3
4q5EkL253iHOJ6+IoKQANgtBlADpScg08rfzBdY53bvZBN48wQTDCsfRtMdj7g3j
ALVLd2+zmx5KCYMab2nyLGSTgnU43KwXdRE9PdECgYAZptPeA0evUc61TFvpBYTm
Ag7KNk1hikr3Ae/0Nd3kcWdr46EO8cUBg5SA7eqnwADfYGVzjCLRazEUd5RqLMpe
DWjqDeiZzu5SEMhOzsO2oh3hn5te9DCYm9D5ynboXQTsFutFUIDIXghbfGCJlR44
gGCgJHp52vXj1VdupuO22QKBgBqI3+Bk1wd5SD1JgneT09Keq/zwg4VSKu1B/66q
YB/3qHhAcz4WHERT0nL1N8xvY+vILZmZp8W0K8X66VDzdjYKDoC+7/UqHDMOQSPf
5XXxnfz73PgQ5QLCj642sn2Xr0tSciUvrJ0O8UNwD4+c8eHeKv5NdoewK4UTICy7
C8NRAoGALmB7np+s+wCZCpA+cTkgZpzbqnwfRnqCrBx7Yj+ZVAa5CDZWqztwmSkY
u8Y5q/qsPB5Fbno7rVAWuyk/smrDLVi0w6trv6RaOS4dhhKGSOhsAK2jXka6OztX
y7mCud9RuNytEuuLjWQFt5syjyrmVtI55TxHrF9Q9ylQAdvL9DU=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUaTJzz6JzsH2ZddKgtyDaLvK0+fgwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkzMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCcusqOeHXjSZtVYgT32PKxIjsW/TPBlv/ovjQpFIkBZTCC
Rp+O0BNUJ13Kv9MVyyprKlR3EMldjIxolACVS+UIieuIERjufyMQVBuqJg+qr80l
rbBwcKmzB496Lopi4DpX3W3kqaXd1c65RNCAhiQ50ZfEvFwLIhRzxC/ZofRW/iFX
0B2x+LE7TZ8uEXhtzVPc9GYVnEk/I2hN426pX59WmF/+xQ+HKguzCCBQ/7V6TiS8
1dLw4z5aIKedBgvlX8ibDkCUp6jOOfUTh12Xx6nHd3TX9qhL5h9zDfWbdoBdr3PU
tYEgNXrYVq75HTlHoSRCuG4SccoVCwNzdKyjJ4mDAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAKaLVA7Ogf7S4gIwv/3K88
PGJxIhTcgMSyCVdKnPLWRUEofdZVMZEDcVI+l+4iB8sJ0XOs7fZp+bAnaQfgXzE2
wyWAODuytYlYZYc42xlT0PhqNnRKLUKf6uLCtNZFgpmiVmqgvAkzk/SJXTPw2F7q
hFA8K70Z6Wh08rZCP3hXLk5A8h6ejcNBHAoOg7B8Z9AMPlHW474xoGUrLjl01H4S
6C2/7D/URCQFBTrLt4sIvtxe+cAtggB4DVpJk7eoxk7JL4CsRu8flqGLn1wFraqr
jIb+X70mOXY7cO1R0n0uJLgHTU1dDkMlV3xOVfqhE+pe7caknwI0Nfzvlar491Ct
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAnLrKjnh140mbVWIE99jysSI7Fv0zwZb/6L40KRSJAWUwgkaf
jtATVCddyr/TFcsqaypUdxDJXYyMaJQAlUvlCInriBEY7n8jEFQbqiYPqq/NJa2w
cHCpswePei6KYuA6V91t5Kml3dXOuUTQgIYkOdGXxLxcCyIUc8Qv2aH0Vv4hV9Ad
sfixO02fLhF4bc1T3PRmFZxJPyNoTeNuqV+fVphf/sUPhyoLswggUP+1ek4kvNXS
8OM+WiCnnQYL5V/Imw5AlKeozjn1E4ddl8epx3d01/aoS+Yfcw31m3aAXa9z1LWB
IDV62Fau+R05R6EkQrhuEnHKFQsDc3SsoyeJgwIDAQABAoIBACKhf3plkZ7sN79x
Din5rP6I0sesoRAInnk99eaR3AgL5OEUW9NBlNPGcwoGwsyQ/Ml7K/i3I9dg4/GD
qnFSuMPfPcTuCjVAsG2+N/KrwFB10f2eWFsv+b9OT1yvBfL9GscpbUvWVIkk4i27
z9pmSYDhGAjnmer3188QrYYILCZAXnYmTQrqvHAOJEpxf7/4z2rcSVbVdez/58He
xjloGfKSWfITpPLhpcM0Fh4cpx9fUJHgK0rV6CcL369XXHiJZ/OtEY6n57jqfEZd
SQMUCAbxyZnb5Trl73ucBdcAkELjyURstlEBXuMQ65/USAZd1ndObjt25hYRBVTy
SBf6VnECgYEAyVvg3xBZduR8ioxnflQoyQmrgWBN3BNVNIypmMicF1fsaHVAXXB2
gk7RjSKLNCzEZGkqcIOfw7nmC/aRdb6K6xOxeA2jC76ZP65dRqczOzDR7sDtW7CH
3zrMGMtvvjxzhtA7JhWtmDBmVzC8M3JeXiaVKuAjtEfKqwdB34RXfBkCgYEAx0KU
1ZCsIHY0BScRg/udckakILTVI76uGkQ/lEnEcbnTt2SB1NE7ityEVhTlcqWoKLbL
6N7X6BLENAifVgi+wj/n/v/OURCmQZZIWSgJNpV7q2XEURnRgcLqznUU95A8S1hq
QVeCABmzzNFX9NUsxG2MXkybqmgPBAtmEVYjZfsCgYACh1PYmUT2WEI0HzVBgd8N
P0DXHBV+OQPt6AJNN9+171W5rhdD1SC33DOHeTKUUieZNzTgOtbrx07bQZpsBxuJ
fjLRViKBCEC2awMi2wCqsp9AR03zw9DA/eUIPq3Fjs7Il57WiJkoexsd5y/F2Z7T
wdpHso7gObKS2UF7hBbxKQKBgEFRPw6e5P2jIbxKqUA1e9AY/fZGsNONzu6HTrwi
TkXlX1RvmuuTRsxnKu443Vnumaf2+/KzEd1eQXi5FtoR9c4hOsBpRE1ogsdfJwoq
yJJe//IYYvke2IGLzoKs+JmKa2lba0FOGSxFQJ40RXvZYVpmeqvyuthqUfnGbsfi
D6p/AoGAVQyoyJ3bgy2xWInoq49Dc99uo4bLmn4blaENuIUrEDV1p2JTd41jRLGx
pcv80SfZZtMa5YclBoezEhv8mrtBtnxNnNJ1UkDPmGagG88+avl/8FiBNtB+rZru
9Kh/jDmFddfY831nOdwgCMEZB/x9qCmyRTtzE35sKNZoAY2AVfs=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUaXeigR1NhYcViVNvWOSNgb1hguMwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkzMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDlm9CbdDwaD7gUkwY+Y2by3np+QtBFoJtk4hcbdAQ4Vd27
7sJGve+iYg4vCCg3fdpxKZrM7p8VlRlQOMu2+Nkel726yhvs9hALWx0UVppk4iKV
rj/dzd/Oiwaf/Tk3DwMnfiv4RyUU1YnVusUnche1KKHfwHGCzLAnlu286wQXruug
Xl6onBQiF3rDqkLVrHcqMiasCJHLS2S9xktDiKwNCphATHFuZtzUIZeJK+yNiF+M
JKXN1xQFq8k9kb2q8y8qAgf1dY3wW9Xj4iP1Qo9Bzx1CxJTLpezIk3QTcCWKUkE+
2/4Nly+M5GoJDv59gzjvPmyWPTr6TZ3lrls/Z/rjAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBQBbv4tGvdNY+P2A62GfhR
cyNDjXUKk+YHY64hGeiXp61l8e2Hf58lV9lgBoMpniXUvMk9Nx0g+d1Gsoc9VWHs
LP1MhVaf0zodeK45jJxuzCC+eDHSNmvhkUJEVD8LDgmHTJlddpwYBwKocyr4m3XX
2QMcgiKcYaqIt5MLFwCWuarQ6bXKT88qRVTxKTA4FoqXXqJKCbAsEMql1h+dvXeV
yTwPK3vuRrZxyiIYlILG/tgNS6P+qUwLCnYjoPX2Ml3djMkUhRBdsTWR8wWTYkb0
qmqKNsNL7+OHzUI+Z8WBoja8MHVZohl0iDAvFO7Y67ovldeYS8mlb0Tv3nVRUhiM
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA5ZvQm3Q8Gg+4FJMGPmNm8t56fkLQRaCbZOIXG3QEOFXdu+7C
Rr3vomIOLwgoN33acSmazO6fFZUZUDjLtvjZHpe9usob7PYQC1sdFFaaZOIila4/
3c3fzosGn/05Nw8DJ34r+EclFNWJ1brFJ3IXtSih38BxgsywJ5btvOsEF67roF5e
qJwUIhd6w6pC1ax3KjImrAiRy0tkvcZLQ4isDQqYQExxbmbc1CGXiSvsjYhfjCSl
zdcUBavJPZG9qvMvKgIH9XWN8FvV4+Ij9UKPQc8dQsSUy6XsyJN0E3AlilJBPtv+
DZcvjORqCQ7+fYM47z5slj06+k2d5a5bP2f64wIDAQABAoIBAQDd6juzk6LnGVwz
3mnBcLc2ctp3H8JGGVU3KuFkcjwF6s+U7M0uLDLogdbtk/eyslum1aw890AgTuuZ
Qlt564eFbuk8GEznOGcHYrd3ScCNUpZUjoZBrNHrwSjVBpv+3+6Pg/2hR7nKKhy+
ynX0iuvo9m2FYW0UGxsCGHiMB6T78QoxeHczwLq2c8isG9cW4xsXvFOls/5du6a2
+wHP0qMAk6BRJ2XNlEw5bHXcV9yTdLK+HhSyNDtzUGTQuj0BPAHKl31M72JsHpYn
ofiIem0+P1XWj/pvPAofNp545vmjfhlVTkkjEjwXZbSujBQRhZ5JRshR9T3nlB5a
+WKBHVJhAoGBAPVvqmMPbW2oOIg4drBwgTIXIgBvMtUvIMI2fDqyMm+aQXfKowty
17Q470D2RHZ4CKm4KtGxP7zoPnsJ39XHXTrr2gono3t+mghwkYuroFNXOs0y1P3U
Y2BH++6rGpLv8yxMPaJo+1mVjXSIzeJSlGgKGaoy/+9qbcpf3NcUv1BxAoGBAO99
wPlQYHgrp9C0KDjh8OWXiI9HdCTBZ+qE7AuiM2HGoF4WSe+BvpeBWQTzPcEPB/sK
nHW8GQ6u1TPpJamuvdg/hnLOmx7sPwsD98FkocMmbeaf/vnlSwXNZEdbypRNeggy
5utbfYf2520dmn73dMGEZSXfgj7ldJgouptBHmqTAoGAGcT0rdvz0FymOt86zwGw
/vJg1ozWWH3PQbT4zCzjkMYwc4RqJAyVy01jCX4R6CJoPnGgxU2H9Kypyr9Zqhd5
mXMj/Ib26kN7psEy9ug5OCbjfKIGrPP8zyIfuIpsitr4vEDxA7lkEp7aME8g1s92
14mf8jfSmW+iQWpZRJfgEnECgYBIdu6LAY0PD3aJqdl5zLPNZJqHcAFula7RwUKD
CqMtdKJVlbztYX6/7P14h/kpj1jE1yMcZLvYO4J7YJJq01rSMfaGiolZQ/aXaK3w
sHhZyij63XKTPpQCv3EWPmn/kanZDT3d/SLwnv7Lf2ed/1Yur9bDLOwGB/vNhpVg
IMYJTQKBgHp287GYTmfEIYQt8TwpFdIiehOc51bV62iD5ittj8oh98s+1+TxVvED
rpkuO0w2IV/CCMPagmh+5zHVeEjr87w2qTEzukw/uhsyqDDlwgStxv5mqGTHPBDQ
EDnFBXhZeOJsVFQFZ89HQ8hR4EyvkDRIW7X5oX54VxizlNpfpb4H
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_CRAWLER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUdCBu6ITWB8mIr3CFYUGSoidgl9IwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkzMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC6CqdPjfQSDqwE+0QwTkW3Gq2z+SdyOkCbA1f65tpk9dzN
yLx2xtHRV433IUFRxY4slpeO/ff/yWI11e8aubv1TJt1Df2XJWsrTSpasHiB0cQu
sBIUPCw0KkvNsZ93UVRArKyiNIut3tFTvM54hzUsSpMnH3gUiF2osJP/qFi9Fm4w
nHhhvjnm98YZ73r9qmS7x1pRLkduOLauQrZeMGtfqPbrDn+zrXISJz/WlVs1RFtj
S//fsuWYX1mecsowyj2uPgCiWxd4uYcnYEmv8o1+3yMucR6dWQCQxxLFaN4vgksz
vxQRQ+GzLYBG4rGXaJhuTd7zNX4MAvFC7dZF4Ey/AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCWFqbiMrpwtfPP9S5YKnFw
kv6aDeUeq6GYfoBdKYnVpfaXQgPXzc8eiNXptAPuMIVoSn811Hg+p9SsEjKBjPlZ
jdbbl44S2owhrJ7N4H5qTSoryBvuTwlh+aQDsDh+x5uO7PQzb2F3yU2cM2MvtU+2
4pYr0Pucs2A0XzqWp+cZLhWHcTOm391Ab+Vr+Q/ZguvOxbmsBCs+qwSlPaktd9Yw
AqNKFau9hAnb++jd3k08EN8GBVlQBP/njdEoWEGjHD2SnTo2z1sv5jF+t9E28Swm
QbkNYNrgryTYJzPDZMMrK6DkkEFnH0djbKjwAdkooHr0pa9COcuYMhsqNMZ8irgY
-----END CERTIFICATE-----
"""

SSL_TEST_CRAWLER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAugqnT430Eg6sBPtEME5Ftxqts/kncjpAmwNX+ubaZPXczci8
dsbR0VeN9yFBUcWOLJaXjv33/8liNdXvGrm79UybdQ39lyVrK00qWrB4gdHELrAS
FDwsNCpLzbGfd1FUQKysojSLrd7RU7zOeIc1LEqTJx94FIhdqLCT/6hYvRZuMJx4
Yb455vfGGe96/apku8daUS5Hbji2rkK2XjBrX6j26w5/s61yEic/1pVbNURbY0v/
37LlmF9ZnnLKMMo9rj4AolsXeLmHJ2BJr/KNft8jLnEenVkAkMcSxWjeL4JLM78U
EUPhsy2ARuKxl2iYbk3e8zV+DALxQu3WReBMvwIDAQABAoIBAFXwie1EA9U7ldcP
QyaVYbr9xfP3SnOH2URCPSgX8BbnREKDUhwEJ/RuX5QjdosRmWWbgxN42lD8dDOu
Sa+s0Ni1tLJT7iseC+2Kzd/q2SAPCHMQvqk+SqUmTLIONT3nAeaGXZDoeQWugkAO
XcprmvKE2IkgDlZdz/YW66cT2zotEggMAubtRTRZy5k9UwhZkHCB98dbCrLKDS2T
TECySx4OnhTbvVheIjXLZSHAI4KDyOfnkb4yYiiOYNnXaGMMqXJ6ITc4L055W+Sg
aqPXxifgK04cuceyciQH74HxWypFQMJX1HyOJ9qz5dF8FsJO8vw+USEcsMQvkaSi
+/iT02ECgYEA7cLr2c2vtAzEz/KqFH1ll5LALSmFlDfIr/s7ljDEmrgMMuJc8gQ5
2UPiZhd5DMUBD1yncAd+O8QjoC/GBecsoAfeRYwowCO1VFZ+EdbL4X5NwdL4HwLe
KNiR3EzfWpEZPO8FAKHJdyoZhogV2aj8Wd1JgcW8xrIQHZIImeRg3scCgYEAyFAT
h+h2zWk76JTAvSDLWSRXBDdYuMc3dINu0Nv3pY86Kpxjq8nFdsdsP4gIoHleG5M6
3RWljKFxALckNzgRoRt18GqX9k0c3svXWY1UhVgI+TFTwjm5JgkzIvAzWqB0BeZ8
scxNyAkn/sYBa+SQw4l66Cq7uS/4OS3sC90LCkkCgYEAtsm0KK5I9lMavAQDXd1J
zU21EQNq/pgkYab0GHNFsuzr8/KzIhy9nJrj4zkIhxitx/GjiC06jxgri2svAjrH
xABIkY8/hPfu3/fe1DgeZi2D+g8HUlASG7Tj7knrLOWAUagwYFwBVuu21AarRbr0
xuGpMWujxd3/JbyvgCBjmOECgYA4LNS9WYDvrCJj4EuI/ohocFuC0C6uaxfvMejC
4904bclHJ+J/y67314dQ7cpVjpPIsephE/AAV0oEhFfAsJWpE7VofcwuA4QkKxAy
igL4/i5OC/pMTrnQo+XWV3xfXv4KpY+0oPHzNjYkKc0+P7QlUgnI0CsjDQPUrT80
OIIfGQKBgGSf00zTS9KDIHKtWkZi4qdMmUDiIoxlZ27eZelfF7XMNxm+eP5gtGPZ
Hq0JKSswlMQZE+KWakyaVh6OnGRdGLM2yuU4tYjU5ZgJ/O5BuZykCFLb4OPq7Uos
Wx8tJU4lx2r0q+TFzVwMv92K/p0sIGvHVfTn9/xNwtZAI561vEcu
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_DAEMON_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUJWB6PMvY6/sycKKe2rKlyk2Jhx0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkzMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDpNyGq9RLF09KE+uiFLgNAWUXiUWRDWS86+S+knZMa40Pi
iDdpxcRxNgxUVioleNfKIuXQp1eKCwCuAv8js9hRqOIkEfZHtiNaai4iJWYKD8v6
/Mh1iTQ8evvsxR9Edlr2vpf86uWcIZ6NfD2R0QuDNi/rEQimilQr9O0zgpVcZ/rX
lu/ApUkBZP7nRXSgFDwyxub9eGO/XXYCFiaznFEewdEwMxJ7mekMejT+47QZj1PJ
JLII1sgGUMOnwauUqub4L3ibcFtWVI948ckq/vaYsX/MVYZ+Vr8sDpcuAZC+2FuZ
Wj8cjoFXGG2uHbXilw/+9uHiIpH9jE7sQLz7RUOjAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCCivAYNk17t6dwt0l3GmiO
eEQp2nXF7hkt3Nws4+GefOrcCzyTAoinwGzoSJpuv6YdIp8txyylWeEVVrvJRXyg
3m648yIgnp3U5fSD6a2V7GnCSOjCoT1dlcIMFPuOk/XKN/0acfAEsJGscS0y/mVQ
MiJjjNv3K+ZzY8nDu+UxdC+cqLaY3KFF9QarWNjyiDjRi+7NrJN6mdGtZITSND1w
3RXLCSaaB5VTHqkSTGNrSMr8Y5CGgXyPq9sQMLS2Hfb8K/Y57xlnuJJEkHo09pUF
mz79hUFHqgjrtxAd4UoBUujTpwBN1on/KFrYa7fGwmisb1V35Qjjogs8AGD8tnh7
-----END CERTIFICATE-----
"""

SSL_TEST_DAEMON_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA6TchqvUSxdPShProhS4DQFlF4lFkQ1kvOvkvpJ2TGuND4og3
acXEcTYMVFYqJXjXyiLl0KdXigsArgL/I7PYUajiJBH2R7YjWmouIiVmCg/L+vzI
dYk0PHr77MUfRHZa9r6X/OrlnCGejXw9kdELgzYv6xEIpopUK/TtM4KVXGf615bv
wKVJAWT+50V0oBQ8Msbm/Xhjv112AhYms5xRHsHRMDMSe5npDHo0/uO0GY9TySSy
CNbIBlDDp8GrlKrm+C94m3BbVlSPePHJKv72mLF/zFWGfla/LA6XLgGQvthbmVo/
HI6BVxhtrh214pcP/vbh4iKR/YxO7EC8+0VDowIDAQABAoIBAAPMBP1OjiawYy4N
E7oPXLgwe+XKY3KBQjaYlgD9G8cFSjam9xf+w0sAkUTSPk9r3z+IP+ucvd0efr1W
iSbgp7X0pPHnZPYX7g1ryyJ9L2McjLqiYPUg7bvKWM2rC+5Gawa3ZawVevWGypkN
G8eC+sgBGtid52EmwWYRz8bV6m6drs+JJ0wY6TBMggL5z7aOBgVmMhJosdTxBlg2
mUMYVGXFkwhoOtTvQP4C4jTJ7cgLAqXvfnKiT1LAWrt8uQLeplyHCvabAP2yyM45
YpkTMwtlidK5dJ4qL1TFRCaHrQzRcgg41GDB/BR6MOLo4QNyh1RcKxISCM/5pheE
Hry6x1ECgYEA+ZoZ5eAuAwku/073VtL+nmiL5yslEynJVf3WoW7BZbwjBdE1cyPL
kiFT47Pw+RYB1Z5OWhPKzzeWrH11I2FP1IwuahPbCrM04Z4VvjYrXj6GsX4CXLyT
9zyyGq4WQh1eW+MwZk9zrTgL2H70Wkybl6cdmDssXKV3Sy5s1rc1g9kCgYEA7zGA
MpqZCL0FsvFcG1Bi+VcDtBmjocQokeyCWHn5/dXKgfVcVeLxJW4ts/sFTtB/prpH
QZ0Na/Tzy93kw8y/yPZYCCLSl7n4c0+oQv0IWZa6d96xXxx/9n27wWg1TghJFxBo
kDPyFIzeq3kdYUQJrd+G493hH4Iyv82cp+viodsCgYEAuObsinsg+sTB2QYBeoNB
dc3S3gP7KhAJgzdQ2TP39sqBU1zg8JOyyWUBBSyWtZ8U6s+kEVyaIBl49/zUWspK
3hSeiZx95pZM9Vorl0X/qIg/NZs4WsSkBEIlWlheSsoAzacmgpQXCFn9hHq/v2kC
1jxJUy16toMpNTuGCyWbcjkCgYByAdENzZwlixrdSKdTKYSTPcM5I4NXxkxkCSuz
iif6sdz9BnrFQQ8ZfSNxhrLn9v7w9BakknvkOfO99vxjywKagbhB4H8p7G0cYRpd
G4fQU8R6//zgzY+8Z/+G1umZUN+ti5ebK/c1jlNPvcGgK7LFWiZME+SKhR81RoZl
j0wNQwKBgQD5QzQkxZmprgcoMfpg9KQKnAnEjRT09v0JygBCSkc9lyjU16xL32hS
miOy+/MGYilWacKiqkky+AvjnjHRtE9lSmvxaLLkuObFuMwPyELDOsQkkKEofztG
HI0r3T+jYkXCDt33mW9uE84DlJf0n5QQbpEJNsfumB6ODTh/rLl0MA==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_INTRODUCER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUIOpxHZYryCoSWIfdQ8uCSoeS3KkwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkzMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC/LMgHvqhwBTGYi8fLSDC5BAMvpZlHojkCtD2tAe8x4xES
ziFbEN0h3majAaFEbKWf38QwZb8+MTqtqC3hBXLlmQMOHJ98B+pcJiquWmDFadWm
mRv/aSsDcN8Nuil07mTYVl4KjqJ3BIuBgBF6VHU5EtALFPwM/xnFONPB5BC4Gm6X
/Bb9QQ4lBZVbXvuaHoiY/qXZeM/M0J4jGjgW3CvFKx6Cg3QrSPTZQRo7YoFOJzCe
WEU1NjaY32vstiK7qTFJCZ+Vfk3NNU0QealoqUdd7SeTNgPwEpYlTLalyKJHGPAU
yeq2LHmUX9F81MZIdk3Y2ugwonIjdAgo2d1Bft1nAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQC1ACGsaR3WXsh2iMZEtbFU
JDbmDgviv1WCft7Lt0lpTWCNq24PXn5EOFU2UPBcsLCjoMfgvjj+b4dVcGt7mX91
dtMIwEORe9stfr1Y1Frql9nMgk8PyRYDt4oUUUwwZ/MjqU3ZiP4znsiZuEGTAdKb
BqhVubSZdYOIrYV5Chbta7/OXxXpOv458CWLKqvfoDVsWldhQDWOkeh6nz8dkPO3
Jt0IRUPqS7TV2fUcbHLpO3z1xUxL83xN3wgoBafSSbvVcLAN1+//+1JqLPxznSjV
rYf9ERqDwJpIGysbRvIyu+ahf0zJwBwob/O6+1vuryLQ2SdMFIlk57U6JOkePfEy
-----END CERTIFICATE-----
"""

SSL_TEST_INTRODUCER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAvyzIB76ocAUxmIvHy0gwuQQDL6WZR6I5ArQ9rQHvMeMREs4h
WxDdId5mowGhRGyln9/EMGW/PjE6ragt4QVy5ZkDDhyffAfqXCYqrlpgxWnVppkb
/2krA3DfDbopdO5k2FZeCo6idwSLgYARelR1ORLQCxT8DP8ZxTjTweQQuBpul/wW
/UEOJQWVW177mh6ImP6l2XjPzNCeIxo4FtwrxSsegoN0K0j02UEaO2KBTicwnlhF
NTY2mN9r7LYiu6kxSQmflX5NzTVNEHmpaKlHXe0nkzYD8BKWJUy2pciiRxjwFMnq
tix5lF/RfNTGSHZN2NroMKJyI3QIKNndQX7dZwIDAQABAoIBAQCoMQPDHJAgDdG2
fbPHOrny7H7JGo4iIay6nkxsu3jvkO/idYuPDOUf+QSfgL2a72M/pqR6V+nLE5Cm
W4IRqLOPH/E6JyCBBI3BiKqgPk9JH3WiXq3tJV98ZX84GoKCp4H9eu69pwN0ZoE9
66h00X1YOx7hwRKHdJ/9jaNvv/CdpsyNHsqK86HyI80WbdN/y0ib2CpWvDD0hMqz
x2svsUE7FPSpqqMVyXR9OH1gZ7xPDf9fO4/wFlK6BaGcbcq9/nLG5gsWMGGrH7i2
yPGn5K80yzNW4b23SHVVcwKQY2+Q6bOu4t68Vvft+m1kMe8IkyEGyNNcksRjb9FO
L3RBSVTxAoGBAPMJ6dqGMBPeqkfk6QgAPTwVtJQerPO3O3hdTha8VTRY5k70xQOI
hC6fusAnuy//ZtqYS/U2rScEa3rpJk3UjVZ/fRzkSUK898MwHNiDNsFZrspDS/Yl
wYk0vRMgz7+cG/VfG2N8DV8BngxIBNa0X3C8A3vT/MsHVxYlsbGuZZVjAoGBAMle
zBzczZe1W2vkrvhTsIK6kovsMXBU9bz6VKMusZ8lWATrXkjaDYSCla0OT9IATfOX
w43KmG2t3Z+TXcm3CU9UpAZRkpFErd7hxGGApAP0TWOHG3NK3KiI137G4RHRoxE1
eHpImN1MJFl0SgMMyOrVIvbfvb1jgcYcH7t4imktAoGBAO82LbeJZh7Yha+XronS
enL+RiuX+dEz41P4OlkEa7THX4ANSTDOGJQvYUeqk4KNlrXHOtQTSeBiaEuk2a+3
apndh859H2KRzieO3oV4uNccJ38rN8QBq3kZsJP4MqK8y4P6ZWHJAvwlAmPCKwkM
pfe3BpLFt0Y6ZkwFM93X8mJTAoGAfjklyJG/bXEItUDLTG1pHwjEA2EyPC+FOcfQ
ddk3DYLjAXJnz1KfVohkOe3WqtP2CNMAiUiM83MgkH5XM7G/7DIp/qvzK4vZUPRD
nLp+FNx2BgUSd9pdJmdgbN9NBVZa2NajhkMrTswDnO7/1ZmV911SZV0qGiTdm8jV
OzX7zKECgYA7XzxqMEiTeyWnKbewk+QomhddzPpQ8JKTBVTSCY+LVsBaRNSLqloX
0jSpEfr1Zd8WocUYdheV+DEPC0XbUtdZhC33QYviEbnZ+DKZ+h5fxNVPf8MRBY13
xDGazUAN3pGUwMzKB9MhLCAQl/iiJUEid1nxIzgvV3uQkeqjxJkffQ==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_PRIVATE_CA_CERT_AND_KEY_7: Tuple[bytes, bytes] = (SSL_TEST_PRIVATE_CA_CRT, SSL_TEST_PRIVATE_CA_KEY)

SSL_TEST_NODE_CERTS_AND_KEYS_7: Dict[str, Dict[str, Dict[str, bytes]]] = {
    "full_node": {
        "private": {"crt": SSL_TEST_FULLNODE_PRIVATE_CRT, "key": SSL_TEST_FULLNODE_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FULLNODE_PUBLIC_CRT, "key": SSL_TEST_FULLNODE_PUBLIC_KEY},
    },
    "wallet": {
        "private": {"crt": SSL_TEST_WALLET_PRIVATE_CRT, "key": SSL_TEST_WALLET_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_WALLET_PUBLIC_CRT, "key": SSL_TEST_WALLET_PUBLIC_KEY},
    },
    "farmer": {
        "private": {"crt": SSL_TEST_FARMER_PRIVATE_CRT, "key": SSL_TEST_FARMER_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FARMER_PUBLIC_CRT, "key": SSL_TEST_FARMER_PUBLIC_KEY},
    },
    "harvester": {
        "private": {"crt": SSL_TEST_HARVESTER_PRIVATE_CRT, "key": SSL_TEST_HARVESTER_PRIVATE_KEY},
    },
    "timelord": {
        "private": {"crt": SSL_TEST_TIMELORD_PRIVATE_CRT, "key": SSL_TEST_TIMELORD_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_TIMELORD_PUBLIC_CRT, "key": SSL_TEST_TIMELORD_PUBLIC_KEY},
    },
    "crawler": {
        "private": {"crt": SSL_TEST_CRAWLER_PRIVATE_CRT, "key": SSL_TEST_CRAWLER_PRIVATE_KEY},
    },
    "daemon": {
        "private": {"crt": SSL_TEST_DAEMON_PRIVATE_CRT, "key": SSL_TEST_DAEMON_PRIVATE_KEY},
    },
    "introducer": {
        "public": {"crt": SSL_TEST_INTRODUCER_PUBLIC_CRT, "key": SSL_TEST_INTRODUCER_PUBLIC_KEY},
    },
}
