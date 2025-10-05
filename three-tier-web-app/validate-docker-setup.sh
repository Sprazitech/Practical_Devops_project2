#!/bin/bash

# Docker Setup Validation Script
# Validates that all required files are present and properly configured

set -e

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "================================================"
echo "Docker Setup Validation"
echo "================================================"
echo ""

ERRORS=0
WARNINGS=0

# Function to check file exists
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} Found: $1"
        return 0
    else
        echo -e "${RED}✗${NC} Missing: $1"
        ERRORS=$((ERRORS + 1))
        return 1
    fi
}

# Function to check file contains string
check_content() {
    if grep -q "$2" "$1" 2>/dev/null; then
        echo -e "${GREEN}  ✓${NC} Contains: $2"
        return 0
    else
        echo -e "${YELLOW}  ⚠${NC} Missing content: $2"
        WARNINGS=$((WARNINGS + 1))
        return 1
    fi
}

echo "Checking Docker configuration files..."
echo "--------------------------------------"

# Check backend Dockerfile
echo -e "\n1. Backend Dockerfile:"
if check_file "application-code/app-tier/Dockerfile"; then
    check_content "application-code/app-tier/Dockerfile" "FROM node:"
    check_content "application-code/app-tier/Dockerfile" "EXPOSE 4000"
    check_content "application-code/app-tier/Dockerfile" "HEALTHCHECK"
fi

# Check backend .dockerignore
echo -e "\n2. Backend .dockerignore:"
check_file "application-code/app-tier/.dockerignore"

# Check frontend Dockerfile
echo -e "\n3. Frontend Dockerfile:"
if check_file "application-code/web-tier/Dockerfile"; then
    check_content "application-code/web-tier/Dockerfile" "FROM node:"
    check_content "application-code/web-tier/Dockerfile" "FROM nginx:"
    check_content "application-code/web-tier/Dockerfile" "EXPOSE 80"
    check_content "application-code/web-tier/Dockerfile" "multi-stage"
fi

# Check frontend .dockerignore
echo -e "\n4. Frontend .dockerignore:"
check_file "application-code/web-tier/.dockerignore"

# Check nginx configuration
echo -e "\n5. Nginx Configuration:"
if check_file "application-code/web-tier/nginx.conf"; then
    check_content "application-code/web-tier/nginx.conf" "location /api/"
    check_content "application-code/web-tier/nginx.conf" "proxy_pass"
    check_content "application-code/web-tier/nginx.conf" "backend:4000"
fi

# Check database init script
echo -e "\n6. Database Initialization Script:"
if check_file "application-code/db-init/init.sql"; then
    check_content "application-code/db-init/init.sql" "CREATE DATABASE"
    check_content "application-code/db-init/init.sql" "CREATE TABLE"
    check_content "application-code/db-init/init.sql" "transactions"
fi

# Check docker-compose.yml
echo -e "\n7. Docker Compose Configuration:"
if check_file "docker-compose.yml"; then
    check_content "docker-compose.yml" "version:"
    check_content "docker-compose.yml" "mysql:"
    check_content "docker-compose.yml" "backend:"
    check_content "docker-compose.yml" "frontend:"
    check_content "docker-compose.yml" "networks:"
    check_content "docker-compose.yml" "volumes:"
    check_content "docker-compose.yml" "healthcheck:"
fi

# Check .env.example
echo -e "\n8. Environment Variables Example:"
if check_file ".env.example"; then
    check_content ".env.example" "MYSQL_"
    check_content ".env.example" "DB_HOST"
fi

# Check documentation
echo -e "\n9. Documentation:"
check_file "DOCKER_README.md"

# Check build script
echo -e "\n10. Build and Test Script:"
check_file "build-and-test.sh"

# Check backend package.json
echo -e "\n11. Backend Dependencies:"
if check_file "application-code/app-tier/package.json"; then
    check_content "application-code/app-tier/package.json" "express"
    check_content "application-code/app-tier/package.json" "mysql"
fi

# Check frontend package.json
echo -e "\n12. Frontend Dependencies:"
if check_file "application-code/web-tier/package.json"; then
    check_content "application-code/web-tier/package.json" "react"
    check_content "application-code/web-tier/package.json" "react-scripts"
fi

# Summary
echo ""
echo "================================================"
echo "Validation Summary"
echo "================================================"

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✓ All checks passed! Docker setup is complete.${NC}"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠ ${WARNINGS} warning(s) found, but all required files are present.${NC}"
    exit 0
else
    echo -e "${RED}✗ ${ERRORS} error(s) and ${WARNINGS} warning(s) found.${NC}"
    echo "Please review the missing files above."
    exit 1
fi
