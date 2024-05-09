FROM nginx:latest

# Update package lists
RUN apt-get update

# Install necessary tools for protection
RUN apt-get install -y iptables

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy website files
COPY website /usr/share/nginx/html

EXPOSE 80
