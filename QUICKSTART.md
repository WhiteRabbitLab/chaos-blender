# 🚀 Quick Start - Chaos Blender

Get up and running in 5 minutes!

## Fastest Setup (Automated)

```bash
# 1. Run the setup script
./setup.sh

# 2. Start backend (Terminal 1)
cd server/src
source ../venv/bin/activate
python main.py

# 3. Start frontend (Terminal 2)
cd client
npm start

# 4. Open http://localhost:3000
```

## Docker Setup (Database Only)

```bash
# 1. Start PostgreSQL
./start-docker.sh

# 2. Setup backend
cd server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
cd src && python init_data.py

# 3. Setup frontend
cd client
npm install

# 4. Run backend
cd server/src && python main.py

# 5. Run frontend (new terminal)
cd client && npm start
```

## Full Docker Setup

```bash
# Run everything in Docker
docker-compose up --build

# Visit http://localhost:3000
```

## Stop Services

```bash
# Stop Docker database
./stop-docker.sh

# Stop full Docker stack
docker-compose down
```

## Useful Commands

```bash
# View API docs
open http://localhost:5000/docs

# Reset database
cd server/src && python init_data.py

# Stop Docker and remove data
./stop-docker.sh --remove-data

# Check Docker status
docker-compose ps
```

## Default Credentials

**Database (Docker):**
- Host: `localhost:5432`
- User: `chaos_user`
- Password: `chaos_password`
- Database: `chaos_blender`

**URLs:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- API Docs: http://localhost:5000/docs

## Troubleshooting

**Port already in use:**
```bash
# Find process using port
lsof -i :3000  # or :5000, :5432
kill -9 <PID>
```

**Database connection error:**
```bash
# Check if Docker database is running
docker-compose -f docker-compose.db-only.yml ps

# Restart database
docker-compose -f docker-compose.db-only.yml restart
```

**Module not found:**
```bash
# Backend
cd server
source venv/bin/activate
pip install -r requirements.txt

# Frontend
cd client
rm -rf node_modules
npm install
```

## More Information

- **Detailed Setup**: [SETUP.md](SETUP.md)
- **Docker Guide**: [DOCKER.md](DOCKER.md)
- **Deployment**: [DEPLOYMENT.md](DEPLOYMENT.md)
- **Main README**: [README.md](README.md)

---

Happy Blending! 🎮✨
