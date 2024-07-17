# DB Tax Service

### Overview:

This Django app provides an API endpoint for users to retrieve sales tax rates for regions within the US.

### Dependencies:

Install Docker and Docker Compose:
   - Docker version 26.0.0+ and Docker Compose version 2.28.0+ are required.
   - For Ubuntu, refer to the following link: [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/).
   - If you're using Debian or Ubuntu, you can use the bash scripts in the `/helpers` directory to install Docker and Docker Compose:
     ```bash
     bash helpers/install_docker.sh
     bash helpers/install_docker_compose.sh
     ```

### Configuration:

1. Create Configuration Files:
   - Create the following files in the root directory:
     - `dev.env`
     - `prod.env`
     - `superusers.json`
   - Use the respective `*.dist` files as templates for these new files.

2. Generate Django Secret Key:
   - Visit [https://djecrety.ir/](https://djecrety.ir/) or any other suitable tool.
   - Generate a new Django secret key.

3. Set Django Secret Key:
   - Open `dev.env` and `prod.env` files.
   - Set the value of `DJANGO_SECRET_KEY` to the newly obtained secret key.

4. Set Admin Email and Site Name:
   - Open `dev.env` and `prod.env` files.
   - Set the value of `DJANGO_SITE_NAME` to the desired site name.
   - Set the value of `DJANGO_SITE_DOMAIN` to the desired site domain.
   - Set the value of `ADMIN_EMAIL` to the desired admin email address.

5. Set Allowed Hosts (for production environment):
   - Open the `prod.env` file.
   - Set the value of `DJANGO_ALLOWED_HOSTS` to the desired host address(es).
     - Example: `DJANGO_ALLOWED_HOSTS=example.com,www.example.com`

6. Set Database Password:
   - Open the `prod.env` file.
   - Set the value of `DB_PASSWORD` to the desired database password.

7. Set New Admin Account Credentials:
   - Open the `superusers.json` file.
   - Set a new email and password for the admin account in the JSON format.

8. Encrypt/ decrypt *.env/ superusers.json files (optional):
	```bash
	bash helpers/gpg_wrapper.sh -f *.env -e encrypt
	bash helpers/gpg_wrapper.sh -f *.env.gpg -e decrypt
	```

9. Update the included django utilities (optional):
	```bash
	git fetch https://github.com/buswedg/django-utils.git main
	git subtree pull --prefix=apps/utils https://github.com/buswedg/django-utils.git main --squash
	```

### Run:

- Run locally for development:
	```bash
	docker compose -f docker-compose.dev.yml --env-file dev.env up
	```

- Run for production (without ssl):
	```bash
	docker compose -f docker-compose.prod.yml --env-file prod.env up
	```

- Run for production (with ssl):
	```bash
	docker compose -f docker-compose.prod.nginx.yml --env-file prod.env up
	```
