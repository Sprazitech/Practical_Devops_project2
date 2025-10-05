# Quick Start Guide - Three-Tier Docker Application

## Prerequisites
- Docker Engine 20.10+
- Docker Compose 2.0+
- 4GB+ RAM available
- Ports 80, 4000, 3306 available

## Installation & Startup (5 minutes)

### Step 1: Navigate to Project Directory
```bash
cd three-tier-web-app
```

### Step 2: Build and Start All Services
```bash
# Option A: Use the automated script (recommended)
./build-and-test.sh

# Option B: Manual startup
docker compose up -d --build
```

### Step 3: Wait for Services to Start
The services will take 30-60 seconds to fully initialize. Monitor with:
```bash
docker compose logs -f
```

Press `Ctrl+C` to stop following logs.

### Step 4: Verify All Services Are Healthy
```bash
docker compose ps
```

All three services should show status as "healthy".

### Step 5: Access the Application
Open your browser and navigate to:
- **Frontend**: http://localhost
- **API**: http://localhost:4000
- **Health Check**: http://localhost:4000/health

## Testing the Application

### Test 1: Web Interface
1. Open http://localhost in your browser
2. Click on "Database Demo" (burger menu in top-right)
3. You should see 3 sample transactions
4. Add a new transaction:
   - Amount: 100.50
   - Description: Test transaction
   - Click "ADD"
5. Verify the transaction appears in the list
6. Click "DEL" to delete all transactions

### Test 2: API Testing (Command Line)
```bash
# Get all transactions
curl http://localhost:4000/transaction

# Add a transaction
curl -X POST http://localhost:4000/transaction \
  -H "Content-Type: application/json" \
  -d '{"amount": "250.75", "desc": "API test"}'

# Delete all transactions
curl -X DELETE http://localhost:4000/transaction
```

### Test 3: Database Direct Access
```bash
# Access MySQL container
docker compose exec mysql mysql -uadmin -padmin123 webappdb

# Run queries
SELECT * FROM transactions;

# Exit MySQL
exit
```

## Common Operations

### View Logs
```bash
# All services
docker compose logs

# Specific service
docker compose logs frontend
docker compose logs backend
docker compose logs mysql

# Follow logs in real-time
docker compose logs -f
```

### Restart Services
```bash
# Restart all
docker compose restart

# Restart specific service
docker compose restart backend
```

### Stop Services
```bash
# Stop all services
docker compose stop

# Stop specific service
docker compose stop backend
```

### Start Services
```bash
# Start all services
docker compose start

# Start specific service
docker compose start backend
```

### Rebuild After Code Changes
```bash
# Rebuild all
docker compose up -d --build

# Rebuild specific service
docker compose up -d --build backend
```

### Clean Up Everything
```bash
# Stop and remove containers, networks
docker compose down

# Stop and remove everything including volumes (data loss!)
docker compose down -v
```

## Troubleshooting

### Issue: Port already in use
**Error**: `Bind for 0.0.0.0:80 failed: port is already allocated`

**Solution**:
```bash
# Check what's using the port
sudo lsof -i :80
sudo lsof -i :4000
sudo lsof -i :3306

# Stop the conflicting service or change ports in docker-compose.yml
```

### Issue: Services not healthy
**Error**: Services stuck in "starting" state

**Solution**:
```bash
# Check logs
docker compose logs

# Restart services
docker compose down
docker compose up -d

# If problem persists, rebuild
docker compose down -v
docker compose up -d --build
```

### Issue: Database connection error
**Error**: Backend can't connect to MySQL

**Solution**:
```bash
# Wait longer for MySQL to fully start (can take 30-60s)
# Check MySQL logs
docker compose logs mysql

# Restart backend after MySQL is healthy
docker compose restart backend
```

### Issue: Frontend shows blank page
**Error**: React app doesn't load

**Solution**:
```bash
# Check frontend logs
docker compose logs frontend

# Check nginx configuration
docker compose exec frontend cat /etc/nginx/conf.d/default.conf

# Rebuild frontend
docker compose up -d --build frontend
```

## Default Credentials

### MySQL Database
- **Host**: localhost (or `mysql` from other containers)
- **Port**: 3306
- **Database**: webappdb
- **User**: admin
- **Password**: admin123
- **Root Password**: rootpassword

### Application
- No authentication required for this demo

## File Structure
```
three-tier-web-app/
├── docker-compose.yml           # Main orchestration file
├── build-and-test.sh           # Automated build/test script
├── validate-docker-setup.sh    # Validation script
├── QUICKSTART.md               # This file
├── DOCKER_README.md            # Comprehensive guide
└── application-code/
    ├── app-tier/               # Backend
    │   └── Dockerfile
    ├── web-tier/               # Frontend
    │   ├── Dockerfile
    │   └── nginx.conf
    └── db-init/                # Database
        └── init.sql
```

## Production Deployment Checklist

Before deploying to production:

- [ ] Change all default passwords
- [ ] Use environment variables from `.env` file
- [ ] Enable SSL/TLS for HTTPS
- [ ] Remove MySQL port exposure (use only internal network)
- [ ] Set up proper backup strategy for database
- [ ] Configure monitoring and logging
- [ ] Review and update security settings
- [ ] Use container registry for images
- [ ] Implement CI/CD pipeline
- [ ] Set up health check monitoring
- [ ] Configure resource limits
- [ ] Review and update restart policies

## Support

For issues or questions:
1. Check the logs: `docker compose logs`
2. Review `DOCKER_README.md` for detailed troubleshooting
3. Verify setup: `./validate-docker-setup.sh`
4. Check Docker status: `docker info`

## Useful Links

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [MySQL Docker Image](https://hub.docker.com/_/mysql)
- [Nginx Docker Image](https://hub.docker.com/_/nginx)
- [Node.js Docker Image](https://hub.docker.com/_/node)

---

**Last Updated**: October 5, 2025  
**Version**: 1.0.0
