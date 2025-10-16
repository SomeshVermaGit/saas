# 🌐 Deployment URLs Guide

## 📍 Where Your App Will Be Accessible

### Local Development (Current)
```
Frontend:  http://localhost:3000
Backend:   http://localhost:8000
API Docs:  http://localhost:8000/docs
```

---

## 🚀 Production Deployment Options

### Option 1: Recommended Setup (Easiest)

**Frontend on Vercel + Backend on Railway**

#### Frontend (Vercel)
```
Production URL:  https://your-app-name.vercel.app
Custom Domain:   https://app.yourcompany.com (optional)
```

**Steps:**
1. Push code to GitHub: `git push`
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Set root directory: `frontend`
6. Add environment variable: `NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app`
7. Deploy!

**Result:** Live in ~2 minutes ✅

#### Backend (Railway)
```
Production URL:  https://your-backend.up.railway.app
API Docs:        https://your-backend.up.railway.app/docs
Custom Domain:   https://api.yourcompany.com (optional)
```

**Steps:**
1. Go to [railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Set root directory: `backend`
6. Add environment variables (see below)
7. Deploy!

**Required Environment Variables:**
```bash
# Railway Backend Environment Variables
OPENAI_API_KEY=sk-your-key
SECRET_KEY=generate-random-string-here
POSTGRES_HOST=<railway-provides>
POSTGRES_USER=<railway-provides>
POSTGRES_PASSWORD=<railway-provides>
POSTGRES_DB=<railway-provides>
MONGODB_URL=<from-mongodb-atlas>
REDIS_URL=<railway-provides>
ALLOWED_ORIGINS=["https://your-app-name.vercel.app"]
```

**Cost:** ~$5-20/month

---

### Option 2: All-in-One (Railway)

**Everything on Railway**

```
Frontend:    https://your-app-frontend.up.railway.app
Backend:     https://your-app-backend.up.railway.app
API Docs:    https://your-app-backend.up.railway.app/docs
```

**Cost:** ~$10-30/month

---

### Option 3: AWS (Production Scale)

**Frontend on CloudFront + S3**
```
CloudFront:      https://d1234abcd.cloudfront.net
Custom Domain:   https://app.yourcompany.com
```

**Backend on ECS/EC2**
```
Load Balancer:   https://your-alb.region.elb.amazonaws.com
API Gateway:     https://api.yourcompany.com
API Docs:        https://api.yourcompany.com/docs
```

**Cost:** ~$50-200/month (depends on traffic)

---

### Option 4: Self-Hosted (VPS)

**Your Own Server (DigitalOcean, Linode, etc.)**

```
Server IP:       http://123.45.67.89
Custom Domain:   https://yourdomain.com
API:             https://api.yourdomain.com
Frontend:        https://app.yourdomain.com
```

**Cost:** ~$5-20/month

---

## 🎯 Recommended for This Project

### Best for Getting Started (Free/Cheap)

**Frontend: Vercel** (Free tier available)
- URL: `https://ai-knowledge-assistant.vercel.app`
- Auto-deploys on git push
- Free SSL certificate
- Global CDN
- **Cost: FREE** (hobby plan)

**Backend: Railway** ($5 credit free, then pay-as-you-go)
- URL: `https://ai-knowledge-backend.up.railway.app`
- Includes PostgreSQL + Redis
- Auto-deploys on git push
- Easy environment variables
- **Cost: ~$5-10/month**

**Database: MongoDB Atlas** (Free tier)
- For vector search
- 512MB free forever
- **Cost: FREE**

**Total Monthly Cost: ~$5-10** 🎉

---

## 📋 Step-by-Step Deployment

### Step 1: Prepare Your Code

Already done! ✅ Your repository is ready.

### Step 2: Deploy Backend to Railway

```bash
# 1. Push to GitHub (if not done)
git push

# 2. Go to railway.app and sign in with GitHub
# 3. Click "New Project" → "Deploy from GitHub repo"
# 4. Select: SomeshVermaGit/saas
# 5. Root Directory: backend
# 6. Add environment variables:

OPENAI_API_KEY=sk-your-actual-key
SECRET_KEY=your-secret-key-min-32-chars
POSTGRES_HOST=${{POSTGRES.HOST}}  # Railway provides
POSTGRES_USER=${{POSTGRES.USER}}
POSTGRES_PASSWORD=${{POSTGRES.PASSWORD}}
POSTGRES_DB=${{POSTGRES.DATABASE}}
MONGODB_URL=mongodb+srv://user:pass@cluster.mongodb.net/dbname
REDIS_URL=${{REDIS.URL}}  # Railway provides
ALLOWED_ORIGINS=["https://your-frontend.vercel.app"]

# 7. Railway will auto-detect Python and deploy
# 8. You'll get a URL like: https://ai-knowledge-backend.up.railway.app
```

### Step 3: Set Up MongoDB Atlas

```bash
# 1. Go to mongodb.com/cloud/atlas
# 2. Create free account
# 3. Create cluster (M0 Free tier)
# 4. Create database user
# 5. Whitelist all IPs (0.0.0.0/0) for Railway access
# 6. Get connection string:
#    mongodb+srv://<user>:<password>@cluster.mongodb.net/<dbname>
# 7. Add to Railway environment variables as MONGODB_URL
```

### Step 4: Deploy Frontend to Vercel

```bash
# 1. Go to vercel.com and sign in with GitHub
# 2. Click "New Project"
# 3. Import your repository: SomeshVermaGit/saas
# 4. Root Directory: frontend
# 5. Framework Preset: Next.js (auto-detected)
# 6. Add environment variable:

NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app

# 7. Click "Deploy"
# 8. You'll get a URL like: https://ai-knowledge-assistant.vercel.app
```

### Step 5: Update Backend CORS

Go back to Railway and update `ALLOWED_ORIGINS`:
```bash
ALLOWED_ORIGINS=["https://ai-knowledge-assistant.vercel.app"]
```

### Step 6: Test Your Deployment

```bash
# Visit your frontend URL
https://ai-knowledge-assistant.vercel.app

# Test backend health
curl https://your-backend.up.railway.app/health

# Check API docs
https://your-backend.up.railway.app/docs
```

---

## 🌐 Custom Domain Setup (Optional)

### For Vercel (Frontend)

1. Buy domain (e.g., from Namecheap, GoDaddy)
2. In Vercel: Settings → Domains
3. Add domain: `app.yourcompany.com`
4. Update DNS records as instructed
5. SSL auto-configured ✅

### For Railway (Backend)

1. In Railway: Settings → Networking
2. Add custom domain: `api.yourcompany.com`
3. Update DNS CNAME record
4. SSL auto-configured ✅

---

## 📊 Expected URLs After Deployment

### Development
```
Local Frontend:     http://localhost:3000
Local Backend:      http://localhost:8000
Local API Docs:     http://localhost:8000/docs
```

### Production (Recommended Setup)
```
Production Frontend:  https://ai-knowledge-assistant.vercel.app
Production Backend:   https://ai-knowledge-backend.up.railway.app
Production API Docs:  https://ai-knowledge-backend.up.railway.app/docs
Health Check:         https://ai-knowledge-backend.up.railway.app/health
```

### With Custom Domain
```
Frontend:  https://app.yourcompany.com
Backend:   https://api.yourcompany.com
API Docs:  https://api.yourcompany.com/docs
```

---

## 🔐 Security Checklist

Before going live:

- [ ] Change `SECRET_KEY` in production (generate new random string)
- [ ] Update `ALLOWED_ORIGINS` with actual frontend URL
- [ ] Use environment variables for all secrets
- [ ] Enable HTTPS only (Vercel/Railway do this automatically)
- [ ] Set up MongoDB Atlas network access rules
- [ ] Configure rate limiting
- [ ] Add monitoring (Sentry, LogRocket)

---

## 💰 Cost Breakdown

### Free Tier (For Testing)
```
Vercel (Frontend):        $0/month (free tier)
Railway (Backend):        $5/month (after free credit)
MongoDB Atlas:            $0/month (512MB free)
Redis on Railway:         Included
PostgreSQL on Railway:    Included
──────────────────────────────────
Total:                    ~$5/month
```

### Production Scale
```
Vercel Pro:              $20/month
Railway (scaled):        $20-50/month
MongoDB Atlas M10:       $57/month
──────────────────────────────────
Total:                   ~$97-127/month
```

---

## 🚀 Quick Deploy Commands

### If Using Railway CLI
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Deploy backend
cd backend
railway init
railway up

# Deploy frontend (use Vercel for frontend)
```

### If Using Vercel CLI
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy frontend
cd frontend
vercel --prod
```

---

## 📞 Your Deployment URLs Will Be

**After following the guide above:**

```
✅ Frontend: https://[your-project-name].vercel.app
✅ Backend:  https://[your-project-name].up.railway.app
✅ API Docs: https://[your-project-name].up.railway.app/docs
```

You can customize the subdomain names in Vercel and Railway settings!

---

## 🎯 Next Steps

1. **Push your code:** `git push`
2. **Deploy backend** to Railway (5 minutes)
3. **Deploy frontend** to Vercel (2 minutes)
4. **Test** your live app
5. **Share** the link with users!

---

## ✅ Summary

**Question:** "What will be the link?"

**Answer:**
- **Development:** http://localhost:3000 (already works)
- **Production (recommended):**
  - Frontend: `https://your-app-name.vercel.app`
  - Backend: `https://your-backend.up.railway.app`
- **Custom domain:** Whatever you want! (e.g., `https://app.yourcompany.com`)

**Time to deploy:** ~15-30 minutes
**Cost:** ~$5/month to start

**When you're ready to deploy, follow the "Step-by-Step Deployment" section above!** 🚀

---

*Current status: Code is ready to deploy!*
*Just push to GitHub and follow the deployment steps.*
