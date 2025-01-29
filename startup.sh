#!/bin/bash
# © Chancellors, Masters and Scholars of The University of Oxford. All rights reserved.

gunicorn --bind=0.0.0.0:443 app:app