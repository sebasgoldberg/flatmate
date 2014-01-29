#!/bin/bash
./manage.py dbcreate
./manage.py a2create
./manage.py domainupdate
mkdir -p uploads/inmueble/foto
mkdir -p static
sudo chgrp -R www-data uploads
sudo chmod 775 -R uploads
sudo chgrp -R www-data static
sudo chmod 775 -R static
./manage.py collectstatic
