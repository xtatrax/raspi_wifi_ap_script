echo "SUBSYSTEM=='ieee80211', ACTION=='add|change', ATTR{macaddress}=='dc:a6:32:c4:b3:a8', KERNEL=='phy0', \
  RUN+='/sbin/iw phy phy0 interface add ap0 type __ap', \
  RUN+='/bin/ip link set ap0 address ee:ee:ee:12:34:56'
" > /etc/udev/rules.d/99-ap0.rules