# 🚂 Railway Deployment Guide

## 📋 Quick Configuration Reference

### Backend Service Settings

| Setting | Value |
|---------|-------|
| **Root Directory** | `backend` |
| **Builder** | Railpack (auto-detects Dockerfile) |
| **Build Command** | (empty - uses Dockerfile) |
| **Start Command** | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |
| **Healthcheck Path** | `/health` |
| **Watch Paths** | `backend/**` |
| **Port** | 8000 (set via env var) |

### Frontend Service Settings

| Setting | Value |
|---------|-------|
| **Root Directory** | `frontend` |
| **Builder** | Railpack (auto-detects Next.js) |
| **Build Command** | `npm install && npm run build` |
| **Start Command** | `npm run start` |
| **Watch Paths** | `frontend/**` |
| **Port** | 3000 (default for Next.js) |

---

## 🎯 Step-by-Step Setup

### Step 1: Push Code to GitHub

```bash
git add .
git commit -m "Add Railway configuration files"
git push
```

### Step 2: Create Railway Project

1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose: `SomeshVermaGit/saas`

### Step 3: Set Up Backend Service

1. **Create Service:**
   - In Railway dashboard, click **"New Service"**
   - Select **"GitHub Repo"**
   - Choose your repository

2. **Configure Root Directory:**
   - Go to **Settings** → **Build**
   - Set **Root Directory**: `backend`
   - Railway will auto-detect the Dockerfile

3. **Add Environment Variables:**
   - Go to **Settings** → **Variables**
   - Add these variables:

```bash
# Required - Add Your Keys
OPENAI_API_KEY=sk-your-actual-openai-key

# Security - Generate a random 32+ character string
SECRET_KEY=your-super-secret-random-32-char-string

# Database - Will be auto-filled when you add PostgreSQL
POSTGRES_HOST=${{POSTGRES.HOST}}
POSTGRES_USER=${{POSTGRES.USER}}
POSTGRES_PASSWORD=${{POSTGRES.PASSWORD}}
POSTGRES_DB=${{POSTGRES.DATABASE}}
POSTGRES_PORT=5432

# MongoDB Atlas - Get from mongodb.com/cloud/atlas
MONGODB_URL=mongodb+srv://user:password@cluster.mongodb.net/database

# Redis - Will be auto-filled when you add Redis
REDIS_URL=${{REDIS.URL}}

# CORS - Update after frontend deployment
ALLOWED_ORIGINS=["https://your-frontend-url.up.railway.app"]

# Port
PORT=8000
```

4. **Add PostgreSQL Database:**
   - Click **"New"** → **"Database"** → **"Add PostgreSQL"**
   - Link it to your backend service
   - Variables auto-populate

5. **Add Redis:**
   - Click **"New"** → **"Database"** → **"Add Redis"**
   - Link it to your backend service
   - `REDIS_URL` auto-populates

6. **Deploy:**
   - Railway will auto-deploy
   - Wait for build to complete
   - Copy the backend URL: `https://your-backend.up.railway.app`

### Step 4: Set Up Frontend Service

1. **Create Service:**
   - Click **"New Service"**
   - Select same GitHub repo

2. **Configure Root Directory:**
   - Go to **Settings** → **Build**
   - Set **Root Directory**: `frontend`

3. **Set Build & Start Commands:**
   - **Build Command**: `npm install && npm run build`
   - **Start Command**: `npm run start`

4. **Add Environment Variables:**

```bash
# Backend API URL (from Step 3)
NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app

# Port (optional, Next.js defaults to 3000)
PORT=3000
```

5. **Deploy:**
   - Railway deploys automatically
   - Copy frontend URL: `https://your-frontend.up.railway.app`

### Step 5: Update Backend CORS

1. Go back to **Backend Service** → **Variables**
2. Update `ALLOWED_ORIGINS`:
```bash
ALLOWED_ORIGINS=["https://your-frontend.up.railway.app"]
```
3. Save (auto-redeploys)

### Step 6: Set Up MongoDB Atlas (Free)

1. Go to [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Create free account
3. **Create Cluster:**
   - Choose **M0 Free** tier
   - Select region closest to Railway backend
   - Create cluster

4. **Create Database User:**
   - Security → Database Access
   - Add new user with password
   - Save credentials

5. **Allow Railway Access:**
   - Security → Network Access
   - Click **"Add IP Address"**
   - Select **"Allow Access from Anywhere"** (0.0.0.0/0)

6. **Get Connection String:**
   - Click **"Connect"** on your cluster
   - Choose **"Connect your application"**
   - Copy connection string:
   ```
   mongodb+srv://<username>:<password>@cluster.mongodb.net/<database>
   ```
   - Replace `<username>`, `<password>`, `<database>`

7. **Add to Railway:**
   - Backend Service → Variables
   - Update `MONGODB_URL` with your connection string

---

## 🔧 Railway Dashboard Settings Reference

### Networking

**Backend:**
- ✅ **Public Networking**: Enable
- ✅ **Generate Domain**: Click to get public URL
- ✅ **Private Networking**: `backend.railway.internal`
- 📝 **Custom Domain** (optional): Add your own domain

**Frontend:**
- ✅ **Public Networking**: Enable
- ✅ **Generate Domain**: Click to get public URL
- 📝 **Custom Domain** (optional): Add your own domain

### Build Settings

**Backend:**
- **Builder**: Railpack ✅
- **Metal Build Environment**: Optional (beta)
- **Build Command**: (empty - uses Dockerfile)
- **Watch Paths**:
  - Add: `backend/**`
  - Add: `!backend/__pycache__/**`

**Frontend:**
- **Builder**: Railpack ✅
- **Build Command**: `npm install && npm run build`
- **Watch Paths**:
  - Add: `frontend/**`
  - Add: `!frontend/node_modules/**`
  - Add: `!frontend/.next/**`

### Deploy Settings

**Both Services:**
- **Start Command**: (see table above)
- **Regions**: US West (or closest to you)
- **Replicas**: 1
- **Restart Policy**: On Failure
- **Max Restart Retries**: 10

---

## ✅ Verification Checklist

After deployment, verify everything works:

### Backend Health Check
```bash
curl https://your-backend.up.railway.app/health
```
Should return: `{"status": "healthy"}`

### API Documentation
Visit: `https://your-backend.up.railway.app/docs`

### Frontend
Visit: `https://your-frontend.up.railway.app`

### Database Connections
Check Railway logs:
- PostgreSQL: Connected ✅
- Redis: Connected ✅
- MongoDB: Connected ✅

---

## 🎨 Custom Domain Setup (Optional)

### Backend (api.yourcompany.com)

1. **In Railway:**
   - Backend Service → Settings → Networking
   - Click **"Custom Domain"**
   - Enter: `api.yourcompany.com`

2. **In Your DNS Provider:**
   - Add CNAME record:
   ```
   Type: CNAME
   Name: api
   Value: <provided-by-railway>.up.railway.app
   TTL: 3600
   ```

3. **Wait for SSL:**
   - Railway auto-generates SSL certificate
   - Usually takes 5-10 minutes

### Frontend (app.yourcompany.com)

Same process as backend, use subdomain `app` instead.

---

## 💰 Cost Estimate

### Hobby/Trial Phase
```
Backend Service:      $5/month
Frontend Service:     $5/month
PostgreSQL:           Included
Redis:                Included
MongoDB Atlas:        FREE (M0 tier)
──────────────────────────────
Total:                ~$10/month
```

### Production Scale
```
Backend (scaled):     $20/month
Frontend (scaled):    $10/month
PostgreSQL:           Included
Redis:                Included
MongoDB Atlas M10:    $57/month
──────────────────────────────
Total:                ~$87/month
```

**Free Trial:** Railway gives $5 free credit to start!

---

## 🐛 Troubleshooting

### Build Fails

**Backend:**
- Check `requirements.txt` exists in `backend/`
- Verify Dockerfile syntax
- Check Railway logs for Python errors

**Frontend:**
- Ensure `package.json` exists in `frontend/`
- Check for build errors in logs
- Verify Node version compatibility (should be 20+)

### Connection Errors

**CORS Issues:**
- Verify `ALLOWED_ORIGINS` includes frontend URL
- No trailing slash in URLs
- Use HTTPS, not HTTP

**Database Connection:**
- Check environment variables are set
- Verify MongoDB IP whitelist includes 0.0.0.0/0
- Test connection strings locally first

### Environment Variables Not Working

- Must be in format: `KEY=value` (no spaces around `=`)
- For arrays: `KEY=["value1","value2"]` (JSON format)
- For Railway variables: `${{SERVICE.VARIABLE}}`

---

## 📊 Monitoring & Logs

### View Logs

**In Railway Dashboard:**
1. Select your service
2. Click **"Logs"** tab
3. See real-time logs

**Filter Logs:**
- Click "Filter" to search
- Errors appear in red
- Warnings in yellow

### Metrics

**In Railway Dashboard:**
1. Select service
2. Click **"Metrics"** tab
3. View:
   - CPU usage
   - Memory usage
   - Network traffic
   - Request latency

---

## 🚀 CI/CD (Auto-Deploy)

Railway automatically deploys when you push to GitHub!

### Setup Auto-Deploy

1. **Enable in Railway:**
   - Service Settings → General
   - **"Wait for CI"**: Enable if using GitHub Actions
   - Railway monitors your branch

2. **Deploy Trigger:**
   ```bash
   git add .
   git commit -m "Update feature"
   git push
   ```
   - Railway detects changes in watch paths
   - Builds and deploys automatically

### Manual Deploy

If needed:
1. Service → Deployments
2. Click **"Deploy"**
3. Or use Railway CLI: `railway up`

---

## 🎯 Quick Reference URLs

After setup, you'll have:

```
Backend API:         https://backend-production-xxxx.up.railway.app
Backend API Docs:    https://backend-production-xxxx.up.railway.app/docs
Frontend:            https://frontend-production-xxxx.up.railway.app
PostgreSQL:          Internal (via environment variables)
Redis:               Internal (via REDIS_URL)
MongoDB:             External (MongoDB Atlas)
```

---

## 📞 Support

- **Railway Docs:** [docs.railway.app](https://docs.railway.app)
- **Discord:** [discord.gg/railway](https://discord.gg/railway)
- **MongoDB Atlas:** [mongodb.com/docs/atlas](https://www.mongodb.com/docs/atlas)

---

## ✨ Next Steps

1. ✅ Push code to GitHub
2. ✅ Follow steps above
3. ✅ Deploy and test
4. 🎉 Share your app!

**Your deployment should take ~15-20 minutes total.**

Good luck! 🚀
