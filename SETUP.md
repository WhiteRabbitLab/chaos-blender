# Chaos Blender - Setup Guide

## Prerequisites

**Option A: With Docker (Easiest)**
- **Docker Desktop** - [Download](https://www.docker.com/products/docker-desktop)
- **Node.js** (v16 or higher) - [Download](https://nodejs.org/)
- **Python** (v3.9 or higher) - [Download](https://www.python.org/)

**Option B: Without Docker**
- **Node.js** (v16 or higher) - [Download](https://nodejs.org/)
- **Python** (v3.9 or higher) - [Download](https://www.python.org/)
- **PostgreSQL** (v14 or higher) - [Download](https://www.postgresql.org/)
- **npm** or **yarn** package manager

---

## Quick Start with Docker 🐳 (Recommended)

This is the fastest way to get started. Docker will handle the PostgreSQL database for you.

### 1. Start the Database

```bash
# Start PostgreSQL in Docker
docker-compose -f docker-compose.db-only.yml up -d

# Verify it's running
docker-compose -f docker-compose.db-only.yml ps
```

The database will be available at `localhost:5432` with:
- Username: `chaos_user`
- Password: `chaos_password`
- Database: `chaos_blender`

### 2. Backend Setup

```bash
cd server
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Copy environment file (already configured for Docker)
cp .env.example .env

# Initialize database
cd src
python init_data.py
python main.py
```

### 3. Frontend Setup

```bash
cd client
npm install
npm start
```

**That's it!** Visit http://localhost:3000

For full Docker setup (including backend and frontend in containers), see **[DOCKER.md](DOCKER.md)**.

---

## Quick Start Without Docker

### 1. Database Setup

First, create a PostgreSQL database for the application:

```bash
# Connect to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE chaos_blender;

# Exit psql
\q
```

### 2. Backend Setup (FastAPI)

```bash
# Navigate to server directory
cd server

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env file with your database credentials
# DATABASE_URL=postgresql://username:password@localhost:5432/chaos_blender
```

#### Initialize the Database

Run the initialization script to populate the database with game objects and scoring systems:

```bash
cd src
python init_data.py
```

You should see output confirming the initialization:
```
Initializing Chaos Blender database...
✓ Initialized 10 scoring systems
✓ Initialized 22 game objects
✓ Database initialization complete!
```

#### Start the Backend Server

```bash
# From the server directory
cd src
python main.py
```

The API server will start on `http://localhost:5000`

You can verify it's running by visiting:
- `http://localhost:5000/` - Root endpoint
- `http://localhost:5000/health` - Health check
- `http://localhost:5000/docs` - Interactive API documentation (FastAPI Swagger UI)

### 3. Frontend Setup (React + TypeScript)

Open a new terminal window:

```bash
# Navigate to client directory
cd client

# Install dependencies
npm install

# Start the development server
npm start
```

The application will open in your browser at `http://localhost:3000`

## Development Workflow

### Running Both Servers Concurrently

**Terminal 1 - Backend:**
```bash
cd server/src
source ../venv/bin/activate  # or venv\Scripts\activate on Windows
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd client
npm start
```

### API Endpoints

The FastAPI backend provides the following endpoints:

**Objects:**
- `GET /api/objects/available/{blend_count}` - Get available objects
- `GET /api/objects/random/{blend_count}/{count}` - Get random objects for selection
- `GET /api/objects/{object_id}` - Get specific object

**Scores:**
- `POST /api/scores/blend` - Process a blend
- `GET /api/scores/session/{session_id}` - Get session info
- `POST /api/scores/reset/{session_id}` - Reset session
- `GET /api/scores/new-session` - Generate new session ID

**Leaderboard:**
- `GET /api/leaderboard/{scoring_system}` - Get leaderboard for a system
- `GET /api/leaderboard/` - Get all available leaderboards
- `POST /api/leaderboard/submit/{session_id}` - Submit scores

Visit `http://localhost:5000/docs` for interactive API documentation.

## Environment Variables

### Backend (.env)

Create a `server/.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/chaos_blender
HOST=0.0.0.0
PORT=5000
```

### Frontend (.env)

Create a `client/.env` file (optional):

```env
REACT_APP_API_URL=http://localhost:5000
```

## Database Management

### Reset Database

To completely reset the database:

```bash
psql -U postgres -d chaos_blender
DROP DATABASE chaos_blender;
CREATE DATABASE chaos_blender;
\q

# Then re-run initialization
cd server/src
python init_data.py
```

### Backup Database

```bash
pg_dump chaos_blender > backup.sql
```

### Restore Database

```bash
psql chaos_blender < backup.sql
```

## Troubleshooting

### Backend Issues

**Port already in use:**
```bash
# Change PORT in server/.env
PORT=5001
```

**Database connection error:**
- Verify PostgreSQL is running: `pg_isready`
- Check DATABASE_URL in .env
- Ensure database exists: `psql -l | grep chaos_blender`

**Module not found:**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Frontend Issues

**Port 3000 already in use:**
- The dev server will automatically offer port 3001
- Or set PORT=3001 in client/.env

**API connection error:**
- Verify backend is running on http://localhost:5000
- Check browser console for CORS errors
- Ensure proxy is set in client/package.json

**Build errors:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

## Testing the Application

1. **Start both servers** (backend and frontend)
2. **Open browser** to http://localhost:3000
3. **Select 2 objects** for your first blend
4. **Click "BLEND IT!"** to blend them
5. **Watch the animation** and see your scores
6. **Continue blending** to unlock new objects and scoring systems
7. **Submit your scores** to the global leaderboard

## Next Steps

- Read [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment instructions
- Customize game objects in `server/src/init_data.py`
- Add new scoring systems in `server/src/models.py`
- Modify styling in `client/src/styles/`

## Support

If you encounter issues:
1. Check this setup guide
2. Review error messages in console/terminal
3. Verify all prerequisites are installed
4. Ensure ports are not in use
5. Check database connection

Happy blending! 🎮
