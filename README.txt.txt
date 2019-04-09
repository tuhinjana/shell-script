1) extract bosch-test.zip to a directory
2) copy add_sudo_user.service to /etc/systemd/system/ directory.
3) replace PWD with current working directory.
4) change hostname in ./config file
5) execute below steps


sudo systemctl daemon-reload
sudo systemctl enable add_sudo_user.service