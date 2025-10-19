# 🔧 Backend Setup Guide

## Current Status

Your frontend is deployed on Vercel but showing "Backend not configured" because the `NEXT_PUBLIC_API_URL` environment variable is pointing to `localhost:8000`.

## 📋 Quick Setup Steps

### Step 1: Deploy Backend to Railway

1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose: `SomeshVermaGit/saas`
6. Click **"Add Variables"** and configure:

```bash
# Required Environment Variables for Railway Backend
OPENAI_API_KEY=sk-your-actual-openai-key
SECRET_KEY=generate-a-random-32-character-string
MONGODB_URL=mongodb+srv://user:password@cluster.mongodb.net/database
PORT=8000

# CORS - Update after getting Vercel URL
ALLOWED_ORIGINS=["https://saas-eta-mauve.vercel.app"]
```

### Step 2: Generate Public Domain in Railway

1. In your Railway backend service, go to **Settings**
2. Click on **Networking** tab
3. Under **Public Networking**, click **"Generate Domain"**
4. Copy the generated URL (e.g., `https://nexus-flow-backend.up.railway.app`)

### Step 3: Add Environment Variable to Vercel

**Option A: Via Vercel Dashboard** (Easiest)

1. Go to: https://vercel.com/arks-projects-01dfc75a/saas/settings/environment-variables
2. Click **"Add New"**
3. Enter:
   - **Name:** `NEXT_PUBLIC_API_URL`
   - **Value:** `https://nexus-flow-backend.up.railway.app` (your Railway URL)
   - **Environments:** Check all three boxes (Production, Preview, Development)
4. Click **"Save"**

**Option B: Via Vercel CLI**

```bash
vercel env add NEXT_PUBLIC_API_URL production
# When prompted, paste your Railway backend URL

vercel env add NEXT_PUBLIC_API_URL preview
vercel env add NEXT_PUBLIC_API_URL development
```

### Step 4: Update Railway Backend CORS

Go back to Railway and update the `ALLOWED_ORIGINS` variable:

```bash
ALLOWED_ORIGINS=["https://saas-eta-mauve.vercel.app","https://saas-arks-projects-01dfc75a.vercel.app","http://localhost:3000"]
```

### Step 5: Redeploy

**Vercel (Frontend):**
```bash
vercel --prod
```

Or just push to GitHub (auto-deploys):
```bash
git push
```

**Railway (Backend):**
- Automatically redeploys when you save environment variables

### Step 6: Verify Connection

1. Visit: https://saas-eta-mauve.vercel.app
2. Check the **Backend Status** card
3. Should show **🟢 Connected** with green dot
4. Click "Open Swagger Docs" to test backend directly

---

## 🗄️ Additional Services Needed

### PostgreSQL (for user data, documents)

1. In Railway, click **"New"** → **"Database"** → **"PostgreSQL"**
2. Link to your backend service
3. Railway auto-populates these variables:
   ```bash
   POSTGRES_HOST=${{POSTGRES.HOST}}
   POSTGRES_USER=${{POSTGRES.USER}}
   POSTGRES_PASSWORD=${{POSTGRES.PASSWORD}}
   POSTGRES_DB=${{POSTGRES.DATABASE}}
   ```

### Redis (for caching, sessions)

1. In Railway, click **"New"** → **"Database"** → **"Redis"**
2. Link to your backend service
3. Railway auto-populates:
   ```bash
   REDIS_URL=${{REDIS.URL}}
   ```

### MongoDB Atlas (for vector storage)

1. Go to [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Create free account
3. Create **M0 (Free)** cluster
4. Create database user with password
5. Go to **Network Access** → Add IP: `0.0.0.0/0` (allow all)
6. Get connection string:
   ```
   mongodb+srv://username:password@cluster.mongodb.net/database
   ```
7. Add to Railway as `MONGODB_URL`

---

## 📊 Complete Environment Variables List

### Railway Backend

```bash
# AI Service
OPENAI_API_KEY=sk-your-openai-key-here

# Security
SECRET_KEY=generate-random-32-chars-minimum

# Database - PostgreSQL (auto-filled by Railway)
POSTGRES_HOST=${{POSTGRES.HOST}}
POSTGRES_USER=${{POSTGRES.USER}}
POSTGRES_PASSWORD=${{POSTGRES.PASSWORD}}
POSTGRES_DB=${{POSTGRES.DATABASE}}
POSTGRES_PORT=5432

# Database - MongoDB Atlas (manual)
MONGODB_URL=mongodb+srv://user:password@cluster.mongodb.net/dbname

# Cache - Redis (auto-filled by Railway)
REDIS_URL=${{REDIS.URL}}

# CORS - Frontend URLs (IMPORTANT!)
ALLOWED_ORIGINS=["https://saas-eta-mauve.vercel.app","https://saas-arks-projects-01dfc75a.vercel.app","http://localhost:3000"]

# Server
PORT=8000
```

### Vercel Frontend

```bash
# Backend API URL (from Railway public domain)
NEXT_PUBLIC_API_URL=https://nexus-flow-backend.up.railway.app
```

---

## 🧪 Testing the Connection

### Test 1: Health Check

```bash
curl https://your-backend.up.railway.app/health
```

Should return:
```json
{"status":"healthy","version":"1.0.0"}
```

### Test 2: API Documentation

Visit: `https://your-backend.up.railway.app/docs`

Should see Swagger UI with all API endpoints.

### Test 3: Frontend Connection

Visit: `https://saas-eta-mauve.vercel.app`

Backend Status card should show:
- **Green dot** 🟢
- "Backend connected successfully!"
- Version number displayed

---

## 🐛 Troubleshooting

### Issue: Backend Status still shows localhost

**Solution:**
1. Verify `NEXT_PUBLIC_API_URL` is set in Vercel
2. Redeploy frontend: `vercel --prod`
3. Hard refresh browser: Ctrl+Shift+R

### Issue: CORS Error in Browser Console

**Solution:**
Add all your Vercel URLs to Railway `ALLOWED_ORIGINS`:
```json
["https://saas-eta-mauve.vercel.app","https://saas-arks-projects-01dfc75a.vercel.app","https://saas-git-main-arks-projects-01dfc75a.vercel.app"]
```

### Issue: Backend shows 503 Error

**Check:**
1. Is Railway backend deployed and running?
2. Check Railway logs for errors
3. Verify all required environment variables are set

### Issue: Database connection errors

**PostgreSQL:**
- Verify PostgreSQL service is linked to backend
- Check `POSTGRES_*` variables are populated

**MongoDB:**
- Verify IP whitelist includes `0.0.0.0/0`
- Check connection string is correct
- Test connection locally first

---

## 💰 Cost Estimate

```
Railway Backend:         ~$5/month
Railway PostgreSQL:      Included
Railway Redis:           Included
Vercel Frontend:         FREE (Hobby)
MongoDB Atlas M0:        FREE
OpenAI API:              Pay per use
────────────────────────────────────
Total:                   ~$5/month + OpenAI costs
```

---

## 📞 Support Links

- **Railway Dashboard:** https://railway.app
- **Vercel Dashboard:** https://vercel.com/arks-projects-01dfc75a/saas
- **Railway Docs:** https://docs.railway.app
- **Vercel Docs:** https://vercel.com/docs

---

## ✅ Checklist

- [ ] Railway backend deployed
- [ ] Public domain generated in Railway
- [ ] All environment variables set in Railway
- [ ] PostgreSQL added to Railway
- [ ] Redis added to Railway
- [ ] MongoDB Atlas configured
- [ ] `NEXT_PUBLIC_API_URL` added to Vercel
- [ ] `ALLOWED_ORIGINS` updated in Railway
- [ ] Frontend redeployed
- [ ] Backend status shows green
- [ ] `/health` endpoint responds
- [ ] `/docs` endpoint accessible

---

**Once completed, your full-stack application will be live and fully connected!** 🚀
