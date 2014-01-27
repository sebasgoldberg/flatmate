# coding=utf-8
from base_ambiente import BaseAmbiente
import os

site_id='iamcast'

class Ambiente(BaseAmbiente):
  site_id=site_id

  dominio='%s.com.ar'%site_id
  puerto_http='80'
  puerto_https='443'

  class db:
    name=site_id
    user=site_id
    password='password'

  class ciudades:
    class db:
      name='ciudades'

  project_directory = '%s/' % os.path.abspath('%s/..' % os.path.split(os.path.abspath(__file__))[0])

  class email:
    host = 'smtp.gmail.com'
    user = 'user@gmail.com'
    password = 'password'
    port = 587

  class zonomi:
    api_key = None

ambiente=Ambiente()
