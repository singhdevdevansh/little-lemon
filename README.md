# Little Lemon Restaurant API

Please follow these testing instructions:
1. Ensure you have Django, DRF and Djoser installed
2. In your MySQL Client, run the following commands:
   - `CREATE DATABASE restaurant`
   - `CREATE USER 'lemon'@'localhost' IDENTIFIED BY 'Lemon@123!'`
   - `GRANT ALL PRIVILEGES ON restaurant TO 'lemon'@'localhost'`
3. Install app and run the server. Test the following endpoints:
   - `/restaurant/`
   - `/restaurant/booking/`
   - `/restaurant/menu/`
   - `/auth/token/login/`
