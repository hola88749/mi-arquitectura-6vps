server {
    listen 80;
    server_name 20.171.127.68;

    location /api/auth {
        proxy_pass http://localhost:3000;
    }

    location / {
        root /var/www/html;
        index index.html;
    }
}
