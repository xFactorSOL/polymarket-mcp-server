# 🚀 Quick Deploy to Render

Get your Polymarket MCP Dashboard live on Render in 5 minutes!

## Step 1: Push to GitHub

Make sure your code is pushed to a GitHub repository.

## Step 2: Deploy on Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repository
4. Render will auto-detect `render.yaml`
5. Click **"Apply"**

## Step 3: Configure Environment Variables

In the Render dashboard, go to your service → **Environment** tab:

### For DEMO Mode (Read-Only):
```env
DEMO_MODE=true
```

### For Full Trading Mode:
```env
POLYGON_PRIVATE_KEY=your_key_without_0x
POLYGON_ADDRESS=0xYourAddress
POLYMARKET_CHAIN_ID=137
```

See `env.template` for all available options.

## Step 4: Deploy!

Click **"Manual Deploy"** → **"Deploy latest commit"**

Your dashboard will be live at: `https://your-service-name.onrender.com`

## That's It! 🎉

Your Polymarket MCP Dashboard is now live and accessible from anywhere.

---

**Need help?** See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for detailed instructions.
