certbot certonly --webroot -d api.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d as-vpn.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d cdn.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d db.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d eu-vpn.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d in-vpn.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d mail.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d me-vpn.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d na-vpn.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d oc-vpn.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d panel.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d sa-vpn.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d us-vpn.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d smtp.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d node1.csl.sh --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal
certbot certonly --webroot -d gential-ai.com --email talbaskin.business@gmail.com -w /var/www/_letsencrypt -n --agree-tos --force-renewal

sed -i -r 's/#?;#//g' /etc/nginx/sites-available/*


