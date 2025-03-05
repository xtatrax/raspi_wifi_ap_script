#!/bin/sh
#
# 共通の設定
#


self_model=$(cat /proc/cpuinfo)

apt_install_list="dnsmasq vim"
wlan0_macadd=$(cat /sys/class/net/wlan0/address)
vmacadd=ee:ee:ee:12:34:56
target_name="Raspberry"

dhcp_root_addr=
dhcp_lange_start=
dhcp_lange_end=


vnic_name=
ssid=
ssid_key=
ct_name=

ieee80211_band=bg
ieee80211_channel=11
ieee80211_kmg=wpa-psk
ieee80211_proto=rsn
ieee80211_group=ccmp
ieee80211_pairwise=ccmp
ieee80211_method=shared
