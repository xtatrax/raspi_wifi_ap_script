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
  echo "sudo &0"
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

dnsmasq_conf_path=/etc/dnsmasq.conf
dhcpcd_conf_path=/etc/dhcpcd.conf
hostapd_conf_path=/etc/hostapd/hostapd.conf

apt_install_list="hostapd dnsmasq dhcpcd vim"
wlan0_macadd=$(cat /sys/class/net/wlan0/address)
vmacadd=ee:ee:ee:12:34:56
target_name="Raspberry"

dhcp_root_addr=192.168.200.1
dhcp_lange_start=192.168.200.2
dhcp_lange_end=192.168.200.254

vnic_name=ap0
ssid=dev_net_01
ssid_key=devnet_user1234

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

echo "SUBSYSTEM==\"ieee80211\", ACTION==\"add|change\", ATTR{macaddress}==\"$wlan0_macadd\", KERNEL==\"phy0\", \
  RUN+=\"/sbin/iw phy phy0 interface add $vnic_name type __ap\", \
  RUN+=\"/bin/ip link set $vnic_name address $vmacadd\"
" > /etc/udev/rules.d/99-$vnic_name.rules

##################
#
#   
#
if [ ! -e $dnsmasq_conf_path.old ]; then
	# $dnsmasq_conf_path.old 存在しないなら
	cp $dnsmasq_conf_path $dnsmasq_conf_path.old

	echo "interface=$vnic_name
dhcp-range=$dhcp_lange_start,$dhcp_lange_end,255.255.255.0,12h" >> $dnsmasq_conf_path
else
	echo "line : $LINENO → file $self_path"
	echo "未実装"
	exit 1
fi

##################
#
#   
#
if [ ! -e $dhcpcd_conf_path.old];then

	cp $dhcpcd_conf_path $dhcpcd_conf_path.old
	echo "
interface $vnic_name
static ip_address=$dhcp_root_addr/24
nohook wpa_supplicant" >> $dhcpcd_conf_path

else
	echo "line : $LINENO → file $self_path"
	echo "未実装"
	exit 1
fi

##################
#
#   
#
if [ ! -e $hostapd_conf_path.old];then
	cp $hostapd_conf_path $hostapd_conf_path.old
else
	echo "line : $LINENO → file $self_path"
	echo "未実装"
	exit 1
fi
echo "ctrl_interface=/var/run/hostapd
ctrl_interface_group=0
interface=$vnic_name
driver=nl80211
ssid=$ssid
hw_mode=g
country_code=JP
channel=11
ieee80211d=1
wmm_enabled=0
macaddr_acl=0
auth_algs=2
wpa=2
wpa_passphrase=$ssid_key
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
" > $hostapd_conf_path

systemctl unmask hostapd.service
systemctl enable hostapd.service
systemctl restart hostapd.service
systemctl restart dhcpcd.service
systemctl restart dnsmasq.service
