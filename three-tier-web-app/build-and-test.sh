#!/bin/bash

# Three-Tier Web Application - Build and Test Script
# This script builds, tags, and tests all Docker containers locally

set -e  # Exit on error

# Color codes for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}Three-Tier Web App - Docker Build & Test${NC}"
echo -e "${BLUE}================================================${NC}\n"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Error: Docker is not installed${NC}"
    exit 1
fi

# Check if Docker daemon is running
if ! docker info &> /dev/null; then
    echo -e "${RED}Error: Docker daemon is not running${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Docker is installed and running${NC}\n"

# Step 1: Clean up old containers and images (optional)
echo -e "${YELLOW}Step 1: Cleaning up old containers...${NC}"
docker-compose down -v 2>/dev/null || true
echo -e "${GREEN}✓ Cleanup complete${NC}\n"

# Step 2: Build all images
echo -e "${YELLOW}Step 2: Building Docker images...${NC}"
docker compose build --no-cache

# Tag images with version
VERSION="v1.0.0"
echo -e "\n${YELLOW}Step 3: Tagging images...${NC}"
docker tag three-tier-web-app-frontend:latest three-tier-frontend:${VERSION}
docker tag three-tier-web-app-backend:latest three-tier-backend:${VERSION}
docker tag mysql:8.0 three-tier-mysql:${VERSION}

echo -e "${GREEN}✓ Images tagged as ${VERSION}${NC}\n"

# Step 4: List built images
echo -e "${YELLOW}Step 4: Built images:${NC}"
docker images | grep -E "three-tier|REPOSITORY"

# Step 5: Start all services
echo -e "\n${YELLOW}Step 5: Starting all services...${NC}"
docker compose up -d

# Step 6: Wait for services to be healthy
echo -e "\n${YELLOW}Step 6: Waiting for services to be healthy...${NC}"
echo "This may take 30-60 seconds..."

MAX_WAIT=120
ELAPSED=0
INTERVAL=5

while [ $ELAPSED -lt $MAX_WAIT ]; do
    MYSQL_HEALTH=$(docker inspect --format='{{.State.Health.Status}}' three-tier-mysql 2>/dev/null || echo "starting")
    BACKEND_HEALTH=$(docker inspect --format='{{.State.Health.Status}}' three-tier-backend 2>/dev/null || echo "starting")
    FRONTEND_HEALTH=$(docker inspect --format='{{.State.Health.Status}}' three-tier-frontend 2>/dev/null || echo "starting")
    
    echo "  MySQL: $MYSQL_HEALTH | Backend: $BACKEND_HEALTH | Frontend: $FRONTEND_HEALTH"
    
    if [ "$MYSQL_HEALTH" = "healthy" ] && [ "$BACKEND_HEALTH" = "healthy" ] && [ "$FRONTEND_HEALTH" = "healthy" ]; then
        echo -e "${GREEN}✓ All services are healthy!${NC}\n"
        break
    fi
    
    sleep $INTERVAL
    ELAPSED=$((ELAPSED + INTERVAL))
done

if [ $ELAPSED -ge $MAX_WAIT ]; then
    echo -e "${RED}Warning: Services did not become healthy within ${MAX_WAIT} seconds${NC}"
    echo "Checking logs..."
    docker compose logs
fi

# Step 7: Run tests
echo -e "${YELLOW}Step 7: Running tests...${NC}\n"

# Test 1: Check if containers are running
echo "Test 1: Checking container status..."
docker compose ps

# Test 2: Test MySQL database
echo -e "\nTest 2: Testing MySQL database..."
if docker exec three-tier-mysql mysql -uadmin -padmin123 -e "USE webappdb; SELECT COUNT(*) FROM transactions;" &> /dev/null; then
    echo -e "${GREEN}✓ MySQL database is accessible and initialized${NC}"
    docker exec three-tier-mysql mysql -uadmin -padmin123 -e "USE webappdb; SELECT * FROM transactions;"
else
    echo -e "${RED}✗ MySQL database test failed${NC}"
fi

# Test 3: Test backend health endpoint
echo -e "\nTest 3: Testing backend health endpoint..."
if curl -s http://localhost:4000/health | grep -q "health check"; then
    echo -e "${GREEN}✓ Backend health check passed${NC}"
else
    echo -e "${RED}✗ Backend health check failed${NC}"
fi

# Test 4: Test backend API - Get transactions
echo -e "\nTest 4: Testing backend API - Get transactions..."
TRANSACTIONS=$(curl -s http://localhost:4000/transaction)
if [ ! -z "$TRANSACTIONS" ]; then
    echo -e "${GREEN}✓ Backend API responding${NC}"
    echo "Response: $TRANSACTIONS"
else
    echo -e "${RED}✗ Backend API test failed${NC}"
fi

# Test 5: Test backend API - Add transaction
echo -e "\nTest 5: Testing backend API - Add transaction..."
ADD_RESPONSE=$(curl -s -X POST http://localhost:4000/transaction \
    -H "Content-Type: application/json" \
    -d '{"amount": "999.99", "desc": "Docker test transaction"}')
if echo "$ADD_RESPONSE" | grep -q "success"; then
    echo -e "${GREEN}✓ Transaction added successfully${NC}"
    echo "Response: $ADD_RESPONSE"
else
    echo -e "${YELLOW}⚠ Add transaction response: $ADD_RESPONSE${NC}"
fi

# Test 6: Test frontend
echo -e "\nTest 6: Testing frontend..."
if curl -s http://localhost/ | grep -q "html"; then
    echo -e "${GREEN}✓ Frontend is accessible${NC}"
else
    echo -e "${RED}✗ Frontend test failed${NC}"
fi

# Test 7: Test frontend-to-backend proxy
echo -e "\nTest 7: Testing frontend-to-backend API proxy..."
if curl -s http://localhost/api/health | grep -q "health check"; then
    echo -e "${GREEN}✓ Frontend-to-backend proxy working${NC}"
else
    echo -e "${RED}✗ Frontend-to-backend proxy test failed${NC}"
fi

# Step 8: Display access information
echo -e "\n${BLUE}================================================${NC}"
echo -e "${BLUE}Build and Test Complete!${NC}"
echo -e "${BLUE}================================================${NC}\n"

echo -e "${GREEN}Access URLs:${NC}"
echo -e "  Frontend:  http://localhost"
echo -e "  Backend:   http://localhost:4000"
echo -e "  MySQL:     localhost:3306"

echo -e "\n${GREEN}Credentials:${NC}"
echo -e "  MySQL User: admin"
echo -e "  MySQL Pass: admin123"
echo -e "  Database:   webappdb"

echo -e "\n${YELLOW}Useful Commands:${NC}"
echo -e "  View logs:      docker compose logs -f"
echo -e "  Stop services:  docker compose stop"
echo -e "  Start services: docker compose start"
echo -e "  Restart:        docker compose restart"
echo -e "  Clean up:       docker compose down -v"

echo -e "\n${GREEN}Container Images:${NC}"
docker images | grep three-tier

echo -e "\n${BLUE}================================================${NC}"
