Script to generate License for SAP Preview, Evaluation and Developer Versions in batch
===

Usage python script example
---

MINSAPLICTYPE=025
MINSAPLICEMAIL=blablabla@blablabla.io
MINSAPLICHWKEY=D0929189719

```bash
(set -o pipefail && python3 minisaplicgen.py | xpath -q -e '/entry/content/m:properties/d:Licensekey/text()')<<EOF
{
    "Type": "$MINSAPLICTYPE",
    "Name": "$MINSAPLICEMAIL",
    "Email": "$MINSAPLICEMAIL",
    "Hwkey": "$MINSAPLICHWKEY",
    "HostID": "",
    "HostName": ""
}
EOF
```

Usage bash script example for A4H
---

This example related to SAP Demo System `A4H` (A4H - SAP NetWeaver AS ABAP 7.4 and above (Linux / SAP HANA).

```bash
export MINSAPLICTYPE=025
export MINSAPLICHWKEY=$(su - a4hadm -c "saplicense -get | grep -i hardware | tr -d '[:space:]' | sed 's/.*=//'")
export MINSAPLICEMAIL=blablabla@blablabla.io
./minisaplicgen.sh
```
