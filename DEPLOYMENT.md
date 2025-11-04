# Chaos Blender - Deployment Guide

This guide covers deploying Chaos Blender to production environments.

## Architecture Overview

- **Frontend**: React + TypeScript SPA
- **Backend**: FastAPI Python server
- **Database**: PostgreSQL
- **Assets**: Static sprite images

## Deployment Options

### Option 1: Separate Hosting (Recommended)

Deploy frontend and backend separately for better scalability.

**Frontend**: Vercel, Netlify, or AWS S3 + CloudFront
**Backend**: Railway, Render, Heroku, or AWS ECS
**Database**: Managed PostgreSQL (Railway, Render, AWS RDS, or DigitalOcean)

### Option 2: Single Server

Deploy both frontend and backend on a single VPS (DigitalOcean, Linode, AWS EC2).

---

## Frontend Deployment

### Deploy to Vercel

1. **Install Vercel CLI:**
```bash
npm install -g vercel
```

2. **Build the project:**
```bash
cd client
npm run build
```

3. **Deploy:**
```bash
vercel --prod
```

4. **Configure environment variables in Vercel dashboard:**
```
REACT_APP_API_URL=https://your-backend-url.com
```

### Deploy to Netlify

1. **Install Netlify CLI:**
```bash
npm install -g netlify-cli
```

2. **Build and deploy:**
```bash
cd client
npm run build
netlify deploy --prod --dir=build
```

3. **Configure environment variables in Netlify dashboard**

### Deploy to AWS S3 + CloudFront

1. **Build the project:**
```bash
cd client
npm run build
```

2. **Create S3 bucket:**
```bash
aws s3 mb s3://chaos-blender-frontend
```

3. **Upload build files:**
```bash
aws s3 sync build/ s3://chaos-blender-frontend --acl public-read
```

4. **Set up CloudFront distribution** pointing to the S3 bucket
5. **Configure custom domain** (optional)

---

## Backend Deployment

### Deploy to Railway

1. **Install Railway CLI:**
```bash
npm install -g @railway/cli
```

2. **Login and initialize:**
```bash
railway login
railway init
```

3. **Add PostgreSQL:**
```bash
railway add --plugin postgresql
```

4. **Deploy:**
```bash
cd server
railway up
```

5. **Set environment variables:**
```bash
railway variables set DATABASE_URL=$RAILWAY_POSTGRESQL_URL
railway variables set HOST=0.0.0.0
railway variables set PORT=8000
```

6. **Initialize database:**
```bash
railway run python src/init_data.py
```

### Deploy to Render

1. **Create a new Web Service** on Render dashboard
2. **Connect your GitHub repository**
3. **Configure build settings:**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `cd src && uvicorn main:app --host 0.0.0.0 --port $PORT`
4. **Add PostgreSQL database** from Render dashboard
5. **Set environment variables:**
   ```
   DATABASE_URL=<internal-postgres-url>
   HOST=0.0.0.0
   PORT=10000
   ```
6. **Deploy and initialize database**

### Deploy to Heroku

1. **Install Heroku CLI** and login:
```bash
heroku login
```

2. **Create app:**
```bash
cd server
heroku create chaos-blender-api
```

3. **Add PostgreSQL:**
```bash
heroku addons:create heroku-postgresql:mini
```

4. **Create Procfile:**
```
web: cd src && uvicorn main:app --host 0.0.0.0 --port $PORT
```

5. **Create runtime.txt:**
```
python-3.11
```

6. **Deploy:**
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

7. **Initialize database:**
```bash
heroku run python src/init_data.py
```

### Deploy to VPS (DigitalOcean, Linode, AWS EC2)

1. **Set up server** (Ubuntu 22.04 recommended)

2. **Install dependencies:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv postgresql nginx
```

3. **Clone repository:**
```bash
git clone <your-repo>
cd chaos-blender
```

4. **Set up PostgreSQL:**
```bash
sudo -u postgres psql
CREATE DATABASE chaos_blender;
CREATE USER chaos_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE chaos_blender TO chaos_user;
\q
```

5. **Set up Python environment:**
```bash
cd server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. **Create .env file:**
```bash
cat > .env << EOF
DATABASE_URL=postgresql://chaos_user:your_password@localhost:5432/chaos_blender
HOST=0.0.0.0
PORT=8000
EOF
```

7. **Initialize database:**
```bash
cd src
python init_data.py
```

8. **Set up systemd service:**
```bash
sudo nano /etc/systemd/system/chaos-blender.service
```

```ini
[Unit]
Description=Chaos Blender FastAPI
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user/chaos-blender/server/src
Environment="PATH=/home/your_user/chaos-blender/server/venv/bin"
ExecStart=/home/your_user/chaos-blender/server/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000

[Install]
WantedBy=multi-user.target
```

9. **Start service:**
```bash
sudo systemctl start chaos-blender
sudo systemctl enable chaos-blender
```

10. **Set up Nginx reverse proxy:**
```bash
sudo nano /etc/nginx/sites-available/chaos-blender
```

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/chaos-blender /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

11. **Set up SSL with Let's Encrypt:**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

## Database Migration

For production, consider using Alembic for database migrations:

1. **Install Alembic:**
```bash
pip install alembic
```

2. **Initialize Alembic:**
```bash
cd server
alembic init alembic
```

3. **Configure alembic.ini** with your DATABASE_URL

4. **Create migration:**
```bash
alembic revision --autogenerate -m "Initial migration"
```

5. **Apply migration:**
```bash
alembic upgrade head
```

---

## Environment Variables Summary

### Backend Production Environment Variables

```env
DATABASE_URL=postgresql://user:pass@host:5432/dbname
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=https://your-frontend-domain.com
```

### Frontend Production Environment Variables

```env
REACT_APP_API_URL=https://your-backend-api.com
```

---

## Security Checklist

- [ ] Use HTTPS for both frontend and backend
- [ ] Set strong PostgreSQL password
- [ ] Configure CORS to only allow your frontend domain
- [ ] Enable PostgreSQL SSL connections
- [ ] Use environment variables for secrets (never commit .env files)
- [ ] Set up firewall rules (only allow ports 80, 443, 22)
- [ ] Regular database backups
- [ ] Monitor application logs
- [ ] Set up rate limiting on API endpoints
- [ ] Enable CSP headers on frontend

---

## Monitoring and Maintenance

### Health Checks

Set up monitoring for:
- Backend: `GET /health`
- Database connection
- Response times
- Error rates

### Logging

**Backend logging:**
```python
# Add to main.py
import logging
logging.basicConfig(level=logging.INFO)
```

**View logs:**
- Railway: `railway logs`
- Render: View in dashboard
- Heroku: `heroku logs --tail`
- VPS: `journalctl -u chaos-blender -f`

### Database Backups

**Automated backups:**
```bash
# Add to crontab
0 2 * * * pg_dump chaos_blender > /backups/chaos_blender_$(date +\%Y\%m\%d).sql
```

### Updates

```bash
# Backend updates
cd server
git pull
pip install -r requirements.txt
sudo systemctl restart chaos-blender

# Frontend updates
cd client
git pull
npm install
npm run build
# Deploy build folder
```

---

## Performance Optimization

### Backend

- Use connection pooling for PostgreSQL
- Add caching for leaderboard queries
- Enable gzip compression
- Use gunicorn with multiple workers:
  ```bash
  gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
  ```

### Frontend

- Enable code splitting
- Optimize images (use WebP format)
- Enable CDN for static assets
- Add service worker for offline support
- Minify and compress assets

### Database

- Add indexes on frequently queried columns
- Set up read replicas for scaling
- Use connection pooling
- Regular VACUUM and ANALYZE

---

## Scaling Considerations

### Horizontal Scaling

- Deploy multiple backend instances behind a load balancer
- Use managed PostgreSQL with read replicas
- Implement Redis for caching and session management
- Use CDN for frontend static assets

### Vertical Scaling

- Upgrade server resources (CPU, RAM)
- Optimize database queries
- Increase connection pool size

---

## Cost Estimates

### Small Scale (Hobby Project)

- **Frontend**: Vercel/Netlify Free Tier - $0/month
- **Backend**: Railway Free Tier or Render Free - $0-5/month
- **Database**: Railway Free PostgreSQL - $0/month
- **Total**: $0-5/month

### Medium Scale (Growing User Base)

- **Frontend**: Vercel Pro - $20/month
- **Backend**: Render Standard - $25/month
- **Database**: Managed PostgreSQL - $15/month
- **Total**: ~$60/month

### Large Scale (Production)

- **Frontend**: AWS CloudFront + S3 - $50/month
- **Backend**: AWS ECS or multiple instances - $100-200/month
- **Database**: AWS RDS PostgreSQL - $50-100/month
- **CDN**: Cloudflare Pro - $20/month
- **Total**: $220-370/month

---

## Rollback Procedure

If deployment fails:

1. **Frontend**: Revert to previous Vercel/Netlify deployment
2. **Backend**:
   ```bash
   git revert HEAD
   git push
   # Or rollback on platform dashboard
   ```
3. **Database**: Restore from backup
   ```bash
   psql chaos_blender < backup.sql
   ```

---

## Support and Troubleshooting

### Common Issues

**CORS errors:**
- Update CORS_ORIGINS in backend .env
- Add to main.py: `allow_origins=["https://your-frontend.com"]`

**Database connection timeout:**
- Check DATABASE_URL
- Ensure database accepts external connections
- Verify firewall rules

**502 Bad Gateway:**
- Check backend logs
- Verify backend is running
- Check reverse proxy configuration

---

## Conclusion

Your Chaos Blender application is now deployed and ready for users! Monitor logs and performance, and scale as needed.

For questions or issues, refer to the [SETUP.md](SETUP.md) guide or check application logs.

Happy deploying! 🚀
