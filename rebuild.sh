#!/bin/sh

python manage.py run_rebuild_core &&
python manage.py run_rebuild_tax -d apps/tax/data