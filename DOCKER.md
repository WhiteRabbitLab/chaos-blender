# Docker Setup Guide

This guide covers running Chaos Blender with Docker for easy local development and deployment.

## Prerequisites

- **Docker**: [Install Docker Desktop](https://www.docker.com/products/docker-desktop)
- **Docker Compose**: Included with Docker Desktop

## Quick Start

### Option 1: Database Only (Recommended for Development)

Run only PostgreSQL in Docker, and run backend/frontend manually for hot-reloading:

```bash
# Start PostgreSQL
docker-compose -f docker-compose.db-only.yml up -d

# The database will be available at localhost:5432
# Connection string: postgresql://chaos_user:chaos_password@localhost:5432/chaos_blender
```

Then run backend and frontend normally:

```bash
# Terminal 1 - Backend
cd server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Update .env with Docker database URL
echo "DATABASE_URL=postgresql://chaos_user:chaos_password@localhost:5432/chaos_blender" > .env

# Initialize and run
cd src
python init_data.py
python main.py

# Terminal 2 - Frontend
cd client
npm install
npm start
```

### Option 2: Full Stack with Docker

Run everything (database, backend, and frontend) in Docker:

```bash
# Build and start all services
docker-compose up --build

# Or run in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

Services will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- API Docs: http://localhost:5000/docs
- Database: localhost:5432

## Docker Compose Files

### docker-compose.db-only.yml
- Only PostgreSQL database
- Best for active development with hot-reloading
- Lightweight and fast

### docker-compose.yml
- Full stack: PostgreSQL + Backend + Frontend
- All services containerized
- Good for testing the complete setup
- Backend and frontend have volume mounts for code changes

## Common Commands

### Start Services

```bash
# Database only
docker-compose -f docker-compose.db-only.yml up -d

# Full stack
docker-compose up -d

# Build and start
docker-compose up --build
```

### Stop Services

```bash
# Stop and remove containers
docker-compose down

# Stop, remove containers and volumes (deletes database data)
docker-compose down -v
```

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f postgres
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Execute Commands in Containers

```bash
# Access PostgreSQL
docker-compose exec postgres psql -U chaos_user -d chaos_blender

# Access backend shell
docker-compose exec backend bash

# Re-initialize database
docker-compose exec backend python src/init_data.py

# Run backend tests
docker-compose exec backend pytest
```

### Database Management

```bash
# Backup database
docker-compose exec postgres pg_dump -U chaos_user chaos_blender > backup.sql

# Restore database
docker-compose exec -T postgres psql -U chaos_user chaos_blender < backup.sql

# Reset database
docker-compose down -v
docker-compose up -d postgres
docker-compose exec backend python src/init_data.py
```

## Development Workflow

### Hot-Reloading Setup

**Option 1: Database in Docker, Apps Local (Recommended)**

```bash
# Start database
docker-compose -f docker-compose.db-only.yml up -d

# Run backend (auto-reloads on code changes)
cd server/src
python main.py

# Run frontend (auto-reloads on code changes)
cd client
npm start
```

**Option 2: Everything in Docker with Volume Mounts**

```bash
# Start all services
docker-compose up

# Code changes in server/src and client/src will trigger reloads
# Backend uses --reload flag
# Frontend uses webpack dev server
```

## Production Deployment with Docker

### Build Production Images

```bash
# Build backend production image
docker build -f server/Dockerfile.prod -t chaos-blender-backend:prod ./server

# Build frontend production image
docker build -f client/Dockerfile -t chaos-blender-frontend:prod ./client
```

### Production Docker Compose

Create `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    restart: always
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - chaos-network

  backend:
    image: chaos-blender-backend:prod
    restart: always
    environment:
      DATABASE_URL: postgresql://${DB_USER}:${DB_PASSWORD}@postgres:5432/${DB_NAME}
    ports:
      - "8000:8000"
    depends_on:
      - postgres
    networks:
      - chaos-network

  frontend:
    image: chaos-blender-frontend:prod
    restart: always
    ports:
      - "80:80"
    depends_on:
      - backend
    networks:
      - chaos-network

volumes:
  postgres_data:

networks:
  chaos-network:
    driver: bridge
```

Run production:

```bash
# Create .env file with production credentials
cat > .env << EOF
DB_USER=chaos_user
DB_PASSWORD=your_secure_password
DB_NAME=chaos_blender
EOF

# Start production stack
docker-compose -f docker-compose.prod.yml up -d

# Initialize database
docker-compose -f docker-compose.prod.yml exec backend python src/init_data.py
```

## Environment Variables

### Database Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| POSTGRES_USER | chaos_user | Database username |
| POSTGRES_PASSWORD | chaos_password | Database password |
| POSTGRES_DB | chaos_blender | Database name |

### Backend Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| DATABASE_URL | postgresql://... | Full database connection string |
| HOST | 0.0.0.0 | Server host |
| PORT | 5000 | Server port |

### Frontend Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| REACT_APP_API_URL | http://localhost:5000 | Backend API URL |

## Troubleshooting

### Port Already in Use

```bash
# Check what's using the port
lsof -i :5432  # PostgreSQL
lsof -i :5000  # Backend
lsof -i :3000  # Frontend

# Change ports in docker-compose.yml
ports:
  - "5433:5432"  # Use different host port
```

### Container Won't Start

```bash
# Check container logs
docker-compose logs [service-name]

# Check container status
docker-compose ps

# Rebuild container
docker-compose up --build [service-name]
```

### Database Connection Errors

```bash
# Ensure PostgreSQL is ready
docker-compose exec postgres pg_isready

# Check database exists
docker-compose exec postgres psql -U chaos_user -l

# Verify connection from backend
docker-compose exec backend python -c "from src.database import engine; print(engine.connect())"
```

### Volume Permission Issues

```bash
# Fix volume permissions (Linux/Mac)
sudo chown -R $USER:$USER postgres_data/

# Or remove and recreate volumes
docker-compose down -v
docker-compose up -d
```

### Frontend Not Updating

```bash
# Clear Docker cache
docker-compose down
docker system prune -a
docker-compose up --build

# Or rebuild specific service
docker-compose up --build frontend
```

## Performance Optimization

### PostgreSQL Performance

Add to `docker-compose.yml` under postgres service:

```yaml
postgres:
  command:
    - "postgres"
    - "-c"
    - "max_connections=200"
    - "-c"
    - "shared_buffers=256MB"
    - "-c"
    - "effective_cache_size=1GB"
```

### Backend Scaling

Run multiple backend instances:

```yaml
backend:
  deploy:
    replicas: 3
```

### Frontend Build Optimization

Use multi-stage build (already in Dockerfile):
- Smaller image size
- Production-optimized build
- Nginx for static file serving

## Data Persistence

### Backup Strategy

```bash
# Automated daily backups (add to crontab)
0 2 * * * docker-compose exec postgres pg_dump -U chaos_user chaos_blender > /backups/chaos_blender_$(date +\%Y\%m\%d).sql
```

### Volume Management

```bash
# List volumes
docker volume ls

# Inspect volume
docker volume inspect chaos-blender_postgres_data

# Backup volume
docker run --rm -v chaos-blender_postgres_data:/data -v $(pwd):/backup alpine tar czf /backup/postgres_backup.tar.gz /data

# Restore volume
docker run --rm -v chaos-blender_postgres_data:/data -v $(pwd):/backup alpine tar xzf /backup/postgres_backup.tar.gz -C /
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Build and Test

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Start services
        run: docker-compose up -d

      - name: Run backend tests
        run: docker-compose exec -T backend pytest

      - name: Run frontend tests
        run: docker-compose exec -T frontend npm test

      - name: Stop services
        run: docker-compose down
```

## Security Best Practices

1. **Don't use default passwords in production**
   ```bash
   # Use strong passwords in .env
   POSTGRES_PASSWORD=$(openssl rand -base64 32)
   ```

2. **Don't expose database port in production**
   ```yaml
   # Remove from docker-compose.prod.yml
   # ports:
   #   - "5432:5432"
   ```

3. **Use Docker secrets for sensitive data**
   ```yaml
   secrets:
     db_password:
       file: ./secrets/db_password.txt
   ```

4. **Keep images updated**
   ```bash
   docker-compose pull
   docker-compose up -d
   ```

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [PostgreSQL Docker Image](https://hub.docker.com/_/postgres)
- [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---

**Need help?** Check the main [SETUP.md](SETUP.md) or [DEPLOYMENT.md](DEPLOYMENT.md) guides.
