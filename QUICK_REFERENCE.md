# 🚀 Quick Reference Card

## 🌐 Your URLs

### Frontend (Live Now!)
```
Production:  https://saas-eta-mauve.vercel.app
Dashboard:   https://vercel.com/arks-projects-01dfc75a/saas
```

### Backend (Need to Generate Public URL)
```
Internal:    ark.railway.internal (private network only)
Public:      [Generate in Railway Settings → Networking]
API Docs:    {backend-url}/docs
Health:      {backend-url}/health
```

---

## ⚡ Quick Commands

### Deploy to Vercel
```bash
cd /d/projects/saas
vercel --prod
```

### Deploy via Git (Auto-Deploy)
```bash
git add .
git commit -m "Your message"
git push
# Vercel auto-deploys!
```

### Test Locally
```bash
# Frontend
cd frontend
npm run dev
# Visit: http://localhost:3000

# Backend
cd backend
uvicorn app.main:app --reload
# Visit: http://localhost:8000/docs
```

---

## 🔑 Environment Variables

### Vercel (Frontend)
```bash
NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app
```

### Railway (Backend)
```bash
# Required
OPENAI_API_KEY=sk-your-key
SECRET_KEY=random-32-chars
ALLOWED_ORIGINS=["https://saas-eta-mauve.vercel.app"]

# Auto-filled by Railway
POSTGRES_HOST=${{POSTGRES.HOST}}
POSTGRES_USER=${{POSTGRES.USER}}
POSTGRES_PASSWORD=${{POSTGRES.PASSWORD}}
POSTGRES_DB=${{POSTGRES.DATABASE}}
REDIS_URL=${{REDIS.URL}}

# MongoDB Atlas
MONGODB_URL=mongodb+srv://...

# Server
PORT=8000
```

---

## ✅ Setup Checklist

### Frontend ✅
- [x] Deployed to Vercel
- [x] Auto-deploy enabled
- [x] Speed Insights added
- [x] API client created
- [x] Backend status widget

### Backend ⏳
- [ ] Generate public domain in Railway
- [ ] Add environment variables
- [ ] Add PostgreSQL database
- [ ] Add Redis
- [ ] Configure MongoDB Atlas
- [ ] Update CORS settings

### Integration ⏳
- [ ] Add `NEXT_PUBLIC_API_URL` to Vercel
- [ ] Add Vercel URL to Railway `ALLOWED_ORIGINS`
- [ ] Test connection (green status on homepage)

---

## 🔗 Quick Links

| Service | Link |
|---------|------|
| **Live Frontend** | https://saas-eta-mauve.vercel.app |
| **Vercel Dashboard** | https://vercel.com/arks-projects-01dfc75a/saas |
| **Railway Dashboard** | https://railway.app |
| **GitHub Repo** | https://github.com/SomeshVermaGit/saas |
| **Add Env Vars** | https://vercel.com/arks-projects-01dfc75a/saas/settings/environment-variables |

---

## 🆘 Troubleshooting

### Backend shows "error" on homepage
1. Check if Railway backend is deployed
2. Verify public domain is generated
3. Confirm `NEXT_PUBLIC_API_URL` is set in Vercel
4. Check CORS settings in Railway

### CORS error in console
Add all Vercel URLs to Railway `ALLOWED_ORIGINS`:
```json
["https://saas-eta-mauve.vercel.app","https://saas-arks-projects-01dfc75a.vercel.app","http://localhost:3000"]
```

### Changes not showing
1. Hard refresh: Ctrl+Shift+R (or Cmd+Shift+R)
2. Check deployment status in Vercel
3. Verify latest commit is deployed

---

## 📚 Documentation

- [DEPLOYMENT_COMPLETE.md](./DEPLOYMENT_COMPLETE.md) - Full deployment guide
- [VERCEL_RAILWAY_CONNECTION.md](./VERCEL_RAILWAY_CONNECTION.md) - Connection guide
- [RAILWAY_SETUP.md](./RAILWAY_SETUP.md) - Railway configuration

---

## 🎯 Next Step

**⚠️ ACTION REQUIRED**: Generate Railway backend public domain

1. Go to https://railway.app
2. Select your backend service
3. Settings → Networking → Generate Domain
4. Copy the URL
5. Add to Vercel as `NEXT_PUBLIC_API_URL`
6. Add Vercel URL to Railway `ALLOWED_ORIGINS`
7. Redeploy both services

Then visit **https://saas-eta-mauve.vercel.app** and see the green status! 🟢

---

*Generated: October 19, 2025*
