# 🎮 Chaos Blender

A retro pixel art web-based blending game where you blend increasingly absurd objects to earn points across multiple chaotic scoring systems.

![Status](https://img.shields.io/badge/status-ready-brightgreen)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![React](https://img.shields.io/badge/React-18.2-blue)

## 🌟 Features

### Progressive Object System
- Start with mundane fruits and vegetables
- Unlock increasingly bizarre and magical items as you blend
- 22+ unique objects across multiple categories
- Extensible system for adding new objects

### 10 Unique Scoring Systems
- **Nutritional Value** - How healthy is your concoction?
- **Impossibility Index** - How physically impossible is this blend?
- **Awful Colour** - How visually disturbing is this mixture?
- **Deep Lore** - How much forbidden knowledge does this contain?
- **Gift Quality** - Would you give this to someone you care about?
- **Chaos Energy** - Raw chaotic potential emanating from the blend
- **Temporal Displacement** - How much does this bend the fabric of time?
- **Existential Dread** - How much does this make you question reality?
- **Aesthetic Vibes** - Pure vibes radiating from this blend
- **Forbidden Power** - Ancient power that mortals should not possess

### Retro Pixel Art Aesthetic
- Vibrant retro gaming visuals
- Elaborate particle effects when blending
- Smooth 60fps animations
- Responsive design for mobile and desktop

### Global Leaderboards
- Compete with players worldwide
- Separate leaderboards for each scoring system
- Real-time score tracking
- Submit your best runs

### Audio Feedback
- Dynamic blending sound effects (Web Audio API)
- Unlock notifications
- Selection feedback
- Fully synthesized sounds (no audio files needed)

## 🏗️ Technology Stack

### Frontend
- **React 18** with **TypeScript** for type-safe development
- **React Spring** for smooth animations and particle effects
- **Axios** for API communication
- **CSS3** for retro pixel art styling
- **Web Audio API** for sound effects

### Backend
- **FastAPI** (Python) for high-performance API
- **SQLAlchemy** for database ORM
- **Pydantic** for data validation
- **Uvicorn** as ASGI server

### Database
- **PostgreSQL** for data persistence
- Optimized schema for fast queries
- Support for global leaderboards

## 📁 Project Structure

```
chaos-blender/
├── client/                     # React frontend (TypeScript)
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/         # React components
│   │   │   ├── Blender.tsx
│   │   │   ├── ObjectSelection.tsx
│   │   │   ├── ScoreDisplay.tsx
│   │   │   ├── Leaderboard.tsx
│   │   │   ├── GameHeader.tsx
│   │   │   └── Particles.tsx
│   │   ├── types/              # TypeScript type definitions
│   │   │   └── index.ts
│   │   ├── utils/              # Utility functions
│   │   │   ├── api.ts
│   │   │   ├── session.ts
│   │   │   └── audio.ts
│   │   ├── App.tsx
│   │   ├── index.tsx
│   │   └── styles/             # CSS files
│   ├── package.json
│   └── tsconfig.json
├── server/                     # FastAPI backend (Python)
│   ├── src/
│   │   ├── routes/             # API routes
│   │   │   ├── objects.py
│   │   │   ├── scores.py
│   │   │   └── leaderboard.py
│   │   ├── models.py           # Database models
│   │   ├── schemas.py          # Pydantic schemas
│   │   ├── database.py         # Database configuration
│   │   ├── init_data.py        # Database initialization
│   │   └── main.py             # FastAPI application
│   ├── requirements.txt
│   └── .env.example
├── SETUP.md                    # Setup instructions
├── DEPLOYMENT.md               # Deployment guide
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

**Option A: Docker (Easiest)**
- Docker Desktop

**Option B: Manual Setup**
- Node.js v16+
- Python 3.9+
- PostgreSQL 14+

### Installation

#### ⚡ Automated Setup (Easiest)

Run the automated setup script:

```bash
git clone <your-repo-url>
cd chaos-blender
./setup.sh
```

This script will:
- Check prerequisites
- Set up PostgreSQL (Docker or manual)
- Install backend dependencies
- Install frontend dependencies
- Initialize the database

Or choose Docker or Manual setup:

#### 🐳 Docker Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd chaos-blender
   ```

2. **Start the database**
   ```bash
   docker-compose -f docker-compose.db-only.yml up -d
   ```

3. **Set up the backend**
   ```bash
   cd server
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

   # Create .env file (already configured for Docker database)
   cp .env.example .env

   # Initialize database
   cd src
   python init_data.py
   ```

4. **Set up the frontend**
   ```bash
   cd client
   npm install
   ```

See **[DOCKER.md](DOCKER.md)** for complete Docker guide including full-stack setup.

#### 📝 Manual Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd chaos-blender
   ```

2. **Set up the database**
   ```bash
   psql -U postgres
   CREATE DATABASE chaos_blender;
   \q
   ```

3. **Set up the backend**
   ```bash
   cd server
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

   # Create .env file
   echo "DATABASE_URL=postgresql://postgres:password@localhost:5432/chaos_blender" > .env

   # Initialize database
   cd src
   python init_data.py
   ```

4. **Set up the frontend**
   ```bash
   cd client
   npm install
   ```

### Running the Application

**Terminal 1 - Backend:**
```bash
cd server/src
source ../venv/bin/activate
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd client
npm start
```

Open your browser to **http://localhost:3000**

## 🎯 How to Play

1. **Initial Blend**: Choose 2 of 3 starting objects
2. **Subsequent Blends**: After each blend, choose 1 of 3 objects to add
3. **Unlock New Objects**: As you blend more items, stranger objects become available
4. **Discover Scoring Systems**: Scoring categories are revealed as you blend objects that contribute to them
5. **Compete**: Submit your scores to the global leaderboard

## 📚 Documentation

- **[SETUP.md](SETUP.md)** - Detailed setup and development guide
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Production deployment instructions
- **API Documentation** - Available at `http://localhost:5000/docs` when backend is running

## 🔌 API Endpoints

### Objects
- `GET /api/objects/available/{blend_count}` - Get available objects
- `GET /api/objects/random/{blend_count}/{count}` - Get random objects for selection

### Scores
- `POST /api/scores/blend` - Process a blend
- `GET /api/scores/session/{session_id}` - Get session info
- `POST /api/scores/reset/{session_id}` - Reset session

### Leaderboard
- `GET /api/leaderboard/{scoring_system}` - Get leaderboard for a scoring system
- `POST /api/leaderboard/submit/{session_id}` - Submit scores

Visit `http://localhost:5000/docs` for interactive API documentation.

## 🎨 Customization

### Adding New Objects

Edit `server/src/init_data.py`:

```python
{
    "name": "Your Object",
    "category": "magical",
    "unlock_threshold": 5,
    "sprite_path": "/sprites/your_object.png",
    "description": "Description here",
    "rarity": "rare",
    "scores": {
        "chaos_energy": 50.5,
        "deep_lore": 30.2
    }
}
```

### Adding New Scoring Systems

1. Add to `server/src/init_data.py` in `init_scoring_systems()`
2. Update `client/src/components/ScoreDisplay.tsx` with display info

### Styling

All CSS files are in `client/src/components/` and use:
- Press Start 2P font for pixel art aesthetic
- Vibrant retro color palette
- CSS animations for smooth effects

## 🧪 Testing

### Backend Tests
```bash
cd server
pytest
```

### Frontend Tests
```bash
cd client
npm test
```

## 📦 Building for Production

### Frontend
```bash
cd client
npm run build
```

### Backend
```bash
cd server
pip install -r requirements.txt
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete deployment instructions.

## 🔐 Security

- API endpoints are validated with Pydantic
- PostgreSQL prepared statements prevent SQL injection
- CORS configured for specific origins
- Session-based tracking (no authentication required)
- Rate limiting recommended for production

## 🐛 Troubleshooting

### Backend won't start
- Check PostgreSQL is running: `pg_isready`
- Verify DATABASE_URL in `.env`
- Ensure database is initialized: `python init_data.py`

### Frontend build errors
- Clear node_modules: `rm -rf node_modules && npm install`
- Check Node.js version: `node -v` (should be 16+)

### Database connection errors
- Check PostgreSQL logs
- Verify credentials in DATABASE_URL
- Ensure PostgreSQL accepts connections

See [SETUP.md](SETUP.md) for more troubleshooting tips.

## 🚀 Performance

- **Frontend**: Optimized React rendering with hooks
- **Backend**: FastAPI async capabilities for high concurrency
- **Database**: Indexed queries for fast leaderboard access
- **Animations**: 60fps with React Spring
- **Audio**: Synthesized sounds using Web Audio API (no file loading)

## 🗺️ Roadmap

- [ ] Add more objects (50+ total)
- [ ] Implement achievements system
- [ ] Add daily challenges
- [ ] Create multiplayer mode
- [ ] Add object trading system
- [ ] Implement seasonal events
- [ ] Create mobile apps (React Native)
- [ ] Add social sharing features

## 📄 License

MIT License - feel free to use this project for learning or your own games!

## 🤝 Contributing

Contributions welcome! Areas to contribute:
- New game objects and scoring systems
- UI/UX improvements
- Performance optimizations
- Bug fixes
- Documentation improvements

## 👏 Credits

- Built with React, FastAPI, and PostgreSQL
- Pixel art aesthetic inspired by retro gaming
- Sound effects generated with Web Audio API

## 📞 Support

For issues, questions, or suggestions:
- Check [SETUP.md](SETUP.md) for setup help
- Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment help
- Review API docs at `/docs` endpoint
- Check browser console and backend logs for errors

---

**Made with ⚡ and chaos**

Happy Blending! 🎮✨
# chaos-blender
