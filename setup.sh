#!/bin/bash

# Chaos Blender - Complete Setup Script
# This script automates the entire setup process

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🎮 Chaos Blender - Complete Setup${NC}"
echo "=================================="
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Check prerequisites
echo "📋 Checking prerequisites..."
echo ""

# Check Docker
if command_exists docker; then
    if docker info &> /dev/null; then
        echo -e "${GREEN}✅ Docker${NC}"
        USE_DOCKER=true
    else
        echo -e "${YELLOW}⚠️  Docker installed but not running${NC}"
        echo "   Please start Docker Desktop"
        USE_DOCKER=false
    fi
else
    echo -e "${YELLOW}⚠️  Docker not installed${NC}"
    USE_DOCKER=false
fi

# Check Python
if command_exists python3; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo -e "${GREEN}✅ Python $PYTHON_VERSION${NC}"
else
    echo -e "${RED}❌ Python 3 not found${NC}"
    echo "   Please install Python 3.9 or higher"
    exit 1
fi

# Check Node.js
if command_exists node; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✅ Node.js $NODE_VERSION${NC}"
else
    echo -e "${RED}❌ Node.js not found${NC}"
    echo "   Please install Node.js 16 or higher"
    exit 1
fi

# Check npm
if command_exists npm; then
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✅ npm $NPM_VERSION${NC}"
else
    echo -e "${RED}❌ npm not found${NC}"
    exit 1
fi

# Check PostgreSQL (only if not using Docker)
if [ "$USE_DOCKER" = false ]; then
    if command_exists psql; then
        echo -e "${GREEN}✅ PostgreSQL${NC}"
    else
        echo -e "${RED}❌ PostgreSQL not found${NC}"
        echo "   Please install PostgreSQL or use Docker"
        exit 1
    fi
fi

echo ""
echo "=================================="
echo ""

# Step 1: Database Setup
echo -e "${BLUE}📊 Step 1: Database Setup${NC}"
echo ""

if [ "$USE_DOCKER" = true ]; then
    echo "Using Docker for PostgreSQL..."
    ./start-docker.sh
else
    echo "Please set up PostgreSQL manually:"
    echo "  psql -U postgres"
    echo "  CREATE DATABASE chaos_blender;"
    echo "  \q"
    read -p "Press Enter after creating the database..."
fi

echo ""

# Step 2: Backend Setup
echo -e "${BLUE}🔧 Step 2: Backend Setup${NC}"
echo ""

cd server

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

# Create .env file
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
else
    echo ".env file already exists"
fi

# Initialize database
echo "Initializing database with game data..."
cd src
python init_data.py
cd ../..

echo -e "${GREEN}✅ Backend setup complete${NC}"
echo ""

# Step 3: Frontend Setup
echo -e "${BLUE}🎨 Step 3: Frontend Setup${NC}"
echo ""

cd client

# Install dependencies
echo "Installing Node.js dependencies..."
npm install --quiet

echo -e "${GREEN}✅ Frontend setup complete${NC}"
echo ""

cd ..

# Final instructions
echo "=================================="
echo -e "${GREEN}✨ Setup Complete!${NC}"
echo "=================================="
echo ""
echo "🚀 To start the application:"
echo ""
echo "   Terminal 1 - Backend:"
echo "   $ cd server/src"
echo "   $ source ../venv/bin/activate"
echo "   $ python main.py"
echo ""
echo "   Terminal 2 - Frontend:"
echo "   $ cd client"
echo "   $ npm start"
echo ""
echo "Then open http://localhost:3000 in your browser"
echo ""
echo "📚 Documentation:"
echo "   - SETUP.md - Detailed setup guide"
echo "   - DOCKER.md - Docker guide"
echo "   - DEPLOYMENT.md - Production deployment"
echo ""
echo "Happy blending! 🎮✨"
