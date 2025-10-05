# Three-Tier Web Application - Docker Setup

This repository contains a fully containerized three-tier web application stack with Docker and Docker Compose.

## 🏗️ Architecture

- **Frontend (Web Tier)**: React application served by Nginx
- **Backend (App Tier)**: Node.js/Express REST API
- **Database (Data Tier)**: MySQL 8.0

## 📋 Prerequisites

- Docker Engine 20.10+
- Docker Compose 2.0+
- At least 4GB of free RAM
- Ports 80, 4000, and 3306 available

## 🚀 Quick Start

### 1. Clone and Navigate to Directory
```bash
cd three-tier-web-app
```

### 2. Build and Start All Services
```bash
# Build and start all containers in detached mode
docker-compose up -d --build

# Or build first, then start
docker-compose build
docker-compose up -d
```

### 3. Access the Application
- **Frontend**: http://localhost
- **Backend API**: http://localhost:4000
- **MySQL Database**: localhost:3306

### 4. Check Service Health
```bash
# View all running containers
docker-compose ps

# Check logs for all services
docker-compose logs

# Check logs for specific service
docker-compose logs frontend
docker-compose logs backend
docker-compose logs mysql
```

## 🔧 Useful Commands

### Container Management
```bash
# Start services
docker-compose start

# Stop services
docker-compose stop

# Restart services
docker-compose restart

# Stop and remove containers
docker-compose down

# Stop and remove containers + volumes (clean slate)
docker-compose down -v
```

### Monitoring and Debugging
```bash
# View real-time logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f backend

# Execute command in running container
docker-compose exec backend sh
docker-compose exec frontend sh
docker-compose exec mysql bash

# Access MySQL database
docker-compose exec mysql mysql -u admin -padmin123 webappdb
```

### Building and Tagging
```bash
# Build specific service
docker-compose build backend

# Build without cache
docker-compose build --no-cache

# Tag images for registry
docker tag three-tier-frontend:latest your-registry/three-tier-frontend:v1.0.0
docker tag three-tier-backend:latest your-registry/three-tier-backend:v1.0.0

# Push to registry
docker push your-registry/three-tier-frontend:v1.0.0
docker push your-registry/three-tier-backend:v1.0.0
```

## 🧪 Testing

### 1. Test Backend Health
```bash
curl http://localhost:4000/health
```
Expected response: `"This is the health check"`

### 2. Test Database Connection
```bash
# Access MySQL container
docker-compose exec mysql mysql -u admin -padmin123 -e "USE webappdb; SELECT * FROM transactions;"
```

### 3. Test Frontend
Open http://localhost in your browser and navigate to the Database Demo page to test CRUD operations.

### 4. Test API Endpoints
```bash
# Get all transactions
curl http://localhost:4000/transaction

# Add a transaction
curl -X POST http://localhost:4000/transaction \
  -H "Content-Type: application/json" \
  -d '{"amount": "100.50", "desc": "test transaction"}'

# Delete all transactions
curl -X DELETE http://localhost:4000/transaction
```

## 📁 Project Structure

```
three-tier-web-app/
├── docker-compose.yml              # Docker Compose orchestration
├── .env.example                    # Environment variables template
├── DOCKER_README.md               # This file
└── application-code/
    ├── web-tier/                  # React Frontend
    │   ├── Dockerfile            # Frontend Dockerfile
    │   ├── nginx.conf            # Nginx configuration
    │   ├── .dockerignore
    │   └── src/                  # React source code
    ├── app-tier/                  # Node.js Backend
    │   ├── Dockerfile            # Backend Dockerfile
    │   ├── .dockerignore
    │   ├── index.js              # Express server
    │   └── package.json
    └── db-init/                   # Database initialization
        └── init.sql              # MySQL init script
```

## 🔐 Security Notes

### For Production Deployment:
1. **Change default passwords** in docker-compose.yml
2. **Use environment variables** from .env file instead of hardcoding
3. **Enable SSL/TLS** for frontend with proper certificates
4. **Restrict database access** to backend only
5. **Use secrets management** (Docker secrets, Kubernetes secrets, etc.)
6. **Regular security updates** for base images

### Example with .env file:
```bash
# Copy example env file
cp .env.example .env

# Edit with your values
nano .env

# Use with docker-compose
docker-compose --env-file .env up -d
```

## 🐛 Troubleshooting

### Services Won't Start
```bash
# Check logs
docker-compose logs

# Verify ports are available
netstat -tulpn | grep -E ':(80|4000|3306)'

# Remove old containers and try again
docker-compose down -v
docker-compose up -d --build
```

### Database Connection Issues
```bash
# Check MySQL is ready
docker-compose logs mysql

# Verify database initialization
docker-compose exec mysql mysql -u admin -padmin123 -e "SHOW DATABASES;"

# Restart backend after database is ready
docker-compose restart backend
```

### Frontend Can't Connect to Backend
```bash
# Check backend is running
docker-compose ps backend

# Test backend directly
curl http://localhost:4000/health

# Check nginx configuration
docker-compose exec frontend cat /etc/nginx/conf.d/default.conf
```

### Rebuild After Code Changes
```bash
# Rebuild and restart specific service
docker-compose up -d --build backend

# Rebuild everything
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

## 📊 Resource Usage

Typical resource consumption:
- **Frontend**: ~50MB RAM
- **Backend**: ~100MB RAM
- **MySQL**: ~400MB RAM
- **Total Disk**: ~1GB

## 🔄 Development Workflow

For active development with hot-reload:

1. **Backend Development**:
```bash
# Add volume mount for live code updates (add to docker-compose.yml)
volumes:
  - ./application-code/app-tier:/app
  - /app/node_modules
```

2. **Frontend Development**:
```bash
# Use npm start locally instead of Docker
cd application-code/web-tier
npm install
npm start
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📞 Support

For issues and questions:
- Create an issue in the GitHub repository
- Check existing issues for solutions
- Review Docker and Docker Compose documentation

## 🎯 Next Steps

- [ ] Set up CI/CD pipeline
- [ ] Add container orchestration (Kubernetes/ECS)
- [ ] Implement monitoring and logging
- [ ] Add automated testing
- [ ] Set up production environment
