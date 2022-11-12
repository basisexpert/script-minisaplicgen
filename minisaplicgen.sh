#!/bin/bash

(set -o pipefail && python3 minisaplicgen.py | xpath -q -e '/entry/content/m:properties/d:Licensekey/text()')<<EOF
{
    "Type": "$MINSAPLICTYPE",
    "Name": "${MINSAPLICEMAIL:=blablabla}",
    "Email": "${MINSAPLICEMAIL:=blablabla@blablabla.io}",
    "Hwkey": "$MINSAPLICHWKEY",
    "HostID": "${MINSAPHOSTID:=''}",
    "HostName": "${MINSAPHOSTNAME:=''}"
}
EOF
