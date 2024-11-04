#!/bin/sh
#
#  ファイルのバックアップを被らないようにしたい
#

#
# とりあえずroot確認
#
if [ "`whoami`" != "root" ]; then
  echo "Require root privilege"
  echo "権限がありません"
  echo "sudo $0"
  echo "又は root ユーザーで実行してください"
  exit 1
fi
##################
#
#   諸々の変数宣言
#
self_name=$(basename $0)
self_dir=$(cd $(dirname $0); pwd)
self_path=$self_dir/$self_name
self_model=$(cat /proc/cpuinfo | grep Model)

apt_install_list="dnsmasq vim"
wlan0_macadd=$(cat /sys/class/net/wlan0/address)
vmacadd=ee:ee:ee:12:34:56
target_name="Raspberry"

dhcp_root_addr=192.168.200.1
dhcp_lange_start=192.168.200.2
dhcp_lange_end=192.168.200.254


vnic_name=ap0
ssid=dev_net_01
ssid_key=devnet_user1234
ct_name=dev_net_ap

ieee80211_band=bg
ieee80211_channel=11
ieee80211_kmg=wpa-psk
ieee80211_proto=rsn
ieee80211_group=ccmp
ieee80211_pairwise=ccmp
ieee80211_psk=jetbot_ap
ieee80211_method=shared

##################
#
#   
#
if [[$self_model =~ $target_name]]; then
	is_rpi=True
else
	echo "e)This script is written to be run on a Raspberry Pi."
	echo "j)このスクリプトは Raspberry Pi で実行されている想定で書かれています。"
fi

##################
#
#   
#
apt update
apt install -y $apt_install_list
systemctl disable dnsmasq
systemctl stop dnsmasq
echo "SUBSYSTEM==\"ieee80211\", ACTION==\"add|change\", ATTR{macaddress}==\"$wlan0_macadd\", KERNEL==\"phy0\", \
  RUN+=\"/sbin/iw phy phy0 interface add $vnic_name type __ap\", \
  RUN+=\"/bin/ip link set $vnic_name address $vmacadd\"
" > /etc/udev/rules.d/99-$vnic_name.rules

nmcli con add type wifi ifname $vnic_name mode ap con-name $ct_name ssid $ssid
nmcli con modify $ct_name 802-11-wireless.band $ieee80211_band
nmcli con modify $ct_name 802-11-wireless.channel $ieee80211_channel
nmcli con modify $ct_name 802-11-wireless-security.key-mgmt $ieee80211_kmg
nmcli con modify $ct_name 802-11-wireless-security.proto $ieee80211_proto
nmcli con modify $ct_name 802-11-wireless-security.group $ieee80211_group
nmcli con modify $ct_name 802-11-wireless-security.pairwise $ieee80211_pairwise
nmcli con modify $ct_name 802-11-wireless-security.psk $ssid_key
nmcli con modify $ct_name ipv4.method $ieee80211_method
nmcli con modify $ct_name ipv4.addr $dhcp_root_addr/24
nmcli con up $ct_name


systemctl restart NetworkManager.service