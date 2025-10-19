# 🔗 Connecting Vercel Frontend to Railway Backend

## Current Setup

### Frontend (Vercel)
- **URL**: https://saas-eta-mauve.vercel.app
- **Framework**: Next.js 15.5.5
- **Deployment**: Auto-deploy on git push

### Backend (Railway)
- **Internal URL**: `ark.railway.internal` (private network)
- **Public URL**: You need to generate this in Railway
- **Framework**: FastAPI (Python)

---

## 📋 Setup Steps

### 1. Get Railway Backend Public URL

1. Go to [railway.app](https://railway.app)
2. Select your backend service
3. Navigate to **Settings** → **Networking**
4. Under **Public Networking**, click **"Generate Domain"**
5. Copy the generated URL (e.g., `https://backend-production-xxxx.up.railway.app`)

### 2. Add Environment Variable to Vercel

**Option A: Via Vercel Dashboard** (Recommended)

1. Go to: https://vercel.com/arks-projects-01dfc75a/saas/settings/environment-variables
2. Click **"Add New"**
3. Enter the following:
   - **Name**: `NEXT_PUBLIC_API_URL`
   - **Value**: `https://your-backend.up.railway.app` (use your actual Railway URL)
   - **Environments**: Check all three (Production, Preview, Development)
4. Click **"Save"**

**Option B: Via Vercel CLI**

```bash
# Add for production
vercel env add NEXT_PUBLIC_API_URL production
# When prompted, enter: https://your-backend.up.railway.app

# Add for preview
vercel env add NEXT_PUBLIC_API_URL preview

# Add for development
vercel env add NEXT_PUBLIC_API_URL development
```

### 3. Update Railway Backend CORS

Your backend needs to allow requests from Vercel.

1. Go to Railway → **Backend Service** → **Variables**
2. Find or add `ALLOWED_ORIGINS`
3. Set the value to (JSON array format):
   ```json
   ["https://saas-eta-mauve.vercel.app","https://saas-arks-projects-01dfc75a.vercel.app","https://saas-git-main-arks-projects-01dfc75a.vercel.app"]
   ```
4. Click **"Save"** (Railway will auto-redeploy)

### 4. Redeploy Frontend

After setting environment variables in Vercel:

```bash
cd /d/projects/saas
vercel --prod
```

Or simply push to GitHub:
```bash
git add .
git commit -m "Connect frontend to Railway backend"
git push
```

---

## 🧪 Testing the Connection

After deployment:

1. Visit: https://saas-eta-mauve.vercel.app
2. Check the **Backend Status** card on the homepage
3. It should show:
   - **Green dot** = Connected ✅
   - **Yellow dot** = Connecting...
   - **Red dot** = Connection failed ❌

### Manual Testing

```bash
# Test backend health from Vercel
curl https://your-backend.up.railway.app/health

# Should return:
# {"status":"healthy","version":"1.0.0"}
```

---

## 📊 Connection Flow

```
User Browser
    ↓
Vercel Frontend (Next.js)
https://saas-eta-mauve.vercel.app
    ↓
    API Request (fetch)
    ↓
Railway Backend (FastAPI)
https://backend-production-xxxx.up.railway.app
    ↓
    Response (JSON)
    ↓
Vercel Frontend displays data
```

---

## 🔐 CORS Configuration

Your FastAPI backend is already configured with CORS middleware in `backend/app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,  # From environment variable
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Make sure `ALLOWED_ORIGINS` environment variable in Railway includes all your Vercel URLs.

---

## 🚀 What's Been Built

### Frontend Features

✅ **API Client** (`lib/api.ts`)
- Centralized API communication
- Health check endpoint
- Auth, documents, chat, workflows endpoints
- Error handling

✅ **Backend Status Component** (`components/BackendStatus.tsx`)
- Real-time connection status
- Visual indicator (green/yellow/red)
- Retry mechanism
- Displays backend version

✅ **Landing Page** (`app/page.tsx`)
- Hero section with product description
- Backend connection status widget
- Feature showcase (4 main features)
- API information panel
- Tech stack badges
- Responsive design

✅ **Metadata** (Updated in `layout.tsx`)
- SEO-friendly title and description
- Speed Insights enabled

---

## 🛠️ Troubleshooting

### Issue: Backend shows "error" status

**Check:**
1. Is Railway backend deployed and running?
2. Did you generate a public domain in Railway?
3. Is `NEXT_PUBLIC_API_URL` set in Vercel?
4. Is CORS configured correctly in Railway?

**Debug:**
```bash
# Check if backend is accessible
curl https://your-backend.up.railway.app/health

# Check environment variable in Vercel
vercel env ls
```

### Issue: CORS error in browser console

**Solution:**
Add your Vercel URLs to Railway's `ALLOWED_ORIGINS`:

```json
["https://saas-eta-mauve.vercel.app","https://saas-arks-projects-01dfc75a.vercel.app","http://localhost:3000"]
```

### Issue: Environment variable not working

**Remember:**
- Environment variables starting with `NEXT_PUBLIC_` are exposed to the browser
- You must redeploy after changing environment variables
- Clear browser cache if values seem cached

---

## 📝 Current Environment Variables

### Vercel Frontend
```bash
NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app
```

### Railway Backend
```bash
# Authentication & Security
OPENAI_API_KEY=sk-your-key
SECRET_KEY=your-secret-key

# Database
POSTGRES_HOST=${{POSTGRES.HOST}}
POSTGRES_USER=${{POSTGRES.USER}}
POSTGRES_PASSWORD=${{POSTGRES.PASSWORD}}
POSTGRES_DB=${{POSTGRES.DATABASE}}
MONGODB_URL=mongodb+srv://...
REDIS_URL=${{REDIS.URL}}

# CORS (IMPORTANT!)
ALLOWED_ORIGINS=["https://saas-eta-mauve.vercel.app","https://saas-arks-projects-01dfc75a.vercel.app"]

# Server
PORT=8000
```

---

## ✅ Final Checklist

- [ ] Railway backend has public domain generated
- [ ] `NEXT_PUBLIC_API_URL` added to Vercel
- [ ] `ALLOWED_ORIGINS` updated in Railway with Vercel URLs
- [ ] Both services redeployed
- [ ] Backend status shows green on homepage
- [ ] Can access `/health` endpoint
- [ ] Can access `/docs` (Swagger UI)

---

## 🎯 Next Steps

Once connected:

1. **Test All Endpoints**
   - Visit `https://your-backend.up.railway.app/docs`
   - Test auth, documents, chat, workflows

2. **Build Dashboard**
   - Create `/dashboard` page
   - Add authentication flow
   - Build document upload UI
   - Add chat interface

3. **Add Authentication**
   - Implement JWT token storage
   - Protected routes
   - Login/signup forms

4. **Database Setup**
   - Add PostgreSQL to Railway
   - Add Redis to Railway
   - Configure MongoDB Atlas
   - Run migrations

---

**Ready to deploy?** Run:

```bash
git add .
git commit -m "Add frontend UI with backend integration"
git push
```

Vercel will auto-deploy! 🚀
