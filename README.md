# acr122u

(https://oneguyoneblog.com/2015/09/16/acr122u-nfc-usb-reader-raspberry-pi/)
```
sudo apt-get update
sudo apt-get -y install subversion autoconf debhelper flex libusb-dev libpcsclite-dev libpcsclite1 libccid pcscd pcsc-tools libpcsc-perl libusb-1.0-0-dev libtool libssl-dev cmake checkinstall
wget https://github.com/nfc-tools/libnfc/releases/download/libnfc-1.7.0-rc7/libnfc-1.7.0-rc7.tar.gz
tar -xvzf libnfc-1.7.0-rc7.tar.gz
cd libnfc-1.7.0-rc7
./configure --with-drivers=acr122_usb
make
sudo make install
sudo nfc-list
```
If problems
```
sudo sh -c "echo /usr/local/lib > /etc/ld.so.conf.d/usr-local-lib.conf"
sudo ldconfig
```

If USB problem
```
sudo nano /etc/modprobe.d/blacklist-libnfc.conf
```
add
```
blacklist pn533
blacklist nfc
```
Then
```
sudo modprobe -r pn533 nfc
```

## acr120

https://github.com/acshk/acsccid
