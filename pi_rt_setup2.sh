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

source ./config/config.sh

##################
#
#   
#
if echo "$self_model" | grep -q $target_name ; then
	is_rpi=True
else
	echo "e)This script is written to be run on a Raspberry Pi."
	echo "j)このスクリプトは Raspberry Pi で実行されている想定で書かれています。"
fi

##################
#
#
#
get
apt update
apt install -y $apt_install_list
#systemctl disable dnsmasq
#systemctl stop dnsmasq
echo "SUBSYSTEM==\"ieee80211\", ACTION==\"add|change\", ATTR{macaddress}==\"$wlan0_macadd\", KERNEL==\"phy0\", \\
  RUN+=\"/sbin/iw phy phy0 interface add $vnic_name type __ap\", \\
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

nmcli con modify preconfigured type wifi ifname wlan0 mode infrastructure

systemctl restart NetworkManager.service


